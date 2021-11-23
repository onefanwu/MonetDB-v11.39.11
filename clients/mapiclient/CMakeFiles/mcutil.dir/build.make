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
include clients/mapiclient/CMakeFiles/mcutil.dir/depend.make

# Include the progress variables for this target.
include clients/mapiclient/CMakeFiles/mcutil.dir/progress.make

# Include the compile flags for this target's objects.
include clients/mapiclient/CMakeFiles/mcutil.dir/flags.make

clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.o: clients/mapiclient/CMakeFiles/mcutil.dir/flags.make
clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.o: ../clients/mapiclient/dump.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mcutil.dir/dump.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dump.c

clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mcutil.dir/dump.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dump.c > CMakeFiles/mcutil.dir/dump.c.i

clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mcutil.dir/dump.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dump.c -o CMakeFiles/mcutil.dir/dump.c.s

clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.o: clients/mapiclient/CMakeFiles/mcutil.dir/flags.make
clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.o: ../clients/mapiclient/dotmonetdb.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mcutil.dir/dotmonetdb.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dotmonetdb.c

clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mcutil.dir/dotmonetdb.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dotmonetdb.c > CMakeFiles/mcutil.dir/dotmonetdb.c.i

clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mcutil.dir/dotmonetdb.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/dotmonetdb.c -o CMakeFiles/mcutil.dir/dotmonetdb.c.s

# Object files for target mcutil
mcutil_OBJECTS = \
"CMakeFiles/mcutil.dir/dump.c.o" \
"CMakeFiles/mcutil.dir/dotmonetdb.c.o"

# External object files for target mcutil
mcutil_EXTERNAL_OBJECTS =

clients/mapiclient/libmcutil.a: clients/mapiclient/CMakeFiles/mcutil.dir/dump.c.o
clients/mapiclient/libmcutil.a: clients/mapiclient/CMakeFiles/mcutil.dir/dotmonetdb.c.o
clients/mapiclient/libmcutil.a: clients/mapiclient/CMakeFiles/mcutil.dir/build.make
clients/mapiclient/libmcutil.a: clients/mapiclient/CMakeFiles/mcutil.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C static library libmcutil.a"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -P CMakeFiles/mcutil.dir/cmake_clean_target.cmake
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mcutil.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
clients/mapiclient/CMakeFiles/mcutil.dir/build: clients/mapiclient/libmcutil.a

.PHONY : clients/mapiclient/CMakeFiles/mcutil.dir/build

clients/mapiclient/CMakeFiles/mcutil.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -P CMakeFiles/mcutil.dir/cmake_clean.cmake
.PHONY : clients/mapiclient/CMakeFiles/mcutil.dir/clean

clients/mapiclient/CMakeFiles/mcutil.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient/CMakeFiles/mcutil.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : clients/mapiclient/CMakeFiles/mcutil.dir/depend
