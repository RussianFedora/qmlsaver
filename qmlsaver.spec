Summary:    Screensaver with modules written in Qt4/QML
Name:       qmlsaver
Group:      Amusements/Graphics
URL:        https://github.com/proDOOMman/qmlsaver
Version:    0.1
Release:    1%{?dist}.R

License:    GPLv2
Source:     proDOOMman-qmlsaver-a665e9b.tar.gz
Patch0:     qmlsaver-0.1-1.fc16.patch

%description
The qmlsaver package contains digital clock screensaver for Gnome/KDE
written in Qt4/QML.
Qmlsaver may be used as module for xscreensaver.

%prep
%setup -q -n proDOOMman-qmlsaver-a665e9b
%patch0 -p1 -b .fc16

%build
qmake-qt4
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/qmlsaver/qmls/segment-clock/content
cp -r qmls/segment-clock/* ${RPM_BUILD_ROOT}%{_datadir}/qmlsaver/qmls/segment-clock/
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications/screensavers/
cp qmlsaver.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/screensavers/
mkdir -p ${RPM_BUILD_ROOT}%{_libexecdir}/xscreensaver
cp qmlsaver ${RPM_BUILD_ROOT}%{_libexecdir}/xscreensaver
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/xscreensaver/config
cp qmlsaver.xml ${RPM_BUILD_ROOT}%{_datadir}/xscreensaver/config

%files
%defattr(-,root,root)
%dir %{_datadir}/qmlsaver
%{_datadir}/qmlsaver/qmls/segment-clock/*
%{_datadir}/applications/screensavers/qmlsaver*
%{_libexecdir}/xscreensaver/qmlsaver*
%{_datadir}/xscreensaver/config/qmlsaver*

%changelog
* Wed Dec 28 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1.R
- SPEC file updated due to be inline with RFRemix repositary requirements

* Sat Dec 25 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- SPEC file updated for Fedora RFRemix and x86_64 

* Sat Dec 24 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- Initial implementation for Fedora. 
- Previously Debian-only screensaver RPMed to FC 16 / Qt8.4  / Gnome3.

