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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0.2-7mdv2011.0
+ Revision: 661475
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0.2-6mdv2011.0
+ Revision: 602560
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0.2-5mdv2010.1
+ Revision: 520871
- rebuilt for 2010.1

* Thu Oct 08 2009 Götz Waschk <waschk@mandriva.org> 1.0.0.2-4mdv2010.0
+ Revision: 456084
- rebuild for new libusb.la location

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.0.2-3mdv2010.0
+ Revision: 425569
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 1.0.0.2-2mdv2009.1
+ Revision: 217190
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jun 05 2008 Funda Wang <fwang@mandriva.org> 1.0.0.2-2mdv2009.0
+ Revision: 215218
- new devel package policy
- add fedora udev rules

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0.2-1mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 18 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.0.2-1mdv2007.0
+ Revision: 110498
- new release: 1.0.0.2
  pass --with-libusb to ensure library getting built
  make ifpline support 'df -h' (P0 from debian)
  only give warning at read failure to allow for format (P1 from debian)
- Import libifp

* Sat Aug 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0.0.1-1mdk
- initial release (club request)

