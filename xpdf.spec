Summary:	Portable Document Format (PDF) file viewer
Summary(ja):	X Window System ¤Ç¤Î PDF ¥Õ¥¡¥¤¥ë¥ô¥å¡¼¥¢
Summary(pl):	Przegl±darka plików w formacie PDF
Name:		xpdf
Version:	0.92
Release:	6
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
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

%description -l ja
xpdf ¤Ï Portable Document Format (PDF) ¥Õ¥¡¥¤¥ë¤Î X Window System
¾å¤Ç¤Î ¥ô¥å¡¼¥¢¤Ç¤¹¡£PDF ¥Õ¥¡¥¤¥ë¤Ï Adobe Acrobat (Adobe ¤Î PDF
¥ô¥å¡¼¥¢) ¤Ë¤Á¤Ê¤ó¤Ç¡¢ »þ¡¹ Acrobat ¥Õ¥¡¥¤¥ë¤È¸Æ¤Ð¤ì¤Þ¤¹¡£xpdf
¤Ï¾®¤µ¤¯¡¢É¸½àÅª¤Ê X ¤Î¥Õ¥©¥ó¥È¤ò »È¤¦¸ú²ÌÅª¤Ê¥×¥í¥°¥é¥à¤Ç¤¹¡£ PDF
¥Õ¥¡¥¤¥ë¤Î¥ô¥å¡¼¥¢¤¬É¬Í×¤Ê¤é¤Ð¡¢xpdf
¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Þ¤·¤ç¤¦¡£

%description -l pl
Xpdf jest przegl±dark± plików zapisanych w formacie PDF (Portable
Document Format). Xpdf jest zaprojektowany tak, by byæ ma³ym i
wydajnym programem. Nie u¿ywa bibliotek Motif czy Xt u¿ywaj±cym fontów
z zasobów X Window.

%prep
%setup -q

%build
aclocal
autoconf
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
export CXXFLAGS 
%configure \
	--with-gzip \
	--enable-opi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/xpdf.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf ANNOUNCE CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*
