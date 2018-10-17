cmake_minimum_required(VERSION 3.11)

project (Derived)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(Base)

add_subdirectory( ${CMAKE_CURRENT_LIST_DIR}/Derived ${PROJECT_BINARY_DIR}/Derived)
