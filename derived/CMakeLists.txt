cmake_minimum_required(VERSION 3.11)

project (Derived)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(Base)

add_subdirectory( ${CMAKE_CURRENT_LIST_DIR}/Derived ${PROJECT_BINARY_DIR}/Derived)
