Summary:	Graphical IRC (chat) client
Summary(de.UTF-8):	IRC-Client (Chat) mit grafischer Oberfläche
Summary(fr.UTF-8):	Client IRC (chat) avec interface graphique
Summary(pl.UTF-8):	Graficzny klient IRC (chat)
Name:		xchat-gnome
Version:	0.16
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://flapjack.navi.cx/releases/xchat-gnome/%{name}-%{version}.tar.bz2
# Source0-md5:	2b2a4f42b9ea8cbcd15e1ad597cc8b33
Patch0:		%{name}-long-delimiter.patch
Patch1:		%{name}-iconsdir.patch
URL:		http://xchat-gnome.navi.cx/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enchant-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libnotify-devel
BuildRequires:	libsexy-devel
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRequires:	scrollkeeper >= 0.3.11
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper
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
Requires:	perl

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
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-dependency-tracking \
	--enable-gnomefe \
	--enable-ipv6 \
	--disable-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/xchat-gnome/plugins/*.a
rm $RPM_BUILD_ROOT%{_libdir}/xchat-gnome/plugins/*.la

%find_lang xchat-gnome --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f xchat-gnome.lang
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
%dir %{_datadir}/omf/xchat-gnome
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/xchat-gnome
%{_desktopdir}/xchat-gnome.desktop
#%{_pixmapsdir}/xchat-gnome.png
%{_sysconfdir}/gconf/schemas/*.schemas
%{_omf_dest_dir}/%{name}/xchat-gnome-C.omf
%{_datadir}/dbus-1/services/org.gnome.Xchat.service
%{_mandir}/man1/xchat-gnome.1*

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/perl.so

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat-gnome/plugins/python.so
