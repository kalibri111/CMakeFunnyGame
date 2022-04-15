cmake_minimum_required (VERSION 3.4)

project (CMake LANGUAGES CXX)
set (EXECUTABLE_OUTPUT_PATH &{PROJECT_SOURCE_DIR}/bin)

execute_process(COMMAND python3 preparing.py WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/A)
add_library(index STATIC A/index.h A/index.cpp)
add_subdirectory (B ${PROJECT_SOURCE_DIR}/lib)
add_executable (C C/main.cpp)
target_link_libraries(C library)
target_link_libraries(C index)
target_link_libraries(C PUBLIC "${CMAKE_CURRENT_LIST_DIR}")