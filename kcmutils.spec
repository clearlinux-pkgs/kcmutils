#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kcmutils
Version  : 6.5.0
Release  : 80
URL      : https://download.kde.org/stable/frameworks/6.5/kcmutils-6.5.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.5/kcmutils-6.5.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.5/kcmutils-6.5.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Utilities for interacting with KCModules
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-3.0
Requires: kcmutils-bin = %{version}-%{release}
Requires: kcmutils-data = %{version}-%{release}
Requires: kcmutils-lib = %{version}-%{release}
Requires: kcmutils-license = %{version}-%{release}
Requires: kcmutils-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KCMUtils
Utilities for KDE System Settings modules
## Introduction
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package bin
Summary: bin components for the kcmutils package.
Group: Binaries
Requires: kcmutils-data = %{version}-%{release}
Requires: kcmutils-license = %{version}-%{release}

%description bin
bin components for the kcmutils package.


%package data
Summary: data components for the kcmutils package.
Group: Data

%description data
data components for the kcmutils package.


%package dev
Summary: dev components for the kcmutils package.
Group: Development
Requires: kcmutils-lib = %{version}-%{release}
Requires: kcmutils-bin = %{version}-%{release}
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kcmutils-6.5.0
cd %{_builddir}/kcmutils-6.5.0
pushd ..
cp -a kcmutils-6.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1723479233
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1723479233
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcmutils
cp %{_builddir}/kcmutils-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kcmutils/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcmutils/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcmutils/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcmutils/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kcmutils/49e61f7864169f2e356c11a17422d7d20d74b40f || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcmutils/cbca59e0e62dd8bfc0468847678552cadebea0a9 || :
cp %{_builddir}/kcmutils-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kcmutils/cbca59e0e62dd8bfc0468847678552cadebea0a9 || :
cp %{_builddir}/kcmutils-%{version}/autotests/fakekcm/fakekcm.json.license %{buildroot}/usr/share/package-licenses/kcmutils/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/kcmutils-%{version}/autotests/qmlkcm/kcm_testqml.json.license %{buildroot}/usr/share/package-licenses/kcmutils/864bc0eb28c73bd997ac19ff91935ab771846615 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcmutils6
%find_lang kcmshell6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kcmdesktopfilegenerator
/usr/lib64/libexec/kf6/kcmdesktopfilegenerator

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kcmshell6
/usr/bin/kcmshell6

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kcmutils.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KCMUtils/KCModule
/usr/include/KF6/KCMUtils/KCModuleLoader
/usr/include/KF6/KCMUtils/KCMultiDialog
/usr/include/KF6/KCMUtils/KPluginWidget
/usr/include/KF6/KCMUtils/kcmodule.h
/usr/include/KF6/KCMUtils/kcmoduleloader.h
/usr/include/KF6/KCMUtils/kcmultidialog.h
/usr/include/KF6/KCMUtils/kcmutils_export.h
/usr/include/KF6/KCMUtils/kcmutils_version.h
/usr/include/KF6/KCMUtils/kpluginwidget.h
/usr/include/KF6/KCMUtilsCore/KAbstractConfigModule
/usr/include/KF6/KCMUtilsCore/KCModuleData
/usr/include/KF6/KCMUtilsCore/KPluginModel
/usr/include/KF6/KCMUtilsCore/kabstractconfigmodule.h
/usr/include/KF6/KCMUtilsCore/kcmoduledata.h
/usr/include/KF6/KCMUtilsCore/kcmutilscore_export.h
/usr/include/KF6/KCMUtilsCore/kpluginmodel.h
/usr/include/KF6/KCMUtilsQuick/KQuickConfigModule
/usr/include/KF6/KCMUtilsQuick/KQuickConfigModuleLoader
/usr/include/KF6/KCMUtilsQuick/KQuickManagedConfigModule
/usr/include/KF6/KCMUtilsQuick/kcmutilsquick_export.h
/usr/include/KF6/KCMUtilsQuick/kquickconfigmodule.h
/usr/include/KF6/KCMUtilsQuick/kquickconfigmoduleloader.h
/usr/include/KF6/KCMUtilsQuick/kquickmanagedconfigmodule.h
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsConfig.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsConfigVersion.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsMacros.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsTargets.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsToolingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6KCMUtils/KF6KCMUtilsToolingTargets.cmake
/usr/lib64/cmake/KF6KCMUtils/kcmutilsgeneratemoduledata.cpp.in
/usr/lib64/cmake/KF6KCMUtils/kcmutilsgeneratemoduledata.h.in
/usr/lib64/libKF6KCMUtils.so
/usr/lib64/libKF6KCMUtilsCore.so
/usr/lib64/libKF6KCMUtilsQuick.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6KCMUtils.so.6.5.0
/V3/usr/lib64/libKF6KCMUtilsCore.so.6.5.0
/V3/usr/lib64/libKF6KCMUtilsQuick.so.6.5.0
/V3/usr/lib64/qt6/qml/org/kde/kcmutils/libkcmutilsqmlplugin.so
/V3/usr/lib64/qt6/qml/org/kde/kcmutils/private/libkcmutilsprivateqmlplugin.so
/usr/lib64/libKF6KCMUtils.so.6
/usr/lib64/libKF6KCMUtils.so.6.5.0
/usr/lib64/libKF6KCMUtilsCore.so.6
/usr/lib64/libKF6KCMUtilsCore.so.6.5.0
/usr/lib64/libKF6KCMUtilsQuick.so.6
/usr/lib64/libKF6KCMUtilsQuick.so.6.5.0
/usr/lib64/qt6/qml/org/kde/kcmutils/AbstractKCM.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/ContextualHelpButton.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/GridDelegate.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/GridView.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/GridViewKCM.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/PluginDelegate.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/PluginSelector.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/ScrollView.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/ScrollViewKCM.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/SettingHighlighter.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/SettingStateBinding.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/SimpleKCM.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/kcmutilsqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kcmutils/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kcmutils/libkcmutilsqmlplugin.so
/usr/lib64/qt6/qml/org/kde/kcmutils/private/AboutPlugin.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/private/GridDelegateMenu.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/private/GridViewInternal.qml
/usr/lib64/qt6/qml/org/kde/kcmutils/private/kcmutilsprivateqmlplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/kcmutils/private/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kcmutils/private/libkcmutilsprivateqmlplugin.so
/usr/lib64/qt6/qml/org/kde/kcmutils/private/qmldir
/usr/lib64/qt6/qml/org/kde/kcmutils/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcmutils/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kcmutils/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kcmutils/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kcmutils/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/kcmutils/49e61f7864169f2e356c11a17422d7d20d74b40f
/usr/share/package-licenses/kcmutils/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcmutils/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/kcmutils/cbca59e0e62dd8bfc0468847678552cadebea0a9

%files locales -f kcmutils6.lang -f kcmshell6.lang
%defattr(-,root,root,-)

