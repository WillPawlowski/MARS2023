#/opt/ros/melodic/share/catkin/cmake/toplevel.cmake\
		
project(mars)
		
# ---- Include guards ----
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR)
  message(FATAL_ERROR "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there.")
endif()
		
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/tools/cmake)
		
add_subdirectory(mars_robot)
add_subdirectory(mars_robot_drivers)
add_subdirectory(mars_robot_launch)
add_subdirectory(mars_robot_msgs)
add_subdirectory(mars_robot_teleop)
