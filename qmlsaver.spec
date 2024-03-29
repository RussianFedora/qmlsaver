%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global gitcommit a665e9b
%global gitcommit_full a665e9b3fab50b7c740f9d6b4632d1f182f6b293
%global date 20100905
%global realver 0.1
#https://github.com/proDOOMman/qmlsaver/blob/master/debian/changelog


Summary:        Screensaver with modules written in Qt4/QML
Summary(ru):    Хранитель экрана с модулями написанными на Qt4/QML
Name:           qmlsaver
Group:          Amusements/Graphics
URL:            https://github.com/proDOOMman/qmlsaver
Version:        %{realver}
Release:        2%{?dist}
License:        GPLv2
Source:         https://github.com/proDOOMman/qmlsaver/tarball/%{gitcommit_full}
Source99:       qmlsaver-xscreensaverhack.conf
Patch0:         qmlsaver-0.1-1.fc16.patch

BuildRequires:  qt-devel

%description
The qmlsaver package contains digital clock screensaver for Gnome/KDE 
written in Qt4/QML.
Qmlsaver may be used as module for xscreensaver.


%description -l ru
Этот RPM qmlsaver содержит в себе хранитель экрана типа цифровые часы 
для Gnome/KDE написанный на Qt4/QML.
Может быть использован как модуль для xscreensaver.

%prep
%setup -q -n proDOOMman-%{name}-%{gitcommit}
%patch0 -p1 -b .fc16
cp %{SOURCE99} .

%build
qmake-qt4
make %{?_smp_mflags}

%install
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
if [ -f %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi

%postun
if [ -f %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi


%files
%dir %{_datadir}/qmlsaver
%{_datadir}/qmlsaver/qmls/segment-clock/*
%{_datadir}/applications/screensavers/qmlsaver*
%{_libexecdir}/xscreensaver/qmlsaver*
%{_datadir}/xscreensaver/config/qmlsaver*
%{_datadir}/xscreensaver/hacks.conf.d/qmlsaver*


%changelog
* Wed Dec 19 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 0.1-2.R
- Clean spec

* Wed Dec 31 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1.R
- Integration with xscreensaver update script

* Wed Dec 30 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1.R
- SPEC file updated due to be inline with RFRemix repositary requirements

* Sat Dec 25 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- SPEC file updated for Fedora RFRemix and x86_64 

* Sat Dec 24 2011 Yaroslav Cherny <pacifictype@gmail.com> - 0.1-1
- Initial implementation for Fedora. 
- Previously Debian-only screensaver RPMed to FC 16 / Qt8.4  / Gnome3.

