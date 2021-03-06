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
include tools/mserver/CMakeFiles/shutdowntest.dir/depend.make

# Include the progress variables for this target.
include tools/mserver/CMakeFiles/shutdowntest.dir/progress.make

# Include the compile flags for this target's objects.
include tools/mserver/CMakeFiles/shutdowntest.dir/flags.make

tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.o: tools/mserver/CMakeFiles/shutdowntest.dir/flags.make
tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.o: ../tools/mserver/shutdowntest.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/shutdowntest.dir/shutdowntest.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/mserver/shutdowntest.c

tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/shutdowntest.dir/shutdowntest.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/mserver/shutdowntest.c > CMakeFiles/shutdowntest.dir/shutdowntest.c.i

tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/shutdowntest.dir/shutdowntest.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/mserver/shutdowntest.c -o CMakeFiles/shutdowntest.dir/shutdowntest.c.s

# Object files for target shutdowntest
shutdowntest_OBJECTS = \
"CMakeFiles/shutdowntest.dir/shutdowntest.c.o"

# External object files for target shutdowntest
shutdowntest_EXTERNAL_OBJECTS =

tools/mserver/shutdowntest: tools/mserver/CMakeFiles/shutdowntest.dir/shutdowntest.c.o
tools/mserver/shutdowntest: tools/mserver/CMakeFiles/shutdowntest.dir/build.make
tools/mserver/shutdowntest: common/options/libmoptions.a
tools/mserver/shutdowntest: sql/backends/monet5/libmonetdbsql.so.11.39.11
tools/mserver/shutdowntest: common/utils/libmutils.a
tools/mserver/shutdowntest: gdk/libbat.so.21.1.1
tools/mserver/shutdowntest: common/stream/libstream.so.14.0.4
tools/mserver/shutdowntest: monetdb5/tools/libmonetdb5.so.30.0.4
tools/mserver/shutdowntest: tools/mserver/CMakeFiles/shutdowntest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable shutdowntest"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/shutdowntest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tools/mserver/CMakeFiles/shutdowntest.dir/build: tools/mserver/shutdowntest

.PHONY : tools/mserver/CMakeFiles/shutdowntest.dir/build

tools/mserver/CMakeFiles/shutdowntest.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver && $(CMAKE_COMMAND) -P CMakeFiles/shutdowntest.dir/cmake_clean.cmake
.PHONY : tools/mserver/CMakeFiles/shutdowntest.dir/clean

tools/mserver/CMakeFiles/shutdowntest.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/mserver /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/mserver/CMakeFiles/shutdowntest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tools/mserver/CMakeFiles/shutdowntest.dir/depend

