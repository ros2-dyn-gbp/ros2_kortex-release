%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-kinova-gen3-6dof-robotiq-2f-85-moveit-config
Version:        0.2.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS kinova_gen3_6dof_robotiq_2f_85_moveit_config package

License:        BSD-3-Clause
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-controller-manager
Requires:       ros-rolling-joint-state-publisher
Requires:       ros-rolling-joint-state-publisher-gui
Requires:       ros-rolling-kortex-description
Requires:       ros-rolling-moveit-configs-utils
Requires:       ros-rolling-moveit-kinematics
Requires:       ros-rolling-moveit-planners
Requires:       ros-rolling-moveit-ros-move-group
Requires:       ros-rolling-moveit-ros-visualization
Requires:       ros-rolling-moveit-ros-warehouse
Requires:       ros-rolling-moveit-setup-assistant
Requires:       ros-rolling-moveit-simple-controller-manager
Requires:       ros-rolling-picknik-reset-fault-controller
Requires:       ros-rolling-picknik-twist-controller
Requires:       ros-rolling-robot-state-publisher
Requires:       ros-rolling-rviz-common
Requires:       ros-rolling-rviz-default-plugins
Requires:       ros-rolling-rviz2
Requires:       ros-rolling-tf2-ros
Requires:       ros-rolling-xacro
Requires:       ros-rolling-ros-workspace
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
An automatically generated package with all the configuration and launch files
for using the gen3 with the MoveIt Motion Planning Framework

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Wed Jul 26 2023 Anthony Baker <abake48@gmail.com> - 0.2.1-1
- Autogenerated by Bloom

* Mon Jul 24 2023 Anthony Baker <abake48@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

