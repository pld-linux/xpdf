Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System ¤Ç¤Î PDF ¥Õ¥¡¥¤¥ë¥ô¥å¡¼¥¢
Summary(pl):	Przegl±darka plików w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Name:		xpdf
Version:	1.00
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	t1lib-devel >= 1.3.0
BuildRequires:	freetype-devel >= 2.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	pdftops
Obsoletes:	pdftohtml-pdftops

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. PDF files are sometimes called Acrobat files, after Adobe
Acrobat (Adobe's PDF viewer). Xpdf is a small and efficient program
which uses standard X fonts.

%description -l es
Xpdf es un visor de archivos PDF (Portable Document Format). (Estos
son algunas veces llamados de archivos 'Acrobat', nombre del software
PDF del Adobe. Xpdf fue proyectado para ser pequeño y eficiente. Usa
fuentes padrón X y no necesita de las bibliotecas Motif el Xt.

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

%description -l pt_BR
Xpdf é um visualizador de arquivos PDF (Portable Document Format).
(Estes são algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padrão X e não precisa das bibliotecas Motif
ou Xt.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
export CXXFLAGS
%configure2_13 \
	--with-gzip \
    --enable-a4-paper \
	--enable-opi \
	--enable-freetype2 \
	--with-freetype2-includes=/usr/include/freetype2 \
	--with-freetype-includes=/usr/include/freetype
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
