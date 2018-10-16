import glob
import inspect
import os
import subprocess

from conans import ConanFile, CMake, MSBuild, tools, __version__ as conan_version
from conans.client.file_copier import FileCopier
from conans.model.version import Version

class DerivedConan(ConanFile):
    name = "Derived"
    generators = "cmake"
    version = "0.1.0-unreleased-build.local"
    
    exports_sources = "*"
    requires = ("Base/0.1.0-unreleased-build.local@local/test", )
    
    def configure_build(self, options_in=None):
        cmake = CMake(self)
        cmake.configure()
        return cmake
        
    def build(self, cmake_options=None):
        cmake = self.configure_build()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy(self.name + "*.exe", src="bin", dst="bin", keep_path=False, excludes="*Test.exe")
        self.copy(self.name + "*.dll", src="bin", dst="bin", keep_path=False, excludes="*Test.dll")
        self.copy(self.name + "*.pdb", src="bin", dst="bin", keep_path=False, excludes="*Test.pdb")
        self.copy(self.name + "*.xml", src="bin", dst="bin", keep_path=False, excludes="*Test.xml")
        self.copy(self.name + "*.lib", src="lib", dst="lib", keep_path=False, excludes="*Test.lib")
        self.copy(self.name + "*.pdb", src="lib", dst="lib", keep_path=False, excludes="*Test.pdb")

        # copy generated cmake files
        self.copy(self.name + "*.cmake",src="CMakeFiles/Export/cmake", dst="cmake")
        # generate cmake <package>Config.cmake file
        tools.save(os.path.join(self.package_folder, self.name + "Config.cmake"), self.generate_cmake_config())
    
    def generate_cmake_config(self):
        return "\n".join(
              ['get_filename_component(SELF_DIR "${CMAKE_CURRENT_LIST_FILE}" PATH)',
               'include(${SELF_DIR}/cmake/' + self.name + '.cmake)'])

