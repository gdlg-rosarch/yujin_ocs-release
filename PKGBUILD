# Script generated with Bloom
pkgdesc="ROS - Ros navigation utilities."


pkgname='ros-kinetic-yocs-navi-toolkit'
pkgver='0.8.2_1'
pkgrel=1
arch=('any')
license=('Yujin Robot'
)

makedepends=('ros-kinetic-base-local-planner'
'ros-kinetic-catkin'
'ros-kinetic-costmap-2d'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
)

depends=('ros-kinetic-base-local-planner'
'ros-kinetic-costmap-2d'
'ros-kinetic-ecl-build'
'ros-kinetic-ecl-linear-algebra'
'ros-kinetic-nav-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-tf'
)

conflicts=()
replaces=()

_dir=yocs_navi_toolkit
source=()
md5sums=()

prepare() {
    cp -R $startdir/yocs_navi_toolkit $srcdir/yocs_navi_toolkit
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

