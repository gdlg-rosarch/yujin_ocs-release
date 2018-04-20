# Script generated with Bloom
pkgdesc="ROS - Parse a multiple poses from yaml and provide as topic and service. This package is highly inspired by yocs_waypoints_navi"
url='http://ros.org/wiki/yocs_waypoint_provider'

pkgname='ros-kinetic-yocs-waypoint-provider'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-visualization-msgs'
'ros-kinetic-yocs-msgs'
'yaml-cpp'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-visualization-msgs'
'ros-kinetic-yocs-msgs'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=yocs_waypoint_provider
source=()
md5sums=()

prepare() {
    cp -R $startdir/yocs_waypoint_provider $srcdir/yocs_waypoint_provider
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

