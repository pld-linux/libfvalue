Summary:	Library to support various format value types
Summary(pl.UTF-8):	Biblioteka obsługująca różne typy formatów wartości
Name:		libfvalue
Version:	20150104
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libfvalue/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bd1744914612ada381ca4c18d5348493
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libfvalue/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libfdatetime-devel >= 20130928
BuildRequires:	libfguid-devel >= 20120426
BuildRequires:	libfwnt-devel >= 20120426
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
Requires:	libfdatetime >= 20130928
Requires:	libfguid >= 20120426
Requires:	libfwnt >= 20120426
Requires:	libuna >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfvalue is a library to support various format value types.

%description -l pl.UTF-8
libfvalue to biblioteka obsługująca różne typy formatów wartości.

%package devel
Summary:	Header files for libfvalue library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfvalue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libfdatetime-devel >= 20130928
Requires:	libfguid-devel >= 20120426
Requires:	libfwnt-devel >= 20120426
Requires:	libuna-devel >= 20120425

%description devel
Header files for libfvalue library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfvalue.

%package static
Summary:	Static libfvalue library
Summary(pl.UTF-8):	Statyczna biblioteka libfvalue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfvalue library.

%description static -l pl.UTF-8
Statyczna biblioteka libfvalue.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfvalue.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libfvalue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfvalue.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfvalue.so
%{_includedir}/libfvalue
%{_includedir}/libfvalue.h
%{_pkgconfigdir}/libfvalue.pc
%{_mandir}/man3/libfvalue.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libfvalue.a
