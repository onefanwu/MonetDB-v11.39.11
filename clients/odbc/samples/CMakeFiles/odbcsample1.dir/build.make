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
include clients/odbc/samples/CMakeFiles/odbcsample1.dir/depend.make

# Include the progress variables for this target.
include clients/odbc/samples/CMakeFiles/odbcsample1.dir/progress.make

# Include the compile flags for this target's objects.
include clients/odbc/samples/CMakeFiles/odbcsample1.dir/flags.make

clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.o: clients/odbc/samples/CMakeFiles/odbcsample1.dir/flags.make
clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.o: ../clients/odbc/samples/odbcsample1.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/odbcsample1.dir/odbcsample1.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/odbc/samples/odbcsample1.c

clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/odbcsample1.dir/odbcsample1.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/odbc/samples/odbcsample1.c > CMakeFiles/odbcsample1.dir/odbcsample1.c.i

clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/odbcsample1.dir/odbcsample1.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/odbc/samples/odbcsample1.c -o CMakeFiles/odbcsample1.dir/odbcsample1.c.s

# Object files for target odbcsample1
odbcsample1_OBJECTS = \
"CMakeFiles/odbcsample1.dir/odbcsample1.c.o"

# External object files for target odbcsample1
odbcsample1_EXTERNAL_OBJECTS =

clients/odbc/samples/odbcsample1: clients/odbc/samples/CMakeFiles/odbcsample1.dir/odbcsample1.c.o
clients/odbc/samples/odbcsample1: clients/odbc/samples/CMakeFiles/odbcsample1.dir/build.make
clients/odbc/samples/odbcsample1: /usr/lib/x86_64-linux-gnu/libodbc.so
clients/odbc/samples/odbcsample1: clients/odbc/samples/CMakeFiles/odbcsample1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable odbcsample1"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/odbcsample1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
clients/odbc/samples/CMakeFiles/odbcsample1.dir/build: clients/odbc/samples/odbcsample1

.PHONY : clients/odbc/samples/CMakeFiles/odbcsample1.dir/build

clients/odbc/samples/CMakeFiles/odbcsample1.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples && $(CMAKE_COMMAND) -P CMakeFiles/odbcsample1.dir/cmake_clean.cmake
.PHONY : clients/odbc/samples/CMakeFiles/odbcsample1.dir/clean

clients/odbc/samples/CMakeFiles/odbcsample1.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/odbc/samples /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/odbc/samples/CMakeFiles/odbcsample1.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : clients/odbc/samples/CMakeFiles/odbcsample1.dir/depend

