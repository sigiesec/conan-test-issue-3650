add_executable( Derived )

target_sources(Derived PRIVATE derived.cpp)
target_link_libraries(Derived PRIVATE Base::Base)
