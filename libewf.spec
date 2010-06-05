Summary:	Library and tools to support the Expert Witness Compression Format
Summary(pl.UTF-8):	Biblioteka i narzędzia obsługujące format Expert Witness Compression Format
Name:		libewf
Version:	20100226
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/libewf/libewf/%{name}-%{version}/libewf-%{version}.tar.gz
# Source0-md5:	a697d629bb74df1fa68f22658634fdb9
URL:		http://sourceforge.net/projects/libewf/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
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
Requires:	zlib-devel

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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%attr(755,root,root) %{_bindir}/ewf*
%attr(755,root,root) %{_libdir}/libewf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libewf.so.1
%{_mandir}/man1/ewf*.1*

%files devel
%defattr(644,root,root,755)
%doc documents/header*.txt
%attr(755,root,root) %{_libdir}/libewf.so
%{_libdir}/libewf.la
%{_includedir}/libewf
%{_includedir}/libewf.h
%{_pkgconfigdir}/libewf.pc
%{_mandir}/man3/libewf.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libewf.a
