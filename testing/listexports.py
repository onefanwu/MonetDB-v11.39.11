# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0.  If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright 1997 - July 2008 CWI, August 2008 - 2021 MonetDB B.V.

import os
import sys
import re

from . import exportutils

# sets of directories/files that end up in the same shared object
dirlist = {
    'gdk': ['gdk', 'common/options', 'common/utils/mutils.h', 'common/utils/mprompt.h'],
    'mapi': ['clients/mapilib', 'common/options', 'common/utils/mcrypt.h'],
    'monetdb5': ['monetdb5', 'common/utils/msabaoth.h', 'common/utils/muuid.h'],
    'stream': ['common/stream'],
    }
libs = sorted(dirlist.keys())

# directories we skip
skipdirs = ['extras']

# individual files we skip
skipfiles = ['monet_getopt.h']

# where the files are
srcdir = r'/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11'

# the export command; note the keyword we look for is a word that ends
# in "export"
expre = re.compile(r'\b[a-zA-Z_0-9]+export\s+(?P<decl>[^;]*;)', re.MULTILINE)

# the function or variable name
nmere = re.compile(r'\b(?P<name>[a-zA-Z_][a-zA-Z_0-9]*)\s*[([;]')

def extract(f):
    decls = []
    data = open(f).read()

    data = exportutils.preprocess(data)

    res = expre.search(data)
    while res is not None:
        pos = res.end(0)
        decl = res.group('decl')
        if '{' in decl:
            sys.stderr.write('export on definition:\n%s\n' % res.group(0))
        elif '"hidden"' in decl:
            sys.stderr.write('cannot export hidden function\n%s\n' % res.group(0))
        else:
            decl = exportutils.normalize(decl)
            res = nmere.search(decl)
            if res is not None:
                decls.append((res.group('name'), decl))
            else:
                decls.append(('', decl))
        res = expre.search(data, pos)
    return decls

def mywalk(d):
    if os.path.isfile(d):
        root, file = os.path.split(d)
        return [(root, [], [file])]
    return os.walk(d)

def findfiles(dirlist, skipfiles = [], skipdirs = []):
    decls = []
    done = {}
    for d in dirlist:
        for root, dirs, files in mywalk(d):
            for d in skipdirs:
                if d in dirs:
                    dirs.remove(d)
            for f in files:
                if f not in done and \
                        (f.endswith('.c') or f.endswith('.h')) and \
                        not f.startswith('.') and \
                        f not in skipfiles and \
                        os.path.isfile(os.path.join(root, f)):
                    decls.extend(extract(os.path.join(root, f)))
                    done[f] = True
    decls.sort()
    names, decls = list(zip(*decls))
    return decls

def main():
    for lib in libs:
        dirs = dirlist[lib]
        dl = [os.path.join(srcdir, d) for d in dirs]
        decls = findfiles(dl, skipfiles = skipfiles, skipdirs = skipdirs)
        sys.stdout.write('# %s\n' % lib)
        for d in decls:
            sys.stdout.write(d)
            sys.stdout.write('\n')
        sys.stdout.write('\n')

if __name__ == '__main__':
    main()
