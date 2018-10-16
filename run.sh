#!/bin/sh
conan create base test/local
cd derived
mkdir build
cd build
conan install ..
conan build --configure ..
cat CMakeCache.txt | grep _DIR:PATH

