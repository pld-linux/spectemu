Summary:	Sinclair ZX Spectrum emulator
Summary(pl):	Emulator ZX Spectrum 48k
Name:		spectemu
Version:	0.95.3
Release:	1
License:	GPL
Group:		Applications/Emulators
Group(de):	Applikationen/Emulators
Group(pl):	Aplikacje/Emulatory
Source0:	http://www.inf.bme.hu/~mszeredi/spectemu/%{name}-%{version}.tar.gz
Source1:	%{name}-pl-man-pages.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://www.inf.bme.hu/~mszeredi/spectemu/
BuildRequires:	svgalib-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a 48k ZX-Spectrum emulator for Linux, with full
Z80 instruction set, comprehensive screen, sound and tape emulation,
and snapshot file saving and loading.

%description -l pl
Pakiet zawiera emulator ZX Spectrum 48k dla Linuksa z emulacj± prawie
wszystkich instrukcji procesora Z80. spectemu dobrze emuluje
generowanie obrazu i d¼wiêku, ma mo¿liwo¶æ wczytywania i nagrywania
"snapshotów". Ta wersja potrafi wykorzystaæ joystick.

%prep
%setup -q -a1

%build
autoconf
%configure 
%{__make}
%{__make} tapeout

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{,pl}/man1} \
	$RPM_BUILD_ROOT{%{_datadir}/spectemu,%{_pixmapsdir},%{_applnkdir}/Amusements}

install vgaspect xspect tapeout $RPM_BUILD_ROOT%{_bindir}
install xspect.1 tapeout.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xspect.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/xspect.1
install tapeout.man $RPM_BUILD_ROOT%{_mandir}/pl/man1/tapeout.1
install spectemu.cfg $RPM_BUILD_ROOT%{_datadir}/spectemu/spectemu.cfg
install spectkey.gif $RPM_BUILD_ROOT%{_datadir}/spectemu/spectkey.gif
install specsinc.xpm $RPM_BUILD_ROOT%{_datadir}/spectemu/specsinc.xpm
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/man1/vgaspect.1
echo ".so xspect.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/vgaspect.1

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/xspect
%attr(755,root,root) %{_bindir}/tapeout
%attr(755,root,root) %{_bindir}/vgaspect
%{_datadir}/spectemu
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_applnkdir}/Amusements/*
%{_pixmapsdir}/*
