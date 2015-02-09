Name:           ros-indigo-yocs-waypoints-navi
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS yocs_waypoints_navi package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/yocs_waypoints_navi
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-move-base-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
Requires:       ros-indigo-visualization-msgs
Requires:       ros-indigo-yocs-math-toolkit
Requires:       ros-indigo-yocs-msgs
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-move-base-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-yocs-math-toolkit
BuildRequires:  ros-indigo-yocs-msgs

%description
Simple tool for waypoints navigation with two functions: * Command the robot to
go to a goal by passing through a series of waypoints. * Command the robot to
constantly loop through a series of waypoints, useful for patrol.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 09 2015 Jihoon Lee <jihoonl@yujinrobot.com> - 0.6.4-0
- Autogenerated by Bloom

* Fri Dec 05 2014 Jihoon Lee <jihoonl@yujinrobot.com> - 0.6.3-0
- Autogenerated by Bloom

* Sun Nov 30 2014 Jihoon Lee <jihoonl@yujinrobot.com> - 0.6.2-0
- Autogenerated by Bloom

