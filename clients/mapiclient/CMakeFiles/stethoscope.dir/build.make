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
include clients/mapiclient/CMakeFiles/stethoscope.dir/depend.make

# Include the progress variables for this target.
include clients/mapiclient/CMakeFiles/stethoscope.dir/progress.make

# Include the compile flags for this target's objects.
include clients/mapiclient/CMakeFiles/stethoscope.dir/flags.make

clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.o: clients/mapiclient/CMakeFiles/stethoscope.dir/flags.make
clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.o: ../clients/mapiclient/stethoscope.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/stethoscope.dir/stethoscope.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/stethoscope.c

clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/stethoscope.dir/stethoscope.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/stethoscope.c > CMakeFiles/stethoscope.dir/stethoscope.c.i

clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/stethoscope.dir/stethoscope.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/stethoscope.c -o CMakeFiles/stethoscope.dir/stethoscope.c.s

clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.o: clients/mapiclient/CMakeFiles/stethoscope.dir/flags.make
clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.o: ../clients/mapiclient/eventparser.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/stethoscope.dir/eventparser.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/eventparser.c

clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/stethoscope.dir/eventparser.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/eventparser.c > CMakeFiles/stethoscope.dir/eventparser.c.i

clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/stethoscope.dir/eventparser.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/eventparser.c -o CMakeFiles/stethoscope.dir/eventparser.c.s

# Object files for target stethoscope
stethoscope_OBJECTS = \
"CMakeFiles/stethoscope.dir/stethoscope.c.o" \
"CMakeFiles/stethoscope.dir/eventparser.c.o"

# External object files for target stethoscope
stethoscope_EXTERNAL_OBJECTS =

clients/mapiclient/stethoscope: clients/mapiclient/CMakeFiles/stethoscope.dir/stethoscope.c.o
clients/mapiclient/stethoscope: clients/mapiclient/CMakeFiles/stethoscope.dir/eventparser.c.o
clients/mapiclient/stethoscope: clients/mapiclient/CMakeFiles/stethoscope.dir/build.make
clients/mapiclient/stethoscope: clients/mapiclient/libmcutil.a
clients/mapiclient/stethoscope: common/stream/libstream.so.14.0.4
clients/mapiclient/stethoscope: clients/mapilib/libmapi.so.12.0.6
clients/mapiclient/stethoscope: common/utils/libmprompt.a
clients/mapiclient/stethoscope: clients/mapiclient/CMakeFiles/stethoscope.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking C executable stethoscope"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/stethoscope.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
clients/mapiclient/CMakeFiles/stethoscope.dir/build: clients/mapiclient/stethoscope

.PHONY : clients/mapiclient/CMakeFiles/stethoscope.dir/build

clients/mapiclient/CMakeFiles/stethoscope.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -P CMakeFiles/stethoscope.dir/cmake_clean.cmake
.PHONY : clients/mapiclient/CMakeFiles/stethoscope.dir/clean

clients/mapiclient/CMakeFiles/stethoscope.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient/CMakeFiles/stethoscope.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : clients/mapiclient/CMakeFiles/stethoscope.dir/depend

