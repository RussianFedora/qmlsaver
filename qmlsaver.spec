%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global gitcommit a665e9b
%global date 20100905
%global realver 0.1
#https://github.com/proDOOMman/qmlsaver/blob/master/debian/changelog


Summary:    Screensaver with modules written in Qt4/QML
Summary(ru):   Хранитель экрана с модулями написанными на Qt4/QML
Name:       qmlsaver
Group:      Amusements/Graphics
URL:        https://github.com/proDOOMman/qmlsaver
Version:    %{realver}
Release:    1%{?dist}.R
License:    GPLv2
Source:     https://github.com/proDOOMman/qmlsaver/tarball/%{gitcommit}
Source99:   qmlsaver-xcreensaverhack.conf
Source100:  README.RFRemix
Patch0:     qmlsaver-0.1-1.fc16.patch

%description
The qmlsaver package contains digital clock screensaver for Gnome/KDE 
written in Qt4/QML.
Qmlsaver may be used as module for xscreensaver.


%description -l ru
Этот RPM qmlsaver содержит в себе хранитель экрана типа цифровые часы 
для Gnome/KDE написаный на Qt4/QML.
Может быть использован как модуль для xscreensaver.

%prep
%setup -q -n proDOOMman-%{name}-%{gitcommit}
%patch0 -p1 -b .fc16
cp %{SOURCE99} .

%build
qmake-qt4
make %{?_smp_mflags}
cp %{SOURCE100} .

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
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/xscreensaver/hacks.conf.d
cp qmlsaver-xscreensaverhack.conf ${RPM_BUILD_ROOT}%{_datadir}/xscreensaver/hacks.conf.d


%post
if [ -f /usr/bin/update-xscreensaver-hacks ]; then
    /usr/bin/update-xscreensaver-hacks
fi

%postun
#rm -rf ${RPM_BUILD_ROOT}%{_datadir}/xscreensaver/hacks.conf.d/qmlsaver-xscreensaverhack.conf

if [ -f /usr/bin/update-xscreensaver-hacks ]; then
    /usr/bin/update-xscreensaver-hacks
fi


%files
%defattr(-,root,root)
%dir %{_datadir}/qmlsaver
%{_datadir}/qmlsaver/qmls/segment-clock/*
%{_datadir}/applications/screensavers/qmlsaver*
%{_libexecdir}/xscreensaver/qmlsaver*
%{_datadir}/xscreensaver/config/qmlsaver*
%{_datadir}/xscreensaver/hacks.conf.d/qmlsaver*
%doc README.RFRemix


%changelog
* Wed Dec 30 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1.R
- SPEC file updated due to be inline with RFRemix repositary requirements

* Sat Dec 25 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- SPEC file updated for Fedora RFRemix and x86_64 

* Sat Dec 24 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- Initial implementation for Fedora. 
- Previously Debian-only screensaver RPMed to FC 16 / Qt8.4  / Gnome3.

