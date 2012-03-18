Name:           firefox-ojuba-extra
Version:        2.0.2
Release:        4
Summary:        Ojuba extra files and configurations for firefox
Group:          Applications/Internet
License:        Waqf
URL:            http://www.ojuba.org/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires(post):	firefox,desktop-file-utils
Requires:	ojuba-release-notes >= 1
%define searchplugins ojuba.xml islamqa.xml islamweb.xml

%description
This package contains the default configuration for firefox in Ojuba Linux.

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/searchplugins/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
cp localstore.rdf $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/profile/
cp -a searchplugins/* $RPM_BUILD_ROOT%{_libdir}/firefox/searchplugins/

install -D -p -m 644 all-ojuba.js $RPM_BUILD_ROOT%{_libdir}/firefox/defaults/preferences/all-ojuba.js
install -D -p -m 644 firefox-swf.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/firefox-swf.desktop

echo "browser.startup.homepage=file:///usr/share/doc/HTML/index.html" > $RPM_BUILD_ROOT%{_libdir}/firefox/ojuba-browserconfig.properties

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%posttrans
desktop-file-install --rebuild-mime-info-cache %{_datadir}/applications/firefox-swf.desktop &> /dev/null || :
update-desktop-database &> /dev/null || :

PROFILEn=$(echo $RANDOM | base64)
PROFILE=${PROFILEn/=/o}.default
mkdir -p /etc/skel/.mozilla/firefox/$PROFILE/ &> /dev/null || :
#sed -i "s/^\s*\(Path\s*=\s*\).*/\1$PROFILE/" /etc/skel/.mozilla/firefox/profiles.ini &> /dev/null || :
echo -e "[General]\nStartWithLastProfile=1\n\n[Profile0]\nName=default\nIsRelative=1\nPath=$PROFILE" > /etc/skel/.mozilla/firefox/profiles.ini
cp -f %{_libdir}/firefox/defaults/preferences/all-ojuba.js /etc/skel/.mozilla/firefox/$PROFILE/prefs.js &> /dev/null || :

%postun
rm -rf /etc/skel/.mozilla/firefox &> /dev/null || :

%triggerin -- firefox
for i in %{_libdir}/firefox-*
do
 if [ -x $i/firefox ]; then
   for j in %{searchplugins}
   do
     mkdir -p $i/searchplugins/ || :
     ln -sf %{_libdir}/firefox/searchplugins/$j $i/searchplugins/$j &> /dev/null || :
   done
   mkdir -p $i/defaults/preferences/ || :
   ln -sf %{_libdir}/firefox/defaults/preferences/all-ojuba.js $i/defaults/preferences/all-ojuba.js &> /dev/null || :
   mkdir -p $i/firefox/defaults/profile/ || :
   ln -sf %{_libdir}/firefox/defaults/profile/localstore.rdf $i/defaults/profile/localstore.rdf &> /dev/null || :
   ln -sf %{_libdir}/firefox/ojuba-browserconfig.properties $i/ojuba-browserconfig.properties &> /dev/null || :
 fi
done

%triggerpostun -- firefox
for i in %{_libdir}/firefox-*
do
 if [ ! -x $i/firefox ]; then
   
   for j in %{searchplugins}
   do
     [ -e $i/searchplugins/$j ] && rm $i/searchplugins/$j &> /dev/null
   done
   [ -e $i/defaults/profile/localstore.rdf ] && rm -f $i/defaults/profile/localstore.rdf &> /dev/null
   [ -e $i/defaults/preferences/all-ojuba.js ] && rm -f $i/defaults/preferences/all-ojuba.js &> /dev/null
   [ -e $i/ojuba-browserconfig.properties ] && rm -f $i/ojuba-browserconfig.properties &> /dev/null
 fi
done

%files
%defattr(-,root,root,-)
%{_libdir}/firefox/ojuba-browserconfig.properties
%{_libdir}/firefox/searchplugins/*
%{_libdir}/firefox/defaults/preferences/all-ojuba.js
%{_libdir}/firefox/defaults/profile/localstore.rdf
%{_datadir}/applications/firefox-swf.desktop

%changelog
* Thu Jun 17 2010  Muayyad Saleh Alsadi <alsadi@ojuba.org> - 2.0.0-2
- use a source tarball

* Thu Jun 17 2010  Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.0-5
- use libdir rpm macro

* Wed Jan 14 2009  Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.0-4
- use "resource:/ojuba-browserconfig.properties" as home

* Mon Jun 23 2008  Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.0-3
- small fixes in the spec file

* Tue Jun 17 2008 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.0-2
- Assign swf files to firefox

* Tue May 20 2008 Muayyad Saleh Alsadi <alsadi@ojuba.org> - 1.0.0-1
- Initial version

