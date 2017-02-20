Name: ojuba-firefox
Version: 3
Release: 1%{?dist}
Summary: Ojuba Firefox Settings
Summary(ar): إعدادات أعجوبة لفيرفكس
License: WAQFv2
URL: http://ojuba.org
Obsoletes: firefox-ojuba-extra
Provides: firefox-ojuba-extra
Requires: firefox
BuildArch: noarch

%description
Ojuba Firefox Settings

%description -l ar
إعدادات أعجوبة لفيرفكس
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/browser/defaults/preferences
echo 'pref("browser.startup.homepage", "data:text/plain,browser.startup.homepage=http://ojuba.org");
pref("ui.key.menuAccessKeyFocuses",false);
pref("general.autoScroll", true);
pref("browser.bookmarks.restore_default_bookmarks", true);' > $RPM_BUILD_ROOT%{_libdir}/firefox/browser/defaults/preferences/firefox-ojuba-default-prefs.js

%files
%{_libdir}/firefox/browser/defaults/preferences/firefox-ojuba-default-prefs.js

%changelog
* Fri Feb 3 2017 Mosaab Alzoubi <moceap@hotmail.com> - 3-1
- Simplized
- Remove SWF local run for security reason
- Renamed to ojuba-firefox

* Sun Feb 16 2014 Mosaab Alzoubi <moceap@hotmail.com> - 2.0.3-2
- General Revision.

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
