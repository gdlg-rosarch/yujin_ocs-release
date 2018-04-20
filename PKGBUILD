# Script generated with Bloom
pkgdesc="ROS - Yujin Robot's open-source control software"
url='http://ros.org/wiki/yujin_ocs'

pkgname='ros-kinetic-yujin-ocs'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-yocs-cmd-vel-mux'
'ros-kinetic-yocs-controllers'
'ros-kinetic-yocs-diff-drive-pose-controller'
'ros-kinetic-yocs-joyop'
'ros-kinetic-yocs-keyop'
'ros-kinetic-yocs-math-toolkit'
'ros-kinetic-yocs-rapps'
'ros-kinetic-yocs-safety-controller'
'ros-kinetic-yocs-velocity-smoother'
'ros-kinetic-yocs-virtual-sensor'
'ros-kinetic-yocs-waypoints-navi'
)

conflicts=()
replaces=()

_dir=yujin_ocs
source=()
md5sums=()

prepare() {
    cp -R $startdir/yujin_ocs $srcdir/yujin_ocs
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

