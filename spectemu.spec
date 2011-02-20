#
# Conditional build:
%bcond_with	svga	# without SVGAlib version
#
Summary:	Sinclair ZX Spectrum emulator
Summary(pl.UTF-8):	Emulator ZX Spectrum 48k
Name:		spectemu
Version:	0.99.3
Release:	8
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/spectemu/%{name}-%{version}.tar.gz
# Source0-md5:	67330d27e3f5c9127413bd6f35aa664b
Source1:	%{name}-pl-man-pages.tar.gz
# Source1-md5:	ce7665f0dbc898773c6f798a63ee3ec2
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-readline.patch
URL:		http://spectemu.sourceforge.net/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	readline-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a 48k ZX-Spectrum emulator for Linux, with full
Z80 instruction set, comprehensive screen, sound and tape emulation,
and snapshot file saving and loading.

%description -l pl.UTF-8
Pakiet zawiera emulator ZX Spectrum 48k dla Linuksa z emulacją prawie
wszystkich instrukcji procesora Z80. spectemu dobrze emuluje
generowanie obrazu i dźwięku, ma możliwość wczytywania i nagrywania
"snapshotów". Ta wersja potrafi wykorzystać joystick.

%package common
Summary:	Sinclair ZX Spectrum emulator - common part
Summary(pl.UTF-8):	Emulator ZX Spectrum 48k - część wspólna
Group:		Applications/Emulators
Obsoletes:	spectemu

%description common
This package contains a 48k ZX-Spectrum emulator for Linux, with full
Z80 instruction set, comprehensive screen, sound and tape emulation,
and snapshot file saving and loading.

This package contains common files for x11 and svga versions.

%description common -l pl.UTF-8
Pakiet zawiera emulator ZX Spectrum 48k dla Linuksa z emulacją prawie
wszystkich instrukcji procesora Z80. spectemu dobrze emuluje
generowanie obrazu i dźwięku, ma możliwość wczytywania i nagrywania
"snapshotów". Ta wersja potrafi wykorzystać joystick.

Ten pakiet zawiera pliki wspólne dla wersji x11 i svga.

%package svga
Summary:	Sinclair ZX Spectrum emulator - svgalib version
Summary(pl.UTF-8):	Emulator ZX Spectrum 48k - wersja svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description svga
svgalib version of Sinclair ZX Spectrum emulator.

%description svga -l pl.UTF-8
Wersja svgalib emulatora Sinclair ZX Spectrum.

%package x11
Summary:	Sinclair ZX Spectrum emulator - X11 version
Summary(pl.UTF-8):	Emulator ZX Spectrum 48k - wersja X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}-%{release}

%description x11
X11 version of Sinclair ZX Spectrum emulator.

%description x11 -l pl.UTF-8
Wersja X11 emulatora Sinclair ZX Spectrum.

%prep
%setup -q -a1
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
%{__make}
%{__make} tapeout

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}{,/pl}/man1} \
	$RPM_BUILD_ROOT{%{_datadir}/spectemu,%{_pixmapsdir},%{_desktopdir}}

install tapeout $RPM_BUILD_ROOT%{_bindir}
install xspect $RPM_BUILD_ROOT%{_bindir}
install xspect.1 tapeout.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xspect.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/xspect.1
install tapeout.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/tapeout.1
install example.cfg $RPM_BUILD_ROOT%{_datadir}/spectemu/spectemu.cfg
install spectkey.png $RPM_BUILD_ROOT%{_datadir}/spectemu/spectkey.png
install specsinc.xpm $RPM_BUILD_ROOT%{_datadir}/spectemu/specsinc.xpm

%if %{with svga}
install vgaspect $RPM_BUILD_ROOT%{_bindir}
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vgaspect.1
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/vgaspect.1
%endif

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc README ChangeLog TODO example.cfg
%attr(755,root,root) %{_bindir}/tapeout
%{_datadir}/spectemu
%{_mandir}/man1/tapeout.1*
%{_mandir}/man1/xspect.1*
%lang(pl) %{_mandir}/pl/man1/tapeout.1*
%lang(pl) %{_mandir}/pl/man1/xspect.1*

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vgaspect
%{_mandir}/man1/vgaspect.1*
%lang(pl) %{_mandir}/pl/man1/vgaspect.1*
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xspect
%{_desktopdir}/spectemu.desktop
%{_pixmapsdir}/spectemu.png
