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
include tools/merovingian/daemon/CMakeFiles/monetdbd.dir/depend.make

# Include the progress variables for this target.
include tools/merovingian/daemon/CMakeFiles/monetdbd.dir/progress.make

# Include the compile flags for this target's objects.
include tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.o: ../tools/merovingian/daemon/merovingian.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/merovingian.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/merovingian.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/merovingian.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/merovingian.c > CMakeFiles/monetdbd.dir/merovingian.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/merovingian.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/merovingian.c -o CMakeFiles/monetdbd.dir/merovingian.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.o: ../tools/merovingian/daemon/argvcmds.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/argvcmds.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/argvcmds.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/argvcmds.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/argvcmds.c > CMakeFiles/monetdbd.dir/argvcmds.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/argvcmds.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/argvcmds.c -o CMakeFiles/monetdbd.dir/argvcmds.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.o: ../tools/merovingian/daemon/client.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/client.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/client.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/client.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/client.c > CMakeFiles/monetdbd.dir/client.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/client.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/client.c -o CMakeFiles/monetdbd.dir/client.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.o: ../tools/merovingian/daemon/connections.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/connections.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/connections.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/connections.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/connections.c > CMakeFiles/monetdbd.dir/connections.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/connections.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/connections.c -o CMakeFiles/monetdbd.dir/connections.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.o: ../tools/merovingian/daemon/controlrunner.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/controlrunner.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/controlrunner.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/controlrunner.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/controlrunner.c > CMakeFiles/monetdbd.dir/controlrunner.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/controlrunner.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/controlrunner.c -o CMakeFiles/monetdbd.dir/controlrunner.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.o: ../tools/merovingian/daemon/discoveryrunner.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/discoveryrunner.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/discoveryrunner.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/discoveryrunner.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/discoveryrunner.c > CMakeFiles/monetdbd.dir/discoveryrunner.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/discoveryrunner.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/discoveryrunner.c -o CMakeFiles/monetdbd.dir/discoveryrunner.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.o: ../tools/merovingian/daemon/forkmserver.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/forkmserver.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/forkmserver.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/forkmserver.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/forkmserver.c > CMakeFiles/monetdbd.dir/forkmserver.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/forkmserver.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/forkmserver.c -o CMakeFiles/monetdbd.dir/forkmserver.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.o: ../tools/merovingian/daemon/handlers.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/handlers.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/handlers.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/handlers.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/handlers.c > CMakeFiles/monetdbd.dir/handlers.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/handlers.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/handlers.c -o CMakeFiles/monetdbd.dir/handlers.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.o: ../tools/merovingian/daemon/multiplex-funnel.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/multiplex-funnel.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/multiplex-funnel.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/multiplex-funnel.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/multiplex-funnel.c > CMakeFiles/monetdbd.dir/multiplex-funnel.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/multiplex-funnel.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/multiplex-funnel.c -o CMakeFiles/monetdbd.dir/multiplex-funnel.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.o: ../tools/merovingian/daemon/snapshot.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/snapshot.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/snapshot.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/snapshot.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/snapshot.c > CMakeFiles/monetdbd.dir/snapshot.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/snapshot.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/snapshot.c -o CMakeFiles/monetdbd.dir/snapshot.c.s

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.o: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/flags.make
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.o: ../tools/merovingian/daemon/proxy.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building C object tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/monetdbd.dir/proxy.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/proxy.c

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/monetdbd.dir/proxy.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/proxy.c > CMakeFiles/monetdbd.dir/proxy.c.i

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/monetdbd.dir/proxy.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon/proxy.c -o CMakeFiles/monetdbd.dir/proxy.c.s

# Object files for target monetdbd
monetdbd_OBJECTS = \
"CMakeFiles/monetdbd.dir/merovingian.c.o" \
"CMakeFiles/monetdbd.dir/argvcmds.c.o" \
"CMakeFiles/monetdbd.dir/client.c.o" \
"CMakeFiles/monetdbd.dir/connections.c.o" \
"CMakeFiles/monetdbd.dir/controlrunner.c.o" \
"CMakeFiles/monetdbd.dir/discoveryrunner.c.o" \
"CMakeFiles/monetdbd.dir/forkmserver.c.o" \
"CMakeFiles/monetdbd.dir/handlers.c.o" \
"CMakeFiles/monetdbd.dir/multiplex-funnel.c.o" \
"CMakeFiles/monetdbd.dir/snapshot.c.o" \
"CMakeFiles/monetdbd.dir/proxy.c.o"

# External object files for target monetdbd
monetdbd_EXTERNAL_OBJECTS =

tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/merovingian.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/argvcmds.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/client.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/connections.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/controlrunner.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/discoveryrunner.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/forkmserver.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/handlers.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/multiplex-funnel.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/snapshot.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/proxy.c.o
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/build.make
tools/merovingian/daemon/monetdbd: tools/merovingian/utils/libmeroutil.a
tools/merovingian/daemon/monetdbd: common/utils/libmutils.a
tools/merovingian/daemon/monetdbd: common/options/libmoptions.a
tools/merovingian/daemon/monetdbd: common/utils/libmcrypt.a
tools/merovingian/daemon/monetdbd: common/stream/libstream.so.14.0.4
tools/merovingian/daemon/monetdbd: clients/mapilib/libmapi.so.12.0.6
tools/merovingian/daemon/monetdbd: common/utils/libmsabaoth.a
tools/merovingian/daemon/monetdbd: common/utils/libmutils.a
tools/merovingian/daemon/monetdbd: /usr/lib/x86_64-linux-gnu/libcrypto.so
tools/merovingian/daemon/monetdbd: /usr/lib/x86_64-linux-gnu/libuuid.so
tools/merovingian/daemon/monetdbd: tools/merovingian/daemon/CMakeFiles/monetdbd.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Linking C executable monetdbd"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/monetdbd.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tools/merovingian/daemon/CMakeFiles/monetdbd.dir/build: tools/merovingian/daemon/monetdbd

.PHONY : tools/merovingian/daemon/CMakeFiles/monetdbd.dir/build

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon && $(CMAKE_COMMAND) -P CMakeFiles/monetdbd.dir/cmake_clean.cmake
.PHONY : tools/merovingian/daemon/CMakeFiles/monetdbd.dir/clean

tools/merovingian/daemon/CMakeFiles/monetdbd.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/tools/merovingian/daemon /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/tools/merovingian/daemon/CMakeFiles/monetdbd.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tools/merovingian/daemon/CMakeFiles/monetdbd.dir/depend

