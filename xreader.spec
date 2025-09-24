Summary:	Simple document viewer
Summary(pl.UTF-8):	Prosta przeglądarka dokumentów
Name:		xreader
Version:	4.2.9
Release:	3
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/xreader/tags
Source0:	https://github.com/linuxmint/xreader/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	188107ff58405f5ef479ad7f99436ed6
# remove when we get kpathsea.pc in texlive
Patch0:		%{name}-kpathsea-no-pc.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-meson.patch
URL:		https://github.com/linuxmint/xreader
BuildRequires:	appstream-glib
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	gtk-doc
BuildRequires:	gtk-webkit4.1-devel >= 2.34
BuildRequires:	intltool
BuildRequires:	kpathsea-devel
BuildRequires:	libarchive-devel >= 3.6.0
BuildRequires:	libgxps-devel >= 0.2.1
# not used actually
#BuildRequires:	libsecret-devel >= 0.5
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	meson >= 0.46
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	t1lib-devel
BuildRequires:	xapps-devel >= 2.5.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.38.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas
Requires:	hicolor-icon-theme
Requires:	libarchive >= 3.6.0
Requires:	shared-mime-info
Requires:	xapps >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-Apps Document Reader is a document viewer capable of displaying
multiple and single page document formats like PDF and PostScript.

%description -l pl.UTF-8
X-Apps Document Viewer to przeglądarka dokumentów potrafiąca
wyświetlać dokumenty jedno- i wielostronnicowe, takie jak PDF czy
PostScript.

%package libs
Summary:	X-Apps Document Reader shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone X-Apps Document Reader
Group:		X11/Libraries
Requires:	cairo >= 1.14.0
Requires:	glib2 >= 1:2.36.0
Requires:	gtk+3 >= 3.14.0
Requires:	gtk-webkit4.1 >= 2.34

%description libs
X-Apps Document Reader shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone X-Apps Document Reader.

%package devel
Summary:	Header files for X-Apps Document Reader
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek X-Apps Document Reader
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+3-devel >= 3.14.0

%description devel
Header files for X-Apps Document Reader.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek X-Apps Document Reader.

%package apidocs
Summary:	API documentation files for X-Apps Document Reader libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek X-Apps Document Reader
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation files for X-Apps Document Reader libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek X-Apps Document Reader.

%package backend-djvu
Summary:	View DJVu documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów DjVu w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.17

%description backend-djvu
View DJVu documents with X-Apps Document Reader.

%description backend-djvu -l pl.UTF-8
Przeglądanie dokumentów DjVu w przeglądarce X-Apps Document Reader.

%package backend-dvi
Summary:	View DVI documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów DVI w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libspectre >= 0.2.0

%description backend-dvi
View DVI documents with X-Apps Document Reader.

%description backend-dvi -l pl.UTF-8
Przeglądanie dokumentów DVI w przeglądarce X-Apps Document Reader.

%package backend-epub
Summary:	View ePub documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów ePub w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.5.0
Requires:	MathJax-base

%description backend-epub
View ePub documents with X-Apps Document Reader.

%description backend-epub -l pl.UTF-8
Przeglądanie dokumentów ePub w przeglądarce X-Apps Document Reader.

%package backend-pdf
Summary:	View PDF documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów PDF w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	poppler-glib >= 0.22.0

%description backend-pdf
View PDF documents with X-Apps Document Reader.

%description backend-pdf -l pl.UTF-8
Przeglądanie dokumentów PDF w przeglądarce X-Apps Document Reader.

%package backend-ps
Summary:	View PostScript documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów PostScript w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libspectre >= 0.2.0

%description backend-ps
View PostScript documents with X-Apps Document Reader.

%description backend-ps -l pl.UTF-8
Przeglądanie dokumentów PostScript w przeglądarce X-Apps Document
Reader.

%package backend-xps
Summary:	View XPS documents with X-Apps Document Reader
Summary(pl.UTF-8):	Przeglądanie dokumentów XPS w przeglądarce X-Apps Document Reader
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libgxps >= 0.2.1

%description backend-xps
View XPS documents with X-Apps Document Reader.

%description backend-xps -l pl.UTF-8
Przeglądanie dokumentów XPS w przeglądarce X-Apps Document Reader.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%meson \
	--default-library=shared \
	-Dcomics=true \
	-Ddocs=true \
	-Ddjvu=true \
	-Ddvi=true \
	-Dhelp_files=true \
	-Dintrospection=true \
	-Dpixbuf=true \
	-Dmathjax-directory=%{_datadir}/MathJax \
	-Dt1lib=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc 2.39
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,jv}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md debian/{changelog,copyright}
%attr(755,root,root) %{_bindir}/xreader
%attr(755,root,root) %{_bindir}/xreader-previewer
%attr(755,root,root) %{_bindir}/xreader-thumbnailer
%attr(755,root,root) %{_libexecdir}/xreaderd
%dir %{_libdir}/xreader
%dir %{_libdir}/xreader/3
%dir %{_libdir}/xreader/3/backends
%attr(755,root,root) %{_libdir}/xreader/3/backends/libcomicsdocument.so
%{_libdir}/xreader/3/backends/comicsdocument.xreader-backend
%attr(755,root,root) %{_libdir}/xreader/3/backends/libpixbufdocument.so
%{_libdir}/xreader/3/backends/pixbufdocument.xreader-backend
%attr(755,root,root) %{_libdir}/xreader/3/backends/libtiffdocument.so
%{_libdir}/xreader/3/backends/tiffdocument.xreader-backend
%{_datadir}/xreader
%{_datadir}/dbus-1/services/org.x.reader.Daemon.service
%{_datadir}/glib-2.0/schemas/org.x.reader.gschema.xml
%{_datadir}/metainfo/xreader.appdata.xml
%{_datadir}/thumbnailers/xreader.thumbnailer
%{_desktopdir}/xreader.desktop
%{_iconsdir}/hicolor/*x*/apps/xreader.png
%{_iconsdir}/hicolor/scalable/apps/xreader.svg
%{_mandir}/man1/xreader.1*
%{_mandir}/man1/xreader-previewer.1*
%{_mandir}/man1/xreader-thumbnailer.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxreaderdocument.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxreaderdocument.so.3
%attr(755,root,root) %{_libdir}/libxreaderview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxreaderview.so.3
%{_libdir}/girepository-1.0/XreaderDocument-1.5.typelib
%{_libdir}/girepository-1.0/XreaderView-1.5.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxreaderdocument.so
%attr(755,root,root) %{_libdir}/libxreaderview.so
%{_includedir}/xreader
%{_datadir}/gir-1.0/XreaderDocument-1.5.gir
%{_datadir}/gir-1.0/XreaderView-1.5.gir
%{_pkgconfigdir}/xreader-document-1.5.pc
%{_pkgconfigdir}/xreader-view-1.5.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxreaderdocument-1.5
%{_gtkdocdir}/libxreaderview-1.5

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libdjvudocument.so
%{_libdir}/xreader/3/backends/djvudocument.xreader-backend

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libdvidocument.so
%{_libdir}/xreader/3/backends/dvidocument.xreader-backend

%files backend-epub
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libepubdocument.so
%{_libdir}/xreader/3/backends/epubdocument.xreader-backend

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libpdfdocument.so
%{_libdir}/xreader/3/backends/pdfdocument.xreader-backend

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libpsdocument.so
%{_libdir}/xreader/3/backends/psdocument.xreader-backend

%files backend-xps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xreader/3/backends/libxpsdocument.so
%{_libdir}/xreader/3/backends/xpsdocument.xreader-backend
