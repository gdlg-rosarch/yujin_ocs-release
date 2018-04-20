# Script generated with Bloom
pkgdesc="ROS - A controller for driving a differential drive base to a pose goal or along a path specified by multiple poses. A pose consists of a 2D position (x,y) and a 1D orientation (theta)."
url='http://ros.org/wiki/yocs_diff_drive_pose_controller'

pkgname='ros-kinetic-yocs-diff-drive-pose-controller'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-yocs-controllers'
'ros-kinetic-yocs-math-toolkit'
)

depends=('ros-kinetic-ecl-threads'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nodelet'
'ros-kinetic-pluginlib'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-yocs-controllers'
'ros-kinetic-yocs-math-toolkit'
)

conflicts=()
replaces=()

_dir=yocs_diff_drive_pose_controller
source=()
md5sums=()

prepare() {
    cp -R $startdir/yocs_diff_drive_pose_controller $srcdir/yocs_diff_drive_pose_controller
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

