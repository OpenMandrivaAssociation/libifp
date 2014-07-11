%define	major	4
%define	libname	%mklibname ifp %{major}
%define devname %mklibname -d ifp

Summary:	iRiver driver library
Name:		libifp
Version:	1.0.0.2
Release:	14
License:	GPLv2+
Group:		System/Libraries
Url:		http://ifp-driver.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Source1:	libifp.hotplug
Source2:	10-libifp.rules
Patch0:		libifp-1.0.0.2-human-readable.patch
Patch1:		libifp-1.0.0.2-warn-not-error.patch
BuildRequires:	pkgconfig(libusb)

%description
An interface for IRiver's flash-based portable music players

%package -n	%{libname}
Summary:	iRiver driver library
Group:		System/Libraries

%description -n	%{libname}
Libraries for iRiver driver

%package -n	%{devname}
Summary:	iRiver driver library development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}ifp-static-devel < 1.0.0.2-8

%description -n	%{devname}
This package includes the header files and shared libraries
necessary for developing programs which will access iRiver using
the %{name} library.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-libusb
%make

%install
%makeinstall_std
install -D -m 0755 %{SOURCE1} %{buildroot}/sbin/libifp-hotplug
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/udev/rules.d/10-libifp.rules

%files
%doc README ChangeLog TODO
%{_bindir}/ifpline
/sbin/*
%{_sysconfdir}/udev/rules.d/*.rules

%files -n %{libname}
%{_libdir}/libifp.so.%{major}*

%files -n %{devname}
%{_libdir}/libifp.so
%{_includedir}/ifp.h
%{_mandir}/man3/ifp.h.3*

