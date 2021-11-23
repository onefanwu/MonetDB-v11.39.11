# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build

# Include any dependencies generated for this target.
include tools/merovingian/client/CMakeFiles/monetdb.dir/depend.make

# Include the progress variables for this target.
include tools/merovingian/client/CMakeFiles/monetdb.dir/progress.make

# Include the compile flags for this target's objects.
include tools/merovingian/client/CMakeFiles/monetdb.dir/flags.make

tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.o: tools/merovingian/client/CMakeFiles/monetdb.dir/flags.make
tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.o: ../tools/merovingian/client/monetdb.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdb.dir/monetdb.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/client/monetdb.c

tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdb.dir/monetdb.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/client/monetdb.c > CMakeFiles/monetdb.dir/monetdb.c.i

tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdb.dir/monetdb.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/client/monetdb.c -o CMakeFiles/monetdb.dir/monetdb.c.s

# Object files for target monetdb
monetdb_OBJECTS = \
"CMakeFiles/monetdb.dir/monetdb.c.o"

# External object files for target monetdb
monetdb_EXTERNAL_OBJECTS =

tools/merovingian/client/monetdb: tools/merovingian/client/CMakeFiles/monetdb.dir/monetdb.c.o
tools/merovingian/client/monetdb: tools/merovingian/client/CMakeFiles/monetdb.dir/build.make
tools/merovingian/client/monetdb: tools/merovingian/utils/libmeroutil.a
tools/merovingian/client/monetdb: common/utils/libmcrypt.a
tools/merovingian/client/monetdb: common/utils/libmsabaoth.a
tools/merovingian/client/monetdb: common/utils/libmutils.a
tools/merovingian/client/monetdb: common/stream/libstream.so.14.0.4
tools/merovingian/client/monetdb: /usr/lib/x86_64-linux-gnu/libcrypto.so
tools/merovingian/client/monetdb: /usr/lib/x86_64-linux-gnu/libuuid.so
tools/merovingian/client/monetdb: tools/merovingian/client/CMakeFiles/monetdb.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable monetdb"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/monetdb.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tools/merovingian/client/CMakeFiles/monetdb.dir/build: tools/merovingian/client/monetdb

.PHONY : tools/merovingian/client/CMakeFiles/monetdb.dir/build

tools/merovingian/client/CMakeFiles/monetdb.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client && $(CMAKE_COMMAND) -P CMakeFiles/monetdb.dir/cmake_clean.cmake
.PHONY : tools/merovingian/client/CMakeFiles/monetdb.dir/clean

tools/merovingian/client/CMakeFiles/monetdb.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/client /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/client/CMakeFiles/monetdb.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tools/merovingian/client/CMakeFiles/monetdb.dir/depend

