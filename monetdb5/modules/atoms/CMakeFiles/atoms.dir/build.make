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
include monetdb5/modules/atoms/CMakeFiles/atoms.dir/depend.make

# Include the progress variables for this target.
include monetdb5/modules/atoms/CMakeFiles/atoms.dir/progress.make

# Include the compile flags for this target's objects.
include monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make

monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.o: ../monetdb5/modules/atoms/streams.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/streams.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/streams.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/streams.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/streams.c > CMakeFiles/atoms.dir/streams.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/streams.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/streams.c -o CMakeFiles/atoms.dir/streams.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.o: ../monetdb5/modules/atoms/blob.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/blob.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/blob.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/blob.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/blob.c > CMakeFiles/atoms.dir/blob.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/blob.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/blob.c -o CMakeFiles/atoms.dir/blob.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.o: ../monetdb5/modules/atoms/color.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/color.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/color.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/color.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/color.c > CMakeFiles/atoms.dir/color.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/color.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/color.c -o CMakeFiles/atoms.dir/color.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.o: ../monetdb5/modules/atoms/str.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/str.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/str.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/str.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/str.c > CMakeFiles/atoms.dir/str.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/str.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/str.c -o CMakeFiles/atoms.dir/str.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.o: ../monetdb5/modules/atoms/strptime.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/strptime.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/strptime.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/strptime.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/strptime.c > CMakeFiles/atoms.dir/strptime.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/strptime.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/strptime.c -o CMakeFiles/atoms.dir/strptime.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.o: ../monetdb5/modules/atoms/url.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/url.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/url.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/url.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/url.c > CMakeFiles/atoms.dir/url.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/url.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/url.c -o CMakeFiles/atoms.dir/url.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.o: ../monetdb5/modules/atoms/uuid.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/uuid.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/uuid.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/uuid.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/uuid.c > CMakeFiles/atoms.dir/uuid.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/uuid.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/uuid.c -o CMakeFiles/atoms.dir/uuid.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.o: ../monetdb5/modules/atoms/json.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/json.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/json.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/json.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/json.c > CMakeFiles/atoms.dir/json.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/json.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/json.c -o CMakeFiles/atoms.dir/json.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.o: ../monetdb5/modules/atoms/mtime.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/mtime.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/mtime.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime.c > CMakeFiles/atoms.dir/mtime.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/mtime.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime.c -o CMakeFiles/atoms.dir/mtime.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.o: ../monetdb5/modules/atoms/mtime_analytic.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/mtime_analytic.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime_analytic.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/mtime_analytic.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime_analytic.c > CMakeFiles/atoms.dir/mtime_analytic.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/mtime_analytic.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/mtime_analytic.c -o CMakeFiles/atoms.dir/mtime_analytic.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.o: ../monetdb5/modules/atoms/inet.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/inet.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/inet.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/inet.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/inet.c > CMakeFiles/atoms.dir/inet.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/inet.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/inet.c -o CMakeFiles/atoms.dir/inet.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.o: ../monetdb5/modules/atoms/identifier.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/identifier.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/identifier.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/identifier.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/identifier.c > CMakeFiles/atoms.dir/identifier.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/identifier.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/identifier.c -o CMakeFiles/atoms.dir/identifier.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.o: ../monetdb5/modules/atoms/xml.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_13) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/xml.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/xml.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/xml.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/xml.c > CMakeFiles/atoms.dir/xml.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/xml.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/xml.c -o CMakeFiles/atoms.dir/xml.c.s

monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.o: monetdb5/modules/atoms/CMakeFiles/atoms.dir/flags.make
monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.o: ../monetdb5/modules/atoms/batxml.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_14) "Building C object monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/atoms.dir/batxml.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/batxml.c

monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/atoms.dir/batxml.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/batxml.c > CMakeFiles/atoms.dir/batxml.c.i

monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/atoms.dir/batxml.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms/batxml.c -o CMakeFiles/atoms.dir/batxml.c.s

atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/streams.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/blob.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/color.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/str.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/strptime.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/url.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/uuid.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/json.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/mtime_analytic.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/inet.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/identifier.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/xml.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/batxml.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_atom.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_authorize.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_builder.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_client.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_debugger.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_exception.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_factory.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_function.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_import.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_runtime.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_instruction.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_resource.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_interpreter.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_dataflow.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_linker.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_listing.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_module.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_namespace.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_parser.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_profiler.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_resolve.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_scenario.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_session.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_stack.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_type.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_utils.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_embedded.c.o
atoms: monetdb5/mal/CMakeFiles/mal.dir/mal_prelude.c.o
atoms: monetdb5/modules/atoms/CMakeFiles/atoms.dir/build.make

.PHONY : atoms

# Rule to build all files generated by this target.
monetdb5/modules/atoms/CMakeFiles/atoms.dir/build: atoms

.PHONY : monetdb5/modules/atoms/CMakeFiles/atoms.dir/build

monetdb5/modules/atoms/CMakeFiles/atoms.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms && $(CMAKE_COMMAND) -P CMakeFiles/atoms.dir/cmake_clean.cmake
.PHONY : monetdb5/modules/atoms/CMakeFiles/atoms.dir/clean

monetdb5/modules/atoms/CMakeFiles/atoms.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/monetdb5/modules/atoms /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/monetdb5/modules/atoms/CMakeFiles/atoms.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : monetdb5/modules/atoms/CMakeFiles/atoms.dir/depend

