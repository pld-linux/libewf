#
# Conditional build:
%bcond_without	python	# Python bindings (any)
%bcond_without	python2	# CPython 2.x bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcaes_ver		20220529
%define		libcdata_ver		20230108
%define		libcdatetime_ver	20141018
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfdatetime_ver	20180910
%define		libfguid_ver		20120426
%define		libfvalue_ver		20200711
%define		libhmac_ver		20200104
%define		libodraw_ver		20120630
%define		libsmdev_ver		20140406
%define		libsmraw_ver		20120630
%define		libuna_ver		20230702
Summary:	Library to support the Expert Witness Compression Format
Summary(pl.UTF-8):	Biblioteka obsługująca format Expert Witness Compression Format
Name:		libewf
Version:	20231119
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libewf/releases
Source0:	https://github.com/libyal/libewf/releases/download/%{version}/%{name}-experimental-%{version}.tar.gz
# Source0-md5:	9a8a2dc9fa7023e3c7144dcf3cdb256f
URL:		https://github.com/libyal/libewf/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcaes-devel >= %{libcaes_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcdatetime-devel >= %{libcdatetime_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfdatetime-devel >= %{libfdatetime_ver}
BuildRequires:	libfguid-devel >= %{libfguid_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libhmac-devel >= %{libhmac_ver}
BuildRequires:	libodraw-devel >= %{libodraw_ver}
BuildRequires:	libsmdev-devel >= %{libsmdev_ver}
BuildRequires:	libsmraw-devel >= %{libsmraw_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel >= 2.20
BuildRequires:	openssl-devel >= 1.0
%{?with_python2:BuildRequires:	python-devel >= 1:2.5}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	zlib-devel >= 1.2.5
Requires:	bzip2 >= 1.0
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcaes >= %{libcaes_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
Requires:	libfdata >= %{libfdata_ver}
Requires:	libfdatetime >= %{libfdatetime_ver}
Requires:	libfguid >= %{libfguid_ver}
Requires:	libfvalue >= %{libfvalue_ver}
Requires:	libhmac >= %{libhmac_ver}
Requires:	libuna >= %{libuna_ver}
Requires:	zlib >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libewf is a library for support of the Expert Witness Compression
Format (EWF). It allows you to read media information of EWF files in
the SMART (EWF-S01) format and the EnCase (EWF-E01) format, and to
read files created by EnCase 1 to 6, linen and FTK Imager.

%description -l pl.UTF-8
libewf to biblioteka obsługująca format kompresji EWF (Expert Witness
Compression Format). Pozwala odczytywać informacje z plików EWF w
formacie SMART (EWF-S01) i EnCase (EWF-E01) oraz czytać pliki
utworzone przez EnCase w wersji 1 do 6, linen i FTK Imager.

%package devel
Summary:	Header files for libewf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libewf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	bzip2-devel >= 1.0
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcaes-devel >= %{libcaes_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}
Requires:	libfdata-devel >= %{libfdata_ver}
Requires:	libfdatetime-devel >= %{libfdatetime_ver}
Requires:	libfguid-devel >= %{libfguid_ver}
Requires:	libfvalue-devel >= %{libfvalue_ver}
Requires:	libhmac-devel >= %{libhmac_ver}
Requires:	libuna-devel >= %{libuna_ver}
Requires:	openssl-devel >= 1.0
Requires:	zlib-devel >= 1.2.5

%description devel
Header files for libewf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libewf.

%package static
Summary:	Static libewf library
Summary(pl.UTF-8):	Statyczna biblioteka libewf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libewf library.

%description static -l pl.UTF-8
Statyczna biblioteka libewf.

%package tools
Summary:	Tools to support the Expert Witness Compression Format
Summary(pl.UTF-8):	Narzędzia obsługujące format Expert Witness Compression Format
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	libcdatetime >= %{libcdatetime_ver}
Requires:	libfuse >= 2.6
Requires:	libodraw >= %{libodraw_ver}
Requires:	libsmdev >= %{libsmdev_ver}
Requires:	libsmraw >= %{libsmraw_ver}
Requires:	libuuid >= 2.20

%description tools
Tools to support the Expert Witness Compression Format.

%description tools -l pl.UTF-8
Narzędzia obsługujące format Expert Witness Compression Format.

%package -n python-pyewf
Summary:	Python 2 bindings for libewf library
Summary(pl.UTF-8):	Wiązania Pythona 2 do biblioteki libewf
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pyewf
Python 2 bindings for libewf library.

%description -n python-pyewf -l pl.UTF-8
Wiązania Pythona 2 do biblioteki libewf.

%package -n python3-pyewf
Summary:	Python 3 bindings for libewf library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libewf
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pyewf
Python 3 bindings for libewf library.

%description -n python3-pyewf -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libewf.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python2:--enable-python2} \
	%{?with_python3:--enable-python3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libewf.la

%if %{with python2}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyewf.{la,a}
%endif
%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pyewf.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libewf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewf.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libewf.so
%{_includedir}/libewf
%{_includedir}/libewf.h
%{_pkgconfigdir}/libewf.pc
%{_mandir}/man3/libewf.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libewf.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ewfacquire
%attr(755,root,root) %{_bindir}/ewfacquirestream
%attr(755,root,root) %{_bindir}/ewfdebug
%attr(755,root,root) %{_bindir}/ewfexport
%attr(755,root,root) %{_bindir}/ewfinfo
%attr(755,root,root) %{_bindir}/ewfmount
%attr(755,root,root) %{_bindir}/ewfrecover
%attr(755,root,root) %{_bindir}/ewfverify
%{_mandir}/man1/ewfacquire.1*
%{_mandir}/man1/ewfacquirestream.1*
%{_mandir}/man1/ewfexport.1*
%{_mandir}/man1/ewfinfo.1*
%{_mandir}/man1/ewfmount.1*
%{_mandir}/man1/ewfrecover.1*
%{_mandir}/man1/ewfverify.1*

%if %{with python2}
%files -n python-pyewf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyewf.so
%endif

%if %{with python3}
%files -n python3-pyewf
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pyewf.so
%endif
