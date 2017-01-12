Name:           ros-kinetic-yocs-navi-toolkit
Version:        0.8.2
Release:        0%{?dist}
Summary:        ROS yocs_navi_toolkit package

Group:          Development/Libraries
License:        Yujin Robot
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-base-local-planner
Requires:       ros-kinetic-costmap-2d
Requires:       ros-kinetic-ecl-build
Requires:       ros-kinetic-ecl-linear-algebra
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-tf
BuildRequires:  ros-kinetic-base-local-planner
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-costmap-2d
BuildRequires:  ros-kinetic-ecl-build
BuildRequires:  ros-kinetic-ecl-linear-algebra
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-tf

%description
Ros navigation utilities.

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
* Fri Jan 13 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.8.2-0
- Autogenerated by Bloom

* Fri Jun 17 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.8.1-0
- Autogenerated by Bloom

