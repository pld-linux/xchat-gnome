Summary:	Graphical IRC (chat) client
Summary(de):	IRC-Client (Chat) mit grafischer Oberfläche
Summary(fr):	Client IRC (chat) avec interface graphique
Summary(pl):	Graficzny klient IRC (chat)
Name:		xchat-gnome
Version:	0.3
Release:	0
Group:		X11/Applications/Networking
License:	GPL
Source0:	http://navi.cx/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	c057f7fc07c039e876f68529b9994352
URL:		http://xchat.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.0
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

%build
%configure \
	--disable-dependency-tracking \
	--enable-gnomefe \
	--disable-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_libdir}/xchat/plugins

%makeinstall

mv -f $RPM_BUILD_ROOT%{_bindir}/xchat-gnome $RPM_BUILD_ROOT%{_bindir}/xchat
mv -f $RPM_BUILD_ROOT%{_libdir}/perl.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv -f $RPM_BUILD_ROOT%{_libdir}/python.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/apps_xchat.schemas.in.in \
	$RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/apps_xchat.schemas

%find_lang xchat-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f xchat-gnome.lang
%defattr(644,root,root,755)
%doc README ChangeLog faq.html COPYING plugins/plugin20.html plugins/perl/xchat2-perldocs.html
%attr(755,root,root) %{_bindir}/xchat
%{_datadir}/xchat/*
%{_desktopdir}/xchat.desktop
%{_desktopdir}/xchat-gnome.desktop
%{_pixmapsdir}/xchat.png
%{_pixmapsdir}/xchat-gnome.png
%{_sysconfdir}/gconf/schemas/apps_xchat.schemas

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat/plugins/perl.so

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xchat/plugins/python.so
