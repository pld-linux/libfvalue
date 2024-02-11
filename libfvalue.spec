# see m4/${libname}.m4 />= for required version of particular library
%define		libcdata_ver		20230108
%define		libcerror_ver		20120425
%define		libcnotify_ver		20120425
%define		libcthreads_ver		20160404
%define		libfdatetime_ver	20180910
%define		libfguid_ver		20120426
%define		libfwnt_ver		20191217
%define		libuna_ver		20230702
Summary:	Library to support various format value types
Summary(pl.UTF-8):	Biblioteka obsługująca różne typy formatów wartości
Name:		libfvalue
Version:	20240124
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libfvalue/releases
Source0:	https://github.com/libyal/libfvalue/releases/download/%{version}/%{name}-experimental-%{version}.tar.gz
# Source0-md5:	fb09e01c6925a118c87aa69c70329089
URL:		https://github.com/libyal/libfvalue/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfdatetime-devel >= %{libfdatetime_ver}
BuildRequires:	libfguid-devel >= %{libfguid_ver}
BuildRequires:	libfwnt-devel >= %{libfwnt_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfdatetime >= %{libfdatetime_ver}
Requires:	libfguid >= %{libfguid_ver}
Requires:	libfwnt >= %{libfwnt_ver}
Requires:	libuna >= %{libuna_ver}
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
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfdatetime-devel >= %{libfdatetime_ver}
Requires:	libfguid-devel >= %{libfguid_ver}
Requires:	libfwnt-devel >= %{libfwnt_ver}
Requires:	libuna-devel >= %{libuna_ver}

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

%build
%{__gettextize}
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
