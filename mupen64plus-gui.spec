%define debug_package %{nil}

%global commit0 d20459924b6d9db1f3d028aa91a748bc8abc8215
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:		mupen64plus-gui
Summary:	mupen64plus GUI written in Qt5
License:	GPLv3
Group:		Applications/Emulators
URL:		https://github.com/m64p/mupen64plus-gui
Version:	0.1
Release:        1%{?gver}%{dist}
Source0:        https://github.com/m64p/mupen64plus-GLideN64/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1:	mupen64plus-gui
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	%{name}-snapshot
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


BuildRequires:	qt-devel >= 4.4.3
BuildRequires:	qt5-qtbase-devel 
BuildRequires:	SDL2-devel
BuildRequires:	git

BuildRequires:	SDL_ttf-devel
BuildRequires:	gtk2-devel
BuildRequires:	lirc-devel
BuildRequires:	desktop-file-utils

BuildRequires:	mesa-libGLU-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype-devel
BuildRequires:	boost-devel
BuildRequires:	gzip
BuildRequires:	glew-devel
BuildRequires:  binutils
BuildRequires:	nasm

BuildRequires:	mupen64plus
Requires:	mupen64plus

%description
mupen64plus-gui is written in Qt5. It supports everything you'd expect from a 
mupen64plus frontend (plugin selection, configuration editing, save state 
management, screenshots, pausing, etc).

%prep

%{S:4} -c %{commit0}

%setup -T -D -n mupen64plus-gui-%{shortcommit0}

sed -i 's:qmake:qmake-qt5:g' build.sh

%build
chmod a+x build.sh
./build.sh

%install
install -dm 755 %{buildroot}/%{_bindir} \
	%{buildroot}/%{_libdir}/%{name} \
	%{buildroot}/%{_datadir}/applications \
	%{buildroot}/usr/share/pixmaps 

cp -rf mupen64plus/* %{buildroot}/%{_libdir}/%{name}/
#chmod a+x %{buildroot}/%{_libdir}/%{name}/mupen64plus

cp -f mupen64plus-gui/build/mupen64plus-gui %{buildroot}/%{_libdir}/%{name}
chmod a+x %{buildroot}/%{_libdir}/%{name}/mupen64plus-gui

cp -f %{S:1} %{buildroot}/%{_bindir}/
chmod a+x %{buildroot}/%{_bindir}/mupen64plus-gui

install -Dm644 %{S:2} "%{buildroot}/usr/share/applications/%{name}.desktop"
install -Dm644 %{S:3} "%{buildroot}/usr/share/pixmaps/%{name}.png"


%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog

* Wed Aug 30 2017 David Vásquez <davidva AT tutanota DOT com> - 0.1-1.gitd48f86f
- Initial build
