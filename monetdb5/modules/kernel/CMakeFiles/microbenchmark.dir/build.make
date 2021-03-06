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
include monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/depend.make

# Include the progress variables for this target.
include monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/progress.make

# Include the compile flags for this target's objects.
include monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/flags.make

monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.o: monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/flags.make
monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.o: ../monetdb5/modules/kernel/microbenchmark.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/microbenchmark.dir/microbenchmark.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/kernel/microbenchmark.c

monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/microbenchmark.dir/microbenchmark.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/kernel/microbenchmark.c > CMakeFiles/microbenchmark.dir/microbenchmark.c.i

monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/microbenchmark.dir/microbenchmark.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/kernel/microbenchmark.c -o CMakeFiles/microbenchmark.dir/microbenchmark.c.s

# Object files for target microbenchmark
microbenchmark_OBJECTS = \
"CMakeFiles/microbenchmark.dir/microbenchmark.c.o"

# External object files for target microbenchmark
microbenchmark_EXTERNAL_OBJECTS =

monetdb5/modules/kernel/lib_microbenchmark.so: monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/microbenchmark.c.o
monetdb5/modules/kernel/lib_microbenchmark.so: monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/build.make
monetdb5/modules/kernel/lib_microbenchmark.so: gdk/libbat.so.21.1.1
monetdb5/modules/kernel/lib_microbenchmark.so: monetdb5/tools/libmonetdb5.so.30.0.4
monetdb5/modules/kernel/lib_microbenchmark.so: monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared module lib_microbenchmark.so"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/microbenchmark.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/build: monetdb5/modules/kernel/lib_microbenchmark.so

.PHONY : monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/build

monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel && $(CMAKE_COMMAND) -P CMakeFiles/microbenchmark.dir/cmake_clean.cmake
.PHONY : monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/clean

monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/kernel /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : monetdb5/modules/kernel/CMakeFiles/microbenchmark.dir/depend

