#
# Conditional build:
%bcond_without	qt4	# Qt 4 libraries
%bcond_without	qt5	# Qt 5 libraries
#
Summary:	QtGStreamer - libraries integrating Qt 4 with GStreamer
Summary(pl.UTF-8):	QtGStreamer - biblioteki integrujące Qt 4 z GStreamerem
Name:		qt-gstreamer0.10
Version:	0.10.3
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/qt-gstreamer/qt-gstreamer-%{version}.tar.bz2
# Source0-md5:	1dfbca4ffa924b0896dadb42221600e2
URL:		http://gstreamer.net/
BuildRequires:	OpenGL-devel
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.39
BuildRequires:	cmake >= 2.8.9
BuildRequires:	flex
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer0.10-devel >= 0.10.33
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.33
BuildRequires:	libstdc++-devel >= 6:4.5
BuildRequires:	pkgconfig
%if %{with qt4}
BuildRequires:	QtCore-devel >= 4.7
BuildRequires:	QtDeclarative-devel >= 4.7
BuildRequires:	QtGui-devel >= 4.7
BuildRequires:	QtOpenGL-devel >= 4.7
BuildRequires:	QtTest-devel >= 4.7
BuildRequires:	qt4-qmake >= 4.7
%endif
%if %{with qt5}
BuildRequires:	Qt5Core-devel >= 5.0.0
BuildRequires:	Qt5Declarative-devel >= 5.0.0
BuildRequires:	Qt5Gui-devel >= 5.0.0
BuildRequires:	Qt5OpenGL-devel >= 5.0.0
BuildRequires:	Qt5Widgets-devel >= 5.0.0
BuildRequires:	Qt5Test-devel >= 5.0.0
BuildRequires:	qt5-qmake >= 5.0.0
%endif
Requires:	QtCore >= 4.7
Requires:	QtGui >= 4.7
Requires:	QtOpenGL >= 4.7
Requires:	gstreamer0.10 >= 0.10.33
Requires:	gstreamer0.10-plugins-base >= 0.10.33
Obsoletes:	qt-gstreamer < 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtGStreamer is a set of libraries and plugins providing C++ bindings
for GStreamer with a Qt-style API plus some helper classes for
integrating GStreamer better in Qt 4 applications.

Currently, it consists of the following parts:
 * QtGLib - library providing C++/Qt 4 bindings for parts of the GLib
   and GObject APIs, a base on which QtGStreamer is built.
 * QtGStreamer - library providing C++/Qt 4 bindings for GStreamer
 * QtGStreamerUi - library providing integration with QtGui;
   currently, it only provides a video widget that embeds GStreamer's
   video sinks.
 * QtGStreamerUtils - library providing some high level utility
   classes.

In addition, it provides a "qwidgetvideosink" GStreamer element, an
video sink element that can draw directly on QWidgets using QPainter.

%description -l pl.UTF-8
QtGStreamer to zestaw bibliotek i wtyczek z wiązaniami C++ do
GStreamera o API w stylu Qt oraz klasami pomocniczymi dla lepszej
integracji GStreamera w aplikacjach Qt 4.

Obecnie zawiera następujące części:
 - QtGLib - biblioteka z wiązaniami C++/Qt 4 dla części API bibliotek
   GLib i GObject; w oparciu o nią zbudowany jest QtGStreamer
 - QtGStreamer - biblioteka z wiązaniami C++/Qt 4 do GStreamera
 - QtGStreamerUi - biblioteka integrująca z QtGui; obecnie zawiera
   tylko widget wideo osadzający wyjście obrazu (videosink) GStremera.
 - QtGStreamerUtils - biblioteka udostępniająca klasy narzędziowe
   wysokiego poziomu.

Ponadto pakiet udostępnia element GStreamera "qwidgetvideosink" -
element wyjściowy obrazu rysujący bezpośrednio na QWidgetach przy
użyciu QPaintera.

%package devel
Summary:	Header files for QtGStreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.7
Requires:	QtGui-devel >= 4.7
Requires:	gstreamer0.10-devel >= 0.10.33
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.33
Obsoletes:	qt-gstreamer-devel < 1.0

%description devel
Header files for QtGStreamer libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek QtGStreamer.

%package -n QtDeclarative-plugin-gstreamer0.10
Summary:	Qt GStreamer plugin for QtDeclarative
Summary(pl.UTF-8):	Wtyczka Qt GStreamer dla QtDeclarative
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDeclarative >= 4.7
Obsoletes:	QtDeclarative-plugin-gstreamer < 1.0

%description -n QtDeclarative-plugin-gstreamer0.10
Qt GStreamer plugin for QtDeclarative.

%description -n QtDeclarative-plugin-gstreamer0.10 -l pl.UTF-8
Wtyczka Qt GStreamer dla QtDeclarative.

%package -n qt5-gstreamer0.10
Summary:	Qt5GStreamer - libraries integrating Qt 5 with GStreamer
Summary(pl.UTF-8):	Qt5GStreamer - biblioteki integrujące Qt 5 z GStreamerem
Group:		Libraries
Requires:	Qt5Core >= 5.0.0
Requires:	Qt5Gui >= 5.0.0
Requires:	Qt5OpenGL >= 5.0.0
Requires:	gstreamer0.10 >= 0.10.33
Requires:	gstreamer0.10-plugins-base >= 0.10.33
Obsoletes:	qt5-gstreamer < 1.0

%description -n qt5-gstreamer0.10
Qt5GStreamer is a set of libraries and plugins providing C++ bindings
for GStreamer with a Qt-style API plus some helper classes for
integrating GStreamer better in Qt 5 applications.

Currently, it consists of the following parts:
 * Qt5GLib - library providing C++/Qt 5 bindings for parts of the GLib
   and GObject APIs, a base on which Qt5GStreamer is built.
 * Qt5GStreamer - library providing C++/Qt 5 bindings for GStreamer
 * Qt5GStreamerUi - library providing integration with Qt5Gui;
   currently, it only provides a video widget that embeds GStreamer's
   video sinks.
 * Qt5GStreamerUtils - library providing some high level utility
   classes.

In addition, it provides a "qwidgetvideosink" GStreamer element, an
video sink element that can draw directly on QWidgets using QPainter.

%description -n qt5-gstreamer0.10 -l pl.UTF-8
Qt5GStreamer to zestaw bibliotek i wtyczek z wiązaniami C++ do
GStreamera o API w stylu Qt oraz klasami pomocniczymi dla lepszej
integracji GStreamera w aplikacjach Qt 5.

Obecnie zawiera następujące części:
 - Qt5GLib - biblioteka z wiązaniami C++/Qt 5 dla części API bibliotek
   GLib i GObject; w oparciu o nią zbudowany jest QtGStreamer
 - Qt5GStreamer - biblioteka z wiązaniami C++/Qt 5 do GStreamera
 - Qt5GStreamerUi - biblioteka integrująca z Qt5Gui; obecnie zawiera
   tylko widget wideo osadzający wyjście obrazu (videosink) GStremera.
 - QtGStreamerUtils - biblioteka udostępniająca klasy narzędziowe
   wysokiego poziomu.

Ponadto pakiet udostępnia element GStreamera "qwidgetvideosink" -
element wyjściowy obrazu rysujący bezpośrednio na QWidgetach przy
użyciu QPaintera.

%package -n qt5-gstreamer0.10-devel
Summary:	Header files for Qt5GStreamer libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek QtGStreamer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= 5.0.0
Requires:	Qt5Gui-devel >= 5.0.0
Requires:	gstreamer0.10-devel >= 0.10.33
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.33
Obsoletes:	qt5-gstreamer-devel < 1.0

%description -n qt5-gstreamer0.10-devel
Header files for Qt5GStreamer libraries.

%description -n qt5-gstreamer0.10-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Qt5GStreamer.

%package -n Qt5Declarative-plugin-gstreamer0.10
Summary:	Qt GStreamer plugin for Qt5Declarative
Summary(pl.UTF-8):	Wtyczka Qt GStreamer dla Qt5Declarative
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Declarative >= 5.0.0
Obsoletes:	Qt5Declarative-plugin-gstreamer < 1.0

%description -n Qt5Declarative-plugin-gstreamer0.10
Qt GStreamer plugin for Qt5Declarative.

%description -n Qt5Declarative-plugin-gstreamer0.10 -l pl.UTF-8
Wtyczka Qt GStreamer dla Qt5Declarative.

%prep
%setup -q -n qt-gstreamer-%{version}

%build
%if %{with qt4}
install -d build-qt4
cd build-qt4
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DQTGSTREAMER_EXAMPLES=OFF \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt4
%{__make}
cd ..
%endif

%if %{with qt5}
install -d build-qt5
cd build-qt5
%cmake .. \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DQTGSTREAMER_EXAMPLES=OFF \
	-DQT_QMAKE_EXECUTABLE=/usr/bin/qmake-qt5 \
	-DQT_VERSION=5
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with qt4}
%{__make} -C build-qt4 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with qt5}
%{__make} -C build-qt5 install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n qt5-gstreamer0.10 -p /sbin/ldconfig
%postun	-n qt5-gstreamer0.10 -p /sbin/ldconfig

%if %{with qt4}
%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamer-0.10.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUi-0.10.so.0
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQtGStreamerUtils-0.10.so.0
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstqtvideosink.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQtGLib-2.0.so
%attr(755,root,root) %{_libdir}/libQtGStreamer-0.10.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUi-0.10.so
%attr(755,root,root) %{_libdir}/libQtGStreamerUtils-0.10.so
%{_includedir}/QtGStreamer
%{_pkgconfigdir}/QtGLib-2.0.pc
%{_pkgconfigdir}/QtGStreamer-0.10.pc
%{_pkgconfigdir}/QtGStreamerUi-0.10.pc
%{_pkgconfigdir}/QtGStreamerUtils-0.10.pc
%{_libdir}/cmake/QtGStreamer

%files -n QtDeclarative-plugin-gstreamer0.10
%defattr(644,root,root,755)
%dir %{_libdir}/qt4/imports/QtGStreamer
%attr(755,root,root) %{_libdir}/qt4/imports/QtGStreamer/libQtGStreamerQuick1.so
%{_libdir}/qt4/imports/QtGStreamer/qmldir
%endif

%if %{with qt5}
%files -n qt5-gstreamer0.10
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libQt5GLib-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GLib-2.0.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamer-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamer-0.10.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamerUi-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamerUi-0.10.so.0
%attr(755,root,root) %{_libdir}/libQt5GStreamerUtils-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5GStreamerUtils-0.10.so.0
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstqt5videosink.so

%files -n qt5-gstreamer0.10-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5GLib-2.0.so
%attr(755,root,root) %{_libdir}/libQt5GStreamer-0.10.so
%attr(755,root,root) %{_libdir}/libQt5GStreamerUi-0.10.so
%attr(755,root,root) %{_libdir}/libQt5GStreamerUtils-0.10.so
%{_includedir}/Qt5GStreamer
%{_pkgconfigdir}/Qt5GLib-2.0.pc
%{_pkgconfigdir}/Qt5GStreamer-0.10.pc
%{_pkgconfigdir}/Qt5GStreamerUi-0.10.pc
%{_pkgconfigdir}/Qt5GStreamerUtils-0.10.pc
%{_libdir}/cmake/Qt5GStreamer

%files -n Qt5Declarative-plugin-gstreamer0.10
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/imports/QtGStreamer
%attr(755,root,root) %{_libdir}/qt5/imports/QtGStreamer/libQtGStreamerQuick1.so
%{_libdir}/qt5/imports/QtGStreamer/qmldir
%endif
