%?mingw_package_header

Name:           mingw-readline
Version:        6.2
Release:        11%{?dist}
Summary:        MinGW port of readline for editing typed command lines

License:        GPLv2+
Group:          System Environment/Libraries
URL:            http://cnswww.cns.cwru.edu/php/chet/readline/rltop.html
Source0:        ftp://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz

# CVE-2014-2524
Patch0:         readline-6.2-debug_fncs_security_fix.patch

BuildArch:      noarch
ExclusiveArch: %{ix86} x86_64

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-termcap

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-termcap


%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.


# Win32
%package -n mingw32-readline
Summary:        MinGW port of readline for editing typed command lines

%description -n mingw32-readline
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.

%package -n mingw32-readline-static
Summary:        Static version of the cross compiled readline library
Requires:       mingw32-readline = %{version}-%{release}

%description -n mingw32-readline-static
Static version of the cross compiled readline library.

# Win64
%package -n mingw64-readline
Summary:        MinGW port of readline for editing typed command lines

%description -n mingw64-readline
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

This is a port of the library and development tools to Windows.

%package -n mingw64-readline-static
Summary:        Static version of the cross compiled readline library
Requires:       mingw64-readline = %{version}-%{release}

%description -n mingw64-readline-static
Static version of the cross compiled readline library.


%?mingw_debug_package


%prep
%setup -q -n readline-%{version}
%patch0 -p1


%build
%mingw_configure --enable-shared
%mingw_make SHLIB_LIBS=-ltermcap


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Don't want the info files or manpages which duplicate the native package.
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}

rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}

# The examples also duplicate the native package so they can be removed as well
rm -f $RPM_BUILD_ROOT%{mingw32_datadir}/readline/*.c
rm -f $RPM_BUILD_ROOT%{mingw64_datadir}/readline/*.c


# Win32
%files -n mingw32-readline
%{mingw32_bindir}/libreadline6.dll
%{mingw32_bindir}/libhistory6.dll
%{mingw32_libdir}/libreadline.dll.a
%{mingw32_libdir}/libhistory.dll.a
%{mingw32_includedir}/readline/

%files -n mingw32-readline-static
%{mingw32_libdir}/libhistory.a
%{mingw32_libdir}/libreadline.a

# Win64
%files -n mingw64-readline
%{mingw64_bindir}/libreadline6.dll
%{mingw64_bindir}/libhistory6.dll
%{mingw64_libdir}/libreadline.dll.a
%{mingw64_libdir}/libhistory.dll.a
%{mingw64_includedir}/readline/

%files -n mingw64-readline-static
%{mingw64_libdir}/libhistory.a
%{mingw64_libdir}/libreadline.a


%changelog
* Tue Aug 14 2018 Victor Toso <victortoso@redhat.com> - 6.2-11
- ExclusiveArch: i686, x86_64
- Related: rhbz#1615874

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 6.2-4
- Fix CVE-2014-2524 (RHBZ #1077035)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 6.2-1
- Update to 6.2
- Cleaned up old patches and obsolete hacks

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2-12
- Added win64 support
- Automatically generate debuginfo subpackage
- Added -static subpackage

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 5.2-11
- Renamed the source package to mingw-readline (#801022)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 5.2-10
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 5.2-5
- Rebuild for mingw32-gcc 4.4

* Sat Nov 22 2008 Richard W.M. Jones <rjones@redhat.com> - 5.2-4
- Rename *.dll.a to lib*.dll.a so that libtool can use these libraries.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 5.2-3
- Fix paths to mandir, infodir.

* Fri Oct 31 2008 Richard W.M. Jones <rjones@redhat.com> - 5.2-2
- Rebuild against latest termcap.

* Thu Sep 25 2008 Richard W.M. Jones <rjones@redhat.com> - 5.2-1
- Initial RPM release.
