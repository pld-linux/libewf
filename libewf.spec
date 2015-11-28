#
# Conditional build:
%bcond_without	python	# Python bindings
#
Summary:	Library to support the Expert Witness Compression Format
Summary(pl.UTF-8):	Biblioteka obsługująca format Expert Witness Compression Format
Name:		libewf
# see AC_INIT in configure.ac
Version:	20150107
%define	gitrev	f5aa33eaa9f93c60a9005c46c6afe88d8a46645e
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libewf/archive/%{gitrev}/%{name}-%{version}.tar.gz
# Source0-md5:	24ede215847822fe86a88a6ce77fac4a
Patch0:		%{name}-system-libs.patch
Patch1:		%{name}-includes.patch
URL:		https://github.com/libyal/libewf/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel >= 1.0
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libbfio-devel >= 20120426
BuildRequires:	libcaes-devel >= 20130716
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcdatetime-devel >= 20141018
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcpath-devel >= 20120701
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcsystem-devel >= 20141018
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libfcache-devel >= 20140601
BuildRequires:	libfdata-devel >= 20140915
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libfvalue-devel >= 20130415
BuildRequires:	libhmac-devel >= 20130714
BuildRequires:	libodraw-devel >= 20120630
BuildRequires:	libsmdev-devel >= 20140406
BuildRequires:	libsmraw-devel >= 20120630
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	libuuid-devel >= 2.20
BuildRequires:	openssl-devel >= 1.0
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel >= 1.2.5
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
Requires:	libbfio-devel >= 20120426
Requires:	libcaes-devel >= 20130716
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcfile-devel >= 20140503
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcpath-devel >= 20120701
Requires:	libcsplit-devel >= 20120701
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libfcache-devel >= 20140601
Requires:	libfvalue-devel >= 20130415
Requires:	libhmac-devel >= 20130714
Requires:	libuna-devel >= 20120425
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
Requires:	libcdatetime-devel >= 20141018
Requires:	libcsystem >= 20141018
Requires:	libfuse >= 2.6
Requires:	libodraw >= 20120630
Requires:	libsmdev >= 20140406
Requires:	libsmraw >= 20120630

%description tools
Tools to support the Expert Witness Compression Format.

%description tools -l pl.UTF-8
Narzędzia obsługujące format Expert Witness Compression Format.

%package -n python-pyewf
Summary:	Python bindings for libewf library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libewf
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pyewf
Python bindings for libewf library.

%description -n python-pyewf -l pl.UTF-8
Wiązania Pythona do biblioteki libewf.

%prep
%setup -q -n %{name}-%{gitrev}
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libewf.la

%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pyewf.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libewf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewf.so.2

%files devel
%defattr(644,root,root,755)
%doc documents/header*.txt
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

%if %{with python}
%files -n python-pyewf
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pyewf.so
%endif
