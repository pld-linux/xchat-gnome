Summary:	Graphical IRC (chat) client
Summary(de.UTF-8):	IRC-Client (Chat) mit grafischer Oberfläche
Summary(fr.UTF-8):	Client IRC (chat) avec interface graphique
Summary(pl.UTF-8):	Graficzny klient IRC (chat)
Name:		xchat-gnome
Version:	0.26.1
Release:	18
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/xchat-gnome/0.26/%{name}-%{version}.tar.bz2
# Source0-md5:	c9ce3d6e549736edfc1a1dc0282fb363
Patch0:		%{name}-long-delimiter.patch
Patch1:		%{name}-notify.patch
Patch2:		%{name}-makefile.patch
Patch3:		perl-detect.patch
Patch4:		%{name}-openssl-1.1.patch
URL:		http://xchat-gnome.navi.cx/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel >= 0.3
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libsexy-devel >= 0.1.11
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GUI IRC client with DCC file transfers, C plugin interface, Perl and
Python scripting capability, mIRC color, shaded transparency, tabbed
channels and more.

%description -l pl.UTF-8
Klient IRC z graficznym interfejsem użytkownika, z przesyłaniem plików
DCC, interfejsem do wtyczek w C, możliwością uruchamiania skryptów w
Perlu i Pythonie, obsługą kolorów mIRC-a, cieniowaną
przezroczystością, zakładkami z kanałami itd.

%package perl
Summary:	XChat Perl plugin
Summary(pl.UTF-8):	Wtyczka Perla do XChata
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	perl-base

%description perl
Provides Perl scripting capability to XChat.

%description perl -l pl.UTF-8
Wtyczka dodająca do XChata możliwość uruchamiania skryptów w Perlu.

%package python
Summary:	XChat Python plugin
Summary(pl.UTF-8):	Wtyczka Pythona do XChata
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python >= 2.2.0

%description python
Provides Python scripting capability to XChat.

%description python -l pl.UTF-8
Wtyczka dodająca do XChata możliwość uruchamiania skryptów w Pythonie.

%prep
%setup -q
%patch0 -p1
%patch1	-p1
%patch2	-p1
%patch3	-p1
%patch4 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} -fcommon" \
	--enable-compile-warnings=minimum \
	--disable-static \
	--disable-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/xchat-gnome/plugins/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install apps_xchat.schemas
%gconf_schema_install notification.schemas
%gconf_schema_install url_handler.schemas
%gconf_schema_install urlscraper.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall apps_xchat.schemas
%gconf_schema_uninstall notification.schemas
%gconf_schema_uninstall url_handler.schemas
%gconf_schema_uninstall urlscraper.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/xchat-gnome
%dir %{_libdir}/xchat-gnome
%dir %{_libdir}/xchat-gnome/plugins
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/autoaway.so
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/netmonitor.so
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/notification.so
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/notifyosd.so
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/soundnotification.so
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/urlscraper.so
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/xchat-gnome
%{_desktopdir}/xchat-gnome.desktop
%{_sysconfdir}/gconf/schemas/apps_xchat.schemas
%{_sysconfdir}/gconf/schemas/notification.schemas
%{_sysconfdir}/gconf/schemas/url_handler.schemas
%{_sysconfdir}/gconf/schemas/urlscraper.schemas
%{_datadir}/dbus-1/services/org.gnome.Xchat.service
%{_mandir}/man1/xchat-gnome.1*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/perl.so

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/python.so
