Summary:	Sinclair ZX Spectrum emulator
Summary(pl):	Emulator ZX Spectrum 48k
Name:		spectemu
Version:	0.95.3
Release:	7
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.inf.bme.hu/~mszeredi/spectemu/%{name}-%{version}.tar.gz
Source1:	%{name}-pl-man-pages.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-readline.patch
URL:		http://www.inf.bme.hu/~mszeredi/spectemu/
BuildRequires:	XFree86-devel
BuildRequires:	readline-devel
%ifarch %{ix86} ppc
BuildRequires:	svgalib-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin

%description
This package contains a 48k ZX-Spectrum emulator for Linux, with full
Z80 instruction set, comprehensive screen, sound and tape emulation,
and snapshot file saving and loading.

%description -l pl
Pakiet zawiera emulator ZX Spectrum 48k dla Linuksa z emulacj� prawie
wszystkich instrukcji procesora Z80. spectemu dobrze emuluje
generowanie obrazu i d�wi�ku, ma mo�liwo�� wczytywania i nagrywania
"snapshot�w". Ta wersja potrafi wykorzysta� joystick.

%package common
Summary:	Sinclair ZX Spectrum emulator - common part
Summary(pl):	Emulator ZX Spectrum 48k - cz�� wsp�lna
Group:		Applications/Emulators
Obsoletes:	spectemu

%description common
This package contains a 48k ZX-Spectrum emulator for Linux, with full
Z80 instruction set, comprehensive screen, sound and tape emulation,
and snapshot file saving and loading.

This package contains common files for x11 and svga versions.

%description common -l pl
Pakiet zawiera emulator ZX Spectrum 48k dla Linuksa z emulacj� prawie
wszystkich instrukcji procesora Z80. spectemu dobrze emuluje
generowanie obrazu i d�wi�ku, ma mo�liwo�� wczytywania i nagrywania
"snapshot�w". Ta wersja potrafi wykorzysta� joystick.

Ten pakiet zawiera pliki wsp�lne dla wersji x11 i svga.

%package svga
Summary:	Sinclair ZX Spectrum emulator - svgalib version
Summary(pl):	Emulator ZX Spectrum 48k - wersja svgalib
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description svga
svgalib version of Sinclair ZX Spectrum emulator.

%description svga -l pl
Wersja svgalib emulatora Sinclair ZX Spectrum.

%package x11
Summary:	Sinclair ZX Spectrum emulator - X11 version
Summary(pl):	Emulator ZX Spectrum 48k - wersja X11
Group:		Applications/Emulators
Requires:	%{name}-common = %{version}

%description x11
X11 version of Sinclair ZX Spectrum emulator.

%description x11 -l pl
Wersja X11 emulatora Sinclair ZX Spectrum.

%prep
%setup -q -a1
%patch0 -p1

%build
autoconf
%configure
%{__make}
%{__make} tapeout

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_xbindir},%{_mandir}{,/pl}/man1} \
	$RPM_BUILD_ROOT{%{_datadir}/spectemu,%{_pixmapsdir},%{_applnkdir}/Amusements}

install tapeout $RPM_BUILD_ROOT%{_bindir}
install xspect $RPM_BUILD_ROOT%{_xbindir}
install xspect.1 tapeout.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xspect.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/xspect.1
install tapeout.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/tapeout.1
install spectemu.cfg $RPM_BUILD_ROOT%{_datadir}/spectemu/spectemu.cfg
install spectkey.gif $RPM_BUILD_ROOT%{_datadir}/spectemu/spectkey.gif
install specsinc.xpm $RPM_BUILD_ROOT%{_datadir}/spectemu/specsinc.xpm

%ifarch %{ix86} ppc
install vgaspect $RPM_BUILD_ROOT%{_bindir}
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vgaspect.1
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/vgaspect.1
%endif

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO example.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/tapeout
%{_datadir}/spectemu
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%ifarch %{ix86} ppc
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vgaspect
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/xspect
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
