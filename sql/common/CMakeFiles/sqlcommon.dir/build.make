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
include sql/common/CMakeFiles/sqlcommon.dir/depend.make

# Include the progress variables for this target.
include sql/common/CMakeFiles/sqlcommon.dir/progress.make

# Include the compile flags for this target's objects.
include sql/common/CMakeFiles/sqlcommon.dir/flags.make

sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.o: ../sql/common/sql_mem.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_mem.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_mem.c

sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_mem.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_mem.c > CMakeFiles/sqlcommon.dir/sql_mem.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_mem.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_mem.c -o CMakeFiles/sqlcommon.dir/sql_mem.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.o: ../sql/common/sql_list.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_list.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_list.c

sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_list.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_list.c > CMakeFiles/sqlcommon.dir/sql_list.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_list.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_list.c -o CMakeFiles/sqlcommon.dir/sql_list.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.o: ../sql/common/sql_hash.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_hash.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_hash.c

sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_hash.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_hash.c > CMakeFiles/sqlcommon.dir/sql_hash.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_hash.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_hash.c -o CMakeFiles/sqlcommon.dir/sql_hash.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.o: ../sql/common/sql_stack.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_stack.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_stack.c

sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_stack.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_stack.c > CMakeFiles/sqlcommon.dir/sql_stack.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_stack.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_stack.c -o CMakeFiles/sqlcommon.dir/sql_stack.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.o: ../sql/common/sql_backend.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_backend.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_backend.c

sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_backend.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_backend.c > CMakeFiles/sqlcommon.dir/sql_backend.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_backend.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_backend.c -o CMakeFiles/sqlcommon.dir/sql_backend.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.o: ../sql/common/sql_keyword.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_keyword.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_keyword.c

sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_keyword.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_keyword.c > CMakeFiles/sqlcommon.dir/sql_keyword.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_keyword.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_keyword.c -o CMakeFiles/sqlcommon.dir/sql_keyword.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.o: ../sql/common/sql_changeset.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_changeset.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_changeset.c

sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_changeset.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_changeset.c > CMakeFiles/sqlcommon.dir/sql_changeset.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_changeset.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_changeset.c -o CMakeFiles/sqlcommon.dir/sql_changeset.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.o: ../sql/common/sql_types.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_types.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_types.c

sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_types.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_types.c > CMakeFiles/sqlcommon.dir/sql_types.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_types.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_types.c -o CMakeFiles/sqlcommon.dir/sql_types.c.s

sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.o: ../sql/common/sql_string.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building C object sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/sql_string.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_string.c

sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/sql_string.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_string.c > CMakeFiles/sqlcommon.dir/sql_string.c.i

sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/sql_string.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/sql_string.c -o CMakeFiles/sqlcommon.dir/sql_string.c.s

sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.o: sql/common/CMakeFiles/sqlcommon.dir/flags.make
sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.o: ../sql/common/exception_buffer.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building C object sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlcommon.dir/exception_buffer.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/exception_buffer.c

sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlcommon.dir/exception_buffer.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/exception_buffer.c > CMakeFiles/sqlcommon.dir/exception_buffer.c.i

sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlcommon.dir/exception_buffer.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common/exception_buffer.c -o CMakeFiles/sqlcommon.dir/exception_buffer.c.s

# Object files for target sqlcommon
sqlcommon_OBJECTS = \
"CMakeFiles/sqlcommon.dir/sql_mem.c.o" \
"CMakeFiles/sqlcommon.dir/sql_list.c.o" \
"CMakeFiles/sqlcommon.dir/sql_hash.c.o" \
"CMakeFiles/sqlcommon.dir/sql_stack.c.o" \
"CMakeFiles/sqlcommon.dir/sql_backend.c.o" \
"CMakeFiles/sqlcommon.dir/sql_keyword.c.o" \
"CMakeFiles/sqlcommon.dir/sql_changeset.c.o" \
"CMakeFiles/sqlcommon.dir/sql_types.c.o" \
"CMakeFiles/sqlcommon.dir/sql_string.c.o" \
"CMakeFiles/sqlcommon.dir/exception_buffer.c.o"

# External object files for target sqlcommon
sqlcommon_EXTERNAL_OBJECTS =

sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_mem.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_list.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_hash.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_stack.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_backend.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_keyword.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_changeset.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_types.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/sql_string.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/exception_buffer.c.o
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/build.make
sql/common/libsqlcommon.a: sql/common/CMakeFiles/sqlcommon.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Linking C static library libsqlcommon.a"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && $(CMAKE_COMMAND) -P CMakeFiles/sqlcommon.dir/cmake_clean_target.cmake
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sqlcommon.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sql/common/CMakeFiles/sqlcommon.dir/build: sql/common/libsqlcommon.a

.PHONY : sql/common/CMakeFiles/sqlcommon.dir/build

sql/common/CMakeFiles/sqlcommon.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common && $(CMAKE_COMMAND) -P CMakeFiles/sqlcommon.dir/cmake_clean.cmake
.PHONY : sql/common/CMakeFiles/sqlcommon.dir/clean

sql/common/CMakeFiles/sqlcommon.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/common /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/common/CMakeFiles/sqlcommon.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sql/common/CMakeFiles/sqlcommon.dir/depend
