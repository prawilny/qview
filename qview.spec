Name:           qview
Version:        5.0
Release:        1%{?dist}
Summary:        Qt image viewer designed with minimalism and usability in mind
License:        GPLv3
URL:            https://github.com/jurplel/%{name}
# wget https://github.com/jurplel/%{name}/archive/refs/tags/%{version}.tar.gz
Source0:        %{version}.tar.gz
BuildRequires:  make
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtbase-devel
Requires:       qt5-qtbase
Requires:       hicolor-icon-theme

%description
qView is an image viewer designed with minimalism and usability in mind.

%global debug_package %{nil}
%prep
%setup -n qView-%{version}

%build
qmake-qt5 PREFIX="/usr"
make -j

%install
make -j INSTALL_ROOT="%{buildroot}" install

%files
%{_bindir}/qview
%{_datadir}/applications/com.interversehq.qView.desktop
%{_datadir}/icons/hicolor/16x16/apps/com.interversehq.qView.png
%{_datadir}/icons/hicolor/32x32/apps/com.interversehq.qView.png
%{_datadir}/icons/hicolor/64x64/apps/com.interversehq.qView.png
%{_datadir}/icons/hicolor/128x128/apps/com.interversehq.qView.png
%{_datadir}/icons/hicolor/256x256/apps/com.interversehq.qView.png
%{_datadir}/icons/hicolor/scalable/apps/com.interversehq.qView.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.interversehq.qView-symbolic.svg
%{_datadir}/licenses/qview/LICENSE
%{_datadir}/metainfo/com.interversehq.qView.appdata.xml

%changelog
* Sat Apr 2 2022 Adam Czajkowski <a.c.czajkowski@gmail.com> 5.0
- Initial version of the package
