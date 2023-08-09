%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-kinova-gen3-6dof-robotiq-2f-85-moveit-config
Version:        0.2.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS kinova_gen3_6dof_robotiq_2f_85_moveit_config package

License:        BSD-3-Clause
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-controller-manager
Requires:       ros-iron-joint-state-publisher
Requires:       ros-iron-joint-state-publisher-gui
Requires:       ros-iron-kortex-description
Requires:       ros-iron-moveit-configs-utils
Requires:       ros-iron-moveit-kinematics
Requires:       ros-iron-moveit-planners
Requires:       ros-iron-moveit-ros-move-group
Requires:       ros-iron-moveit-ros-visualization
Requires:       ros-iron-moveit-ros-warehouse
Requires:       ros-iron-moveit-setup-assistant
Requires:       ros-iron-moveit-simple-controller-manager
Requires:       ros-iron-picknik-reset-fault-controller
Requires:       ros-iron-picknik-twist-controller
Requires:       ros-iron-robot-state-publisher
Requires:       ros-iron-rviz-common
Requires:       ros-iron-rviz-default-plugins
Requires:       ros-iron-rviz2
Requires:       ros-iron-tf2-ros
Requires:       ros-iron-xacro
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-ros-workspace
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
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
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Wed Aug 09 2023 Anthony Baker <abake48@gmail.com> - 0.2.2-1
- Autogenerated by Bloom

* Wed Jul 26 2023 Anthony Baker <abake48@gmail.com> - 0.2.1-1
- Autogenerated by Bloom

* Tue Jul 18 2023 Anthony Baker <abake48@gmail.com> - 0.2.0-1
- Autogenerated by Bloom

