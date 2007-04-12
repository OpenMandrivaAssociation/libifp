%define	name	libifp
%define	version	1.0.0.2
%define	release	1

%define	major	4
%define	libname	%mklibname ifp %{major}

Summary: 	iRiver driver library
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
License: 	GPL
Group: 		System/Libraries
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: 	%{name}-%{version}.tar.gz
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

%package -n	%{libname}-devel
Summary:	iRiver driver library development files
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This package includes the header files and shared libraries
necessary for developing programs which will access iRiver using
the %{name} library.

If you are going to develop programs which will access iRiver devices,
you should install this package.

%package -n	%{libname}-static-devel
Summary:	Static libraries for libifp
Group:		Development/C
Provides:	%{name}-static-devel = %{version}-%{release}
Requires:	%{libname}-devel = %{version}

%description -n	%{libname}-static-devel
This package includes the static libraries necessary for developing
programs which will access iRiver devices using the %{name} library.

If you are going to develop programs which will access iRiver devices,
you should install this package.

%prep
%setup -q
%patch0 -p1 -b .df-h
%patch1 -p1 -b .warn

%build
%configure	--with-libusb
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post -p /sbin/ldconfig -n %{libname}
%postun -p /sbin/ldconfig -n %{libname}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog TODO
%{_bindir}/ifpline

%files -n %{libname}
%{_libdir}/libifp.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libifp.so
%{_libdir}/libifp.la
%{_includedir}/ifp.h
%{_mandir}/man3/ifp.h.3*

%files -n %{libname}-static-devel
%defattr(-,root,root)
%{_libdir}/libifp.a


