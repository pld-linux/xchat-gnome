Summary:	Graphical IRC (chat) client
Summary(fr):	Client IRC (chat) avec interface graphique
Summary(de):	IRC-Client (Chat) mit grafischer Oberfläche
Name:		xchat-gnome
Version:	0.3
Release:	0
Group:		X11/Applications/Networking
License:	GPL
URL:		http://xchat.org
Source0:	http://navi.cx/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	c057f7fc07c039e876f68529b9994352
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
Conflicts:	xchat

%description
A GUI IRC client with DCC file transfers, C plugin interface, Perl and
Python scripting capability, mIRC color, shaded transparency, tabbed
channels and more.

%package perl
Summary:	XChat Perl plugin
Group:		X11/Applications/Networking
Requires:	xchat-gnome = %{version}
Requires:	perl
%description perl
Provides Perl scripting capability to XChat.

%package python
Summary:	XChat Python plugin
Group:		X11/Applications/Networking
Requires:	xchat-gnome = %{version}
Requires:	python2 >= 2.2.0
%description python
Provides Python scripting capability to XChat.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-dependency-tracking --enable-gnomefe --disable-tcl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/pixmaps $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
%makeinstall
mv -f $RPM_BUILD_ROOT%{_bindir}/xchat-gnome $RPM_BUILD_ROOT%{_bindir}/xchat
strip -R .note -R .comment $RPM_BUILD_ROOT%{_libdir}/perl.so
strip -R .note -R .comment $RPM_BUILD_ROOT%{_libdir}/python.so
mv $RPM_BUILD_ROOT%{_libdir}/perl.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
mv $RPM_BUILD_ROOT%{_libdir}/python.so $RPM_BUILD_ROOT%{_libdir}/xchat/plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
mv $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/apps_xchat.schemas.in.in \
  $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/apps_xchat.schemas

%find_lang xchat-gnome

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/apps_xchat.schemas \
    >/dev/null || :

%files -f xchat-gnome.lang
%defattr(644,root,root,755)
%doc README ChangeLog faq.html COPYING plugins/plugin20.html plugins/perl/xchat2-perldocs.html
%attr(755,root,root) %{_bindir}/xchat
%{_datadir}/applications/xchat.desktop
%{_datadir}/pixmaps/xchat.png
%{_datadir}/xchat/*
%{_sysconfdir}/gconf/schemas/apps_xchat.schemas
%{_datadir}/applications/xchat-gnome.desktop
%{_datadir}/pixmaps/xchat-gnome.png

%files perl
%defattr(644,root,root,755)
%{_libdir}/xchat/plugins/perl.so

%files python
%defattr(644,root,root,755)
%{_libdir}/xchat/plugins/python.so

%clean
rm -rf $RPM_BUILD_ROOT
