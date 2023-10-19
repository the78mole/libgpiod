#
# spec file for package libgpiod
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define libgpiod_soversion 2
%define libgpiodcxx_soversion 1
%define libgpiomockup_soversion 0
# Tests are only available for kernel 5.5+ (so TW and 15.4+ only)

Name:           libgpiod
Version:        2.0.2
Release:        0
Summary:        C library and tools for interacting with the linux GPIO character device
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://gitext.elektrobitautomotive.com/dagl274982/libgpiod.git
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libkmod-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel >= 3.5
BuildRequires:  kernel-devel >= 4.8

%description
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

%package utils
Summary:        Tools for interacting with the linux GPIO character device
Group:          Development/Libraries/C and C++
Provides:       libgpiod = %{version}-%{release}
Obsoletes:      libgpiod < %{version}-%{release}

%description utils
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Command-line tools part.

%package -n libgpiod%{libgpiod_soversion}
Summary:        C library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiod%{libgpiod_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C library part.

%package -n libgpiodcxx%{libgpiodcxx_soversion}
Summary:        C++library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiodcxx%{libgpiodcxx_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

C++ library part.

%package -n libgpiomockup%{libgpiomockup_soversion}
Summary:        C library for interacting with the linux GPIO character device
Group:          System/Libraries
Conflicts:      libgpiod1

%description -n libgpiomockup%{libgpiomockup_soversion}
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

GPIO mockup library part.

%package devel
Summary:        Devel files for libgpiod
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       libgpiod%{libgpiod_soversion} = %{version}
Requires:       libgpiodcxx%{libgpiodcxx_soversion} = %{version}

%description devel
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Devel files part.

%package -n python3-gpiod
Summary:        Python binding for libgpiod
Group:          Development/Languages/Python
Provides:       python-libgpiod
Obsoletes:      python-libgpiod

%description -n python3-gpiod
The libgpiod library encapsulates the ioctl calls and data structures
of the GPIO character devices, the latter of which superseded the
GPIO sysfs interface in Linux 4.8.

Python binding part.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
	--enable-tools=yes \
	--enable-bindings-python \
	--enable-bindings-cxx
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.{a,la}
rm -rf %{buildroot}%{python3_sitearch}/*.{a,la}

%post -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%postun -n libgpiod%{libgpiod_soversion} -p /sbin/ldconfig
%post -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig
%postun -n libgpiodcxx%{libgpiodcxx_soversion} -p /sbin/ldconfig

%files utils
%{_bindir}/gpio*

%files -n libgpiod%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}
%{_libdir}/libgpiod.so.%{libgpiod_soversion}.*

%files -n libgpiodcxx%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}
%{_libdir}/libgpiodcxx.so.%{libgpiodcxx_soversion}.*

%files devel
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgpiod.pc
%{_libdir}/pkgconfig/libgpiodcxx.pc

%files -n python3-gpiod
%{python3_sitearch}/*.so

%changelog
