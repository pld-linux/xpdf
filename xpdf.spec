Summary:	Portable Document Format (PDF) file viewer
Summary(pl):	Przegl±darka plików w formacie PDF
Name:		xpdf
Version:	0.80
Release:	7
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	freeware
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tgz
Source1:	xpdf.desktop
Patch0:		ftp://ftp.sci.usq.edu.au/pub/linux/xpdf/xpdf-0.80-decrypt.patch
Patch1:		xpdf-DESTDIR.patch
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	libstdc++-devel
BuildRequires:	xpm-devel
BuildRequires:	XFree86-devel
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
Xpdf jest przegl±dark± plików zapisanych w formacie PDF (nazywanych równie¿
czasami plikami 'Acrobata', od nazwy programu firmy Adobe). Xpdf jest 
zaprojektowany tak, by byæ ma³ym i wydajnym. Nie u¿ywa bibliotek Motif czy Xt.
Wykorzystuje standardowe czcionki ¶rodowiska X. By móc u¿ywaæ Xpdf wystarczy
komputer klasy PC 486-66 z Linuxem na pok³adzie.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir} \
	--with-gzip
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/usr/X11R6/share/applnk/Graphics/Viewers

make DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Graphics/Viewers/xpdf.desktop

gzip -9nf ANNOUNCE CHANGES README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
/usr/X11R6/share/applnk/Graphics/Viewers/*
