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
include clients/mapilib/CMakeFiles/mapi.dir/depend.make

# Include the progress variables for this target.
include clients/mapilib/CMakeFiles/mapi.dir/progress.make

# Include the compile flags for this target's objects.
include clients/mapilib/CMakeFiles/mapi.dir/flags.make

clients/mapilib/CMakeFiles/mapi.dir/mapi.c.o: clients/mapilib/CMakeFiles/mapi.dir/flags.make
clients/mapilib/CMakeFiles/mapi.dir/mapi.c.o: ../clients/mapilib/mapi.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object clients/mapilib/CMakeFiles/mapi.dir/mapi.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/mapi.dir/mapi.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapilib/mapi.c

clients/mapilib/CMakeFiles/mapi.dir/mapi.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/mapi.dir/mapi.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapilib/mapi.c > CMakeFiles/mapi.dir/mapi.c.i

clients/mapilib/CMakeFiles/mapi.dir/mapi.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/mapi.dir/mapi.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapilib/mapi.c -o CMakeFiles/mapi.dir/mapi.c.s

# Object files for target mapi
mapi_OBJECTS = \
"CMakeFiles/mapi.dir/mapi.c.o"

# External object files for target mapi
mapi_EXTERNAL_OBJECTS =

clients/mapilib/libmapi.so.12.0.6: clients/mapilib/CMakeFiles/mapi.dir/mapi.c.o
clients/mapilib/libmapi.so.12.0.6: clients/mapilib/CMakeFiles/mapi.dir/build.make
clients/mapilib/libmapi.so.12.0.6: common/options/libmoptions.a
clients/mapilib/libmapi.so.12.0.6: common/utils/libmcrypt.a
clients/mapilib/libmapi.so.12.0.6: common/stream/libstream.so.14.0.4
clients/mapilib/libmapi.so.12.0.6: /usr/lib/x86_64-linux-gnu/libcrypto.so
clients/mapilib/libmapi.so.12.0.6: clients/mapilib/CMakeFiles/mapi.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C shared library libmapi.so"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mapi.dir/link.txt --verbose=$(VERBOSE)
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && $(CMAKE_COMMAND) -E cmake_symlink_library libmapi.so.12.0.6 libmapi.so.12 libmapi.so

clients/mapilib/libmapi.so.12: clients/mapilib/libmapi.so.12.0.6
	@$(CMAKE_COMMAND) -E touch_nocreate clients/mapilib/libmapi.so.12

clients/mapilib/libmapi.so: clients/mapilib/libmapi.so.12.0.6
	@$(CMAKE_COMMAND) -E touch_nocreate clients/mapilib/libmapi.so

# Rule to build all files generated by this target.
clients/mapilib/CMakeFiles/mapi.dir/build: clients/mapilib/libmapi.so

.PHONY : clients/mapilib/CMakeFiles/mapi.dir/build

clients/mapilib/CMakeFiles/mapi.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib && $(CMAKE_COMMAND) -P CMakeFiles/mapi.dir/cmake_clean.cmake
.PHONY : clients/mapilib/CMakeFiles/mapi.dir/clean

clients/mapilib/CMakeFiles/mapi.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/clients/mapilib /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/clients/mapilib/CMakeFiles/mapi.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : clients/mapilib/CMakeFiles/mapi.dir/depend

