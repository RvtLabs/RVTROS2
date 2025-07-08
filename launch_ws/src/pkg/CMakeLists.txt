cmake_minimum_required(VERSION 3.8)
project(pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)

add_executable(one src/one.cpp)
target_include_directories(one PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(one PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  one
  "rclcpp"
  "rclpy"
)

add_executable(two src/two.cpp)
target_include_directories(two PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(two PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  two
  "rclcpp"
  "rclpy"
)

add_executable(three src/three.cpp)
target_include_directories(three PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(three PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  three
  "rclcpp"
  "rclpy"
)

install(TARGETS one two three
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
  launch 
  DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
