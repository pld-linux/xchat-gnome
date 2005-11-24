Summary:	Graphical IRC (chat) client
Summary(de):	IRC-Client (Chat) mit grafischer Oberfläche
Summary(fr):	Client IRC (chat) avec interface graphique
Summary(pl):	Graficzny klient IRC (chat)
Name:		xchat-gnome
Version:	0.7
Release:	0.1
Group:		X11/Applications/Networking
License:	GPL
Source0:	http://flapjack.navi.cx/releases/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	a5f0940ee6389d58222a04facca0aa0d
Patch0:	xchat-long-delimiter.patch
URL:		http://xchat.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	python-devel
Requires(post):	GConf2
Conflicts:	xchat
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
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_libdir}/xchat/plugins

%makeinstall
mv -f $RPM_BUILD_ROOT%{_libdir}/dbus.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv -f $RPM_BUILD_ROOT%{_libdir}/perl.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv -f $RPM_BUILD_ROOT%{_libdir}/python.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv -f $RPM_BUILD_ROOT%{_libdir}/notification.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv -f $RPM_BUILD_ROOT%{_libdir}/urlscraper.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang xchat-gnome --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f xchat-gnome.lang
%defattr(644,root,root,755)
%doc README ChangeLog faq.html plugins/plugin20.html
%attr(755,root,root) %{_bindir}/xchat-gnome
%attr(755,root,root) %{_bindir}/xchat-remote
%attr(755,root,root) %{_bindir}/xchat
%dir %{_libdir}/xchat
%dir %{_libdir}/xchat/plugins
%attr(755,root,root) %{_libdir}/xchat/plugins/dbus.so
%attr(755,root,root) %{_libdir}/xchat/plugins/notification.so
%attr(755,root,root) %{_libdir}/xchat/plugins/urlscraper.so
%{_datadir}/xchat
%{_desktopdir}/xchat.desktop
%{_desktopdir}/xchat-gnome.desktop
%{_pixmapsdir}/xchat.png
%{_pixmapsdir}/xchat-gnome.png
%{_sysconfdir}/gconf/schemas/*.schemas
%{_omf_dest_dir}/%{name}/xchat-gnome-C.omf


%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat/plugins/perl.so

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat/plugins/python.so
