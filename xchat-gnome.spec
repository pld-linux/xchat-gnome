Summary:	Graphical IRC (chat) client
Summary(de):	IRC-Client (Chat) mit grafischer Oberfläche
Summary(fr):	Client IRC (chat) avec interface graphique
Summary(pl):	Graficzny klient IRC (chat)
Name:		xchat-gnome
Version:	0.14
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://flapjack.navi.cx/releases/xchat-gnome/%{name}-%{version}.tar.bz2
# Source0-md5:	8686d5328541404415df486fa115eb6d
Patch0:		%{name}-long-delimiter.patch
URL:		http://xchat.org/
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

%description -l pl
Klient IRC z graficznym interfejsem u¿ytkownika, z przesy³aniem plików
DCC, interfejsem do wtyczek w C, mo¿liwo¶ci± uruchamiania skryptów w
Perlu i Pythonie, obs³ug± kolorów mIRC-a, cieniowan±
przezroczysto¶ci±, zak³adkami z kana³ami itd.

%package perl
Summary:	XChat Perl plugin
Summary(pl):	Wtyczka Perla do XChata
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	perl

%description perl
Provides Perl scripting capability to XChat.

%description perl -l pl
Wtyczka dodaj±ca do XChata mo¿liwo¶æ uruchamiania skryptów w Perlu.

%package python
Summary:	XChat Python plugin
Summary(pl):	Wtyczka Pythona do XChata
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	python >= 2.2.0

%description python
Provides Python scripting capability to XChat.

%description python -l pl
Wtyczka dodaj±ca do XChata mo¿liwo¶æ uruchamiania skryptów w Pythonie.

%prep
%setup -q
%patch0 -p1

%build
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
%{_iconsdir}/hicolor/48x48/apps/xchat-gnome.png
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
