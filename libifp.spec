%define	name	libifp
%define	version	1.0.0.2
%define	release	7

%define	major	4
%define	libname	%mklibname ifp %{major}
%define develname %mklibname -d ifp
%define sdevelname %mklibname -d -s ifp

Summary: 	iRiver driver library
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
License: 	GPLv2+
Group: 		System/Libraries
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: 	%{name}-%{version}.tar.gz
Source1:        libifp.hotplug
Source2:        10-libifp.rules
Patch0:		libifp-1.0.0.2-human-readable.patch
Patch1:		libifp-1.0.0.2-warn-not-error.patch
BuildRequires:	libusb-devel
URL:		http://ifp-driver.sourceforge.net/

%description
An interface for IRiver's flash-based portable music players

%package -n	%{libname}
Summary:	iRiver driver library
Group:		System/Libraries

%description -n	%{libname}
Libraries for iRiver driver

%package -n	%{develname}
Summary:	iRiver driver library development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d ifp 4

%description -n	%{develname}
This package includes the header files and shared libraries
necessary for developing programs which will access iRiver using
the %{name} library.

If you are going to develop programs which will access iRiver devices,
you should install this package.

%package -n	%{sdevelname}
Summary:	Static libraries for libifp
Group:		Development/C
Provides:	%{name}-static-devel = %{version}-%{release}
Requires:	%{develname} = %{version}
Obsoletes:	%mklibname -d -s ifp 4

%description -n	%{sdevelname}
This package includes the static libraries necessary for developing
programs which will access iRiver devices using the %{name} library.

If you are going to develop programs which will access iRiver devices,
you should install this package.

%prep
%setup -q
%patch0 -p1 -b .df-h
%patch1 -p1 -b .warn

%build
%configure2_5x	--with-libusb
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -D -m 0755 %{SOURCE1} %buildroot/sbin/libifp-hotplug
install -D -m 0644 %{SOURCE2} %buildroot%{_sysconfdir}/udev/rules.d/10-libifp.rules

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog TODO
%{_bindir}/ifpline
/sbin/*
%{_sysconfdir}/udev/rules.d/*.rules

%files -n %{libname}
%{_libdir}/libifp.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libifp.so
%{_includedir}/ifp.h
%{_mandir}/man3/ifp.h.3*

%files -n %{sdevelname}
%defattr(-,root,root)
%{_libdir}/libifp.a
