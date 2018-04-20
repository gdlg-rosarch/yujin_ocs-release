# Script generated with Bloom
pkgdesc="ROS - The AR pair tracking package"
url='http://wiki.ros.org/yocs_ar_pair_tracking'

pkgname='ros-kinetic-yocs-ar-pair-tracking'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-ar-track-alvar-msgs'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-yocs-ar-marker-tracking'
'ros-kinetic-yocs-math-toolkit'
'ros-kinetic-yocs-msgs'
)

depends=('ros-kinetic-ar-track-alvar-msgs'
'ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-yocs-ar-marker-tracking'
'ros-kinetic-yocs-math-toolkit'
'ros-kinetic-yocs-msgs'
)

conflicts=()
replaces=()

_dir=yocs_ar_pair_tracking
source=()
md5sums=()

prepare() {
    cp -R $startdir/yocs_ar_pair_tracking $srcdir/yocs_ar_pair_tracking
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

