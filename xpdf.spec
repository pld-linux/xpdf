Summary:	Portable Document Format (PDF) file viewer
Summary(pl):	Przegl±darka plików w formacie PDF
Name:		xpdf
Version:	0.90
Release:	3
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tgz
Source1:	xpdf.desktop
Patch0:		http://www.fefe.de/xpdf-0.90-fefe-diff2.gz
Patch1:		xpdf-DESTDIR.patch
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	libstdc++-devel
BuildRequires:	xpm-devel
BuildRequires:	XFree86-devel
BuildRequires:	t1lib-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. PDF files are sometimes called Acrobat files, after Adobe
Acrobat (Adobe's PDF viewer). Xpdf is a small and efficient program
which uses standard X fonts.

%description -l pl
Xpdf jest przegl±dark± plików zapisanych w formacie PDF (Portable
Document Format). Xpdf jest zaprojektowany tak, by byæ ma³ym i
wydajnym programem. Nie u¿ywa bibliotek Motif czy Xt u¿ywaj±cym fontów
z zasobów X Wondow.

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
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/xpdf.desktop

gzip -9nf ANNOUNCE CHANGES README \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Graphics/Viewers/*
