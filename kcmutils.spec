#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kcmutils
Version  : 5.78.0
Release  : 32
URL      : https://download.kde.org/stable/frameworks/5.78/kcmutils-5.78.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.78/kcmutils-5.78.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.78/kcmutils-5.78.0.tar.xz.sig
Summary  : Utilities for interacting with KCModules
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.0
Requires: kcmutils-data = %{version}-%{release}
Requires: kcmutils-lib = %{version}-%{release}
Requires: kcmutils-license = %{version}-%{release}
Requires: kcmutils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdeclarative-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kitemviews-dev
BuildRequires : kservice-dev
BuildRequires : kxmlgui-dev
BuildRequires : qtbase-dev mesa-dev

%description
# KCMUtils
Utilities for KDE System Settings modules
## Introduction
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package data
Summary: data components for the kcmutils package.
Group: Data

%description data
data components for the kcmutils package.


%package dev
Summary: dev components for the kcmutils package.
Group: Development
Requires: kcmutils-lib = %{version}-%{release}
Requires: kcmutils-data = %{version}-%{release}
Provides: kcmutils-devel = %{version}-%{release}
Requires: kcmutils = %{version}-%{release}

%description dev
dev components for the kcmutils package.


%package lib
Summary: lib components for the kcmutils package.
Group: Libraries
Requires: kcmutils-data = %{version}-%{release}
Requires: kcmutils-license = %{version}-%{release}

%description lib
lib components for the kcmutils package.


%package license
Summary: license components for the kcmutils package.
Group: Default

%description license
license components for the kcmutils package.


%package locales
Summary: locales components for the kcmutils package.
Group: Default

%description locales
locales components for the kcmutils package.


%prep
%setup -q -n kcmutils-5.78.0
cd %{_builddir}/kcmutils-5.78.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1611181644
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1611181644
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcmutils
cp %{_builddir}/kcmutils-5.78.0/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcmutils/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/kcmutils-5.78.0/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcmutils/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/kcmutils-5.78.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kcmutils-5.78.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kcmutils-5.78.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kcmutils/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kcmutils-5.78.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kcmutils/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang kcmutils5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservicetypes5/kcmodule.desktop
/usr/share/kservicetypes5/kcmoduleinit.desktop
/usr/share/qlogging-categories5/kcmutils.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KCMUtils/KCModuleContainer
/usr/include/KF5/KCMUtils/KCModuleData
/usr/include/KF5/KCMUtils/KCModuleInfo
/usr/include/KF5/KCMUtils/KCModuleLoader
/usr/include/KF5/KCMUtils/KCModuleProxy
/usr/include/KF5/KCMUtils/KCMultiDialog
/usr/include/KF5/KCMUtils/KPluginSelector
/usr/include/KF5/KCMUtils/kcmodulecontainer.h
/usr/include/KF5/KCMUtils/kcmoduledata.h
/usr/include/KF5/KCMUtils/kcmoduleinfo.h
/usr/include/KF5/KCMUtils/kcmoduleloader.h
/usr/include/KF5/KCMUtils/kcmoduleproxy.h
/usr/include/KF5/KCMUtils/kcmultidialog.h
/usr/include/KF5/KCMUtils/kcmutils_export.h
/usr/include/KF5/KCMUtils/kpluginselector.h
/usr/include/KF5/KCMUtils/ksettings/Dialog
/usr/include/KF5/KCMUtils/ksettings/Dispatcher
/usr/include/KF5/KCMUtils/ksettings/PluginPage
/usr/include/KF5/KCMUtils/ksettings/dialog.h
/usr/include/KF5/KCMUtils/ksettings/dispatcher.h
/usr/include/KF5/KCMUtils/ksettings/pluginpage.h
/usr/include/KF5/kcmutils_version.h
/usr/lib64/cmake/KF5KCMUtils/KF5KCMUtilsConfig.cmake
/usr/lib64/cmake/KF5KCMUtils/KF5KCMUtilsConfigVersion.cmake
/usr/lib64/cmake/KF5KCMUtils/KF5KCMUtilsMacros.cmake
/usr/lib64/cmake/KF5KCMUtils/KF5KCMUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KCMUtils/KF5KCMUtilsTargets.cmake
/usr/lib64/cmake/KF5KCMUtils/kcmutilsgeneratemoduledata.cpp.in
/usr/lib64/cmake/KF5KCMUtils/kcmutilsgeneratemoduledata.h.in
/usr/lib64/libKF5KCMUtils.so
/usr/lib64/qt5/mkspecs/modules/qt_KCMUtils.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KCMUtils.so.5
/usr/lib64/libKF5KCMUtils.so.5.78.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcmutils/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kcmutils/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kcmutils/7d9831e05094ce723947d729c2a46a09d6e90275

%files locales -f kcmutils5.lang
%defattr(-,root,root,-)

