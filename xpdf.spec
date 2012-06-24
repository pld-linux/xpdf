Summary:	Portable Document Format (PDF) file viewer
Summary(pl):	Przegl�darka plik�w w formacie PDF
Name:		xpdf
Version:	0.90
Release:	1
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	freeware
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tgz
Source1:	xpdf.desktop
Patch0:		http://www.fefe.de/xpdf-0.90-fefe-diff2.gz
Patch1:		xpdf-DESTDIR.patch
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	libstdc++-devel
BuildRequires:	xpm-devel
BuildRequires:	XFree86-devel
BuildRequires:	t1lib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
Xpdf is a viewer for Portable Document Format (PDF) files.  (These are also
sometimes also called 'Acrobat' files, from the name of Adobe's PDF
software.) Xpdf is designed to be small and efficient.  It does not use the
Motif or Xt libraries.  It uses standard X fonts.  Xpdf is quite usable on a
486-66 PC running Linux.

%description -l pl
Xpdf jest przegl�dark� plik�w zapisanych w formacie PDF (nazywanych r�wnie�
czasami plikami 'Acrobata', od nazwy programu firmy Adobe). Xpdf jest 
zaprojektowany tak, by by� ma�ym i wydajnym. Nie u�ywa bibliotek Motif czy Xt.
Wykorzystuje standardowe czcionki �rodowiska X. By m�c u�ywa� Xpdf wystarczy
komputer klasy PC 486-66 z Linuxem na pok�adzie.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" 
CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti" 
LDFLAGS="-s"
export CFLAGS CXXFLAGS LDFLAGS
%configure \
	--with-gzip
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers

make DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers/xpdf.desktop

gzip -9nf ANNOUNCE CHANGES README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applnk/Graphics/Viewers/*
