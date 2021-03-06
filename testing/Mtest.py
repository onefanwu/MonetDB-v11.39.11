#!/usr/local/anaconda3/bin/python3.7

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0.  If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright 1997 - July 2008 CWI, August 2008 - 2021 MonetDB B.V.

#TODO:
#=====
# - check all TODO's below
# - tidy -up HTML-generation by "keeping in mind" during testing,
#   which OUT/ERR differ or not and which tests were skipped.
#   dump HTML-stuff only at end
#   print an ascii summary at end, too
# - if no diffs, but warnings, say so at end
# - produce, keep & reference LOG
# - add a "grep-like" function and replace "inlined" grep
#   contains(<file>,<string>)
# - do multi-level prompting?
# - normalize all path's used
# - Python 3? (or do a full rewrite?)

import os
import sys
import shutil
import re
import random
import time
import socket
import struct
import signal
import fnmatch
import glob
try:
    import winreg               # Python 3 on Windows
except ImportError:
    winreg = None               # not on Windows

MonetDB_VERSION = '11.39.11'.split('.')

procdebug = False
verbose = False
quiet = False

initdb = None
single_in_memory = False

global_timeout = 0
start_time = time.time()

# whether output goes to a tty
isatty = os.isatty(sys.stdout.fileno())

# default is no color (these three functions may get redefined)
def prred(str, write = sys.stdout.write):
    write(str)
def prgreen(str, write = sys.stdout.write):
    write(str)
def prpurple(str, write = sys.stdout.write):
    write(str)
if isatty:
    if os.name != 'nt':
        # color output a little
        RED = '\033[1;31m'
        GREEN = '\033[0;32m'
        PURPLE = '\033[1;35m'       # actually magenta
        BLACK = '\033[0;0m'
        def prred(str, write = sys.stdout.write):
            try:
                write(RED)
                write(str)
            finally:
                write(BLACK)
        def prgreen(str, write = sys.stdout.write):
            try:
                write(GREEN)
                write(str)
            finally:
                write(BLACK)
        def prpurple(str, write = sys.stdout.write):
            try:
                write(PURPLE)
                write(str)
            finally:
                write(BLACK)
    else:
        try:
            import ctypes
        except ImportError:
            pass
        else:
            STD_OUTPUT_HANDLE = -11
            try:
                handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
            except AttributeError:
                pass
            else:
                def get_csbi_attributes(handle):
                    # Based on IPython's winconsole.py, written by Alexander Belchenko
                    csbi = ctypes.create_string_buffer(22)
                    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
                    assert res
                    (bufx, bufy, curx, cury, wattr,
                    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                    return wattr
                reset = get_csbi_attributes(handle)
                def prred(str,
                          write=sys.stdout.write,
                          flush=sys.stdout.flush,
                          scta=ctypes.windll.kernel32.SetConsoleTextAttribute):
                    try:
                        flush()
                        scta(handle, 0x4)
                        write(str)
                        flush()
                    finally:
                        scta(handle, reset)
                def prgreen(str,
                            write=sys.stdout.write,
                            flush=sys.stdout.flush,
                            scta=ctypes.windll.kernel32.SetConsoleTextAttribute):
                    try:
                        flush()
                        scta(handle, 0x2)
                        write(str)
                        flush()
                    finally:
                        scta(handle, reset)
                def prpurple(str,
                             write=sys.stdout.write,
                             flush=sys.stdout.flush,
                             scta=ctypes.windll.kernel32.SetConsoleTextAttribute):
                    try:
                        flush()
                        scta(handle, 0x5)
                        write(str)
                        flush()
                    finally:
                        scta(handle, reset)

if os.path.exists('/usr/bin/coredumpctl'):
    # probably Linux if /usr/bin/coredumpctl exists
    # try raising the core dump size limit to infinite so that when we
    # get a crash we have a chance to retrieve the stack trace
    try:
        import resource
    except ImportError:
        pass
    else:
        try:
            resource.setrlimit(resource.RLIMIT_CORE,
                               (resource.RLIM_INFINITY,
                                resource.getrlimit(resource.RLIMIT_CORE)[1]))
        except ValueError:
            # if we can't raise the limit, just forget it
            pass

def ErrExit(msg):
    sys.stderr.write(msg + '\n')
    sys.exit(1)

def _configure(str):
    # expand configure variables in str and return result
    config = [
        ('{source}', '/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11'),
        ('${build}', '/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build'),

        ('${bindir}', '/usr/local/bin'),
##        ('${sbindir}', ''),
        ('${libexecdir}', 'libexec'),
        ('${datarootdir}', 'share'),
        ('${datadir}', 'share'),
        ('${sysconfdir}', '/usr/local/etc'),
        ('${localstatedir}', '/usr/local/var'),
        ('${libdir}', '/usr/local/lib'),
        ('${includedir}', 'include'),
##        ('${oldincludedir}', ''),
        ('${infodir}', 'share/info'),
        ('${mandir}', 'share/man'),
        ('${Qbindir}', '/usr/local/bin'),
##        ('${Qsbindir}', ''),
        ('${Qlibexecdir}', 'libexec'),
        ('${Qdatarootdir}', 'share'),
        ('${Qdatadir}', 'share'),
        ('${Qsysconfdir}', '/usr/local/etc'),
        ('${Qlocalstatedir}', '/usr/local/var'),
        ('${Qlibdir}', '/usr/local/lib'),
        ('${Qincludedir}', 'include'),
##        ('${Qoldincludedir}', ''),
        ('${Qinfodir}', 'share/info'),
        ('${Qmandir}', 'share/man'),
        # put these at end (in this order!) for efficiency
        ('${exec_prefix}', '/usr/local'),
        ('${Qexec_prefix}', '/usr/local'),
        ('${prefix}', '/usr/local'),
        ('${Qprefix}', '/usr/local'),
        ]
    if os.name == 'nt':
        str = str.replace('%prefix%', '${prefix}')
        str = str.replace('%exec_prefix%', '${exec_prefix}')
    changed = True
    while '$' in str and changed:
        changed = False
        for key, val in config:
            if os.name == 'nt':
                val = val.replace('%prefix%', '${prefix}')
                val = val.replace('%exec_prefix%', '${exec_prefix}')
            nstr = str.replace(key, val)
            changed = changed or str != nstr
            str = nstr
    return str

try:
    import Mfilter
except ImportError:
    try:
        import MonetDBtesting.Mfilter as Mfilter
    except ImportError:
        p = _configure(os.path.join('/usr/local', 'lib/python3.7/site-packages'))
        sys.path.insert(0, p)
        import MonetDBtesting.Mfilter as Mfilter
        if 'PYTHONPATH' in os.environ:
            p += os.pathsep + os.environ['PYTHONPATH']
        os.environ['PYTHONPATH'] = p

# use our own process module because it has _BufferedPipe
try:
    import process
except ImportError:
    import MonetDBtesting.process as process

# Replace os.fork by a version that forks but also sets the process
# group in the child.  This is done so that we can easily kill a
# subprocess and its children in case of a timeout.
# To use this, set the global variable setpgrp to True before calling
# subprocess.Popen.  It is reset automatically to False so that
# subprocess of our child don't get their own process group.
try:
    os.setpgrp
except AttributeError:
    try:
        os.setpgid
    except AttributeError:
        # no function to set process group, so don't replace
        pass
    else:
        # use os.setpgid to set process group
        def myfork(osfork = os.fork):
            global setpgrp
            _setpgrp = setpgrp
            setpgrp = False
            pid = osfork()
            if pid == 0 and _setpgrp:
                os.setpgid(0, 0)
            return pid
        os.fork = myfork
else:
    # use os.setpgrp to set process group
    def myfork(osfork = os.fork):
        global setpgrp
        _setpgrp = setpgrp
        setpgrp = False
        pid = osfork()
        if pid == 0 and _setpgrp:
            os.setpgrp()
        return pid
    os.fork = myfork
setpgrp = False

try:
    ttywidth = os.get_terminal_size(1).columns
except:
    ttywidth = 0
else:
    if ttywidth > 0 and os.name == 'nt':
        ttywidth -= 1           # don't go to the edge

import string                   # for whitespace
def splitcommand(cmd):
    '''Like string.split, except take quotes into account.'''
    q = None
    w = []
    command = []
    for c in cmd:
        if q:
            if c == q:
                q = None
            else:
                w.append(c)
        elif c in string.whitespace:
            if w:
                command.append(''.join(w))
            w = []
        elif c == '"' or c == "'":
            q = c
        else:
            w.append(c)
    if w:
        command.append(''.join(w))
    if len(command) > 1 and command[0] == 'call':
        del command[0]
    return command

def remove(file):
    try:
        os.remove(file)
    except:
        pass

def isexecutable(TST, ext = '.sh') :
    if   os.name == "nt":
        for ext in ".exe", ".com", ".bat", ".cmd":
            if TST.lower().endswith(ext):
                ext = ''
            if os.path.isfile(TST+ext) or os.path.isfile(TST+ext+".src"):
                return (True, ext)
    elif os.name == "posix":
        #TODO:
        # check with "file", and set executable
        TST += ext
        if ( os.path.isfile(TST       ) and os.access(TST       ,os.X_OK) ) or \
           ( os.path.isfile(TST+".src") and os.access(TST+".src",os.X_OK) ):
            return (True, ext)
    #TODO:
    #else:
        # ???
    return (False, '')
### isexecutable(TST, ext = '.sh') #

def CheckExec(cmd) :
    for p in os.environ['PATH'].split(os.pathsep):
        x = isexecutable(os.path.join(p,cmd),'')
        if x[0]:
            return os.path.join(p, cmd + x[1])
    return ""
### CheckExec(cmd) #

import argparse

import threading

randomPortRepeat = 9

F_SKIP = -1
F_OK = 0
F_WARN = 1
F_SOCK = 2
F_MISSING = 3
F_ERROR = 4
F_TIME = 5
F_ABRT = 6
F_RECU = 7
F_SEGV = 8

FAILURES = {
    F_SKIP  : ("F_SKIP",  '-'),
    F_OK    : ("F_OK",    'o'),
    F_WARN  : ("F_WARN",  'x'),
    F_SOCK  : ("F_SOCK",  'S'),
    F_ERROR : ("F_ERROR", 'X'),
    F_TIME  : ("F_TIME",  'T'),
    F_ABRT  : ("F_ABRT",  'A'),
    F_RECU  : ("F_RECU",  'R'),
    F_SEGV  : ("F_SEGV",  'C'),
    F_MISSING: ("F_MISSING", 'M'),
}

CONDITIONALS = {
    # X == true   =>  ='',  ='#'
    # X == false  =>  ='#', =''
    # from configure.ag:
    # These should cover all AM_CONDITIONALS defined in configure.ag, i.e.,
    # `grep AM_CONDITIONAL configure.ag | sed 's|^AM_CONDITIONAL(\([^,]*\),.*$|\1|' | sort -u`
    'HAVE_CURL'            : "#",
    'HAVE_FITS'            : "",
    'HAVE_GEOM'            : "",
    'HAVE_HGE'             : "#",
    'HAVE_LIBBZ2'          : "#",
    'HAVE_LIBLZ4'          : "",
    'HAVE_LIBLZMA'         : "#",
    'HAVE_LIBPCRE'         : "#",
    'HAVE_LIBPY3'          : "#",
    'HAVE_LIBR'            : "",
    'HAVE_LIBXML'          : "#",
    'HAVE_LIBZ'            : "#",
    'HAVE_NETCDF'          : "",
    'HAVE_ODBC'            : "#",
    'HAVE_PROJ'            : "",
    'HAVE_SHP'             : "",
    'NATIVE_WIN32'         : "",
    'NOT_WIN32'            : "#",
    # unknown at compile time;
    # hence, we set them only at runtime in main() below
    'KNOWNFAIL'            : "", # skip on release branch when not in testweb
    'HAVE_MONETDBJDBC_JAR' : "",
    'HAVE_JAVA'            : "",
    'HAVE_JAVAJDBC'        : "",
    'HAVE_JAVAMEROCONTROL' : "",
    'HAVE_JDBCCLIENT_JAR'  : "",
    'HAVE_JDBCTESTS_JAR'   : "",
    'HAVE_JDBCTESTS_DIR'   : "",
    'HAVE_JDBCTESTS'       : "",
#    'HAVE_LIBPANDAS3'      : "",
    'HAVE_LIBSCIPY3'       : "",
    'HAVE_PERL'            : "",
    'HAVE_PHP'             : "",
    'HAVE_PYMONETDB'       : "", # default PYTHON can import pymonetdb
    'HAVE_PY3MONETDB'      : "", # PYTHON3 exists and can import pymonetdb
    'HAVE_PYTHON_LZ4'      : "", # module lz4 is available
    'HAVE_RUBY'            : "",
    'HAVE_DATA_PATH'       : "",
    'MERCURIAL'            : "",
    'RELEASERUN'           : "",
    'BAD_HOSTNAME'         : "",
    'HAVE_IPV6'            : "",
}

# a bunch of classes to help with generating (X)HTML files
class _Encode:
    # mix-in class for encoding text and attribute values so that they
    # don't get interpreted as something else by the browser
    def encode(self, data, attr):
        map = [('&', '&amp;'),          # MUST be first
               ('<', '&lt;'),
               ('>', '&gt;'),
               (None, None),
               # following chars only translated in attr values (attr is True)
               ('"', '&quot;'),
               ('\t', '&#9;'),
               ('\n', '&#10;'),
               ('\r', '&#13;'),
               ]
        for c, tr in map:
            if c is None:
                if not attr:
                    break
                continue
            data = data.replace(c, tr)
        return data

class Element(_Encode):
    # class to represent an (X)HTML element with its attributes and
    # children

    # inline elements, we do not add newlines to the contents of these
    # elements
    inline = ['tt','i','b','big','small','em','strong','dfn','code',
              'samp','kbd','var','cite','abbr','acronym','a','img',
              'object','br','script','map','q','sub','sup','span',
              'bdo','input','select','textarea','label','button','font']
    # empty elements
    empty = ['link', 'basefont', 'br', 'area', 'img', 'param', 'hr',
             'input', 'col', 'frame', 'isindex', 'base', 'meta', ]
    xml = True                          # write XHTML instead of HTML

    def __init__(self, tag, attrdict = None, *children):
        self.tag = tag
        if attrdict is None:
            attrdict = {}
        self.attrdict = attrdict
        if children is None:
            children = []
        self.isempty = tag.lower() in self.empty
        if self.isempty:
            if children:
                raise ValueError("empty element can't have children")
            self.children = None
        else:
            self.children = list(children)

    def __str__(self):
        # string representation of the element with its children
        s = ['<%s' % self.tag]
        for name, value in sorted(self.attrdict.items()):
            s.append(' %s="%s"' % (name, self.encode(value, True)))
        if self.children or (not self.xml and not self.isempty):
            s.append('>')
            for c in self.children:
                s.append(str(c))
            s.append('</%s>' % self.tag)
        elif self.xml:
            s.append('/>')
        else:
            s.append('>')               # empty HTML element
        return ''.join(s)

    def write(self, f, newline = False):
        # write the element with its children to a file
        # if newline is set, add newlines at strategic points
        if self.tag.lower() == 'html':
            # before we write the DOCTYPE we should really check
            # whether the document conforms...
            if self.xml:
                f.write('<!DOCTYPE html PUBLIC '
                        '"-//W3C//DTD XHTML 1.0 Transitional//EN"\n'
                        '                      '
                        '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')
            else:
                f.write('<!DOCTYPE html PUBLIC '
                        '"-//W3C//DTD HTML 4.01 Transitional//EN"\n'
                        '                      '
                        '"http://www.w3.org/TR/html4/loose.dtd">\n')
        inline = self.tag.lower() in self.inline
        f.write('<%s' % self.tag)
        for name, value in sorted(self.attrdict.items()):
            f.write(' %s="%s"' % (name, self.encode(value, True)))
        if self.children or (not self.xml and not self.isempty):
            if not inline:
                for c in self.children:
                    if not isinstance(c, Element):
                        inline = True
                        break
            f.write('>')
            if newline and not inline:
                f.write('\n')
            for c in self.children:
                c.write(f, newline and not inline)
            f.write('</%s>' % self.tag)
        elif self.xml:
            f.write('/>')
        else:
            f.write('>')                # empty HTML element
        if newline:
            f.write('\n')

    def addchild(self, child):
        self.children.append(child)

    def addchildren(self, children):
        for child in children:
            self.children.append(child)

    def inschild(self, index, child):
        self.children.insert(index, child)

class Text(_Encode):
    # class to represent text in (X)HTML
    def __init__(self, text = '', raw = False):
        self.text = text
        self.raw = raw

    def __str__(self):
        if self.raw:
            return self.text
        return self.encode(self.text, False)

    def write(self, f, newline = False):
        f.write(str(self))
        if newline and not self.raw:
            f.write('\n')

class Comment:
    # class to represent an (X)HTML comment (not currently used)
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return '<!--%s-->' % self.text

    def write(self, f, newline = False):
        f.write(str(self))

class Timer:
    # interface to the threading.Timer function that interprets a
    # timeout of 0 as no timeout
    def __init__(self, interval, function, args):
        self.timer = None
        if interval > 0:
            self.timer = threading.Timer(interval, function, args = args)

    def start(self):
        if self.timer is not None:
            self.timer.start()

    def cancel(self):
        if self.timer is not None:
            self.timer.cancel()

STDOUT = sys.stdout
STDERR = sys.stdout     # err
REV = ''                # revision (output of hg id), default unknown

black = 'black'                         # #000000
white = 'white'                         # #ffffff
red = 'red'                             # #ff0000
lime = 'lime'                           # #00ff00
green = '#00aa00'
darkgreen = '#005500'
orange = '#ffaa00'
purple = '#aa00aa'
stylesheet = Element('style', None, Text('''
.error     { font-weight: bold; font-style: italic; color: red; }
.segfault  { font-weight: bold; font-style: italic; color: purple; }
.abort     { font-weight: bold; font-style: italic; color: purple; }
.recursion { font-weight: bold; font-style: italic; color: purple; }
.timeout   { font-weight: bold; font-style: italic; color: purple; }
.socket    { font-weight: bold; font-style: italic; color: purple; }
.warning   { font-weight: bold; color: orange; }
.good      {  }
.header    { font-family: helvetica, arial; text-align: center; }
.black     { color: black; }
'''))

TIMES = []

random.seed(time.time())

#TODO:
#class TimeoutError:
#       def __init__(self, text):
#               self.text = text
#       def __str__(self):
#               return self.text
#
#def AlarmHandler(signum, frame) :
#       raise TimeoutError, "Timeout"
#### AlarmHandler(signum, frame) #

def ErrMsg(TEXT) :
    STDOUT.flush()
    STDERR.write("\n%s:  ERROR:  %s\n\n" % (THISFILE, TEXT))
    STDERR.flush()
### ErrMsg(TEXT) #

def ErrXit(TEXT) :
    ErrMsg(TEXT)
    sys.exit(1)
### ErrXit(TEXT) #

def Warn(TEXT) :
    try:
        STDOUT.flush()
    except IOError:
        pass
    try:
        STDERR.write("\n%s  Warning:  %s\n\n" % (THISFILE, TEXT))
        STDERR.flush()
    except IOError:
        pass
### Warn(TEXT) #

def startswithpath(str,pre) :
    return os.path.normcase(str[:len(pre)]) == os.path.normcase(pre)
### startswithpath(str,pre) #

##def path(str) :
##    return str.replace('/', os.sep)
### path(str) #
##def url(str) :
##    return str.replace(os.sep, '/')
### url(str) #
if sys.version_info[0] == 2:
    import urllib
    path = urllib.url2pathname
    def url(str) :
        url = urllib.pathname2url(str)
        # on Windows, C:\tmp\foo becomes ///C:/tmp/foo, turn into /C:/tmp/foo
        if url.startswith('///'):
            url = url[2:]
        return url
elif sys.version_info[0] == 3:
    import urllib.request
    path = urllib.request.url2pathname
    def url(str) :
        url = urllib.request.pathname2url(str)
        # on Windows, C:\tmp\foo becomes ///C:/tmp/foo, turn into /C:/tmp/foo
        if url.startswith('///'):
            url = url[2:]
        return url

def openutf8(file, mode='r'):
    return open(file, mode, encoding='utf-8', errors='replace')

def try_open(path, mode) :
    try:
        f = openutf8(path, mode)
    except IOError as err:
        Warn("Opening file '%s' in mode '%s' failed with #%d: '%s'." % (path, mode, err.errno, err.strerror))
        f = None
    return f
###  try_open(path, mode) #

def CreateHtmlIndex (env, ssout, sserr, *body) :
    TSTDIR=env['TSTDIR']
    TSTTRGDIR=env['TSTTRGDIR']

    if TSTDIR:
        INDEX=".index"
    else:
        INDEX="index"

    if body:
        BACK = os.getcwd()
        os.chdir(TSTTRGDIR)

        if TSTDIR:
            header = Text(TSTDIR)
            if URLPREFIX:
                header = Element('a',
                                 {'href': '%s%s/%s' % (URLPREFIX, url(TSTDIR), TSTSUFF),
                                  'target': '%s_%s_body' % (DISTVER, TSTDIR),
                                  'class': 'black'},
                                 header)
            th = Element('th', {'class': 'header'}, header)
            if os.path.exists('SingleServer.out.html'):
                th.addchild(Element('br'))
                th.addchildren(AddHref('SingleServer.out.html',
                                       '%s_%s_body' % (DISTVER, TSTDIR),
                                       'out', ssout))
                th.addchild(Text(' | '))
                th.addchildren(AddHref('SingleServer.err.html',
                                       '%s_%s_body' % (DISTVER, TSTDIR),
                                       'err', sserr))
            tr = Element('tr', {'valign': 'top'}, th)
            tr.addchildren(body)
            hbody = Element('body',
                            {'bgcolor': white,
                             'text': black,
                             'link': green,
                             'vlink': darkgreen,
                             'alink': lime},
                            Element('center', {},
                                    Element('table',
                                            {'align': 'abscenter',
                                             'border': '1',
                                             'cellspacing': '0',
                                             'cellpadding': '3'},
                                            tr)))
        else:
            header = Element('h3', {},
                             Text(DISTVER))
            hbody = Element('body',
                            {'bgcolor': white,
                             'text': black,
                             'link': green,
                             'vlink': darkgreen,
                             'alink': lime},
                            header)
            hbody.addchildren(body)
        html = Element('html', {},
                       Element('head', {},
                               Element('meta', {'charset':'utf8'}),
                               Element('title', {}, Text(HTMLTITLE)),
                               stylesheet),
                       hbody)
        f = openutf8("%s.head.html" % INDEX,"w")
        html.write(f, True)
        f.close()

        if TSTDIR:
            layout = 'rows'
            ROWS="8%"
        else:
            layout = 'cols'
            ROWS="10%"
        html = Element('html', {},
                       Element('head', {},
                               Element('meta', {'charset':'utf8'}),
                               Element('title', {}, Text(HTMLTITLE))),
                       Element('frameset',
                               {layout: '%s,*' % ROWS,
                                'frameborder': 'yes',
                                'border': '1',
                                'bordercolor': white,
                                'marginwidth': '0',
                                'marginheight': '0'},
                               Element('frame',
                                       {'src': '%s.head.html' % INDEX,
                                        'scrolling': 'auto',
                                        'name': '%s_%s_head' % (DISTVER, TSTDIR),
                                        'frameborder': 'yes',
                                        'bordercolor': white,
                                        'marginwidth': '0',
                                        'marginheight': '0'}),
                               Element('frame',
                                       {'src': url(env['_%s_BODY_' % TSTDIR][0]),
                                        'scrolling': 'auto',
                                        'name': '%s_%s_body' % (DISTVER, TSTDIR),
                                        'frameborder': 'yes',
                                        'bordercolor': white,
                                        'marginwidth': '0',
                                        'marginheight': '0'})))
        f = openutf8("%s.html" % INDEX, "w")
        html.write(f, True)
        f.close()
        env['_%s_BODY_' % TSTDIR] = ["", 0]
        os.chdir(BACK)
### CreateHtmlIndex (env, ssout, sserr, *body) #

bugre = re.compile(r'\.(sf|bug)-(?P<bugno>[1-9]\d+)', re.I)

def CreateTstWhatXhtml (env, TST, stableWHAT, EXT, result) :
    WHAT = stableWHAT[7:11]
    TSTDIR    = env['TSTDIR']
    TSTSRCDIR = env['TSTSRCDIR']

    if result == F_OK:
        diffclass = 'good'
        difftext = 'No differences'
    elif result == F_WARN:
        diffclass = 'warning'
        difftext = 'Minor differences'
    else:                       # result == F_ERROR:
        difftext = 'Major differences'
        if result == F_SOCK:
            diffclass = 'socket'
            difftext += ' (Socket)'
        elif result == F_TIME:
            diffclass = 'timeout'
            difftext += ' (Timeout)'
        elif result == F_RECU:
            diffclass = 'recursion'
            difftext += ' (Recursion)'
        elif result == F_ABRT:
            diffclass = 'abort'
            difftext += ' (Aborted)'
        elif result == F_SEGV:
            diffclass = 'segfault'
            difftext += ' (Crash)'
        elif result == F_MISSING:
            diffclass = 'error'
            difftext += ' (Output missing)'
        else:
            diffclass = 'error'

    SYSTEM = "%s:" % DISTVER

    html = Element('html', {},
                   Element('head', {},
                           Element('title', {}, Text(HTMLTITLE)),
                           stylesheet),
                   Element('frameset', {'rows': '42,*',
                                        'frameborder': 'yes',
                                        'border': '1',
                                        'bordercolor': white,
                                        'marginwidth': '0',
                                        'marginheight': '0'},
                           Element('frame',
                                   {'src': '.%s%s.head.html' % (TST, WHAT),
                                    'scrolling': 'auto',
                                    'name': '%s_%s_%s_%s_head' % (DISTVER, TSTDIR, TST, WHAT[1:]),
                                    'frameborder': 'yes',
                                    'bordercolor': white,
                                    'marginwidth': '0',
                                    'marginheight': '0'}),
                           Element('frame',
                                   {'src': '%s%s.diff.html' % (TST, WHAT),
                                    'scrolling': 'auto',
                                    'name': '%s_%s_%s_%s_body' % (DISTVER, TSTDIR, TST, WHAT[1:]),
                                    'frameborder': 'yes',
                                    'bordercolor': white,
                                    'marginwidth': '0',
                                    'marginheight': '0'})))
    f = openutf8(".%s%s.html" % (TST, WHAT), "w")
    html.write(f, True)
    f.close()
    f = openutf8(".%s%s.head.html" % (TST, WHAT),"w")
    target = '%s_%s_%s_%s_body' % (DISTVER, TSTDIR, TST, WHAT[1:])
    if REV:                     # implies URLPREFIX is not None
        urlpref = '%s%s/%s' % (URLPREFIX, url(TSTDIR), TSTSUFF)
        hg = Element('a', {'href': urlpref,
                           'target': target},
                     Text('hg'))
    else:
        hg = None
    text = Element('div', {'class': 'header'},
                   Text(SYSTEM),
                   Text(' '),
                   Element('a', {'href': '%s%s.diff.html' % (TST, WHAT),
                                 'target': target,
                                 'class': diffclass},
                           Text(difftext)),
                   Text(' between '),
                   Element('a', {'href': '%s%s' % (TST, stableWHAT),
                                 'target': target},
                           Text(stableWHAT[1:])))
    if REV:
        d = urlpref
        if os.path.isfile(TST + stableWHAT + '.src'):
            # there's only one file like this...
            fl = openutf8(TST + stableWHAT + '.src').readline().strip()
            if fl.startswith('$RELSRCDIR/'):
                fl = fl[11:]
                while fl.startswith('../'):
                    fl = fl[3:]
                    d = d[:d.rindex('/')]
            fl = '%s/%s' % (d, fl)
        else:
            fl = '%s/%s%s' % (d, TST, stableWHAT)
        text.addchildren([
                Text(' (id '),
                Element('a', {'href': fl,
                              'target': target}, Text(REV)),
                Text(')')])
    text.addchildren([
            Text(' and '),
            Element('a', {'href': '%s.test%s' % (TST, WHAT),
                          'target': target},
                    Text('test%s' % WHAT)),
            Text(' of '),
            Element('a', {'href': TST + EXT, 'target': target},
                    Text(TST + EXT))])
    if REV:
        d = urlpref
        if os.path.isfile(TST + EXT + '.src'):
            fl = openutf8(TST + EXT + '.src').readline().strip()
            if fl.startswith('$RELSRCDIR/'):
                fl = fl[11:]
                while fl.startswith('../'):
                    fl = fl[3:]
                    d = d[:d.rindex('/')]
            fl = '%s/%s' % (d, fl)
        elif os.path.isfile(TST + EXT + '.in'):
            fl = '%s/%s%s.in' % (d, TST, EXT)
        else:
            fl = '%s/%s%s' % (d, TST, EXT)
        text.addchildren([
                Text(' (id '),
                Element('a', {'href': fl,
                              'target': target}, Text(REV)),
                Text(')')])
    text.addchildren([
            Text(' in '),
            Element('a', {'href': './', 'target': target},
                    Text(TSTDIR)),
            Text(' (')])
    if hg:
        text.addchild(hg)
        text.addchild(Text(', '))
    text.addchildren([
            Element('a', {'href': url(env['RELSRCDIR']),
                          'target': target},
                    Text('src')),
            Text(')')])
    res = bugre.search(TST)
    if res is not None:
        bugno = res.group('bugno')
        text.addchildren([
                Text(' ('),
                Element('a', {'href': 'http://bugs.monetdb.org/%s' % bugno,
                              'target': '_blank'},
                        Text('Bugzilla')),
                Text(')')])
    html = Element('html', {},
                   Element('head', {},
                           Element('title', {},
                                   Text(HTMLTITLE)),
                           stylesheet),
                   Element('body',
                           {'bgcolor': white,
                            'text': black,
                            'link': green,
                            'vlink': darkgreen,
                            'alink': lime},
                           text))

    html.write(f, True)
    f.close()
#TODO?
# <A HREF='.Mtest.Slave.Log.OutErr' TARGET='"""+DISTVER+"_"+TSTDIR+"_"+TST+"_"+WHAT[1:]+"""_body'>LOG</A>).
### CreateTstWhatXhtml (env, TST, stableWHAT, EXT, results) #

def CreateSrcIndex (env, TST, EXT) :
    TSTSRCDIR = env['TSTSRCDIR']
    TSTDIR    = env['TSTDIR']

    if URLPREFIX:
        framesrc = '%s%s/%s/%s%s' % (URLPREFIX, url(TSTDIR), TSTSUFF, TST, EXT)
    else:
        f = openutf8(".%s.nosrc.index.html" % TST, "w")
        html = Element('html', {},
                       Element('head', {},
                               Element('title', {},
                                       Text(HTMLTITLE)),
                               stylesheet),
                       Element('body',
                               {'bgcolor': white,
                                'text': black,
                                'link': green,
                                'vlink': darkgreen,
                                'alink': lime},
                               Element('center', {},
                                       Text('no source available'))))
        framesrc = '.%s.nosrc.index.html' % TST
    html = Element('html', {},
                   Element('head', {},
                           Element('title', {}, Text(HTMLTITLE))),
                   Element('frameset',
                           {'rows': '54,*',
                            'frameborder': 'yes',
                            'border': '1',
                            'bordercolor': white,
                            'marginwidth': '0',
                            'marginheight': '0'},
                           Element('frame',
                                   {'src': '.%s.src.index.head.html' % TST,
                                    'scrolling': 'auto',
                                    'name': '%s_%s_%s_head' % (DISTVER, TSTDIR, TST),
                                    'frameborder': 'yes',
                                    'bordercolor': white,
                                    'marginwidth': '0',
                                    'marginheight': '0'}),
                           Element('frame',
                                   {'src': framesrc,
                                    'scrolling': 'auto',
                                    'name': '%s_%s_%s_body' % (DISTVER, TSTDIR, TST),
                                    'frameborder': 'yes',
                                    'bordercolor': white,
                                    'marginwidth': '0',
                                    'marginheight': '0'})))
    f = openutf8(".%s.src.index.html" % TST,"w")
    html.write(f, True)
    f.close()

    tr = Element('tr', {},
                 Element('th', {'class': 'header'},
                         Text(TST)))
    for s in listdir(TSTSRCDIR):
        if s.startswith(TST):
            slink = Text(s)
            if URLPREFIX:
                slink = Element('a',
                                {'href': '%s%s/%s/%s' % (URLPREFIX, url(TSTDIR), TSTSUFF, s),
                                 'target': '%s_%s_%s_body' % (DISTVER, TSTDIR, TST)},
                                slink)
            tr.addchild(Element('td', {'class': 'header'},
                                slink))
    html = Element('html', {},
                   Element('head', {},
                           Element('title', {},
                                   Text(HTMLTITLE)),
                           stylesheet),
                   Element('body',
                           {'bgcolor': white,
                            'text': black,
                            'link': green,
                            'vlink': darkgreen,
                            'alink': lime},
                           Element('center', {},
                                   Element('table',
                                           {'align': 'abscenter',
                                            'border': '1',
                                            'cellspacing': '0',
                                            'cellpadding': '3'},
                                           tr))))
    f = openutf8(".%s.src.index.head.html" % TST, "w")
    html.write(f, True)
    f.close()
### CreateSrcIndex (env, TST, EXT) #

def AddHref (href, target, linktext, diff) :
    if   diff == F_ERROR:
        klass = 'error'
    elif diff == F_RECU:
        klass = 'recursion'
    elif diff == F_TIME:
        klass = 'timeout'
    elif diff == F_SOCK:
        klass = 'socket'
    elif diff == F_ABRT:
        klass = 'abort'
    elif diff == F_SEGV:
        klass = 'segfault'
    elif diff == F_WARN:
        klass = 'warning'
    elif diff == F_MISSING:
        klass = 'error'
    else:
        klass = 'good'
    a = Element('a', {'href': href, 'target': target, 'class': klass},
                Text(linktext))
    if klass == 'good':
        return [Text('('), a, Text(')')]
    else:
        return [a]
### AddHref (TSTDIR, TST, WHAT, diff) #

def AddTstToHtmlIndex (env, TST, STABLEout, STABLEerr, EXT, o, e) :
    TSTDIR = env['TSTDIR']

    CreateTstWhatXhtml(env, TST, STABLEout, EXT, o)
    CreateTstWhatXhtml(env, TST, STABLEerr, EXT, e)

    if e == F_RECU:
        tstclass = 'recursion'
    elif e == F_TIME:
        tstclass = 'timeout'
    elif e == F_SOCK:
        tstclass = 'socket'
    elif e == F_ABRT:
        tstclass = 'abort'
    elif e == F_SEGV:
        tstclass = 'segfault'
    elif o == F_MISSING or e == F_MISSING:
        tstclass = 'error'
    elif o == F_ERROR or e == F_ERROR:
        tstclass = 'error'
    elif o == F_WARN or e == F_WARN:
        tstclass = 'warning'
    else:
        tstclass = 'good'

    td = Element('td', {'class': 'header'},
                 Element('a', {'href': '.%s.src.index.html' % TST,
                               'target': '%s_%s_body' % (DISTVER, TSTDIR),
                               'class': tstclass},
                         Text(TST)),
                 Element('br'))
    td.addchildren(AddHref('.%s%s.html' % (TST, '.out'),
                           '%s_%s_body' % (DISTVER, TSTDIR),
                           'out', o))
    td.addchild(Text("&nbsp;|&nbsp;", raw = True))
    td.addchildren(AddHref('.%s%s.html' % (TST, '.err'),
                           '%s_%s_body' % (DISTVER, TSTDIR),
                           'err', e))
    if '_%s_BODY_' % TSTDIR not in env  or  \
       not env['_%s_BODY_' % TSTDIR][0]  or  \
       ( (not env['_%s_BODY_' % TSTDIR][1])  and  (o or e) ):
        if e and not o:
            env['_%s_BODY_' % TSTDIR] = [".%s.err.html" % TST, e]
        else:
            env['_%s_BODY_' % TSTDIR] = [".%s.out.html" % TST, o]

    CreateSrcIndex(env, TST, EXT)

    return td
### AddTstToHtmlIndex (env, TST, STABLEout, STABLEerr, EXT) #

def AddSubToHtmlIndex (env, TSTDIR, diff) :
    elem = Element('p', {})
    elem.addchildren(AddHref('%s/.index.html' % url(TSTDIR),
                             '%s__body' % DISTVER,
                             TSTDIR, diff))
    if '__BODY_' not in env  or  \
       not env['__BODY_'][0]  or  \
       ( (not env['__BODY_'][1])  and  diff ):
        env['__BODY_'] = ["%s/.index.html" % TSTDIR, diff]
    return elem
### AddSubToHtmlIndex (env, TSTDIR, diff) #

def SkipTest(env, TST, EXT, REASON, length) :
    TSTDIR = env['TSTDIR']
    TEXT = "Skipping test %s%s %s" % (TST, EXT, REASON)
    if quiet:
        STDOUT.write("-")
    elif verbose:
        Warn(TEXT)
    else:
        if REASON.startswith('as '):
            REASON = REASON[3:]
        if REASON.endswith('.'):
            REASON = REASON[:-1]
        if length + 10 + len(REASON) + 11 > ttywidth:
            # 10 - length of prompt()
            # 11 - length of " skipped ()"
            l = ttywidth - 10 - 11 - len(REASON)
            if len(TST) <= l:
                s = '%-*s' % (l, TST)
            else:
                s = '%s...%s' % (TST[:l//2 - 2], TST[-(l//2 - 1):])
        else:
            s = '%-*s' % (length, TST)
        STDOUT.write('%s%s skipped (%s)\n' % (prompt(), s, REASON))

    if testweb:
        return None

    f = openutf8(".%s.SKIPPED.html" % TST, "w")
    Element('html', {},
            Element('body', {},
                    Element('p', {},
                            Text("%s Warning: %s" % (THISFILE, TEXT))))).write(f, newline=True)
    f.close()
    target = '%s_%s_body' % (DISTVER, TSTDIR)
    td = Element('td', {'class': 'header'},
                 Element('a', {'href': '.%s.src.index.html' % TST,
                               'target': target,
                               'class': 'black'},
                         Text(TST)),
                 Element('br'),
                 Element('a', {'href': '.%s.SKIPPED.html' % TST,
                               'target': target},
                         Text('(skipped)')))
    if '_%s_BODY_' % TSTDIR not in env  or  \
       not env['_%s_BODY_' % TSTDIR][0]  or  \
       not env['_%s_BODY_' % TSTDIR][1]:
        env['_%s_BODY_' % TSTDIR] = [".%s.SKIPPED.html" % TST, F_SKIP]
    CreateSrcIndex(env, TST, EXT)
    return td
### SkipTest(env, TST, EXT, REASON) #

def find_test_dirs(thisdir) :
    testdirs = []
    thisdir = os.path.realpath(thisdir)
    dirnme = os.path.basename(thisdir)
    dirlst = listdir(thisdir)
    if dirnme == TSTSUFF  and  "All" in dirlst  and  os.path.isfile(os.path.join(thisdir,"All")):
        testdirs.append(os.path.dirname(thisdir))
    for d in dirlst:
        d = os.path.join(thisdir,d)
        if os.path.isdir(d):
            testdirs = testdirs + find_test_dirs(d)
    return testdirs
### find_test_dirs(thisdir) #

def PerformDir(env, testdir, testlist, BusyPorts, all_tests = False) :
    interrupted = False
    td = 0
    elem = None
    FdOut = F_SKIP
    FdErr = F_SKIP
    ssout = F_SKIP
    sserr = F_SKIP
    if testdir == TSTSRCBASE:
        TSTDIR = os.curdir
    else:
        TSTDIR = testdir[len(TSTSRCBASE + os.sep):]
    TSTSRCDIR = os.path.normpath(os.path.join(testdir, TSTSUFF))
    TSTTRGDIR = os.path.normpath(os.path.join(TSTTRGBASE, TSTPREF, TSTDIR))

    if THISFILE == "Mtest.py":
        TSTDB = TSTPREF + "_" + TSTDIR.replace(os.sep, '_')
    else: # THISFILE == "Mapprove.py"
        TSTDB = ""

    alltests = []
    try:
        allf = openutf8(os.path.join(TSTSRCDIR, "All"))
    except IOError:
        pass
    else:
        for tc in allf:
            if '#' in tc:
                # get rid of comment anywhere on line
                tc = tc[:tc.index('#')]
            tc = tc.strip()
            if tc:
                if '?' in tc:
                    cond,tst = tc.split('?')
                else:
                    cond,tst = None,tc
                alltests.append((tst,cond))
        allf.close()
    try:
        f = openutf8(os.path.join(TSTSRCDIR, "SingleServer"))
    except IOError:
        oneserver = False
        options = []            # not used
    else:
        oneserver = True
        options = f.read().split()
        f.close()

    if testlist:
        tl = []
        missing = False
        for tst in testlist:
            for t, c in alltests:
                if t == tst:
                    tl.append((t, c))
                    break
            else:
                tl.append((tst,None))
                missing = True
        testlist = tl
        if not missing:
            all_tests = True
    else:
        testlist = alltests
    if not testlist:
        Warn("No tests found in '%s`; skipping directory!" % TSTSRCDIR)
        return td, elem, max(FdOut, FdErr), interrupted

    # find length of longest test name
    length = 0
    for tst in testlist:
        if len(tst[0]) > length:
            length = len(tst[0])

    env['TSTDB']     = TSTDB
    env['TSTDIR']    = TSTDIR
    env['TSTSRCDIR'] = TSTSRCDIR
    env['UTSTSRCDIR'] = 'file://' + url(TSTSRCDIR)
    env['TSTTRGDIR'] = TSTTRGDIR
    if TSTDIR == os.curdir:
        env['RELSRCDIR'] = os.path.join(os.pardir, env['RELSRCBASE'], TSTSUFF)
    else:
        env['RELSRCDIR'] = os.path.join(* [os.pardir] * (len(TSTDIR.split(os.sep)) + 1) + [env['RELSRCBASE'], TSTDIR, TSTSUFF])
    os.environ['TSTDB']     = TSTDB
    os.environ['TSTDIR']    = TSTDIR
    os.environ['TSTSRCDIR'] = TSTSRCDIR
    os.environ['TSTTRGDIR'] = TSTTRGDIR
    os.environ['RELSRCDIR'] = env['RELSRCDIR']
    if 'TSTDATAPATH' not in os.environ and TSTDATAPATH:
        env['TSTDATAPATH'] = TSTDATAPATH
        os.environ['TSTDATAPATH'] = TSTDATAPATH


    #STDERR.flush()
    #for v in 'RELSRCDIR':
    #       print(v+" = "+str(env[v]))
    #STDOUT.flush()

    if THISFILE == "Mtest.py":
        if 'GDK_DBFARM' in env:
            LogDBdir = os.path.join(env['GDK_DBFARM'],TSTDB)
            if not env.get('NOCLEAN') and LogDBdir and os.path.exists(LogDBdir):
                try:
                    shutil.rmtree(LogDBdir)
                except:
                    Warn("database '%s` exists, but destroying it failed; skipping tests in '%s`!" % (TSTDB, TSTSRCDIR))
                    #TODO:
                    # add "something" to HTML output
                    return td, elem, max(FdOut, FdErr), interrupted
            if os.path.isabs(LogDBdir) and not os.path.exists(LogDBdir):
                try:
                    os.makedirs(LogDBdir)
                except:
                    Warn("creating database '%s` failed; skipping tests in '%s`!" % (TSTDB, TSTSRCDIR))
                    #TODO:
                    # add "something" to HTML output
                    return td, elem, max(FdOut, FdErr), interrupted
            if initdb:
                import zipfile
                try:
                    z = zipfile.ZipFile(initdb)
                except IOError:
                    Warn("initial database '%s` cannot be opened; skipping tests in '%s`!" % (initdb, TSTSRCDIR))
                    #TODO:
                    # add "something" to HTML output
                    return td, elem, max(FdOut, FdErr), interrupted
                try:
                    z.extractall(LogDBdir)
                except:
                    Warn("initial database '%s` cannot be extracted; skipping tests in '%s`!" % (initdb, TSTSRCDIR))
                    #TODO:
                    # add "something" to HTML output
                    return td, elem, max(FdOut, FdErr), interrupted
                z.close()
                if not oneserver:
                    pSrvr = ServerClass(splitcommand(env['exe']['mserver5'][1]) + ['--dbpath=%s' % LogDBdir], open(os.devnull, 'w'), open(os.devnull, 'w'), par['TIMEOUT'], os.path.join(LogDBdir, '.started'), int(env['MAPIPORT']))
                    pSrvr.LaunchIt()
                    pSrvr.terminate()
        if not os.path.exists(TSTTRGDIR):
            #TODO: set mode to umask
            os.makedirs(TSTTRGDIR)

        body_good = []
        body_bad = []
        oktests = []
        if not verbose and not quiet:
            print('\nRunning in %s' % TSTDIR)
        alllinks = []
        pSrvr = None
        try:
            try:
                for TST,COND in testlist:
                    if oneserver and (pSrvr is None or pSrvr.poll() is not None):
                        # restart server
                        inmem = single_in_memory
                        for o in options:
                            if o.startswith('embedded'):
                                inmem = False
                                break
                        if inmem:
                            cmd = splitcommand(env['exe']['mserver5'][1]) + ['--set', 'gdk_dbname=%s' % TSTDB, '--in-memory'] + options
                            pollfile = None
                        else:
                            cmd = splitcommand(env['exe']['mserver5'][1]) + ['--dbpath=%s' % LogDBdir] + options
                            pollfile = os.path.join(LogDBdir, '.started')
                        pSrvr = ServerClass(cmd,
                                            openutf8(os.path.join(TSTTRGDIR, 'SingleServer.out'), 'a'),
                                            openutf8(os.path.join(TSTTRGDIR, 'SingleServer.err'), 'a'),
                                            0,
                                            pollfile,
                                            int(env['MAPIPORT']))
                        os.chdir(TSTTRGDIR)
                        pSrvr.LaunchIt()
                    if global_timeout and start_time + global_timeout < time.time():
                        if not testweb:
                            print('\nGlobal testing timeout reached\n')
                            break
                        tt, FtOut, FtErr, bodyline, reason = 0,F_SKIP,F_SKIP,None,"as the global timeout has been reached"
                    else:
                        os.environ['TST'] = TST
                        tt, FtOut, FtErr, bodyline, reason, links = RunTest(env, TST, BusyPorts, COND, oktests, length, all_tests, pSrvr)
                        alllinks.extend(links)
                    if tt:
                        t = "%7.3f" % tt
                    else:
                        t = '-.---'
                    TIMES.append((TSTDIR, TST, t, tt, FtOut, FtErr, reason))
                    td += tt
                    FdOut = max(FdOut,FtOut)
                    FdErr = max(FdErr,FtErr)
                    if bodyline is not None:
                        if FtOut <= F_OK and FtErr <= F_OK:
                            body_good.append(bodyline)
                        else:
                            body_bad.append(bodyline)
                    if FtOut in (F_OK, F_WARN) and FtErr in (F_OK, F_WARN):
                        oktests.append(TST)
            except KeyboardInterrupt:
                print('\nInterrupted')
                interrupted = True
        finally:
            if pSrvr is not None:
                pSrvr.terminate()
                pSrvr = None
                o = openutf8(os.path.join(TSTTRGDIR, 'SingleServer.out.html'), 'w')
                o.write('<html><head><title>{} standard output</title></head>'
                        '<body><pre>\n'.format(TSTDIR))
                e = F_OK
                for line in openutf8(os.path.join(TSTTRGDIR, 'SingleServer.out')):
                    if line != '\n' and not line.startswith('#'):
                        e = F_ERROR
                        ssout = F_ERROR
                    o.write(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                o.write('</pre></body></html>\n')
                o.close()
                o = openutf8(os.path.join(TSTTRGDIR, 'SingleServer.err.html'), 'w')
                o.write('<html><head><title>{} standard error</title></head>'
                        '<body><pre>\n'.format(TSTDIR))
                e = F_OK
                for line in openutf8(os.path.join(TSTTRGDIR, 'SingleServer.err')):
                    if line != '\n' and not line.startswith('#'):
                        e = F_ERROR
                        sserr = F_ERROR
                    o.write(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
                o.write('</pre></body></html>\n')
                o.close()
        TIMES.append((TSTDIR, '', "%7.3f" % td, td, FdOut, FdErr, None))
        if testweb:
            os.chdir(TSTTRGDIR)
            for f in alllinks:
                remove(f)

        if THISFILE == "Mtest.py":
            if not testweb:
                body = body_bad + body_good
                CreateHtmlIndex(env, ssout, sserr, *body)
                elem = AddSubToHtmlIndex(env, TSTDIR, max(FdOut, FdErr, ssout, sserr))

        # remove extra files created by tests
        for f in listdir(TSTTRGDIR):
            ff = os.path.join(TSTTRGDIR, f)
            if os.path.islink(ff):
                continue
            for pat in ['.Mapprove.rc', '.index.head.html', '.index.html',
                        'index.head.html', 'index.html',
                        'times.lst', 'times.sql',
                        '.*.nosrc.index.html',
                        '.*.src.index.head.html', '.*.src.index.html',
                        '*.FILTERED', '.*.SKIPPED.html',
                        '*.client.err', '*.client.out',
                        '*.err.diff.html', '*.err.head.html', '*.err.html',
                        '*.out.diff.html', '*.out.head.html', '*.out.html',
                        '*.server.err', '*.server.out',
                        '*.stable.err*', '*.stable.out*',
                        '*.test.err', '*.test.out',
                        'SingleServer.out', 'SingleServer.err']:
                if fnmatch.fnmatch(f, pat):
                    break
            else:
                remove(ff)

        if testweb:
            try:
                os.removedirs(TSTTRGDIR)
            except:
                pass

    else: # THISFILE == "Mapprove.py"
        if not os.path.exists(TSTTRGDIR):
            Warn("Output directory '%s` missing; skipping directory!" % TSTTRGDIR)
            return td, elem, max(FdOut, FdErr), interrupted

        for TST,COND in testlist:
            td += ApproveOutput(env, TST)

    return td, elem, max(FdOut, FdErr, ssout, sserr), interrupted
### PerformDir(env, testdir, testlist, BusyPorts) #

def ApproveOutput (env, TST) :
    sem = 0
    TSTDB = env['TSTDB']
    TSTDIR  = env['TSTDIR']
    TSTSRCDIR = env['TSTSRCDIR']
    TSTTRGDIR = env['TSTTRGDIR']
    os.chdir(TSTSRCDIR)
    EXTENSIONS = par['EXTENSION']
    FORCE = par['FORCE']
    NOPATCH = par['NOPATCH']

#       filter = re.compile( "^!WARNING: TCPlisten\([0-9]*\): stopped.$"        "|"
#                            "^!WARNING: TCPepilogue: terminate [01] listeners$", re.MULTILINE)

    TO = re.compile("(^\+(|[^#]*[\t ])((Memory|Segmentation) [Ff]ault|Bus [Ee]rror|Aborted|Assertion (|.* )failed[:\.]|!FATAL: BATSIGabort:|ERROR = !Connection terminated|!Mtimeout: Timeout:)([ \t]|$)|aborted too deep recursion)", re.MULTILINE)

    for WHAT in EXTENSIONS:
        testOUTPUT = os.path.join(TSTTRGDIR, "%s.test.%s" % (TST, WHAT))
        TSTSRCDIRTST = os.path.join(TSTSRCDIR, TST)
        stableOUT  = "%s.stable.%s" % (TSTSRCDIRTST, WHAT)
        if par['SYSTEM']:
            SYSTEM = par['SYSTEM']
            stableOUTPUT = stableOUT + SYSTEM
        else:
            if WHAT == 'out':
                w = 0
            else: # WHAT == 'err'
                w = 1
            stableOUTPUT = TSTSRCDIRTST + StableOutErr(env, par, TSTSRCDIRTST, SYST, RELEASE, DIST, VERSION)[w]
            SYSTEM = stableOUTPUT.split(WHAT)[-1]

        if os.path.isfile(testOUTPUT):
            if os.path.isfile(stableOUTPUT):
                oc = '   (overwriting old file)'
            else:
                oc = '   (creating new file)'
                if os.path.isfile(stableOUT):
                    shutil.copy(stableOUT,stableOUTPUT)
                else:
                    openutf8(stableOUTPUT,"w").close()

            for d in ('TMPDIR', 'TMP', 'TEMP'):
                if d in os.environ:
                    patch = os.environ[d]
                    break
            else:
                patch = os.path.join(os.sep, 'tmp')
            patch = os.path.join(patch, "%s.patch-%s" % (os.path.basename(stableOUTPUT), str(os.getpid())))
            f = openutf8(patch + '.0', 'w')
            proc = process.Popen(['diff', '-Bb', '-I^[#=]', '-I^MAPI *=', '-U0',
                                  stableOUTPUT, testOUTPUT],
                                 stdout=f, text=True)
            proc.wait()
            f.close()
            if os.path.getsize(patch + ".0"):
                # if a file TST.stable.{out,err}-noapprove exists, we
                # refuse to approve the output by (silently) skipping
                if os.path.isfile(TSTSRCDIRTST + '.stable.' + WHAT + '-noapprove'):
                    remove(patch + ".0")
                    if verbose:
                        print("NOT approving %s  ->  stable.%s%s" % (os.path.join(TSTDIR, "%s.test.%s" % (TST, WHAT)), WHAT, SYSTEM))
                    continue
                if not verbose:
                    oc = ''
                print("Approving  %s  ->  stable.%s%s%s" % (os.path.join(TSTDIR, "%s.test.%s" % (TST, WHAT)), WHAT, SYSTEM, oc))

                f = openutf8(patch + ".1", "w")
                for l in openutf8(patch + ".0"):
                    if TO.search(l):
                        f.write(l[:1] + '\n')
                        Warn('Rejecting (error) message: "%s"' % l[1:].replace(os.linesep, ''))
                    elif len(l) < 2  or  \
                         (l[:2] not in ['+!','+='] and
                          not l.startswith('+ERROR = !') and
                          not l.startswith('+ERROR: ') and
                          not l.startswith('+WARNING: ')): # or  filter.match(ln):
                        f.write(l)
                    else:
                        if FORCE:
                            f.write(l)
                            sa = 'Approving'
                        else:
                            f.write(l[:1] + '\n')
                            sa = 'Skipping'
                        Warn('%s new (error) message: "%s"' % (sa,l[1:].replace(os.linesep, '')))
                        sem = 1
                f.flush()
                f.close()
                o = openutf8(stableOUTPUT).read()
                openutf8(stableOUTPUT + ".ORG", 'w').write(o)
                openutf8(stableOUTPUT, 'w').write(o)
                patchcmd = ['patch']
                if not verbose:
                    patchcmd.append('--quiet')
                proc = process.Popen(patchcmd + [stableOUTPUT, patch + '.1'],
                                     text=True)
                proc.wait()
                f = openutf8(patch, 'w')
                proc = process.Popen(['diff', '-u', stableOUTPUT + '.ORG',
                                      stableOUTPUT],
                                     stdout=f, text=True)
                proc.wait()
                f.close()
                remove(stableOUTPUT + ".ORG")
                remove(patch + ".1")
                o = openutf8(stableOUTPUT).read()
                openutf8(stableOUTPUT, 'w').write(o)
                o = None

                thefile = os.path.split(stableOUTPUT)[1]
                dir,file = os.path.split(stableOUT)
                test = re.compile('^%s.*$' % re.escape(file))
                list = []
                if not NOPATCH:
                    for f in listdir(dir or os.curdir):
                        if f.endswith('.rej') or f.endswith('.orig') or f.endswith('~'):
                            pass
                        elif f != thefile and test.match(f):
                            remove(os.path.join(dir or os.curdir, f + '.rej'))
                            remove(os.path.join(dir or os.curdir, f + '.orig'))
                            proc = process.Popen(patchcmd + ['--forward', os.path.join(dir or os.curdir, f)], stdin=openutf8(patch), text=True)
                            proc.wait()
                            if os.path.exists(os.path.join(dir or os.curdir, f + '.rej')):
                                list.append(f)
                if len(list) > 0:
                    Warn('There are other (specific) stable outputs for test\n%s for which patching failed:\n  %s\n\n  Look at the *.rej files in directory %s.' % (os.path.join(TSTDIR,'Tests',TST), str(list), os.path.join(TSTDIR,'Tests')))
            elif verbose:
                print("No differences detected between  %s and  stable.%s%s  that are not ignored by Mtest.py." % (os.path.join(TSTDIR, "%s.test.%s" % (TST, WHAT)), WHAT, SYSTEM))
            remove(patch + ".0")
        elif verbose:
            i = TST.rfind('.')
            if i > 0:
                return ApproveOutput(env, TST[:i])
            Warn("Output file missing: '%s`; skipping test!" % testOUTPUT)
    return sem
### ApproveOutput (env, TST) #

# this function is a slightly modified copy of the posixpath version
# the differences are the doubling of \'s in the replacement value
# under a very specific condition: when the variable name starts with
# a Q and the variable name (with Q prefix) does not occur in the
# environment and the variable name minus the Q prefix does occur in
# the environment; and the addition of an extra parameter with default
# so that the environment which is used to expand can be replace.
_varprog = None
def expandvars(path, environ = os.environ):
    """Expand shell variables of form $var and ${var}.  Unknown variables
    are left unchanged."""
    global _varprog
    if '$' not in path:
        return path
    if not _varprog:
        import re
        _varprog = re.compile(r'\$(\w+|\{[^}]*\})')
    i = 0
    while True:
        m = _varprog.search(path, i)
        if not m:
            break
        i, j = m.span(0)
        name = m.group(1)
        if name.startswith('{') and name.endswith('}'):
            name = name[1:-1]
        if name in environ:
            tail = path[j:]
            val = environ[name]
            path = path[:i] + val
            i = len(path)
            path += tail
        elif name.startswith('Q') and name[1:] in environ:
            tail = path[j:]
            val = environ[name[1:]].replace('\\', '\\\\')
            path = path[:i] + val
            i = len(path)
            path += tail
        else:
            i = j
    return path

def coredumpctl(pid):
    import tempfile
    # can't use tempfile.NamedTemporaryFile because it opens the file
    # exclusively
    fd, name = tempfile.mkstemp(suffix='.sh')
    fd2, name2 = tempfile.mkstemp()
    os.close(fd2)
    os.write(fd, b'#!/bin/sh\ngdb -nx -batch -ex "thread apply all bt" "$@" > %s\n' % name2.encode('utf-8'))
    os.close(fd)
    os.chmod(name, 0o700)
    if procdebug:
        print('Starting: coredumpctl -q --debugger=%s gdb %d' % (name, pid))
    with process.Popen(['coredumpctl', '-q', '--debugger=%s' % name, 'gdb', str(pid)],
                       stdout=process.PIPE,
                       stderr=process.PIPE,
                       text=True) as p:
        out, err = p.communicate()
    os.unlink(name)
    s = []
    for l in out.split('\n'):
        if not l.startswith('                '):
            s.append(l)
    out = '\n'.join(s) + open(name2).read()
    os.unlink(name2)
    return out, err

def returnCode(proc, f = None):
    '''Interpret the return code of a process.
    If second arg sepcified, write a message to it.'''
    if proc.killed:
        # don't write for timeout, killProc did that already
        return 'timeout'
    if os.name == 'nt':
        if proc.returncode == 3:
            # heuristic: abort() causes exit code 3
            if f is not None:
                f.write('\nAborted\n')
                f.flush()
            return 'abort'
        if proc.returncode == -1073741819: # 0xC0000005
            if f is not None:
                f.write('\nSegmentation fault\n')
                f.flush()
            return 'segfault'
        if proc.returncode == -1073741510: # 0xC000013A
            if f is not None:
                f.write('\nInterrupt\n')
                f.flush()
            return 'interrupt'  # Interrupt
        if proc.returncode != 0:
            return 'error'
    else:
        if proc.returncode == -signal.SIGSEGV:
            if f is not None:
                f.write('\nSegmentation fault\n')
                if os.path.exists('/usr/bin/coredumpctl'):
                    # wait a few seconds for the core to be dumped
                    time.sleep(10)
                    out, err = coredumpctl(proc.pid)
                    if out:
                        f.write(out)
                f.flush()
            return 'segfault'   # Segmentation fault
        if proc.returncode == -signal.SIGBUS:
            if f is not None:
                f.write('\nBus error\n')
                f.flush()
            return 'segfault'   # Bus error, treat as segfault
        if proc.returncode == -signal.SIGABRT:
            if f is not None:
                f.write('\nAborted\n')
                if os.path.exists('/usr/bin/coredumpctl'):
                    # wait a few seconds for the core to be dumped
                    time.sleep(10)
                    out, err = coredumpctl(proc.pid)
                    if out:
                        f.write(out)
                f.flush()
            return 'abort'      # Aborted
        if proc.returncode == -signal.SIGINT:
            if f is not None:
                f.write('\nInterrupt\n')
                f.flush()
            return 'interrupt'  # Interrupt
        if proc.returncode < 0:
            if f is not None:
                f.write('\nSignal %d\n' % -proc.returncode)
                f.flush()
            return 'signal'     # some other signal
        if proc.returncode > 0:
            return 'error'
    return None                 # no error

def GetBitsAndModsAndThreads(env) :
    global setpgrp
    rtrn = 0
    cmd = splitcommand(env['exe']['mserver5'][1])
    dbpath = os.path.join(env['GDK_DBFARM'], TSTPREF)
    try:
        os.unlink(os.path.join(dbpath, '.started'))
    except OSError:
        pass
    cmd.append('--dbpath=%s' % dbpath)
    if env.get('MULTIFARM'):
        cmd.append('--dbextra=%s' % os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'))
        shutil.rmtree(os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'),
                      ignore_errors = True)
        os.makedirs(os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'))
    if procdebug:
        print('GetBitsAndModsAndThreads: starting process "%s" (inpipe, outpipe, errpipe)\n' % '" "'.join(cmd))
    setpgrp = True
    proc = process.Popen(cmd, stdin=process.PIPE, stdout=process.PIPE,
                         stderr=process.PIPE, text=True)
    proc.killed = False
    proc.onechild = True
    t = Timer(float(par['TIMEOUT']), killProc, args = [proc, proc.stderr, cmd])
    qOut = qErr = None
    try:
        t.start()
        while True:
            proc.poll()
            if proc.returncode is not None:
                break
            if os.path.exists(os.path.join(dbpath, '.started')):
                break
            time.sleep(0.001)
        if proc.returncode is None:
            cmd = splitcommand(env['exe']['MAL_Client'][1])
            if procdebug:
                print('GetBitsAndModsAndThreads: starting process "%s" (inpipe, outpipe, errpipe)\n' % '" "'.join(cmd))
            clnt = process.Popen(cmd, stdin=process.PIPE, stdout=process.PIPE,
                                 stderr=process.PIPE, text=True)
            input = '''\
                c := mdb.modules();
                modsid := algebra.unique(c);
                mods := algebra.projection(modsid,c);
                s := "\\nModules: ";
                sep := "";
                barrier (h:oid,t:str) := iterator.new(mods);
                        s := s + sep;
                        s := s + "\'";
                        s := s + t;
                        s := s + "\'";
                        sep := ",";
                redo (h:oid,t:str) := iterator.next(mods);
                exit h;
                s := s + "\\n";
                io.printf(s);
            '''
            ##module("NoModule");
            qOut, qErr = clnt.communicate(input=input)
            proc.terminate()
            sOut = proc.stdout.read()
            sErr = proc.stderr.read()
            proc.wait()
            qOut = sOut + qOut
            qErr = sErr + qErr
    finally:
        t.cancel()
        if proc.returncode is None:
            killProc(proc, proc.stderr, cmd)
            proc.wait()
        if procdebug:
            print('GetBitsAndModsAndThreads: process exited "%s" (%s)\n' % ('" "'.join(cmd), proc.returncode))
    env['TST_MODS'] = []
    env['TST_BITS'] = ""
    env['TST_INT128'] = ""
    env['TST_SINGLE'] = ""
    env['TST_THREADS'] = ""
    env['TST_ARCH'] = ""
    if qOut:
        tbos = re.compile("^# Compiled for (?P<arch>[^-]+).*/(?P<bits>[63][42]bit)(?P<int128> with 128bit integers|)", re.MULTILINE)
        tt = re.compile("^# Serving database .*, using ([0-9]+) threads?", re.MULTILINE)
        tm = re.compile("^Modules: (.+)$", re.MULTILINE)
        for l in qOut.split('\n'):
            obs = tbos.match(l)
            if obs is not None:
                env['TST_BITS'] = obs.group('bits')
                os.environ['TST_BITS'] = env['TST_BITS']
                if obs.group('int128') == " with 128bit integers":
                    env['TST_INT128'] = "int128"
                    os.environ['TST_INT128'] = env['TST_INT128']
                arch = obs.group('arch')
                if arch == 'amd64':
                    arch = 'x86_64' # normalize name
                env['TST_ARCH'] = arch
            t = tt.match(l)
            if t:
                if t.group(1) == "1":
                    env['TST_SINGLE'] = "single"
                    os.environ['TST_SINGLE'] = env['TST_SINGLE']
                env['TST_THREADS'] = t.group(1)
            m = tm.match(l)
            if m:
                env['TST_MODS'] = eval(m.group(1))
        if not env['TST_BITS']:
            ErrMsg("Checking for Bits failed!")
        if not env['TST_MODS']:
            ErrMsg("Checking for Modules failed!")
        if not env['TST_BITS'] or not env['TST_MODS']:
            STDERR.write(' '.join(cmd) + "\n\n")
            STDERR.write(qOut)
            STDERR.write("\n")
            STDERR.write(qErr)
            STDERR.write("\n")
            STDERR.flush()
            rtrn = 1
    else:
        rtrn = 1
        ErrMsg("No output from mserver5 when checking for Bits, Modules & Threads!?")
        if qErr:
            STDERR.write(' '.join(cmd) + "\n\n")
            STDERR.write(qErr)
            STDERR.write("\n")
            STDERR.flush()
    os.environ['TST_MODS'] = str(env['TST_MODS'])
    return rtrn
### GetBitsAndModsAndThreads(env) #

def CheckMods(env, TST, SERVER, CALL) :
    missing = []
    if os.path.isfile(TST + ".modules"):
        for m in openutf8(TST + ".modules"):
            m = m.strip()
            if m  and  m[0] != "#"  and  m not in env['TST_MODS']:
                missing.append(m)
    if SERVER == "SQL":
        sql_mods = ["sql"]
        for m in sql_mods:
            if m not in env['TST_MODS']:
                missing.append(m)
    return missing
### CheckMods(env, TST, SERVER, CALL) #

def CheckTests(env, TST, oktests):
    missing = []
    if not os.path.isfile(TST + '.reqtests'):
        # no required tests, so none missing
        return missing
    if env.get('NOCLEAN'):
        # we didn't clean up from a previous run, assume tests were done
        return missing

    for test in openutf8(TST + '.reqtests'):
        test = test.strip()
        if not test or test.startswith('#'):
            continue
        if test not in oktests:
            missing.append(test)
    return missing
### CheckTests(env, TST, oktests) #

def StableOutErr(env,par,TST,SYST,RELEASE,DIST,VERSION) :
    BITS = env['TST_BITS']
    INT128 = env['TST_INT128']
    if INT128:
        INT128 = r"(\.int128)?"
    SINGLE = env['TST_SINGLE']
    if SINGLE:
        SINGLE = r"(\.single)?"
    ARCH = env['TST_ARCH']
    dir,file = os.path.split(TST)
    outre = re.compile(r'^%s\.stable\.(?P<tp>out|err)(\.(%s(%s)?|%s(%s)?))?(\.(%s|%s))?%s%s$' % (re.escape(file), re.escape(SYST), re.escape(RELEASE), re.escape(DIST), re.escape(VERSION), BITS, ARCH, INT128, SINGLE))
    bestout = besterr = ''
    for f in listdir(dir or os.curdir):
        res = outre.match(f)
        if res is not None:
            if res.group('tp') == 'out':
                if len(bestout) < len(f):
                    bestout = f
            else:                   # res.group('tp') == 'err'
                if len(besterr) < len(f):
                    besterr = f
    if bestout:
        STABLEout = os.path.join(dir, bestout)[len(TST):]
    else:
        STABLEout = '.stable.out'
    if besterr:
        STABLEerr = os.path.join(dir, besterr)[len(TST):]
    else:
        STABLEerr = '.stable.err'
    return STABLEout, STABLEerr
### StableOutErr(env,par,TST,SYST,RELEASE,DIST,VERSION) #

def CategorizeResult(TST, SockTime, outmissing, errmissing):
    l = '<!--MajorDiffs-->'   # assign something in case file is empty
    for l in openutf8("%s.out.diff.html" % TST):
        pass
    if   l.startswith('<!--NoDiffs-->'):
        o = F_OK
    elif l.startswith('<!--MinorDiffs-->'):
        o = F_WARN
    elif l.startswith('<!--MajorDiffs-->'):
        if outmissing:
            o = F_MISSING
        else:
            o = F_ERROR
    else:
        Warn("Unexpected last line in %s.out.diff.html:\n%s" % (TST, l))
        ff = openutf8("%s.out.diff.html" % TST, "a")
        ff.write("\n<!--MajorDiffs-->\n")
        ff.close()
        o = F_ERROR
    l = '<!--MajorDiffs-->'   # assign something in case file is empty
    for l in openutf8("%s.err.diff.html" % TST):
        pass
    if   l.startswith('<!--NoDiffs-->'):
        e = F_OK
    elif l.startswith('<!--MinorDiffs-->'):
        e = F_WARN
    elif l.startswith('<!--MajorDiffs-->'):
        if errmissing:
            e = F_MISSING
        else:
            e = F_ERROR
    else:
        Warn("Unexpected last line in %s.err.diff.html:\n%s" % (TST, l))
        ff = openutf8("%s.err.diff.html" % TST, "a")
        ff.write("\n<!--MajorDiffs-->\n")
        ff.close()
        e = F_ERROR
    if e in (F_ERROR, F_MISSING) and SockTime in (F_SOCK, F_TIME, F_RECU, F_ABRT, F_SEGV):
        e = SockTime
    return o, e

relcond = {
    # upgrade testing conditionals:
    # key is condition, value is tuple with file name and part of message
    'PREVREL': ('prevrel.zip', 'previous'),
    'PREVHGEREL': ('prevhgerel.zip', 'previous hugeint'),
    'PREVCHAINREL': ('prevchainrel.zip', 'previous chained'),
    'PREVHGECHAINREL': ('prevhgechainrel.zip', 'previous hugeint chained'),
    'PREVRELEMPTY': ('prevrelempty.zip', 'previous empty'),
    'PREVHGERELEMPTY': ('prevhgerelempty.zip', 'previous hugeint empty'),
    'PREVCHAINRELEMPTY': ('prevchainrelempty.zip', 'previous chained empty'),
    'PREVHGECHAINRELEMPTY': ('prevhgechainrelempty.zip',
                             'previous hugeint chained empty'),
}

def RunTest(env, TST, BusyPorts, COND, oktests, length, all_tests, pSrvr) :
    global setpgrp
    Failed = F_SKIP
    FailedOut = F_SKIP
    FailedErr = F_SKIP
    TSTDB = env['TSTDB']
    TSTDIR  = env['TSTDIR']
    TSTSRCDIR = env['TSTSRCDIR']
    RELSRCDIR = env['RELSRCDIR']
    TSTTRGDIR = env['TSTTRGDIR']
    os.chdir(TSTSRCDIR)
    elem = None
    reason = None               # reason for skipping (if any)
    links = []                  # symlinks we make
    threads = None              # set if we override number of threads

    TX = 0
    EXT = CALL = SERVER = ""
    x  = isexecutable(TST)
    if not x[0]:
        x  = isexecutable(TST,'')
    xA = isexecutable(TST + ".MAL")
    xS = isexecutable(TST + ".SQL")
    if   x[0]:
        EXT = x[1]
        CALL = "other"
    elif xA[0]:
        EXT = ".MAL"+xA[1]
        CALL = "other"
        SERVER = "MAL"
    elif xS[0]:
        EXT = ".SQL"+xS[1]
        CALL = "other"
        SERVER = "SQL"
    else:
        tests = (
            # file extention  EXT        CALL      SERVER
            ('.py',           '.py',     'python', ''),
            ('.MAL.py',       '.MAL.py', 'python', 'MAL'),
            ('.SQL.py',       '.SQL.py', 'python', 'SQL'),
            ('.malC',         '.malC',   'mal',    'MAL'),
            ('_s00.malC',     '.malC',   'malXs',  'MAL'),
            ('_p00.malC',     '.malC',   'malXp',  'MAL'),
            ('.sql',          '.sql',    'sql',    'SQL'),
            ('_s00.sql',      '.sql',    'sqlXs',  'SQL'),
            ('_p00.sql',      '.sql',    'sqlXp',  'SQL'),
            ('.test',         '.test',   'sqltest','SQL'),
            ('.R',            '.R',      'R',      'SQL'),
            ('.rb',           '.rb',     'ruby',   'SQL'),
            #TODO:
            # ('.java',         '.java',   'Java',   'SQL'),
            # ('_s00.java',     '.java',   'JavaXs', 'SQL'),
            # ('_p00.java',     '.java',   'JavaXp', 'SQL'),
            # ('.odmg',         '.odmg',   'odmg',   'SQL'),
        )
        for tst, ext, cll, srv in tests:
            if os.path.isfile(TST + tst) or \
               os.path.isfile(TST + tst + '.src') or \
               os.path.isfile(TST + tst + '.in'):
                EXT = ext
                CALL = cll
                SERVER = srv
                break
        else:
            if os.name == "nt":
                reason = "test missing: '"+os.path.join(TSTSRCDIR,TST)+".(exe|com|bat|cmd|py|malC|sql)`"
            #TODO:
            #elif os.name == "posix":
            else:
                reason = "test missing: '"+os.path.join(TSTSRCDIR,TST)+"[.py|.malC|.sql|.R|.rb]`"
            if quiet:
                pass
            elif verbose:
                STDOUT.write('%s%s  ' %
                             (prompt(), os.path.join(env['TSTDIR'], TST + EXT)))
                prred('TEST MISSING')
                STDOUT.write('\n')
            else:
                if ttywidth > 0 and length + 10 + 21 >= ttywidth:
                    # 10 - length of prompt()
                    # 21 - length of time plus result
                    l = ttywidth - 10 - 21 - 1
                    if len(TST) <= l:
                        s = '%-*s ' % (l, TST)
                    else:
                        s = '%s...%s ' % (TST[:l//2 - 2], TST[l//2+1-l:])
                else:
                    s = '%-*s ' % (length, TST)
                STDOUT.write('%s%s' % (prompt(), s))
                prred('TEST MISSING')
                STDOUT.write('\n')

            return TX,Failed,Failed,elem,reason,links

    MissingMods = CheckMods(env, TST, SERVER, CALL)
    MissingTests = CheckTests(env, TST, oktests)
    nomito = os.path.isfile(TST + '.nomito')
    user = None
    passwd = None


    os.chdir(TSTTRGDIR)

    if COND:
        for cond in COND.split('&'):
            if cond.startswith('!'):
                negate = True
                cond = cond[1:]
            else:
                negate = False
            if cond in relcond:
                if not os.path.exists(os.path.join(env['GDK_DBFARM'], relcond[cond][0])):
                    reason = "as %s release database is not available" % relcond[cond][1]
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
            elif cond.startswith('THREADS='):
                if negate:
                    reason = "impossible combination of THREADS= and negation"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
                elif env['GDK_NR_THREADS'] == '0' or \
                   int(env['TST_THREADS']) >= int(cond[8:]):
                    threads = cond[8:]
                elif env['TST_THREADS'] != cond[8:]:
                    reason = "as number of threads is wrong"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
            elif cond.startswith('THREADS<='):
                if (int(env['TST_THREADS']) <= int(cond[9:])) == negate:
                    reason = "as number of threads is wrong"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
            elif cond.startswith('THREADS>='):
                if (int(env['TST_THREADS']) >= int(cond[9:])) == negate:
                    reason = "as number of threads is wrong"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
            elif cond.startswith('USER='):
                if negate:
                    reason = "impossible combination of USER= and negation"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
                user = cond[5:]
            elif cond.startswith('PASSWD='):
                if negate:
                    reason = "impossible combination of PASSWD= and negation"
                    elem = SkipTest(env, TST, EXT, reason, length)
                    break
                passwd = cond[7:]
            elif cond not in CONDITIONALS:
                reason = "as conditional '%s' is unknown." % cond
                elem = SkipTest(env, TST, EXT, reason, length)
                break
            elif (not CONDITIONALS[cond]) != negate:
                if negate:
                    reason = "as conditional '%s' holds." % cond
                else:
                    reason = "as conditional '%s' does not hold." % cond
                elem = SkipTest(env, TST, EXT, reason, length)
                break
    if reason:
        pass
    elif MissingTests:
        reason = "as required test%s '%s' failed." % (len(MissingTests) != 1 and 's' or '', "', '".join(MissingTests))
        elem = SkipTest(env, TST, EXT, reason, length)
    elif EXT == ".malC" and  not env['exe']['MAL_Client'][0]:
        reason = "as %s is not available." % env['MALCLIENT'].split(None, 1)[0]
        elem = SkipTest(env, TST, EXT, reason, length)
    elif EXT == ".sql" and  not env['exe']['SQL_Client'][0]:
        reason = "as %s is not available." % env['SQLCLIENT'].split(None, 1)[0]
        elem = SkipTest(env, TST, EXT, reason, length)
    elif EXT == ".sql" and  not env['exe']['SQL_Dump'][0]:
        reason = "as %s is not available." % env['SQLDUMP'].split(None, 1)[0]
        elem = SkipTest(env, TST, EXT, reason, length)
    elif EXT == ".test" and not CONDITIONALS['HAVE_PYMONETDB']:
        reason = "as pymonetdb is not available."
        elem = SkipTest(env, TST, EXT, reason, length)
    elif SERVER in ["MAL", "SQL"] and not env['exe']['mserver5'][0]:
        reason = "as %s is not available." % env['MSERVER'].split(None, 1)[0]
        elem = SkipTest(env, TST, EXT, reason, length)
    elif EXT == ".malS" and not env['exe']['mserver5'][0]:
        reason = "as %s is not available." % env['MSERVER'].split(None, 1)[0]
        elem = SkipTest(env, TST, EXT, reason, length)
    elif CALL == "python"  and  not env['exe']['python'][0]:
        reason = "as python is not available."
        elem = SkipTest(env, TST, EXT, reason, length)
        #TODO:
        #elif [ "$EXT" = "java"  -a  ! "`type -path java`" ] ; then
        #elem = SkipTest(env, TST, EXT, "as java is not in $PATH.", length)
    elif MissingMods:
        reason = "as modules '%s` are missing." % str(MissingMods)
        elem = SkipTest(env, TST, EXT, reason, length)
    elif CALL == "malXp":
        reason = "as multiple MAL clients in parallel are currently not supported by %s." % THISFILE
        elem = SkipTest(env, TST, EXT, reason, length)
    elif CALL == "sqlXp":
        reason = "as multiple SQL clients in parallel are currently not supported by %s." % THISFILE
        elem = SkipTest(env, TST, EXT, reason, length)
    elif SERVER in ["MAL", "SQL"] and "MAPI" in BusyPorts:
        reason = "as MAPIPORT=%s is not available." % env['MAPIPORT']
        elem = SkipTest(env, TST, EXT, reason, length)
    else:
        test = re.compile("^"+TST+"((_[sp][0-9][0-9])?\..*)?$", re.MULTILINE)
        for f in listdir(RELSRCDIR):
            if test.match(f):
                try:
                    SymlinkOrCopy(os.path.join(RELSRCDIR, f), f)
                    links.append(os.path.join(TSTTRGDIR, f))
                except IOError as err:
                    if not env.get('NOCLEAN'):
                        ErrMsg("SymlinkOrCopy('%s','%s') in '%s' failed with #%d: '%s'."
                               % (os.path.join(RELSRCDIR, f), f, os.getcwd(), err.errno, err.strerror))
                except OSError:
                    if not env.get('NOCLEAN'):
                        raise

        # Check for available sockets and block them until we're ready to run the actual test
        if pSrvr is None:
            MAPIsockets, reason = CheckSocket2(env, "MAPI")   #, SrvrErr)
            if MAPIsockets is None:
                reason = 'as ' + reason
                elem = SkipTest(env, TST, EXT, reason, length)
                return TX,Failed,Failed,elem,reason,links
        else:
            MAPIsockets = None

        if os.path.isfile(TST+EXT+".src")  and not os.path.isfile(TST+EXT):
            f = openutf8(TST+EXT+".src","r")
            TSTSRC = expandvars(path(f.readline().strip()), env)
            f.close()
            if os.path.isfile(TSTSRC):
                try:
                    SymlinkOrCopy(TSTSRC, TST + EXT)
                    links.append(TST + EXT)
                except IOError as err:
                    ErrMsg("SymlinkOrCopy('%s','%s') in '%s' failed with #%d: '%s'."
                           % (TSTSRC, TST + EXT, os.getcwd(), err.errno, err.strerror))
            else:
                reason = "as source file '%s` is missing." % TSTSRC
                elem = SkipTest(env, TST, EXT+".src", reason, length)
                if MAPIsockets is not None:
                    # Release reserved sockets before bailing out
                    MAPIsockets[0].close()
                    MAPIsockets[1].close()
                return TX,Failed,Failed,elem,reason,links
        test = re.compile("^"+TST+"((_[sp][0-9][0-9])?\..*)?\.src$", re.MULTILINE)
        for ff in listdir(TSTTRGDIR):
            if test.match(ff) and not os.path.isfile(ff[:-4]):
                f = openutf8(ff,"r")
                TSTSRC = expandvars(path(f.readline().strip()), env)
                f.close()
                if os.path.isfile(TSTSRC):
                    try:
                        if '.stable.' in ff:
                            f1 = openutf8(TSTSRC, "r")
                            f2 = openutf8(ff[:-4], "w")
                            line = f1.readline()
                            f2.write("%s of test '%s` in directory '%s` itself:\n" % (line[:6], TST, TSTDIR.replace('\\', '/')))
                            f2.write(f1.read())
                            f1.close()
                            f2.close()
                        else:
                            SymlinkOrCopy(TSTSRC, ff[:-4])
                        links.append(ff[:-4])
                    except IOError as err:
                        ErrMsg("SymlinkOrCopy('%s','%s') in '%s' failed with #%d: '%s'."
                               % (TSTSRC, ff[:-4], os.getcwd(), err.errno, err.strerror))
                else:
                    Warn("source file '"+TSTSRC+"` is missing.")
        test = re.compile("^"+TST+"(_[sp][0-9][0-9])?\..*\.in$", re.MULTILINE)
        for ff in listdir(TSTTRGDIR):
            fff = ff[:-3]
            if test.match(ff) and not os.path.isfile(fff):
                f = openutf8(fff,"w")
                for l in openutf8(ff):
                    f.write(expandvars(l, env))
                f.close()

        ACCURACYout = par['ACCURACY']
        ACCURACYerr = par['ACCURACY']
        STABLEout,STABLEerr = StableOutErr(env,par,TST,SYST,RELEASE,DIST,VERSION)
        outmissing = errmissing = False
        if not os.path.isfile(TST+STABLEout):
            openutf8(TST+STABLEout,"w").close()
            ACCURACYout = 0
            outmissing = True
        if not os.path.isfile(TST+STABLEerr):
            openutf8(TST+STABLEerr,"w").close()
            ACCURACYerr = 0
            errmissing = True
        if (outmissing or errmissing) and not CONDITIONALS['KNOWNFAIL']:
            # no stable output, so known to fail
            reason = "as conditional 'KNOWNFAIL' does not hold."
            elem = SkipTest(env, TST, EXT, reason, length)
            return TX,Failed,Failed,elem,reason,links

        TIMEOUT = par['TIMEOUT']
        if os.path.isfile(TST+".timeout"):
            for f in openutf8(TST+".timeout"):
                TOf = float(f.strip())
                if TOf > 0:
                    TIMEOUT = int(TIMEOUT * TOf)
                if TIMEOUT < 1 and par['TIMEOUT'] > 0:
                    TIMEOUT = 1
        CTIMEOUT = 0
        if   CALL in ["other", "python", "ruby"]:
            if TIMEOUT > 0:
                CTIMEOUT = CTIMEOUT + min(TIMEOUT, par['TIMEOUT'])
        elif CALL == "sqlXs":
            test = re.compile("^"+TST+"_s[0-9][0-9]"+EXT+"$", re.MULTILINE)
            d = listdir(os.getcwd())
            for f in d:
                if test.match(f):
                    CTIMEOUT = CTIMEOUT + TIMEOUT
        elif CALL in ["mal", "sql"]:
            CTIMEOUT = CTIMEOUT + TIMEOUT
        if  CTIMEOUT < TIMEOUT:
            CTIMEOUT = TIMEOUT
        STIMEOUT = CTIMEOUT
        if  SERVER in ["MAL", "SQL"] and TIMEOUT > 0:
            STIMEOUT = STIMEOUT + TIMEOUT + min(TIMEOUT, par['TIMEOUT'])

        ME = ""

        TestOutFile = TST+".test.out"
        TestErrFile = TST+".test.err"
        TestOut = openutf8(TestOutFile,"w")
        TestErr = openutf8(TestErrFile,"w")
        TestOut.write("stdout of test '"+TST+"` in directory '"+url(TSTDIR)+"` itself:\n\n")
        TestErr.write("stderr of test '"+TST+"` in directory '"+url(TSTDIR)+"` itself:\n\n")
        TestOut.close()
        TestErr.close()

        t0 = time.time()
        tres = DoIt(env, SERVER, CALL, TST, EXT, TestOutFile, TestErrFile, STIMEOUT, CTIMEOUT, TIMEOUT, ME, MAPIsockets, length, nomito, threads, user, passwd, COND, all_tests, pSrvr)

        t1 = time.time()
        TX = t1 - t0
        if not quiet:
            STDOUT.write(" %7.3fs " % TX)

        if tres == 'timeout':
            errcode = F_TIME
        elif tres == 'recursion':
            errcode = F_RECU
        elif tres == 'segfault':
            errcode = F_SEGV
        elif tres == 'abort':
            errcode = F_ABRT
        elif tres == 'socket':
            errcode = F_SOCK
        elif tres == 'error':
            errcode = F_WARN
        elif tres is not None:
            errcode = F_ERROR
        else:
            errcode = F_OK

        if pSrvr is None:
            sockerr = CheckSocket3(env, "MAPI", TestErrFile)
        elif pSrvr.poll() is None:
            sockerr = F_OK
        else:
            sres = returnCode(pSrvr.proc, openutf8(TestErrFile, 'a'))
            if sres == 'segfault':
                sockerr = F_SEGV
            elif sres == 'abort':
                sockerr = F_ABRT
            else:
                sockerr = F_ERROR

        #TODO:
        ##if [ ! -f $TSTTRGBASE/Tests/.old.left-over.tmp.bats. ] ; then  touch $TSTTRGBASE/Tests/.old.left-over.tmp.bats. ; fi
        ##LEFTOVERTMPBATS="`find $MONETDBFARM/dbfarm/*/bat/ -name tmp_\* -print 2> /dev/null`"
        ##if [ "$LEFTOVERTMPBATS" ] ; then
        ##      ls -alF $LEFTOVERTMPBATS 2> /dev/null > .all.left-over.tmp.bats.
        ##      diff -u0 $TSTTRGBASE/Tests/.old.left-over.tmp.bats. .all.left-over.tmp.bats. | grep '^\+[^\+]' > .new.left-over.tmp.bats.
        ##fi
        ##if [ -s .new.left-over.tmp.bats. ] ; then
        ##      echo -e "\n!ERROR: persistent temporary bats remained:" >> $LOGFILE.err
        ##      sed 's|^\+|! |g' .new.left-over.tmp.bats.               >> $LOGFILE.err
        ##      echo                                                    >> $LOGFILE.err
        ##fi
        ##rm -f .new.left-over.tmp.bats. $TSTTRGBASE/Tests/.old.left-over.tmp.bats.
        ##if [ -f .all.left-over.tmp.bats. ] ; then  mv -f .all.left-over.tmp.bats. $TSTTRGBASE/Tests/.old.left-over.tmp.bats. ; fi

        if tres == 'socket':
            if quiet:
                STDOUT.write("\n%s : Socket!\n" % TST)
            elif verbose:
                STDOUT.write("(Socket!) ")

        if tres == 'timeout':
            if quiet:
                STDOUT.write("\n%s : Timeout!\n" % TST)
            elif verbose:
                STDOUT.write("(Timeout!) ")

        if tres == 'recursion':
            if quiet:
                STDOUT.write("\n%s : Recursion!\n" % TST)
            elif verbose:
                STDOUT.write("(Recursion!) ")

        if tres == 'segfault':
            if quiet:
                STDOUT.write("\n%s : Crashed!\n" % TST)
            elif verbose:
                STDOUT.write("(Crashed!) ")

        if tres == 'signal':
            if quiet:
                STDOUT.write("\n%s : Signaled!\n" % TST)
            elif verbose:
                STDOUT.write("(Signaled!) ")

        if verbose:
            STDOUT.write("\n")

        try:
            STDOUT.flush()
        except IOError as err:
            Warn("Flushing STDOUT in RunTest failed with #%d: '%s'." % (err.errno, err.strerror))

        Mfilter.mFilter(TST+STABLEout,par['IGNORE'])
        Mfilter.mFilter(TST+STABLEerr,par['IGNORE'])
        Mfilter.mFilter(TST+".test.out",par['IGNORE'])
        Mfilter.mFilter(TST+".test.err",par['IGNORE'])

        if REV:
            d = '%s%s/%s' % (URLPREFIX, url(TSTDIR), TSTSUFF)
            if os.path.isfile(TST + EXT + '.src'):
                f = openutf8(TST + EXT + '.src').readline().strip()
                if f.startswith('$RELSRCDIR/'):
                    f = f[11:]
                    while f.startswith('../'):
                        f = f[3:]
                        d = d[:d.rindex('/')]
                f = '%s/%s' % (d, f)
            elif os.path.isfile(TST + EXT + '.in'):
                f = '%s/%s%s.in' % (d, TST, EXT)
            else:
                f = '%s/%s%s' % (d, TST, EXT)
            if testweb:
                # splice in a link to the bug report if we recognize a
                # reference
                res = bugre.search(TST)
                if res is not None:
                    bugno = res.group('bugno')
                    tst = '%s<a target="_blank" href="http://bugs.monetdb.org/%s">%s</a>%s' % (TST[:res.start(0)+1], bugno, res.group(0)[1:], TST[res.end(0):])
                else:
                    tst = TST
                titlefmt = '-tTest %s%s (id <a href="%s">%s</a>) (<a href="%s.%%s.diff.html">%%s</a>)' % (tst, EXT, f, REV, TST)
            else:
                # no need (and no space) to add link to bug report:
                # it's done already elsewhere
                titlefmt = '-tTest <a href="%s%s">%s%s</a> (id <a href="%s">%s</a>) (<a href="%s.%%s.diff.html">%%s</a>)' % (TST, EXT, TST, EXT, f, REV, TST)
        elif testweb:
            titlefmt = '-tTest %s%s (<a href="%s.%%s.diff.html">%%s</a>)' % (TST, EXT, TST)
        else:
            titlefmt = '-tTest <a href="%s%s">%s%s</a> (<a href="%s.%%s.diff.html">%%s</a>)' % (TST, EXT, TST, EXT, TST)
        diff_html = openutf8('%s.out.diff.html' % TST,"w")
        diff_html.write('<!--MajorDiffs-->\n')
        diff_html.close()
        timedout = True
        if tres is not None:
            # test program exited with error => expect major differences!
            ACCURACYout = -1
        else:
            szs = os.stat("%s%s.FILTERED" % (TST, STABLEout)).st_size
            szt = os.stat("%s.test.out.FILTERED" % TST).st_size
            if szt < szs*0.5 or szt > szs*1.5:
                # filesizes differ significantly => expect major differences!
                ACCURACYout = -1
        out = err = ''
        while timedout:
            cmd = ['Mdiff']
            if ACCURACYout == -1:
                ACCURACYout = 0
            else:
                cmd.append('-d')
            if not verbose:
                cmd.append('-q')
            cmd.extend(['-F^#', '-I%s' % par['IGNORE'],
                        '-C%s' % par['CONTEXT'], '-A%d' % ACCURACYout,
                        titlefmt % ('err', 'err'),
                        '%s%s.FILTERED' % (TST, STABLEout),
                        '%s.test.out.FILTERED' % TST,
                        '%s.out.diff.html' % TST])
            if procdebug:
                print('RunTest: starting process "%s"\n' % '" "'.join(cmd))
            setpgrp = True
            proc = process.Popen(cmd, stdout=process.PIPE,
                                 stderr=process.PIPE,
                                 text=True)
            proc.killed = False
            proc.onechild = False
            t = Timer(float(par['TIMEOUT']), killProc, args = [proc])
            try:
                t.start()
                out, err = proc.communicate()
                t.cancel()
                if verbose or quiet:
                    if out:
                        STDOUT.write(out)
                    if err:
                        sys.stderr.write(err)
                if procdebug:
                    print('RunTest: process exited "%s" (%s)\n' %
                          ('" "'.join(cmd), proc.returncode))
            except KeyboardInterrupt:
                t.cancel()
                killProc(proc)
                if procdebug:
                    print('RunTest: process killed "%s"\n' % '" "'.join(cmd))
                raise
            timedout = proc.killed
            ACCURACYout = ACCURACYout - 1
            if ACCURACYout < 0:
                timedout = False # don't try again
        if env.get('ECHO_DIFF'):
            cmd = ['diff']
            if ACCURACYout >= 0:
                cmd.append('-d')
            cmd.extend(['-Bb', '-F^#', '-I%s' % par['IGNORE'],
                        '-U%s' % par['CONTEXT'],
                        '%s%s.FILTERED' % (TST, STABLEout),
                        '%s.test.out.FILTERED' % TST])
            proc = process.Popen(cmd, text=True)
            proc.wait()

        diff_html = openutf8('%s.err.diff.html' % TST,"w")
        diff_html.write('<!--MajorDiffs-->\n')
        diff_html.close()
        timedout = True
        if tres is not None:
            # test program exited with error => expect major differences!
            ACCURACYerr = -1
        else:
            szs = os.stat("%s%s.FILTERED" % (TST, STABLEerr)).st_size
            szt = os.stat("%s.test.err.FILTERED" % TST).st_size
            if szt < szs*0.5 or szt > szs*1.5:
                # filesizes differ significantly => expect major differences!
                ACCURACYerr = -1
        while timedout:
            cmd = ['Mdiff']
            if ACCURACYerr == -1:
                ACCURACYerr = 0
            else:
                cmd.append('-d')
            if not verbose:
                cmd.append('-q')
            cmd.extend(['-F^#', '-I%s' % par['IGNORE'],
                        '-C%s' % par['CONTEXT'], '-A%d' % ACCURACYerr,
                        titlefmt % ('out', 'out'),
                        '%s%s.FILTERED' % (TST, STABLEerr),
                        '%s.test.err.FILTERED' % TST,
                        '%s.err.diff.html' % TST])
            if procdebug:
                print('RunTest: starting process "%s"\n' % '" "'.join(cmd))
            setpgrp = True
            proc = process.Popen(cmd, stdout=process.PIPE,
                                 stderr=process.PIPE,
                                 text=True)
            proc.killed = False
            proc.onechild = False
            t = Timer(float(par['TIMEOUT']), killProc, args = [proc])
            try:
                t.start()
                out, err = proc.communicate()
                t.cancel()
                if verbose or quiet:
                    if out:
                        STDOUT.write(out)
                    if err:
                        sys.stderr.write(err)
                if procdebug:
                    print('RunTest: process exited "%s" (%s)\n' %
                          ('" "'.join(cmd), proc.returncode))
            except KeyboardInterrupt:
                t.cancel()
                killProc(proc)
                if procdebug:
                    print('RunTest: process killed "%s"\n' % '" "'.join(cmd))
                raise
            timedout = proc.killed
            ACCURACYerr = ACCURACYerr - 1
            if ACCURACYerr < 0:
                timedout = False # don't try again
        if env.get('ECHO_DIFF'):
            cmd = ['diff']
            if ACCURACYerr >= 0:
                cmd.append('-d')
            cmd.extend(['-Bb', '-F^#', '-I%s' % par['IGNORE'],
                        '-U%s' % par['CONTEXT'],
                        '%s%s.FILTERED' % (TST, STABLEerr),
                        '%s.test.err.FILTERED' % TST])
            proc = process.Popen(cmd, text=True)
            proc.wait()

        FailedOut, FailedErr = CategorizeResult(TST, max(sockerr, errcode), outmissing, errmissing)
        if FailedOut == F_OK and FailedErr == F_OK and testweb:
            for f in ['%s.out.diff.html' % TST, '%s.test.out' % TST,
                      '%s.server.out' % TST, '%s.client.out' % TST,
                      '%s.test.out.FILTERED' % TST,
                      '%s%s.FILTERED' % (TST, STABLEout),
                      '%s.err.diff.html' % TST, '%s.test.err' % TST,
                      '%s.server.err' % TST, '%s.client.err' % TST,
                      '%s.test.err.FILTERED' % TST,
                      '%s%s.FILTERED' % (TST, STABLEerr)]:
                remove(f)

        if not testweb:
            elem = AddTstToHtmlIndex(env, TST, STABLEout, STABLEerr, EXT,
                                     FailedOut, FailedErr)

        if not verbose and not quiet:
            if tres == 'socket':
                prpurple('SOCKET')
            elif tres == 'timeout':
                prpurple('TIMEOUT')
            elif tres == 'recursion':
                prpurple('RECURSION')
            elif tres == 'segfault':
                prpurple('CRASHED')
            elif tres == 'abort':
                prpurple('ABORTED')
            elif tres == 'signal':
                prpurple('SIGNALED')
            else:
                if FailedOut == F_OK:
                    prgreen('OK   ')
                elif FailedOut == F_WARN:
                    prgreen('minor')
                elif FailedOut == F_MISSING:
                    prred('MISS ')
                else:
                    prred('MAJOR')
                STDOUT.write(' ')
                if FailedErr == F_OK:
                    prgreen('OK')
                elif FailedErr == F_WARN:
                    prgreen('minor')
                elif FailedErr == F_MISSING:
                    prred('MISS')
                else:
                    prred('MAJOR')
            STDOUT.write('\n')

    return TX,FailedOut,FailedErr,elem,reason,links
### RunTest(env, TST, BusyPorts, COND, oktests) #

def CheckPort(port) :
    # Since 'localhost' and $HOST (i.e., `hostname`) are usually
    # different interfaces, we check both, unless $HOST (`hostname`)
    # appears to be merely an alias for 'localhost'.  That is, if the
    # hostname works, we prefer it over localhost, but don't require it,
    # such as e.g. on interwebless laptops.
    busy = 0
    Serrno = 0
    Serrstr = ""
    S0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    S1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    S0.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    S1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host = os.environ['HOST']
    try:
        S1.bind((host,port))
    except socket.error as err:
        Serrno = err.errno
        Serrstr = err.strerror
        S1.close();
        host = 'localhost'
        try:
            S0.bind((host,port))
        except socket.error as err:
            Serrno = err.errno
            Serrstr = err.strerror
            S0.close()
            busy = 1

    return busy, host, Serrno, Serrstr, (S0, S1)
### CheckPort(port) #

def randomPort(l,h) :
    repeat = randomPortRepeat
    port = 0
    rpt = 0
    ports = []
    while rpt < repeat:
        port = random.randrange(l,h,1)
        ports.append(port)
        busy, host, Serrno, Serrstr, S = CheckPort(port)
        S[0].close()
        S[1].close()
        if busy:
            rpt = rpt + 1
            port = 0
        else:
            break
    return (port,host)
### randomPort(l,h) #

def CheckSocket2(env,SERVER) :  #,SrvrErr) :
    port = int(env[SERVER+'PORT'])
    newport = port
    busy, host, Serrno, Serrstr, S = CheckPort(port)
    if busy:
        S[0].close()
        S[1].close()
        Smsg = """
! Socket-Check failed for %sserver on <%s:%d> with #%d; '%s' !
""" % (SERVER, host, port, Serrno, Serrstr)
        newport = eval(dft[SERVER+'PORT'])
        if newport == 0:
            S[0].close()
            S[1].close()
            Smsg = Smsg + """
! Socket-Check failed for %sserver on <%s> !
! Giving up after %d attepts !
""" % (SERVER, host, randomPortRepeat)
            return None, Smsg

        env[SERVER+'PORT'] = newport
        os.environ[SERVER+'PORT'] = env[SERVER+'PORT']
        op = 'port=%d' % port
        np = 'port=%s' % env[SERVER+'PORT']
        env['exe']['mserver5']      = env['exe']['mserver5'][0]      , env['exe']['mserver5'][1].replace(op, np)
        env['exe']['MAL_Client']    = env['exe']['MAL_Client'][0]    , env['exe']['MAL_Client'][1].replace(op, np)
        env['exe']['SQL_Client']    = env['exe']['SQL_Client'][0]    , env['exe']['SQL_Client'][1].replace(op, np)
        env['exe']['SQL_Dump']      = env['exe']['SQL_Dump'][0]      , env['exe']['SQL_Dump'][1].replace(op, np)
        os.environ['MSERVER']       = os.environ['MSERVER'].replace(op, np)
        os.environ['MAL_CLIENT']    = os.environ['MAL_CLIENT'].replace(op, np)
        os.environ['SQL_CLIENT']    = os.environ['SQL_CLIENT'].replace(op, np)
        os.environ['SQL_DUMP']      = os.environ['SQL_DUMP'].replace(op, np)
        Smsg = Smsg + """
! Using new %sPORT=%s !
""" % (SERVER, env[SERVER+'PORT'])
#        STDERR.write(Smsg)
#        STDERR.flush()
#        SrvrErr.write(Smsg)
#        SrvrErr.flush()

    return S, None
### CheckSocket2(env,SERVER)    #,SrvrErr) #

def CheckSocket3(env,SERVER,ErrFileName) :
    res = F_OK
    port = int(env[SERVER+'PORT'])
    busy, host, Serrno, Serrstr, S = CheckPort(port)
    S[0].close()
    S[1].close()
    if busy:
        res = F_SOCK
        Smsg = """
! Socket-Check failed for %sserver on <%s:%d> with #%d; '%s' !
! %sPORT was not properly released by mserver5 !
""" % (SERVER, host, port, Serrno, Serrstr, SERVER)
        STDERR.write(Smsg)
        STDERR.flush()
        ErrFile = openutf8(ErrFileName, 'a')
        ErrFile.write(Smsg)
        ErrFile.flush()
        ErrFile.close()
    return res
### CheckSocket3(env,SERVER,ErrFileName) #

def prompt() :
    return time.strftime('%H:%M:%S> ',time.localtime(time.time()))
### prompt() #

def Prompt(cmd) :
    if type(cmd) is type([]):
        cmd = '" "'.join(cmd)
    prmpt = time.strftime('\n# %H:%M:%S >  ',time.localtime(time.time()))
    return '%s%s"%s"%s\n\n' % (prmpt, prmpt, cmd, prmpt)
### Prompt(cmd) #

def getkids():
    # return a dictionary with process IDs as key and a list of child
    # processes as value
    p = process.Popen(['ps', '-lu', os.getenv('USER')],
                      stdout=process.PIPE, stderr=process.PIPE,
                      text=True)
    out, err = p.communicate()
    if err:
        return {}
    lines = out.split('\n')
    line0 = lines[0].split()
    del lines[0]
    del lines[-1]
    pidcol = ppidcol = None
    for i in range(len(line0)):
        if line0[i] == 'PID':
            pidcol = i
        elif line0[i] == 'PPID':
            ppidcol = i
    if pidcol is None or ppidcol is None:
        return {}
    procs = {}
    for line in lines:
        line = line.split()
        try:
            pid = int(line[pidcol])
            ppid = int(line[ppidcol])
        except (ValueError, IndexError):
            continue
        if ppid not in procs:
            procs[ppid] = []
        procs[ppid].append(pid)
    return procs

def killchildren(pid, procs = None):
    # not called on Windows
    # kill the specified process ID and all its children
    if procs is None:
        try:
            os.killpg(pid, signal.SIGKILL)
            return
        except AttributeError:
            try:
                os.kill(-pid, signal.SIGKILL)
                return
            except OSError:
                pass
        except OSError:
            pass
        procs = getkids()
    for kid in procs.get(pid, []):
        killchildren(kid, procs)
    if procdebug:
        print('killing process %d' % pid)
    try:
        os.kill(pid, signal.SIGKILL)
    except OSError:
        if procdebug:
            print('killing process %d failed' % pid)

def reallyKill(proc):
    # not called on Windows
    killchildren(proc.pid, getkids())

def killProc(proc, outfile = None, cmd = None):
    if type(cmd) is type([]):
        cmd = ' '.join(cmd)
    if procdebug:
        print('timeout for process %d (%s)' % (proc.pid, cmd))
    if outfile is not None and cmd is not None:
        try:
            outfile.write('\n!Mtimeout: Timeout: %s\n' % cmd)
        except (ValueError, IOError):
            print('cannot write timeout message ' + cmd)
    if os.name == "nt":
        sym = ''
        if os.path.exists(r'c:\Program Files\Debugging Tools for Windows (x64)\cdb.exe'):
            cdb = r'c:\Program Files\Debugging Tools for Windows (x64)\cdb.exe'
            if os.path.exists(r'c:\Symbols'):
                sym = r'c:\Symbols;'
        elif os.path.exists(r'c:\Program Files\Debugging Tools for Windows (x86)\cdb.exe'):
            cdb = r'c:\Program Files\Debugging Tools for Windows (x86)\cdb.exe'
            if os.path.exists('c:\WINDOWS\Symbols'):
                sym = r'c:\WINDOWS\Symbols;'
        else:
            cdb = None
        if cdb:
            p = process.Popen([cdb, '-pv', '-p', str(proc.pid),
                               '-y', '%scache*;srv*http://msdl.microsoft.com/download/symbols' % sym, '-lines', '-c', '~*kP;!locks;q'],
                              stdout=process.PIPE, text=True)
            out, err = p.communicate()
        else:
            out = ''
    else:
        try:
            p = process.Popen(['pstack', str(proc.pid)], stdout=process.PIPE,
                              text=True)
            try:
                # pstack (gdb) sometimes hangs when trying to get the
                # stack trace: kill it mercilessly if it does
                t = Timer(60, reallyKill, args = [p])
                t.start()
            except AttributeError:
                t = None
            out, err = p.communicate()
            if t is not None:
                t.cancel()
        except:
            out = ''
    if outfile is not None and out:
        try:
            outfile.write('\n%s\n' % out)
        except (ValueError, IOError):
            print('cannot write stack trace')
            print(out)
    proc.killed = True
    if proc.onechild:
        if procdebug:
            print('killProc: calling proc.kill() on PID %d' % proc.pid)
        proc.kill()
    elif os.name == 'nt':
        if procdebug:
            print('killProc: starting process "taskkill" "/F" "/T" "/PID" "%s"\n' % str(proc.pid))
        p = process.Popen(['taskkill','/F','/T','/PID',str(proc.pid)],
                          stdout=process.PIPE, stderr=process.PIPE,
                          text=True)
        out, err = p.communicate()
        if procdebug:
            print('killProc: process exited "taskkill" "/F" "/T" "/PID" "%s" (%s)\n' % (str(proc.pid), proc.returncode))
        proc.kill()
    else:
        killchildren(proc.pid)

class ServerClass:
    def __init__(self, cmd, TestOut, TestErr, TimeOut, pollfile, port):
        self.proc = None
        self.timer = None
        self.outfile = TestOut
        self.errfile = TestErr
        self.code = None
        self.started = False
        self.cmd = cmd
        self.timeout = TimeOut
        self.pollfile = pollfile
        self.port = port

    def poll(self):
        return self.proc.poll()

    def terminate(self):
        self.timer.cancel()
        t = Timer(60, killProc, args = [self.proc, self.errfile, self.cmd])
        t.start()
        if os.name == 'nt':
            self.proc.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.proc.terminate()
        self.proc.wait()
        t.cancel()
        self.code = returnCode(self.proc, self.errfile)
        self.outfile.close()
        self.errfile.close()

    def LaunchIt(self):
        global setpgrp

        self.outfile.write(Prompt(self.cmd))
        self.outfile.flush()
        self.errfile.write(Prompt(self.cmd))
        self.errfile.flush()

        if procdebug:
            print('LaunchIt: starting process "%s" (inpipe)\n' % '" "'.join(self.cmd))
        setpgrp = True
        if self.pollfile:
            try:
                os.unlink(self.pollfile)
            except OSError:
                pass
        if os.name == "nt":
            proc = process.Popen(self.cmd, stdin=open(os.devnull), stdout=self.outfile,
                                 stderr=self.errfile, text=True,
                                 creationflags=process.CREATE_NEW_PROCESS_GROUP)
        else:
            proc = process.Popen(self.cmd, stdin=open(os.devnull), stdout=self.outfile,
                                 stderr=self.errfile, text=True)
        # maybe buffer output as it comes to avoid deadlock
        if self.outfile == process.PIPE:
            proc.stdout = process._BufferedPipe(proc.stdout)
        if self.errfile == process.PIPE:
            proc.stderr = process._BufferedPipe(proc.stderr)
        proc.killed = False
        proc.onechild = True
        t = Timer(self.timeout, killProc, args = [proc, self.errfile, self.cmd])
        t.start()
        self.proc = proc
        self.timer = t

        port = self.port
        if self.pollfile:
            while True:
                proc.poll()
                if proc.returncode is not None:
                    # exited
                    proc.wait()
                    t.cancel()
                    return
                if os.path.exists(self.pollfile):
                    break
                time.sleep(0.001)
        elif port is not None:
            while True:
                proc.poll()
                if proc.returncode is not None:
                    # exited
                    proc.wait()
                    t.cancel()
                    return
                if mapi_ping(port):
                    break
                time.sleep(0.1)
            port = None         # don't try again
        if port is not None and not mapi_ping(port):
            # check whether we can connect
            if os.name == "nt":
                proc.send_signal(signal.CTRL_BREAK_EVENT)
            else:
                proc.terminate()
            proc.wait()
            t.cancel()
            return
        self.started = True

### LaunchIt(cmd, TestIn, TestOut, TestErr, TimeOut, pollfile, port) #

def RunIt(cmd, onechild, TestIn, TestOut, TestErr, TimeOut) :
    global setpgrp
    if type(TestIn) is type(''):
        TestInput = TestIn
        TestIn = process.PIPE
    else:
        TestInput = None
    TestOut.write(Prompt(cmd))
    TestOut.flush()
    TestErr.write(Prompt(cmd))
    TestErr.flush()
    if procdebug:
        print('RunIt: starting process "%s"\n' % '" "'.join(cmd))
    setpgrp = True
    proc = process.Popen(cmd, stdin=TestIn, stdout=TestOut,
                         stderr=TestErr, text=True)
    proc.killed = False
    proc.onechild = onechild
    t = Timer(TimeOut, killProc, args = [proc, TestErr, cmd])
    try:
        t.start()
        # since both stdout and stderr are redirected to files,
        # communicate will not return any useful data
        proc.communicate(input = TestInput)
        t.cancel()
        if procdebug:
            print('RunIt: process exited "%s" (%s)\n' % ('" "'.join(cmd), proc.returncode))
    except KeyboardInterrupt:
        t.cancel()
        killProc(proc, TestErr, cmd)
        if procdebug:
            print('RunIt: process killed "%s"\n' % '" "'.join(cmd))
        raise
    rc = returnCode(proc, TestErr)
    if rc == 'interrupt':
        raise KeyboardInterrupt
    return rc
### RunIt(cmd, onechild, TestIn, TestOut, TestErr) #

def Log() :
    time.strftime('%H:%M:%S> ',time.localtime(time.time()))
### Log() #

def mapi_ping(port) :
    retry = 0
    wait = 1
    host = 'localhost'
    while retry < 3:
        retry += 1
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            flag = sock.recv(2)
            unpacked = struct.unpack( '<H', flag )[0]  # little endian short
            len = ( unpacked >> 1 )     # get length
            data = sock.recv(len)
            # we don't send
            return True
        except socket.error:
            pass
        time.sleep(wait)
    return False
### mapi_ping() #

def DoIt(env, SERVER, CALL, TST, EXT, TestOutFile, TestErrFile, STIMEOUT, CTIMEOUT, TIMEOUT, ME, MAPIsockets, length, nomito, threads, user, passwd, COND, all_tests, PSRVR) :
    ATJOB2 = ""
    STDERR.flush()
    if quiet:
        STDOUT.write(".")
    elif verbose:
        STDOUT.write('%s%s  (<=%d,%d,%d) ...' %
                     (prompt(), os.path.join(env['TSTDIR'], TST + EXT),
                      TIMEOUT, CTIMEOUT, STIMEOUT))
    else:
        if ttywidth > 0 and length + 10 + 21 >= ttywidth:
            # 10 - length of prompt()
            # 21 - length of time plus result
            l = ttywidth - 10 - 21 - 1
            if len(TST) <= l:
                s = '%-*s ' % (l, TST)
            else:
                s = '%s...%s ' % (TST[:l//2 - 2], TST[l//2+1-l:])
        else:
            s = '%-*s ' % (length, TST)
        STDOUT.write('%s%s' % (prompt(), s))
        if isatty and TIMEOUT > 0:
            s = '(<=%d,%d,%d)' % (TIMEOUT, CTIMEOUT, STIMEOUT)
            STDOUT.write(s + '\b' * len(s))

    try:
        STDOUT.flush()
    except IOError as err:
        Warn("Flushing STDOUT in DoIt failed with #%d: '%s'." % (err.errno, err.strerror))
    TSTDB = env['TSTDB']
    exe = env['exe']

    if MAPIsockets is not None:
        # Release reserved sockets and run the actual test
        MAPIsockets[0].close()
        MAPIsockets[1].close()

    returncode = None
    pSrvr = PSRVR
    try:
        if SERVER in ["MAL", "SQL"]:
            SrvrOutFile = TST+".server.out"
            SrvrErrFile = TST+".server.err"
            SrvrOut = openutf8(SrvrOutFile,"w")
            SrvrErr = openutf8(SrvrErrFile,"w")
            ClntOutFile = TST+".client.out"
            ClntErrFile = TST+".client.err"
            ClntOut = openutf8(ClntOutFile,"w")
            ClntErr = openutf8(ClntErrFile,"w")

            Srvr = splitcommand(exe['mserver5'][1])
            if nomito:
                try:
                    Srvr.remove('--forcemito')
                except ValueError:
                    pass
            if threads is not None:
                for i in range(len(Srvr)):
                    if Srvr[i].startswith('gdk_nr_threads='):
                        Srvr[i] = 'gdk_nr_threads=%s' % threads
                        break
            dbpath = os.path.join(env['GDK_DBFARM'], TSTDB)
            Srvr.append('--dbpath=%s' % dbpath)
            if env.get('MULTIFARM'):
                Srvr.append('--dbextra=%s' % os.path.join(env['GDK_DBFARM'], TSTDB + '_transient'))
                shutil.rmtree(os.path.join(env['GDK_DBFARM'], TSTDB + '_transient'),
                              ignore_errors = True)
                os.makedirs(os.path.join(env['GDK_DBFARM'], TSTDB + '_transient'))
            if os.path.isfile(TST + '.options5'):
                Srvr.extend(openutf8(TST + '.options5').read().split())
            lang=""

            if SERVER == "MAL":
                lang="mal"
            if SERVER == "SQL":
                lang="sql"

            # enable r integration in server
            if (not all_tests or (COND != None and "HAVE_LIBR" in COND)) and CONDITIONALS['HAVE_LIBR'] and CONDITIONALS['NOT_WIN32']:
                Srvr.extend(['--set', 'embedded_r=yes'])

            savepath = None
            savepypath = os.environ.get('PYTHONPATH')
            savepyhome = os.environ.get('PYTHONHOME')
            if (COND != None and "HAVE_LIBPY3" in COND) and CONDITIONALS['HAVE_LIBPY3']:
                # enable Python 3 integration in server
                if winreg is not None:
                    if env['TST_BITS'] == '32bit':
                        if sys.maxsize > 2**32:
                            regkey = r'SOFTWARE\Wow6432Node\Python\PythonCore\3.7-32\InstallPath'
                        else:
                            regkey = r'SOFTWARE\Python\PythonCore\3.7-32\InstallPath'
                    else:
                        regkey = r'SOFTWARE\Python\PythonCore\3.7\InstallPath'
                    try:
                        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regkey) as key:
                            instpath = winreg.QueryValue(key, None)
                            os.environ['PYTHONHOME'] = instpath
                            os.environ['PYTHONPATH'] = instpath + 'Lib'
                            savepath = os.environ['PATH']
                            os.environ['PATH'] = instpath.rstrip('\\') + os.pathsep + savepath
                    except WindowsError:
                        pass
                Srvr.extend(['--set', 'embedded_py=3'])

            # enable C integration in server
            Srvr.extend(['--set', 'embedded_c=true'])

            if PSRVR is None:
                pSrvr = ServerClass(Srvr, SrvrOut, SrvrErr, TIMEOUT, os.path.join(dbpath, '.started'), int(env['MAPIPORT']))
                pSrvr.LaunchIt()
            if savepath is not None:
                os.environ['PATH'] = savepath
                if savepypath:
                    os.environ['PYTHONPATH'] = savepypath
                else:
                    del os.environ['PYTHONPATH']
                if savepyhome:
                    os.environ['PYTHONHOME'] = savepyhome
                else:
                    del os.environ['PYTHONHOME']
        else:
            ClntOut = openutf8(TestOutFile, 'a')
            ClntErr = openutf8(TestErrFile, 'a')

        if SERVER not in ["MAL", "SQL"] or pSrvr.started:
            if   CALL == "other":
                cmd = [os.path.join(".", TST + EXT), TST]
                returncode = RunIt(cmd, False, "", ClntOut, ClntErr, CTIMEOUT)
            elif CALL == "python":
                cmd = splitcommand(exe['python'][1]) + [TST + EXT, TST]
                returncode = RunIt(cmd, False, "", ClntOut, ClntErr, CTIMEOUT)
            elif CALL in ["mal", "malXs"]:
                TSTs = []
                if CALL == "mal":
                    X=""
                else:
                    X="_s[0-9][0-9]"
                test = re.compile("^"+TST+X+EXT+"$", re.MULTILINE)
                d = listdir(os.getcwd())
                d.sort()
                for f in d:
                    if test.match(f):
                        TSTs.append(f)

                if CALL.startswith("mal"):
                    Clnt = splitcommand(exe['MAL_Client'][1])
                else:
                    Clnt = []   # cannot happen
                for f in TSTs:
                    returncode = RunIt(Clnt, True, openutf8(f), ClntOut, ClntErr, TIMEOUT)
                    if returncode:
                        break
            elif CALL == "sqltest":
                import MonetDBtesting.sqllogictest as sqllogictest
                sql = sqllogictest.SQLLogic(out=ClntErr)
                try:
                    sql.connect(hostname='localhost',
                                port=int(env['MAPIPORT']),
                                database=TSTDB)
                except:
                    returncode = 'error'
                else:
                    sql.drop()
                    try:
                        sql.parse(TST+EXT)
                    except sqllogictest.SQLLogicSyntaxError:
                        pass
                    except BrokenPipeError:
                        # server timeout
                        pass
                    sql.close()
            elif CALL in ["sql", "sqlXs"]:
                TSTs = []
                if CALL == "sql":
                    X=""
                else:
                    X="_s[0-9][0-9]"
                test = re.compile("^"+TST+X+EXT+"$", re.MULTILINE)
                d = listdir(os.getcwd())
                d.sort()
                for f in d:
                    if test.match(f):
                        TSTs.append(f)

                Clnt = splitcommand(exe['SQL_Client'][1])
                if user:
                    Clnt.append('-u%s' % user)
                if passwd:
                    Clnt.append('-P%s' % passwd)
                for f in TSTs:
                    returncode = RunIt(Clnt, True, openutf8(f), ClntOut, ClntErr, TIMEOUT)
                    if returncode:
                        break
            elif CALL == "R":
                Clnt = splitcommand(exe['R_Client'][1])
                RunIt(Clnt, False, openutf8(TST+EXT), ClntOut, ClntErr, TIMEOUT)
            elif CALL == "ruby":
                Clnt = splitcommand(exe['ruby_client'][1]) + [TST + EXT]

                Clnt[2], Clnt[1] = Clnt[1], Clnt[2]
                Clnt.append(env['TSTDB'])

                RunIt(Clnt, True, "", ClntOut, ClntErr, TIMEOUT)
        else:
            for fp in ClntOut,ClntErr:
                fp.write('\n\n! Server not ready; skipping attempt to start client!\n\n')
        ClntOut.close()
        ClntErr.close()
    finally:
        if SERVER in ["MAL", "SQL"] and pSrvr is not None:
            if PSRVR is None and pSrvr.started:
                pSrvr.terminate()
                if procdebug:
                    print('DoIt: process exited "%s" (%s)\n' % ('" "'.join(Srvr), pSrvr.code))

            AllOut = [SrvrOut, ClntOutFile]
            AllErr = [SrvrErr, ClntErrFile]
            TestOut = openutf8(TestOutFile, 'a')
            for q in AllOut:
                if type(q) is type(''):
                    n = q
                else:
                    n = q.name
                    q.close()
                q = openutf8(n, 'r')
                try:
                    TestOut.write(q.read())
                except IOError as err:
                    Warn("Reading from input '%s' or writing to output '%s' failed with #%d: '%s'." % (q.name, TestOut.name, err.errno, err.strerror))
                except MemoryError:
                    Warn("Reading from input '%s' or writing to output '%s' failed with 'MemoryError'." % (q.name, TestOut.name))
                TestOut.flush()
                q.close()
            TestErr = openutf8(TestErrFile, 'a')
            for q in AllErr:
                if type(q) is type(''):
                    n = q
                else:
                    n = q.name
                    q.close()
                q = openutf8(n,'r')
                TestErr.write(q.read())
                TestErr.flush()
                q.close()
        else:
            TestOut = try_open(TestOutFile, 'a')
            TestErr = try_open(TestErrFile, 'a')

        if TestOut is not None:
            TestOut.write(Prompt('Done.'))
            TestOut.close()
        if TestErr is not None:
            TestErr.write(Prompt('Done.'))
            TestErr.close()

    if returncode is None and pSrvr is not None:
        returncode = pSrvr.code # can still be None
    if returncode is not None:
        # something failed
        if returncode == 'interrupt':
            raise KeyboardInterrupt
        for err in ('timeout', 'segfault', 'abort', 'signal', 'error'):
            if returncode == err:
                return err
        return returncode       # remaining error (shouldn't get here)

    if CALL not in ('python', 'other', 'ruby'):
        # running mserver/mclient directly, so we know they didn't fail
        return None

    # Try to detect segfaults and the like
    # Try to detect aborts due to too deep recursion
    for (regexp, msg) in [("(^(|[^#]*[\t ])((Memory|Segmentation) [Ff]ault|Bus [Ee]rror|Aborted|Assertion (|.* )failed[:\.]|!FATAL: BATSIGabort:)([ \t]|$))",
                           'segfault'),
                          ("aborted too deep recursion",
                           'recursion'),
                          ("mal_mapi\.listen:operation failed: bind to stream socket port",
                           'socket')]:
        TO = re.compile(regexp, re.MULTILINE)
        # FIXME: this begs for a much nicer solution (100% copy of below)
        for f in (TestErrFile, TestOutFile):
            if os.path.isfile(f):
                for l in openutf8(f):
                    if TO.search(l):
                        return msg

    return None

### DoIt(env, SERVER, CALL, TST, EXT, TestOutFile, TestErrFile, STIMEOUT, CTIMEOUT, TIMEOUT, ME, MAPIsockets, length, nomito) #

def Check(command, input) :
    global setpgrp
    if procdebug:
        print('Check: starting process "%s" (inpipe,outpipe,errpipe)\n' % '" "'.join(command))
    setpgrp = True
    proc = process.Popen(command, stdin=process.PIPE, stdout=process.PIPE,
                         stderr=process.PIPE, text=True)
    proc.killed = False
    proc.onechild = True
    t = Timer(float(par['TIMEOUT']), killProc, args = [proc])
    try:
        t.start()
        qOut, qErr = proc.communicate(input = input)
        t.cancel()
        if procdebug:
            print('Check: process exited "%s" (%s)\n' % ('" "'.join(command), proc.returncode))
    except KeyboardInterrupt:
        t.cancel()
        killProc(proc)
        if procdebug:
            print('Check: process killed "%s"\n' % '" "'.join(command))
        raise
    qOut = qOut.split('\n')
    qErr = qErr.split('\n')
    failed = False
    if proc.returncode:
        qOut.append('! Exit 1')
        failed = True
    test = re.compile( r"^!WARNING: BATpropcheck: "                                          "|"
                       r"^!WARNING: monet_checkbat: "                                        "|"
                       r"^!WARNING: GDKlockHome: ignoring empty or invalid .gdk_lock."       "|"
                       r"^!WARNING: BBPdir: initializing BBP.",
                       re.MULTILINE)
    noErr = []
    for l in qOut+qErr:
        if l.startswith("!"):
            if test.match(l):
                if not l.startswith("!WARNING: "):
                    noErr.append(l+"\n")
            else:
                ErrMsg('"%s" failed:' % '" "'.join(command))
                failed = True
                if qOut and qOut[-1].startswith("! Exit 1"):
                    qErr.append(qOut.pop())
                for l in qOut+qErr:
                    STDERR.write(l)
                    STDERR.write("\n")
                STDERR.write("\n")
                STDERR.flush()
                #sys.exit(1)
    if noErr:
        STDOUT.flush()
        STDERR.writelines(noErr)
        STDERR.flush()
    return failed
### Check(command, input) #

def CheckClassPath() :
    if 'CLASSPATH' in os.environ:
        cp = os.environ['CLASSPATH']
        cpx = cp + os.pathsep
    else:
        cp = ''
        cpx = ''
    JARS = {
        'HAVE_MONETDBJDBC_JAR' : re.compile('^monetdb-jdbc-[0-9]\.[0-9]+(-[a-f0-9]{12})?\.jre[0-9]+\.jar$'),
        'HAVE_JDBCCLIENT_JAR'  : re.compile('^jdbcclient\.jre[0-9]+\.jar$'),
        'HAVE_JDBCTESTS_JAR'   : re.compile('^jdbctests\.jar$'),
    }
    # check for known JARs in CLASSPATH files
    for p in cp.split(os.pathsep):
        if os.path.isdir(p):
            for f in os.listdir(p):
                if not f.endswith('.jar'):
                    continue
                for C in JARS:
                    if JARS[C].match(f):
                        CONDITIONALS[C] = '#'
                        cp = os.path.join(p, f) + os.pathsep + cp
                        break
        elif os.path.isfile(p):
            f = os.path.basename(p)
            for C in JARS:
                if JARS[C].match(f):
                    CONDITIONALS[C] = '#'
                    break
    # check for known JARs in CLASSPATH directories
    # + fall-back using pkgdatadir/lib
    cpx += _configure(os.path.join('share','monetdb','lib'))
    for d in cpx.split(os.pathsep):
        if os.path.isdir(d):
            for f in listdir(d):
                p = os.path.join(d,f)
                if os.path.isfile(p):
                    if f == 'BugConcurrent_clients_SF_1504657.class':
                        C = 'HAVE_JDBCTESTS_DIR'
                        if not CONDITIONALS.get(C):
                            cp = cp + os.pathsep + d
                            CONDITIONALS[C] = '#'
                    else:
                        C = 'HAVE_%s' % f.upper().replace('.','_')
                        if C not in JARS:
                            C = 'HAVE_MONETDBJDBC_JAR'
                        if not CONDITIONALS.get(C) and JARS[C].match(f):
                            cp = cp + os.pathsep + p
                            CONDITIONALS[C] = '#'
    if cp:
        os.environ['CLASSPATH'] = cp
    if verbose:
        miss = ''
        for j in ['monetdbjdbc.jar', 'jdbcclient.jar', 'jdbctests.jar']:
            C = 'HAVE_%s' % j.upper().replace('.','_')
            if not CONDITIONALS.get(C):
                miss += ' "%s"' % j
        if miss:
            Warn('Could not find%s in\nCLASSPATH="%s"' % (miss,cpx))
    if CONDITIONALS.get('HAVE_MONETDBJDBC_JAR') and \
       ( CONDITIONALS.get('HAVE_JDBCTESTS_JAR') or
         CONDITIONALS.get('HAVE_JDBCTESTS_DIR') ):
        CONDITIONALS['HAVE_JDBCTESTS'] = '#'
### CheckClassPath() #

def SetExecEnv(exe,verbose) :
    if os.name == "nt":
        CALL = "call "
    else:
        CALL = ""
    if verbose:
        STDERR.flush()
    for v in exe.keys():
        if v == 'mserver5':
            V = 'MSERVER'
        else:
            V = v.upper()
        if exe[v][0]:
            os.environ[V] = CALL+exe[v][1]
        else:
            os.environ[V] = ""
        if verbose:
            print("%s = %s : %s" % (V, exe[v][0], exe[v][1]))
    if verbose:
        STDOUT.flush()
### SetExecEnv(exe,procdebug) #

def ReadMapproveRc(f) :
    v = {}
    v['SYST'] = SYST
    v['RELEASE'] = RELEASE
    v['DIST'] = DIST
    v['VERSION'] = VERSION
    v['BITS'] = ''
    v['INT128'] = ''
    v['SINGLE'] = ''
    v['ARCH'] = ''
    if os.path.isfile(f):
        r = re.compile('^([A-Z][A-Z0-9_]*) = "(.*)".*$')
        for l in openutf8(f):
            m = r.match(l)
            if m:
                v[m.group(1)] = m.group(2)
    return v
### ReadMapproveRc(f) #

#############################################################################
#       MAIN

THISFILE = os.path.basename(sys.argv[0])
THISPATH = os.path.realpath(os.path.dirname(sys.argv[0]))
dftIGNORE = r'^\(| \|\)#'
TSTDBG = str(2+8)
TSTTHREADS = "0"
dftTSTPREF = "mTests"
TSTSUFF = "Tests"

if os.name != 'nt' and hasattr(os, "symlink"):
    SymlinkOrCopy = os.symlink
    listdir = os.listdir
else:
    def SymlinkOrCopy(src, dst):
        shutil.copy(os.path.normpath(os.path.join(os.getcwd(), src)), dst)
    def listdir(d):
        return os.listdir(os.path.abspath(d))

HOST = 'localhost'
if 'HOST' in os.environ:
    HOST = os.environ['HOST']
#else:
#    HOST = ''
elif os.name != "nt":
    HOST = os.uname()[1]
elif 'COMPUTERNAME' in os.environ:
    HOST = os.environ['COMPUTERNAME']
##else:
##    HOST = "WIN2000"
if 'DOMAIN' in os.environ:
    HOST = HOST.replace('.'+os.environ('DOMAIN'),'')
else:
    HOST = HOST.split('.', 1)[0]
os.environ['HOST'] = HOST
# check the host port actually works
_, HOST = randomPort(30000,39999)
os.environ['HOST'] = HOST
os.environ['MAPIHOST'] = HOST

if os.name == "nt":
    SYST    = "Windows"
    RELEASE = "5.0"
    r = re.compile('^Microsoft Windows (.*)\[Version ([0-9]+\.[0-9]+)([^\[0-9].*)\]$')
    if procdebug:
        print('starting process "cmd" "/c" "ver" (inpipe,outpipe)\n')
    proc = process.Popen('cmd /c ver', stdin=process.PIPE,
                         stdout=process.PIPE, stderr=process.PIPE,
                         text=True)
    qOut, qErr = proc.communicate()
    if procdebug:
        print('process exited "cmd" "/c" "ver" (%s)\n' % proc.returncode)
    for l in qOut.split('\n'):
        m = r.match(l.strip())
        if m and m.group(2):
            RELEASE = m.group(2)
else:
    SYST    = os.uname()[0].split("_NT-", 1)[0].replace("-","")
    if SYST == "AIX":
        RELEASE = os.uname()[3]+"."+os.uname()[2]
    else:
        RELEASE = os.uname()[2].split("(", 1)[0]
        MAJOR = RELEASE.split(".", 1)[0]
        if "A" <= MAJOR and MAJOR <= "Z":
            RELEASE = RELEASE.split(".", 1)[1]

# see if we can use UNIX sockets
try:
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
except (socket.error, AttributeError):
    # apparently not
    SOCK = False
else:
    SOCK = True

if SYST == "Linux":
    #  Please keep this aligned / in sync with configure.ag !
    LINUX_DIST=''
    if os.path.isfile('/etc/os-release'):
        l = open('/etc/os-release').read()
        x0 = re.search('^NAME=[\'"]?([^\'"\n]*)[\'"]?$', l, re.MULTILINE)
        if x0:
            x0 = x0.group(1)
        x1 = re.search('^VERSION_ID=[\'"]?([^\'"\n]*)[\'"]?$', l, re.MULTILINE)
        if x1:
            x1 = x1.group(1)
        LINUX_DIST = '%s:%s' % (x0 or 'Linux', x1 or '')
    elif os.path.isfile('/etc/fedora-release'):
        l = open('/etc/fedora-release').readline()
        x = re.match('^.*(Fedora).* release ([0-9][^ \n]*)( .*)*$', l)
        if x:
            LINUX_DIST = '%s:%s' % (x.group(1),x.group(2))
    elif os.path.isfile('/etc/centos-release'):
        l = open('/etc/centos-release').readline()
        x = re.match('^(CentOS).* release ([0-9][^ \n]*)( .*)*$', l)
        if x:
            LINUX_DIST = '%s:%s' % (x.group(1),x.group(2))
    elif os.path.isfile('/etc/yellowdog-release'):
        l = open('/etc/yellowdog-release').readline()
        x = re.match('^(Yellow) Dog Linux release ([0-9][^ \n]*)( .*)*$', l)
        if x:
            LINUX_DIST = '%s:%s' % (x.group(1),x.group(2))
    elif os.path.isfile('/etc/redhat-release'):
        l = open('/etc/redhat-release').readline()
        x0 = re.match('^.*(Red) (Hat).* Linux *([A-Z]*) release ([0-9][^ \n]*)( .*)*$', l)
        x1 = re.match('^Red Hat Enterprise Linux ([AW]S) release ([0-9][^ \n]*)( .*)*$', l)
        x2 = re.match('^(CentOS).* release ([0-9][^ \n]*)( .*)*$', l)
        x3 = re.match('^(Scientific) Linux SL release ([0-9][^ \n]*)( .*)*$', l)
        if x0:
            LINUX_DIST = '%s%s:%s%s' % (x0.group(1),x0.group(2),x0.group(4),x0.group(3))
        elif x1:
            LINUX_DIST = 'RHEL:%s%s' % (x1.group(2),x1.group(1))
        elif x2:
            LINUX_DIST = '%s:%s' % (x2.group(1),x2.group(2))
        elif x3:
            LINUX_DIST = '%s:%s' % (x3.group(1),x3.group(2))
    elif os.path.isfile('/etc/SuSE-release'):
        l = open('/etc/SuSE-release').readline()
        x0 = re.match('^.*(S[Uu]SE) LINUX Enterprise ([SD])[ervsktop]* ([0-9][^ \n]*)( .*)*$', l)
        x1 = re.match('^S[Uu]SE LINUX Enterprise ([SD])[ervsktop]* ([0-9][^ \n]*)( .*)*$', l)
        x2 = re.match('^.*(S[Uu]SE) [Ll][Ii][Nn][Uu][Xx].* ([0-9][^ \n]*)( .*)*$', l)
        x3 = re.match('^open(S[Uu]SE) ([0-9][^ \n]*)( .*)*$', l)
        if x0:
            LINUX_DIST = '%s:%sE%s' % (x0.group(1),x0.group(3),x0.group(2))
        elif x1:
            LINUX_DIST = 'SLE%s:%s' % (x1.group(1),x1.group(2))
        elif x2:
            LINUX_DIST = '%s:%s' % (x2.group(1),x2.group(2))
        elif x3:
            LINUX_DIST = '%s:%s' % (x3.group(1),x3.group(2))
    elif os.path.isfile('/etc/gentoo-release'):
        l = open('/etc/gentoo-release').readline()
        x = re.match('^.*(Gentoo) Base System.* [versionrelease]* ([0-9][^ \n]*)( .*)*$', l)
        if x:
            LINUX_DIST = '%s:%s' % (x.group(1),x.group(2))
    elif os.path.isfile('/etc/lsb-release'):
        x0 = x1 = None
        for l in open('/etc/lsb-release'):
            if not x0:
                x0 = re.match('^DISTRIB_ID=([^ \n]*)( .*)*$', l)
            if not x1:
                x1 = re.match('^DISTRIB_RELEASE=([^ \n]*)( .*)*$', l)
        if x0 and x1:
            LINUX_DIST = '%s:%s' % (x0.group(1),x1.group(1))
    elif os.path.isfile('/etc/debian_version'):
        LINUX_DIST = "Debian:"+open('/etc/debian_version').readline().strip()
    if not LINUX_DIST:
        LINUX_DIST = SYST+':'+re.match('^([0-9\.]*)([^0-9\.].*)$', RELEASE).group(1)
    DIST,VERSION = LINUX_DIST.split(':', 1)
elif SYST == "SunOS" and os.path.isfile('/etc/release'):
    (DIST,VERSION,rest) = open('/etc/release').readline().strip().split(' ',2)
else:
    DIST = SYST
    VERSION = RELEASE

SYSTVER = SYST+RELEASE
DISTVER = DIST+VERSION
os.environ['SYST'] = SYST
os.environ['SYSTVER'] = SYSTVER
os.environ['RELEASE'] = RELEASE
os.environ['DIST'] = DIST
os.environ['DISTVER'] = DISTVER
os.environ['VERSION'] = VERSION

if 'HTMLTITLE' in os.environ:
    HTMLTITLE = os.environ['HTMLTITLE']
else:
    HTMLTITLE = "{} results on {} ({})".format(THISFILE, HOST, DISTVER)       #"+ ("`date`")"

URLPREFIX = 'http://dev.monetdb.org/hg/MonetDB/file/'

par = {}
dft = {}

class OrAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(OrAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        # if first time, override (default) value, otherwise bitwise OR values
        if '__seen_option_' + self.dest in namespace:
            setattr(namespace, self.dest, getattr(namespace, self.dest) | values)
        else:
            setattr(namespace, self.dest, values)
        setattr(namespace, '__seen_option_' + self.dest, True)

def main(argv) :
    #TODO:
    #signal.signal(signal.SIGALRM, AlarmHandler)
    global global_timeout

    VARS = ['TSTSRCBASE', 'TSTTRGBASE']
    if THISFILE == "Mtest.py":
        VARS = VARS + [ 'MALCLIENT', 'SQLCLIENT', 'SQLDUMP', 'RCLIENT', 'RUBYCLIENT']    #, 'MONETDB_MOD_PATH' ]

    env = {}

    # most intuitive (?) default settings
    dft['TSTSRCBASE']     = r"_configure('/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11')"
    dft['TSTTRGBASE']     = r"_configure('/usr/local')"   # or os.getcwd() ?
    if THISFILE == "Mtest.py":
        dft['GDK_DEBUG']      = "TSTDBG"
        dft['GDK_NR_THREADS'] = "TSTTHREADS"
        dft['MONETDB_MOD_PATH'] = "''"
        dft['setMONETDB_MOD_PATH'] = "'--set \"monet_mod_path='+env['MONETDB_MOD_PATH']+'\"'"
        dft['MAPIPORT']       = "str(randomPort(30000,39999)[0])"
        dft['MALCLIENT']      = "'mclient -lmal -ftest -tnone -Eutf-8'"
        dft['SQLCLIENT']      = "'mclient -lsql -ftest -tnone -Eutf-8'"
        dft['SQLDUMP']        = "'msqldump -q'"
        dft['RUBYCLIENT']     = "'ruby'"

        r_noecho = '--no-echo'
        if CheckExec('R'):
            proc = process.Popen(['R', '--version'],
                                 stdout=process.PIPE, stderr=process.PIPE,
                                 text=True)
            r_out, r_err = proc.communicate()
            res = re.search(r'R version (?P<major>\d+)\.', r_out)
            if res is not None and int(res.group('major')) < 4:
                r_noecho = '--slave'
            if CONDITIONALS['HAVE_LIBR']:
                proc = process.Popen(['R', r_noecho, '--no-save', '--no-restore',
                                      '-e', 'print(Sys.getenv("R_LIBS_USER"))'],
                                     stdout=process.PIPE, stderr=process.PIPE,
                                     text=True)
                r_out, r_err = proc.communicate()
                res = re.search(r'\[\d+\] "(?P<dir>.*)"', r_out)
                if res is not None:
                    rdir = os.path.expanduser(res.group('dir'))
                    if not os.path.exists(rdir):
                        os.makedirs(rdir)
        dft['RCLIENT'] = "'R --vanilla {}'".format(r_noecho)

    #par = {}
    # get current environment
    env['HOST'] = os.environ['HOST']
    for v in VARS:
        if v in os.environ:
            env[v] = os.environ[v]
            #TODO:
            # make sure, that PATHs are absolute

    # commandline options overrule environment
    parser = argparse.ArgumentParser(usage='%(prog)s [options] ( [<dir>] [<tests>] | [<dirs>] )', epilog='See %s for details about Mtest.py.' % _configure(os.path.join('/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11','testing','README')))
    parser.add_argument('--version', action='version', version='11.39.11')
    parser.add_argument('--recursive', '-r', action='store_true', dest='recursive', help="recurse into subdirectories (implies 'All')")
    parser.add_argument('--revision', action='store', dest='revision', metavar='<hgid>', help='use given revision as the HG short hash')
    parser.add_argument('--TSTSRCBASE', action='store', dest='TSTSRCBASE', metavar='<path>', help='default: "%s"' % _configure('/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11'))
    parser.add_argument('--TSTTRGBASE', action='store', dest='TSTTRGBASE', metavar='<path>', help='default: "%s"' % _configure('/usr/local'))
    parser.add_argument('--quiet', '-q', action='store_true', dest='quiet', help="suppress messages on stdout")
    parser.add_argument('--verbose', '-v', action='store_true', dest='verbose', help="more verbose test output")
    parser.add_argument('--procdebug', action='store_true', dest='procdebug', help='process debugging (Mtest developers only)')

    if THISFILE == "Mtest.py":
        parser.add_argument('-I', action='store', dest='ignore', default=dftIGNORE, metavar='<exp>', help="ignore lines matching <exp> during diff (default: '%s')" % dftIGNORE)
        parser.add_argument('-C', action='store', dest='context', metavar='<num>', type=int, default=1, help="use <num> lines of context during diff (default: -C1)")
        parser.add_argument('-A', action='store', dest='accuracy', metavar='<num>', type=int, default=1, help="accuracy for diff: 0=lines, 1=words, 2=chars (default: -A1)")
        parser.add_argument('-t', action='store', dest='timeout', metavar='<sec>', type=int, default=60, help="timeout: kill (hanging) tests after <sec> seconds;\n-t0 means no timeout (default: -t60)")
        parser.add_argument('--debug', '-d', action=OrAction, dest='debug', metavar='<num>', type=int, default=int(TSTDBG), help="debug value to be used by mserver5, multiple -d options are ORed together (default: -d%s)\n(see `mserver5 --help' for details)" % TSTDBG)
        parser.add_argument('--nr_threads', '-n', action='store', dest='nr_threads', metavar='<num>', type=int, default=int(TSTTHREADS), help="number of threads for mserver5 (default: -n%s)\n-n0 => mserver5 automatically determines the number of CPU cores" % TSTTHREADS)
        parser.add_argument('--monet_mod_path', action='store', dest='monet_mod_path', metavar='<pathlist>', help="override mserver5's default module search path")
        parser.add_argument('--dbfarm', action='store', dest='gdk_dbfarm', default=_configure(os.path.join('/usr/local/var','MonetDB')), metavar='<directory>', help="override default location of database directory")
        parser.add_argument('--MALCLIENT', action='store', dest='MALCLIENT', metavar='<mal-client program>', help='default: %s' % dft['MALCLIENT'])
        parser.add_argument('--SQLCLIENT', action='store', dest='SQLCLIENT', metavar='<sql-client program>', help='default: %s' % dft['SQLCLIENT'])
        parser.add_argument('--SQLDUMP', action='store', dest='SQLDUMP', metavar='<sql-dump program>', help='default: %s' % dft['SQLDUMP'])
        parser.add_argument('--RCLIENT', action='store', dest='RCLIENT', metavar='<R program>', help='default: %s' % dft['RCLIENT'])
        parser.add_argument('--RUBYCLIENT', action='store', dest='RUBYCLIENT', metavar='<ruby program>', help='default: %s' % dft['RUBYCLIENT'])
        parser.add_argument('--concurrent', action='store_true', dest='concurrent', help='There are concurrent Mtest runs using the same MonetDB installation')
        parser.add_argument('--dbg', action='store', dest='dbg', metavar='<debugger/valgrind>', help="debugger to start before each server")
        parser.add_argument('--echo-diff', action='store_true', dest='echo_diff', help="echo differences between stable and current test output to console (stdout)")
        parser.add_argument('--mserver_set', action='store', dest='mserver_set', metavar='<mserver5_option>', help="This passes a single set to the server")
        parser.add_argument('--no-clean', action='store_true', dest='no_clean', help='Do not clean up before test')
        parser.add_argument('--testweb', action='store_true', dest='testweb', help='Optimize testing for testweb')
        parser.add_argument('--releaserun', action='store_true', dest='releaserun', help='run tests as if for a release test')
        parser.add_argument('--multifarm', action='store_true', dest='multifarm', help='use multiple dbfarms (developers only)')
        parser.add_argument('--nomito', action='store_true', dest='nomito', help='Do not pass --forcemito to server')
        parser.add_argument('--jenkins', action='store_true', dest='jenkins', help='special handling for Jenkins')
        parser.add_argument('--addreqs', action='store_true', dest='addreqs', help='automatically add required tests when testing individual tests')
        parser.add_argument('--global_timeout', '-T', action='store', dest='global_timeout', type=int, default=global_timeout, metavar='<sec>', help='global timeout')
        parser.add_argument('--data_path', '-D', action='store', dest='data_path', metavar='<path>', help='Path to the root directory of the data files needed for testing')
        parser.add_argument('--alltests', action='store_true', dest='alltests', help='also run tests that are known to fail')
        parser.add_argument('--initdb', action='store', dest='initdb', metavar='<zipfile>', help='zip file with contents for initial database')
        parser.add_argument('--single-in-memory', action='store_true', dest='single_in_memory', help='use --in-memory for SingleServer directories')
    elif THISFILE == 'Mapprove.py':
        f = _configure(os.path.join('/usr/local',dftTSTPREF,'.Mapprove.rc'))
        v = ReadMapproveRc(f)
        for i in 'INT128', 'SINGLE':
            if v[i]:
                v[i] = '[.%s]' % v[i]
        parser.add_argument('-x', action='store', dest='ext', choices=['out', 'err'], metavar='<ext>', help="approve only output files *.<ext><sys> (<ext> = 'out' or 'err')\n(default: <ext> = 'out' & 'err')")
        parser.add_argument('-S', action='store', dest='sys', metavar='<sys>', help="approve specific output *.<ext><sys>\n(<sys> = '[.(<SYST>[<RELEASE>]|<DIST>[<VERSION>])][.((32|64)bit|<ARCH>)][.int128][.single]',\n(default: longest match for <sys> = '[.(%s[%s]|%s[%s])][.(%s|%s)%s%s')" % (v['SYST'], v['RELEASE'], v['DIST'], v['VERSION'], v['BITS'], v['ARCH'], v['INT128'], v['SINGLE']))
        parser.add_argument('-f', action='store_true', dest='force', help="force approval of error messages (i.e., lines starting with '!')")
        parser.add_argument('--nopatch', action='store_true', dest='nopatch', help="do not attempt to patch other outputs")

    parser.add_argument('tests', nargs='*', help='The positional arguments are either a list of one or more directories to be tested, or a single directory followed by a list of tests within that directory.')
    opts = parser.parse_args()
    args = opts.tests

    recursive = opts.recursive
    global testweb
    testweb = False
    global quiet
    quiet = opts.quiet
    global verbose
    verbose = opts.verbose
    if quiet and verbose:
        ErrExit('--verbose and --quiet are mutually exclusive')
    global procdebug
    procdebug = opts.procdebug
    nomito = False
    jenkins = False
    addreqs = False
    all_tests = False
    if THISFILE == "Mtest.py":
        testweb = opts.testweb
        CONDITIONALS['RELEASERUN'] = opts.releaserun
        nomito = opts.nomito
        par['IGNORE'] = opts.ignore
        par['CONTEXT'] = str(opts.context)
        a = opts.accuracy
        if testweb or int(MonetDB_VERSION[1])%2 == 0 or opts.alltests or CONDITIONALS['MERCURIAL']:
            CONDITIONALS['KNOWNFAIL'] = 'execute'
        if a not in (-1,0,1,2):
            ErrExit('Accuracy for diff (-A) must be one of: 0=lines, 1=words, 2=chars !')
        par['ACCURACY'] = a
        par['TIMEOUT'] = opts.timeout
        env['GDK_DEBUG'] = str(opts.debug)
        env['GDK_NR_THREADS'] = str(opts.nr_threads)
        a = opts.monet_mod_path
        if a is not None:
            env['MONETDB_MOD_PATH'] = a
        a = opts.gdk_dbfarm
        if a is not None:
            env['GDK_DBFARM'] = a
        a = opts.concurrent
        if a:
            env['CONCURRENT'] = a
        a = opts.dbg
        if a is not None:
            env['DBG'] = a
        a = opts.echo_diff
        if a:
            env['ECHO_DIFF'] = a
        a = opts.mserver_set
        if a is not None:
            env['MSERVER_SET'] = "--set " + a
        else:
            env['MSERVER_SET'] = ""
        a = opts.no_clean
        if a:
            env['NOCLEAN'] = a
        a = opts.multifarm
        if a:
            env['MULTIFARM'] = 'True'
        jenkins = opts.jenkins
        addreqs = opts.addreqs
        a = opts.global_timeout
        if a:
            global_timeout = a
        a = opts.data_path
        if a is not None:
            env['TSTDATAPATH'] = a
        global initdb
        initdb = opts.initdb
        global single_in_memory
        single_in_memory = opts.single_in_memory
    if THISFILE == 'Mapprove.py':
        a = opts.ext
        if a is None:
            par['EXTENSION'] = ['out', 'err']
        elif a in ('out', 'err'):
            par['EXTENSION'] = [a]
        else:
            ErrXit("Extension (-x) must be one of: 'out', 'err' !")
        par['FORCE'] = opts.force
        par['NOPATCH'] = opts.nopatch
        a = opts.sys
        if a is None:
            par['SYSTEM'] = ''
        else:
            par['SYSTEM'] = a
            # -S option implies --nopatch
            par['NOPATCH'] = True
    for v in VARS:
        a = vars(opts).get(v)
        if a is not None:
            env[v] = a

    # display par's
    STDERR.flush()
    if verbose:
        for v in par.keys():
            #os.environ[v] = par[v]
            print("%s = %s" % (v, str(par[v])))
    STDOUT.flush()
    #env['par'] = par

    # unknown at compile time, as Mtest.py is compiled with MonetDB;
    # hence, we set them at runtime.
    # X == true   =>  ='',  ='#'
    # X == false  =>  ='#', =''
    python_version = ''
    if CheckExec('python'):
        proc = process.Popen(['python', '-c', 'import sys; print(sys.version[:1])'],
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        pyout, pyerr = proc.communicate()
        if proc.returncode == 0 and pyout:
            python_version = pyout.strip()
            os.environ['PYTHON' + python_version] = 'python'
    if python_version == '3':
        py3list = ['python']
    else:
        py3list = []
    for py3 in py3list + ['python3', 'python3.7', 'python3.6', 'python3.5', 'python3.4']:
        if CheckExec(py3):
            try:
                proc = process.Popen([py3, '-c', 'import pymonetdb'],
                                     stdout=process.PIPE, stderr=process.PIPE,
                                     text=True)
                pyout, pyerr = proc.communicate()
                if proc.returncode == 0:
                    CONDITIONALS['HAVE_PY3MONETDB'] = '#'
                    os.environ['PYTHON3'] = py3
                    break
            except OSError:
                pass
    else:
        CONDITIONALS['HAVE_PY3MONETDB'] = '' # no pymonetdb for python3
    try:
        import pymonetdb
    except ImportError:
        print('Python available, but pymonetdb package not available')
    else:
        CONDITIONALS['HAVE_PYMONETDB'] = '#'
    try:
        import lz4
    except ImportError:
        CONDITIONALS['HAVE_PYTHON_LZ4'] = False
    else:
        CONDITIONALS['HAVE_PYTHON_LZ4'] = True
    if 'PYTHON3' in os.environ:
        proc = process.Popen([os.environ['PYTHON3'], '-c', 'import scipy'],
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        pyout, pyerr = proc.communicate()
        if proc.returncode == 0:
            CONDITIONALS['HAVE_LIBSCIPY3'] = '#'
        # proc = process.Popen([os.environ['PYTHON3'], '-c', 'import pandas'],
        #                      stdout=process.PIPE, stderr=process.PIPE,
        #                      text=True)
        # pyout, pyerr = proc.communicate()
        # if proc.returncode == 0:
        #     CONDITIONALS['HAVE_LIBPANDAS3'] = '#'
    if env.get('TSTDATAPATH'):
        CONDITIONALS['HAVE_DATA_PATH'] = '#'
    if CheckExec('perl'):
        proc = process.Popen(['perl', '-e', 'use MonetDB::CLI::MapiPP; use DBI;'],
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        perl_out, perl_err = proc.communicate()
        if proc.returncode == 0:
            CONDITIONALS['HAVE_PERL'] = '#'
        else:
            print('Perl available, but MonetDB driver or DBI module not available')
    if CheckExec('php'):
        phpcmd = ['php']
        if 'PHP_INCPATH' in os.environ:
            phpcmd.extend(['-d', 'include_path=%s' % os.environ['PHP_INCPATH']])
        phpcmd.extend(['-r', "require 'monetdb/php_monetdb.php';"])
        proc = process.Popen(phpcmd,
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        php_out, php_err = proc.communicate()
        if proc.returncode == 0:
            CONDITIONALS['HAVE_PHP'] = '#'
        else:
            print('PHP available, but MonetDB driver not available')
    if CheckExec('ruby'):
        # also check ruby version; we require >= 1.9 for "require_relative"
        proc = process.Popen(['ruby', '--version'],
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        ruby_out, ruby_err = proc.communicate()
        ruby_reg = re.compile("^[^ ]* ([0-9]+)\.([0-9]+)[^0-9].*$", re.MULTILINE)
        ruby_ver = ruby_reg.match(ruby_out)
        if ruby_ver and \
           100 * int(ruby_ver.group(1)) + int(ruby_ver.group(2)) >= 109:
            # now check whether the monetdb-ruby gem is available
            proc = process.Popen(['ruby', '-e', "require 'MonetDB'"],
                                 stdout=process.PIPE, stderr=process.PIPE,
                                 text=True)
            ruby_out, ruby_err = proc.communicate()
            if proc.returncode == 0:
                CONDITIONALS['HAVE_RUBY'] = '#'
            else:
                print('Ruby available, but MonetDB gem not available')
    CheckClassPath()

    # tidy-up and fall-back to defaults where necessary
    if THISFILE == "Mtest.py":
        vars_ = VARS + ['MAPIPORT', 'GDK_DEBUG', 'GDK_NR_THREADS', 'MONETDB_MOD_PATH']
    else: # THISFILE == "Mapprove.py"
        vars_ = VARS
    for v in vars_:
        if v not in env:
            env[v] = eval(dft[v])
            #TODO:
            # make sure, that PATHs are absolute
    if THISFILE == "Mtest.py":
        if env['MAPIPORT'] == 0:
            ErrXit('Cannot find a workable MAPIPORT')
        if env['MONETDB_MOD_PATH']:
            env['setMONETDB_MOD_PATH'] = eval(dft['setMONETDB_MOD_PATH'])
        else:
            env['setMONETDB_MOD_PATH'] = ''
        if 'DBG' in env:
            env['setDBG'] = env['DBG']
        else:
            env['setDBG'] = ''

    #TODO:
    ## in case of inconsistencies, try to fallback to "save" settings
    #
    #if not os.path.indir(TSTSRCBASE):
    #       ErrXit("Illegal TSTSRCBASE: directory '"+a"` does not exist!")

    # ensure consistent TSTSRCBASE
    if os.path.basename(env['TSTSRCBASE']) == TSTSUFF and \
            os.path.isfile(os.path.join(env['TSTSRCBASE'], "All")):
        ErrXit('TSTSRCBASE itself must not be a test-directory, i.e., called "%s" and contain an "All" file!' % TSTSUFF)

    # make TSTxxxBASE absolute physical paths
    for p in 'TSTSRCBASE', 'TSTTRGBASE':
        if os.path.isdir(env[p]):
            rp = os.path.realpath(env[p])
            if verbose and os.path.normcase(rp) != os.path.normcase(env[p]):
                Warn("%s: Replacing logical path  %s  by absolute physical path  %s" % (p, env[p], rp))
            env[p] = rp
        else:
            ErrXit("Illegal "+p+": directory '"+env[p]+"' does not exist!")


    global TSTTRGBASE
    TSTTRGBASE = env['TSTTRGBASE']
    global TSTSRCBASE
    TSTSRCBASE = env['TSTSRCBASE']
    global TSTDATAPATH
    TSTDATAPATH = env.get('TSTDATAPATH')

    if THISFILE == "Mapprove.py" \
       and not os.path.exists(os.path.join(TSTTRGBASE, dftTSTPREF )) \
       and     os.path.isfile(os.path.join(TSTTRGBASE, 'times.lst')):
        env['TSTPREF'] = os.path.basename(TSTTRGBASE)
        TSTTRGBASE = env['TSTTRGBASE'] = os.path.dirname(TSTTRGBASE)
    else:
        env['TSTPREF'] = dftTSTPREF
    global TSTPREF
    TSTPREF = env['TSTPREF']

    # check whether we have a Mercurial clone
    BACK = os.getcwd()
    try:
        os.chdir(TSTSRCBASE)
        proc = process.Popen(['hg', 'root'],
                             stdout=process.PIPE, stderr=process.PIPE,
                             text=True)
        out, err = proc.communicate()
        if proc.returncode == 0:
            CONDITIONALS['MERCURIAL'] = '#' # True
        proc = None
    except:
        pass
    os.chdir(BACK)

    # check whether our hostname makes sense
    if os.environ['HOST'] == 'localhost':
        CONDITIONALS['BAD_HOSTNAME'] = '#' # True
    else:
        try:
            socket.getaddrinfo(socket.gethostname(), None)
        except:
            CONDITIONALS['BAD_HOSTNAME'] = '#' # True

    if THISFILE == "Mtest.py": # env['MAPIPORT'] not available on Mapprove.py
        try:
            with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
                s.bind(('::1', int(env['MAPIPORT'])))
        except socket.error as err:
            CONDITIONALS['HAVE_IPV6'] = '' # False
        else:
            CONDITIONALS['HAVE_IPV6'] = '#' # True

    # read '.Mapprove.rc'
    if THISFILE == 'Mapprove.py':
        f = os.path.join(TSTTRGBASE, TSTPREF, '.Mapprove.rc')
        v = ReadMapproveRc(f)
        SYST = v['SYST']
        RELEASE = v['RELEASE']
        SYSTVER = SYST+RELEASE
        DIST = v['DIST']
        VERSION = v['VERSION']
        DISTVER = DIST+VERSION
        os.environ['SYST'] = SYST
        os.environ['SYSTVER'] = SYSTVER
        os.environ['RELEASE'] = RELEASE
        os.environ['DIST'] = DIST
        os.environ['DISTVER'] = DISTVER
        os.environ['VERSION'] = VERSION
        w = {}
        for i in 'SYST', 'RELEASE', 'DIST', 'VERSION', 'BITS', 'ARCH', 'INT128', 'SINGLE':
            w[i] = re.escape(v[i])
        for i in 'BITS', 'ARCH', 'INT128', 'SINGLE':
            j = 'TST_'+i
            env[j] = v[i]
            os.environ[j] = v[i]
        for i in 'INT128', 'SINGLE':
            if v[i]:
                v[i] = '(.%s)?' % v[i]
                w[i] = '(\.%s)?' % w[i]
        sv = '^(.(%s(%s)?|%s(%s)?))?(.(%s|%s))?%s%s$' % (v['SYST'], v['RELEASE'], v['DIST'], v['VERSION'], v['BITS'], v['ARCH'], v['INT128'], v['SINGLE'])
        sw = '^(\.(%s(%s)?|%s(%s)?))?(\.(%s|%s))?%s%s$' % (w['SYST'], w['RELEASE'], w['DIST'], w['VERSION'], w['BITS'], w['ARCH'], w['INT128'], w['SINGLE'])
        r = re.compile(sw)
        if not r.match(par['SYSTEM']):
            ErrXit("System (-S) must match '"+sv+"' !")

    # some relative path's for relocatable HTML output
    RELSRCBASE = os.path.relpath(TSTSRCBASE, TSTTRGBASE)
    env['RELSRCBASE'] = RELSRCBASE

    #STDERR.flush()
    #for v in 'RELSRCBASE':
    #       print(v+" = "+str(env[v]))
    #STDOUT.flush()

    env['BINDIR'] = _configure('/usr/local/bin')
    vars_.append('BINDIR')
    env['LIBDIR'] = _configure('/usr/local/lib')
    vars_.append('LIBDIR')

    # export and display env
    STDERR.flush()
    if THISFILE == "Mtest.py":
        vars_ = vars_ + ['GDK_DBFARM']
        vars_ = vars_ + ['setMONETDB_MOD_PATH']
        vars_ = vars_ + ['TSTDATAPATH']
    else: # THISFILE == "Mapprove.py"
        vars_ = vars_
    for v in vars_:
        if v in env:
            os.environ[v] = env[v]
            if verbose:
                print("%s = %s" % (v, env[v]))
    if verbose or testweb:
        print("%s = %s" % ('PATH', os.environ['PATH']))
        if 'PYTHONPATH' in os.environ:
            print("%s = %s" % ('PYTHONPATH', os.environ['PYTHONPATH']))
        if 'CLASSPATH' in os.environ:
            print("%s = %s" % ('CLASSPATH', os.environ['CLASSPATH']))
    if testweb:
        for v in ['BINDIR']:
            if v in os.environ:
                print("%s = %s" % (v, os.environ[v]))
    STDOUT.flush()

    # add QUIET par to env
    env['QUIET'] = quiet

    ## set/extend PATH & LD_LIBRARY_PATH
    #bp = ""        #_configure(os.path.join('/usr/local',"bin"))
    #if THISFILE == "Mtest.py":
    #       lp = env['MONETDB_MOD_PATH']
    #else: # THISFILE == "Mapprove.py"
    #       lp = ""
    #if os.name == "nt"  and  lp:
    #       if bp:
    #               bp = bp+os.pathsep+lp
    #       else:
    #               bp = lp
    #if 'PATH' in os.environ:
    #       if bp:
    #               bp = bp+os.pathsep+os.environ['PATH']
    #       else:
    #               bp = os.environ['PATH']
    #os.environ['PATH'] = bp
    #print("PATH = "+bp)
    #if os.name == "posix":
    #       if 'LD_LIBRARY_PATH' in os.environ:
    #               if lp:
    #                       lp = lp+os.pathsep+os.environ['LD_LIBRARY_PATH']
    #               else:
    #                       lp = os.environ['LD_LIBRARY_PATH']
    #       os.environ['LD_LIBRARY_PATH'] = lp
    #       print("LD_LIBRARY_PATH = "+lp)

    if not startswithpath(os.getcwd() + os.sep, TSTSRCBASE + os.sep):
        Warn("Current directory %s is no descendant of TSTSRCBASE=%s;" % (os.getcwd(), TSTSRCBASE))
        Warn("changing to TSTSRCBASE=%s, now." % TSTSRCBASE)
        os.chdir(TSTSRCBASE)

    global REV
    global URLPREFIX
    REV = opts.revision
    if REV is None:             # no --revision option: try to find out
        try:
            proc = process.Popen(['hg', 'id', '-i'],
                                 stdout=process.PIPE,
                                 text=True)
            out, err = proc.communicate()
            if proc.returncode == 0:
                REV = out.strip()
            proc = None
        except:
            pass
    # fix up URLPREFIX
    if REV:
        URLPREFIX += '%s/' % REV.split()[0].rstrip('+')
        os.environ['REVISION'] = REV
    else:
        # if no revision known, can't refer to repository
        URLPREFIX = None

    global SOCK, HOST
    try:                        # try/finally to clean up sockdir
        # check for executables, set their standard options and export them
        if THISFILE == "Mtest.py":
            if SOCK:
                # we cannot put the UNIX socket in the mtest root, because that
                # makes the UNIX socket too long on most platforms, so use
                # /var/tmp/mtest and try not to forget to clean that up
                sockdir = "/var/tmp/mtest-%d" % os.getpid()
                try:
                    os.mkdir(sockdir);
                    SOCK = "--set mapi_usock=%s/.s.monetdb.%s" % \
                            (sockdir, env['MAPIPORT'])
                    HOST = sockdir
                    os.environ['MAPIHOST'] = HOST
                except:
                    SOCK = ""
            else:
                SOCK = ""

            exe = {}
            exe['mserver5']       = CheckExec('mserver5')     , '%s mserver5 --debug=%s --set gdk_nr_threads=%s %s --set mapi_listenaddr=all --set mapi_port=%s %s %s %s' % \
                                                                   (env['setDBG'], env['GDK_DEBUG'], env['GDK_NR_THREADS'], env['setMONETDB_MOD_PATH'], env['MAPIPORT'], SOCK, not nomito and '--forcemito' or '', env['MSERVER_SET'])
            exe['Mdiff']         = CheckExec('Mdiff')        , 'Mdiff'
            exe['python']        = CheckExec(sys.executable) , sys.executable
            exe['ruby_client']   = CheckExec(env['RUBYCLIENT'].split(None, 1)[0])   , '%s %s' % (env['RUBYCLIENT'], env['MAPIPORT'])
            exe['MAL_Client']    = CheckExec(env['MALCLIENT'].split(None, 1)[0])  , '%s --host=%s --port=%s' % (env['MALCLIENT'], HOST, env['MAPIPORT'])
            exe['SQL_Client']    = CheckExec(env['SQLCLIENT'].split(None, 1)[0])   , '%s -i -e --host=%s --port=%s' % (env['SQLCLIENT'], HOST, env['MAPIPORT'])
            exe['SQL_Dump']      = CheckExec(env['SQLDUMP'].split(None, 1)[0])     , '%s --host=%s --port=%s' % (env['SQLDUMP'], HOST, env['MAPIPORT'])
            exe['R_Client']   = CheckExec(env['RCLIENT'].split(None, 1)[0])   , '%s --args %s' % (env['RCLIENT'], env['MAPIPORT'])
            env['exe'] = exe
            SetExecEnv(exe,verbose)

            #TODO:
            #exe['JAVA']       = 'java'
            #exe['JAVAC']      = 'javac'

        # parse commandline arguments
        testdirs = []
        testlist = []
        dirlist = []
        if len(args) == 1 and not os.path.isdir(args[0]):
            head, tail = os.path.split(args[0])
            if os.path.isfile(args[0]):
                head, tst = os.path.split(head)
                if tst != 'Tests':
                    ErrXit("%s: not a valid test name" % args[0])
                args = [head]
                if tail != 'All':
                    CONDITIONALS['KNOWNFAIL'] = 'execute'
                    for ext in ('_s00.malC', '_p00.malC', '_s00.sql',
                                '_p00.sql', '.MAL.py', '.SQL.py', '.malC',
                                '.sql', '.py', '.R', ''):
                        # extentions .in and .src are never combined
                        if tail.endswith(ext + '.in'):
                            args.append(tail[:-len(ext + '.in')])
                            break
                        if tail.endswith(ext + '.src'):
                            args.append(tail[:-len(ext + '.src')])
                            break
                        if tail.endswith(ext):
                            args.append(tail[:-len(ext)])
                            break
                    else:
                        ErrXit("%s: not a valid test name" % args[0])
            elif head and tail and os.path.isdir(head) and tail != 'Tests' and os.path.isdir(os.path.join(head, 'Tests')):
                CONDITIONALS['KNOWNFAIL'] = 'execute'
                args = [head, tail]

        if   len(args) == 1:
            if   os.path.isdir(args[0]):
                d = os.path.realpath(args[0])
                if startswithpath(d + os.sep, TSTSRCBASE + os.sep):
                    dirlist.append(d)
                #TODO:
                #else:
                    # WARNING/ERROR
            elif os.sep in args[0]:
                ErrXit("'%s` is neither a valid directory in %s nor a valid test-name!" % (args[0], os.getcwd()))
            elif args[0] != "All":
                #TODO:
                # check, whether args[0] in All
                CONDITIONALS['KNOWNFAIL'] = 'execute'
                testlist.append(args[0])
        elif len(args) > 1:
            i = 0
            while i < len(args)  and  os.path.isdir(args[i]):
                d = os.path.realpath(args[i])
                if startswithpath(d + os.sep, TSTSRCBASE + os.sep):
                    dirlist.append(os.path.realpath(args[i]))
                #TODO:
                #else:
                    # WARNING/ERROR
                i = i + 1
            if len(dirlist) == 1  and  i < len(args)  and  args[i] != "All":
                CONDITIONALS['KNOWNFAIL'] = 'execute'
                while i < len(args):
                    if os.sep not in args[i]:
                        #TODO:
                        # check, whether args[i] in All
                        testlist.append(args[i])
                    #TODO
                    #else:
                        # ERROR/WARNING
                    i = i + 1
            else:
                if i < len(args)  and  args[i] == "All":
                    i = i + 1
                #TODO:
                #if i < len(args):
                    #if len(dirlist) > 1:
                        # Warn: dirlist => ignore testlist, assume All
                    #else:
                        # Warn: All => ignore testlist
        else:
            # len(args) == 0: no explicit tests specified so do all
            recursive = True

        if not dirlist:
            dirlist.append(os.getcwd())
        if recursive:
            #TODO
            #if testlist:
                # WARNING
            testlist = []
            for d in dirlist:
                test_dirs = find_test_dirs(d)
                test_dirs.sort()
                for t in test_dirs:
                    if t not in testdirs:
                        testdirs.append(t)
        else:
            for d in dirlist:
                if   os.path.basename(d) == TSTSUFF  and  os.path.isfile(os.path.join(d,"All")):
                    testdirs.append(os.path.dirname(os.path.realpath(d)))
                elif os.path.isdir(os.path.join(d,TSTSUFF))  and  os.path.isfile(os.path.join(d,TSTSUFF,"All")):
                    testdirs.append(os.path.realpath(d))
                else:
                    Warn("No tests found in '%s`; skipping directory!" % d)

        if len(testdirs) > 1  and  testlist:
            testlist = []
            #TODO
            # WARNING
        if not testdirs:
            Warn("No tests found in %s!" % ', '.join(dirlist))
            sys.exit(1)

        if len(testdirs) == 1 and len(testlist) > 0 and addreqs:
            added = True
            while added:
                added = False
                i = 0
                while i < len(testlist):
                    if os.path.exists(os.path.join(testdirs[0], 'Tests', testlist[i] + '.reqtests')):
                        for t in openutf8(os.path.join(testdirs[0], 'Tests', testlist[i] + '.reqtests')):
                            t = t[:-1] # remove newline
                            if t not in testlist[:i]:
                                testlist.insert(i, t)
                                i = i + 1
                                added = True
                            #elif t in testlist:
                                # WARNING: tests in wrong order
                    i = i + 1

        BusyPorts = []

        if THISFILE == "Mtest.py":
            if not env.get('NOCLEAN') and os.path.exists(os.path.join(TSTTRGBASE, TSTPREF)):
                try:
                    shutil.rmtree(os.path.join(TSTTRGBASE, TSTPREF))
                except:
                    ErrXit("Failed to remove %s" % os.path.join(TSTTRGBASE, TSTPREF))
            if not os.path.exists(env['GDK_DBFARM']):
                #TODO: set mode to umask
                os.makedirs(env['GDK_DBFARM'])

            if not env.get('NOCLEAN') and os.path.exists(os.path.join(env['GDK_DBFARM'], TSTPREF)):
                try:
                    shutil.rmtree(os.path.join(env['GDK_DBFARM'], TSTPREF))
                except:
                    ErrXit("Failed to remove %s" % os.path.join(env['GDK_DBFARM'], TSTPREF))
            try:
                os.makedirs(os.path.join(env['GDK_DBFARM'], TSTPREF))
            except os.error:
                if not env.get('NOCLEAN'):
                    ErrXit("Failed to create %s" % os.path.join(env['GDK_DBFARM'], TSTPREF))

            try:
                os.makedirs(os.path.join(TSTTRGBASE, TSTPREF))
            except os.error:
                if not env.get('NOCLEAN'):
                    ErrXit("Failed to create %s" % os.path.join(TSTTRGBASE, TSTPREF))

            # write .monetdb file for mclient to do authentication with
            dotmonetdbfile = os.path.join(TSTTRGBASE, ".monetdb")
            dotmonetdb = openutf8(dotmonetdbfile, 'w')
            dotmonetdb.write('user=monetdb\n')
            dotmonetdb.write('password=monetdb\n')
            dotmonetdb.close()
            # and make mclient find it
            os.environ['DOTMONETDBFILE'] = dotmonetdbfile

            env['TST_MODS'] = []
            env['TST_BITS'] = ""
            env['TST_INT128'] = ""
            env['TST_SINGLE'] = ""
            env['TST_THREADS'] = ""
            env['TST_ARCH'] = ""
            cmd = splitcommand(env['exe']['mserver5'][1])
            cmd.append('--dbpath=%s' % os.path.join(env['GDK_DBFARM'], TSTPREF))
            if env.get('MULTIFARM'):
                cmd.append('--dbextra=%s' % os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'))
                shutil.rmtree(os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'),
                              ignore_errors = True)
                os.makedirs(os.path.join(env['GDK_DBFARM'], TSTPREF + '_transient'))
            if GetBitsAndModsAndThreads(env):
                sys.exit(1)
            STDERR.flush()
            if verbose:
                print("Bits: " + env['TST_BITS'])
                print("Arch: " + env['TST_ARCH'])
                if env['TST_INT128']:
                    print("Integers: 128bit")
                print("Modules: " + str(env['TST_MODS']))
            STDOUT.flush()

            port = int(env['MAPIPORT'])
            busy, host, Serrno, Serrstr, S = CheckPort(port)
            S[0].close()
            S[1].close()
            if busy:
                Warn("Skipping MAPI tests as MAPIPORT=%s is not available on %s (Error #%d: '%s')!" % (env['MAPIPORT'],host,Serrno,Serrstr))
                BusyPorts.append('MAPI')

            # create '.Mapprove.rc'
            env['SYST'] = os.environ['SYST']
            env['RELEASE'] = os.environ['RELEASE']
            env['DIST'] = os.environ['DIST']
            env['VERSION'] = os.environ['VERSION']
            n = os.path.join(TSTTRGBASE, TSTPREF, '.Mapprove.rc')
            f = openutf8(n, 'w')
            for v in 'SYST', 'RELEASE', 'DIST', 'VERSION', 'TST_BITS', 'TST_ARCH', 'TST_INT128', 'TST_SINGLE':
                w = v.replace('TST_','')
                f.write('%s = "%s"\n' % (w, env[v]))
            f.close()

        STDERR.flush()
        t_ = 0
        body_good = []
        body_bad = []
        try:
            if len(testdirs) == 1:
                if testlist:
                    tsts = "tests "+str(testlist)
                else:
                    tsts = "all tests"
                    all_tests = True
                if verbose:
                    print("\nRunning %s in directory %s.\n" % (tsts , testdirs[0]))
                t_, elem, diff, interrupted = PerformDir(env, testdirs[0], testlist, BusyPorts, all_tests)
                if elem is not None:
                    if diff <= F_OK:
                        body_good.append(elem)
                    else:
                        body_bad.append(elem)
            else:
                if verbose:
                    print("\nRunning all tests in directories %s.\n" % str(testdirs))
                for d in testdirs:
                    t, elem, diff, interrupted = PerformDir(env, d, [], BusyPorts, True)
                    t_ = t_ + t
                    if elem is not None:
                        if diff <= F_OK:
                            body_good.append(elem)
                        else:
                            body_bad.append(elem)
                    if interrupted:
                        break
                    if not testweb:
                        if global_timeout and start_time + global_timeout < time.time():
                            print('\nGlobal testing timeout reached\n')
                            break
                        # after a directory has been tested, create
                        # the index file so that we can look at test
                        # results while the tests are running
                        env['TSTDIR'] = ""
                        env['TSTTRGDIR'] = os.path.join(TSTTRGBASE, TSTPREF)
                        body = body_bad + body_good
                        CreateHtmlIndex(env, F_SKIP, F_SKIP, *body)
        except KeyboardInterrupt:
            # if we get interrupted between directories, we still want output
            pass
        body = body_bad + body_good

        if THISFILE == "Mtest.py":
            if testweb:
                # some more cleanup
                # note that we create the file so that os.removedirs in PerformDir
                # doesn't remove os.path.join(TSTTRGBASE, TSTPREF)
                remove(os.path.join(TSTTRGBASE, TSTPREF, '.Mapprove.rc'))
            fn = os.path.join(TSTTRGBASE, TSTPREF, "times.")
            fl = openutf8(fn+"lst","w")
            Failure = [[] for i in FAILURES]
            for TSTDIR, TST, tt, ms, FtOut, FtErr, reason in TIMES:
                fl.write('%s:\t%s\t%s\t%s\t%s\n' % (url(os.path.join(TSTDIR, TST)),
                                                    tt,
                                                    FAILURES[FtOut][0],
                                                    FAILURES[FtErr][0],
                                                    reason or ''))
                if TST != '':
                    Failure[max(FtOut,FtErr)].append(os.path.join(TSTDIR,TST))
            fl.write(":\t%7.3f\t\n" % t_)
            fl.close()

            fl = openutf8(fn+"sql","w")
            host = socket.gethostname()
            product = os.path.split(TSTSRCBASE)[-1]

            compiler = ''
            # TODO:
            # use  for this
            # (and then also allow compiler-specific output)
            #if os.name == 'nt':
            #    compiler = 'Mic' # Microsoft Visual Studio C
            #    #compiler = 'Int' # Intel icc
            #else:
            #    f = os.path.join(env['TSTBLDBASE'],'Makefile')
            #    if os.path.isfile(f):
            #        r = re.compile("^CC = (.*)$", re.MULTILINE)
            #        for l in openutf8(f):
            #            mt = r.match(l)
            #            if mt:
            #                compiler = mt.group(1)

            # start of times.sql output preparation
            try:
                from mx import DateTime
                now = "timestamp '" + str(DateTime.now()) + "'"
            except ImportError:
                now = 'now()'

            if env['TST_INT128'] != '':
                isInt128 = 'true'
            else:
                isInt128 = 'false'

            if env['TST_SINGLE'] != '':
                isSingle = 'true'
            else:
                isSingle = 'false'

            # ok, we're not prepared for the 128 bits world yet
            bits = env['TST_BITS'][:2]

            # we write in SQL the same codes as testweb uses in the HTML
            # pages, for readability

            # we are not interested in the compiler, nor its path, nor its
            # options.  We do store the options separately, though
            hasSpace = compiler.find(' ')
            if hasSpace != -1:
                ccname = os.path.split(compiler[:hasSpace])[-1]
                ccopts = compiler[hasSpace + 1:]
            else:
                ccname = os.path.split(compiler)[-1]
                ccopts = ''

            for TSTDIR, TST, tt, ms, FtOut, FtErr, reason in TIMES:
                if FtOut == F_SKIP and FtErr == F_SKIP:
                    tms = 'NULL'
                else:
                    tms = '%d' % ms

                if TST != '':
                    # target is a platform and compilation options etc
                    fl.write("""
INSERT INTO mtest (\"date\", \"machine\", \"os\", \"release\",
    \"compiler\", \"compiler_opts\", \"bits\", \"oid\", \"int128\", \"single\", \"static\",
    \"product\", \"dir\", \"test\",
    \"time\", \"stdout\", \"stderr\")
VALUES (%s, '%s', '%s', '%s',
    '%s', '%s', %s, %s, %s, %s, %s,
    '%s', '%s', '%s',
    %s, '%s', '%s');
""" % (now, host, env['SYST'], env['RELEASE'],
           ccname, ccopts, bits, bits, isInt128, isSingle, 'false',
           product, TSTDIR, TST,
           tms, FAILURES[FtOut][1], FAILURES[FtErr][1]))
            fl.close()

        if THISFILE == "Mtest.py":
            env['TSTDIR'] = ""
            env['TSTTRGDIR'] = os.path.join(TSTTRGBASE, TSTPREF)
            if not testweb:
                CreateHtmlIndex(env, F_SKIP, F_SKIP, *body)

            Failed = 0
            for f in Failure[1:-1]:
                Failed += len(f)
            num_tests = 0
            for f in Failure:
                num_tests += len(f)
            how = ""
            what = ""
            for x, y, z in [(F_SKIP, "could not be executed", ""),
                            (F_WARN, "produced slightly different output", "slightly"),
                            (F_SOCK, "did not properly release socket(s)", "SIGNIFICANTLY"),
                            (F_TIME, "ran into timeout", "SIGNIFICANTLY"),
                            (F_ABRT, "caused an abort (assertion failure)", "SIGNIFICANTLY"),
                            (F_SEGV, "resulted in a crash", "SIGNIFICANTLY"),
                            (F_RECU, "ran into too deep recursion", "SIGNIFICANTLY"),
                            (F_ERROR, "produced SIGNIFICANTLY different output", "SIGNIFICANTLY"),
                            (F_MISSING, "produced SIGNIFICANTLY different output", "SIGNIFICANTLY")]:
                if Failure[x]:
                    how = z
                    what += "  %3d out of %3d tests %s\n" % (len(Failure[x]),num_tests, y)
                    # only report failed tests if there aren't too many
                    if Failed < 30 and \
                           (x != F_SKIP or len(Failure[F_SKIP]) + Failed < 30):
                        for f in Failure[x]:
                            what += "        %s\n" % f
            STDERR.flush()
            if Failed:
                print("""\

 !ERROR:  Testing FAILED %s (%d out of %d tests failed)

%s
""" % (how, Failed, num_tests, what))
                if not testweb:
                    print("""\
 First, check the testing results in  %s  !

 Then, fix the problems by:
  - fixing sources and test scripts
  - fixing stable output by hand
  - approving test output by Mapprove.py (cf. Mapprove.py -?)

 After that, re-run Mtest.
""" % os.path.join(TSTTRGBASE, TSTPREF, "index.html"))
                if jenkins:
                    sys.exit(0)
                sys.exit(1)
            else:
                if quiet:
                    pass
                elif verbose:
                    print("""\

 No differences encountered during testing.

 If necessary, you can checkin your modifications, now.
""")
                else:
                    print("No differences encountered during testing.")
                sys.exit(0)

        if THISFILE == "Mapprove.py":
            if not quiet:
                print("""\

 First, run 'hg diff` to check what you have changed.

 Then, re-run Mtest.py.
""")
            if t_:
                if par['FORCE']:
                    print("""\
 In case (some of) the approved error messages are not correct/expected,
 re-run Mapprove.py without -f to skip their approval.
""")
                else:
                    print("""\
 In case (some of) the skipped error messages are correct/expected,
 re-run Mapprove.py with -f to force their approval.
""")
    finally:
        # cleanup the place where we put our UNIX sockets
        if THISFILE == "Mtest.py" and SOCK:
            try:
                shutil.rmtree(sockdir);
            except:
                pass

### main(argv) #

if __name__ == "__main__":
    if '--debug' in sys.argv:
        sys.argv.remove('--debug')
        import pdb
        pdb.run('main(sys.argv)')
    else:
        main(sys.argv)

#       END
#############################################################################
# vim: set ts=4 sw=4 expandtab:
