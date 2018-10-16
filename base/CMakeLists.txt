cmake_minimum_required(VERSION 3.11)

project (Base)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

install(EXPORT Base DESTINATION cmake NAMESPACE Base::)

add_subdirectory( ${CMAKE_CURRENT_LIST_DIR}/Base ${PROJECT_BINARY_DIR}/Base)
