Name:           ros-kinetic-yocs-waypoint-provider
Version:        0.8.2
Release:        0%{?dist}
Summary:        ROS yocs_waypoint_provider package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/yocs_waypoint_provider
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-visualization-msgs
Requires:       ros-kinetic-yocs-msgs
Requires:       yaml-cpp-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  ros-kinetic-yocs-msgs
BuildRequires:  yaml-cpp-devel

%description
Parse a multiple poses from yaml and provide as topic and service. This package
is highly inspired by yocs_waypoints_navi

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Jan 13 2017 Jihoon Lee <jihoonl@yujinrobot.com> - 0.8.2-0
- Autogenerated by Bloom

* Fri Jun 17 2016 Jihoon Lee <jihoonl@yujinrobot.com> - 0.8.1-0
- Autogenerated by Bloom

