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
include clients/mapiclient/CMakeFiles/mclient.dir/depend.make

# Include the progress variables for this target.
include clients/mapiclient/CMakeFiles/mclient.dir/progress.make

# Include the compile flags for this target's objects.
include clients/mapiclient/CMakeFiles/mclient.dir/flags.make

clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.o: clients/mapiclient/CMakeFiles/mclient.dir/flags.make
clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.o: ../clients/mapiclient/mclient.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mclient.dir/mclient.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mclient.c

clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mclient.dir/mclient.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mclient.c > CMakeFiles/mclient.dir/mclient.c.i

clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mclient.dir/mclient.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mclient.c -o CMakeFiles/mclient.dir/mclient.c.s

clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.o: clients/mapiclient/CMakeFiles/mclient.dir/flags.make
clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.o: ../clients/mapiclient/ReadlineTools.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mclient.dir/ReadlineTools.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/ReadlineTools.c

clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mclient.dir/ReadlineTools.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/ReadlineTools.c > CMakeFiles/mclient.dir/ReadlineTools.c.i

clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mclient.dir/ReadlineTools.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/ReadlineTools.c -o CMakeFiles/mclient.dir/ReadlineTools.c.s

clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.o: clients/mapiclient/CMakeFiles/mclient.dir/flags.make
clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.o: ../clients/mapiclient/mhelp.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mclient.dir/mhelp.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mhelp.c

clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mclient.dir/mhelp.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mhelp.c > CMakeFiles/mclient.dir/mhelp.c.i

clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mclient.dir/mhelp.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient/mhelp.c -o CMakeFiles/mclient.dir/mhelp.c.s

# Object files for target mclient
mclient_OBJECTS = \
"CMakeFiles/mclient.dir/mclient.c.o" \
"CMakeFiles/mclient.dir/ReadlineTools.c.o" \
"CMakeFiles/mclient.dir/mhelp.c.o"

# External object files for target mclient
mclient_EXTERNAL_OBJECTS =

clients/mapiclient/mclient: clients/mapiclient/CMakeFiles/mclient.dir/mclient.c.o
clients/mapiclient/mclient: clients/mapiclient/CMakeFiles/mclient.dir/ReadlineTools.c.o
clients/mapiclient/mclient: clients/mapiclient/CMakeFiles/mclient.dir/mhelp.c.o
clients/mapiclient/mclient: clients/mapiclient/CMakeFiles/mclient.dir/build.make
clients/mapiclient/mclient: clients/mapiclient/libmcutil.a
clients/mapiclient/mclient: common/utils/libmprompt.a
clients/mapiclient/mclient: common/options/libmoptions.a
clients/mapiclient/mclient: common/utils/libmutils.a
clients/mapiclient/mclient: clients/mapilib/libmapi.so.12.0.6
clients/mapiclient/mclient: common/stream/libstream.so.14.0.4
clients/mapiclient/mclient: /usr/lib/x86_64-linux-gnu/libreadline.so
clients/mapiclient/mclient: /usr/lib/x86_64-linux-gnu/libc.so
clients/mapiclient/mclient: clients/mapiclient/CMakeFiles/mclient.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking C executable mclient"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mclient.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
clients/mapiclient/CMakeFiles/mclient.dir/build: clients/mapiclient/mclient

.PHONY : clients/mapiclient/CMakeFiles/mclient.dir/build

clients/mapiclient/CMakeFiles/mclient.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient && $(CMAKE_COMMAND) -P CMakeFiles/mclient.dir/cmake_clean.cmake
.PHONY : clients/mapiclient/CMakeFiles/mclient.dir/clean

clients/mapiclient/CMakeFiles/mclient.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapiclient/CMakeFiles/mclient.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : clients/mapiclient/CMakeFiles/mclient.dir/depend

