# Script generated with Bloom
pkgdesc="ROS - Simple tool for waypoints navigation with two functions: <br/> * Command the robot to go to a goal by passing through a series of waypoints. <br/> * Command the robot to constantly loop through a series of waypoints, useful for patrol."
url='http://ros.org/wiki/yocs_waypoints_navi'

pkgname='ros-kinetic-yocs-waypoints-navi'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'ros-kinetic-yocs-math-toolkit'
'ros-kinetic-yocs-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-move-base-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
'ros-kinetic-yocs-math-toolkit'
'ros-kinetic-yocs-msgs'
)

conflicts=()
replaces=()

_dir=yocs_waypoints_navi
source=()
md5sums=()

prepare() {
    cp -R $startdir/yocs_waypoints_navi $srcdir/yocs_waypoints_navi
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

