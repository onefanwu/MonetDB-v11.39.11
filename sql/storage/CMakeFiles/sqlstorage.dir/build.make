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
include sql/storage/CMakeFiles/sqlstorage.dir/depend.make

# Include the progress variables for this target.
include sql/storage/CMakeFiles/sqlstorage.dir/progress.make

# Include the compile flags for this target's objects.
include sql/storage/CMakeFiles/sqlstorage.dir/flags.make

sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.o: sql/storage/CMakeFiles/sqlstorage.dir/flags.make
sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.o: ../sql/storage/store_dependency.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlstorage.dir/store_dependency.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_dependency.c

sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlstorage.dir/store_dependency.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_dependency.c > CMakeFiles/sqlstorage.dir/store_dependency.c.i

sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlstorage.dir/store_dependency.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_dependency.c -o CMakeFiles/sqlstorage.dir/store_dependency.c.s

sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.o: sql/storage/CMakeFiles/sqlstorage.dir/flags.make
sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.o: ../sql/storage/store_sequence.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlstorage.dir/store_sequence.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_sequence.c

sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlstorage.dir/store_sequence.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_sequence.c > CMakeFiles/sqlstorage.dir/store_sequence.c.i

sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlstorage.dir/store_sequence.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store_sequence.c -o CMakeFiles/sqlstorage.dir/store_sequence.c.s

sql/storage/CMakeFiles/sqlstorage.dir/store.c.o: sql/storage/CMakeFiles/sqlstorage.dir/flags.make
sql/storage/CMakeFiles/sqlstorage.dir/store.c.o: ../sql/storage/store.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object sql/storage/CMakeFiles/sqlstorage.dir/store.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlstorage.dir/store.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store.c

sql/storage/CMakeFiles/sqlstorage.dir/store.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlstorage.dir/store.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store.c > CMakeFiles/sqlstorage.dir/store.c.i

sql/storage/CMakeFiles/sqlstorage.dir/store.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlstorage.dir/store.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/store.c -o CMakeFiles/sqlstorage.dir/store.c.s

sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.o: sql/storage/CMakeFiles/sqlstorage.dir/flags.make
sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.o: ../sql/storage/sql_catalog.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.o"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/sqlstorage.dir/sql_catalog.c.o   -c /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/sql_catalog.c

sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/sqlstorage.dir/sql_catalog.c.i"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/sql_catalog.c > CMakeFiles/sqlstorage.dir/sql_catalog.c.i

sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/sqlstorage.dir/sql_catalog.c.s"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage/sql_catalog.c -o CMakeFiles/sqlstorage.dir/sql_catalog.c.s

# Object files for target sqlstorage
sqlstorage_OBJECTS = \
"CMakeFiles/sqlstorage.dir/store_dependency.c.o" \
"CMakeFiles/sqlstorage.dir/store_sequence.c.o" \
"CMakeFiles/sqlstorage.dir/store.c.o" \
"CMakeFiles/sqlstorage.dir/sql_catalog.c.o"

# External object files for target sqlstorage
sqlstorage_EXTERNAL_OBJECTS =

sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/store_dependency.c.o
sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/store_sequence.c.o
sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/store.c.o
sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/sql_catalog.c.o
sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/build.make
sql/storage/libsqlstorage.a: sql/storage/CMakeFiles/sqlstorage.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking C static library libsqlstorage.a"
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && $(CMAKE_COMMAND) -P CMakeFiles/sqlstorage.dir/cmake_clean_target.cmake
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sqlstorage.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
sql/storage/CMakeFiles/sqlstorage.dir/build: sql/storage/libsqlstorage.a

.PHONY : sql/storage/CMakeFiles/sqlstorage.dir/build

sql/storage/CMakeFiles/sqlstorage.dir/clean:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage && $(CMAKE_COMMAND) -P CMakeFiles/sqlstorage.dir/cmake_clean.cmake
.PHONY : sql/storage/CMakeFiles/sqlstorage.dir/clean

sql/storage/CMakeFiles/sqlstorage.dir/depend:
	cd /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11 /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/sql/storage /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage /home/wyf/PIM4DB-May2021-SP1/MonetDB-11.39.11/build/sql/storage/CMakeFiles/sqlstorage.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : sql/storage/CMakeFiles/sqlstorage.dir/depend

