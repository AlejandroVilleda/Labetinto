cmake_minimum_required(VERSION 3.25)
project(Avance_1a)

set(CMAKE_CXX_STANDARD 17)
set(SFML_STATIC_LIBRARIES true)
set(SFML_DIR D:/SFML-2.6.0/lib/cmake/SFML)

add_executable(Avance_1a main.cpp GenerarLaberinto.h)
find_package(SFML 2.6 COMPONENTS system window graphics audio network)

include_directories(D:/SFML-2.6.0/include/SFML)
target_link_libraries(Avance_1a sfml-system sfml-window sfml-graphics sfml-audio)