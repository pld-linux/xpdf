#
# Conditional build:
%bcond_without	protections	# remove protections against fair use (printing and copying)
#
Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System ¤Ç¤Î PDF ¥Õ¥¡¥¤¥ë¥ô¥å¡¼¥¢
Summary(pl):	Przegl±darka plików w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Summary(ru):	ðÒÏÇÒÁÍÍÁ ÄÌÑ ÐÒÏÓÍÏÔÒÁ PDF ÆÁÊÌÏ×
Summary(uk):	ðÒÏÇÒÁÍÁ ÄÌÑ ÐÅÒÅÇÌÑÄÕ PDF ÆÁÊÌ¦×
Name:		xpdf
Version:	3.01
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tar.gz
# Source0-md5:	e004c69c7dddef165d768b1362b44268
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}rc
Patch0:		%{name}-remove_protections.patch
Patch1:		%{name}-fontdirs.patch
# probably obsolete
Patch2:		%{name}-nonumericlocale.patch
Patch3:		%{name}-%{version}pl1.patch
URL:		http://www.foolabs.com/xpdf/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	t1lib-devel >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libXm.so.1 libXm.so.2
%define		specflags_ia32	 -fomit-frame-pointer 

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. PDF files are sometimes called Acrobat files, after Adobe
Acrobat (Adobe's PDF viewer). Xpdf is a small and efficient program
which uses standard X fonts.
%{!?with_protections:This version ignores protections for both: printing and copying.}

%description -l es
Xpdf es un visor de archivos PDF (Portable Document Format). (Estos
son algunas veces llamados de archivos 'Acrobat', nombre del software
PDF del Adobe. Xpdf fue proyectado para ser pequeño y eficiente. Usa
fuentes padrón X.

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
wydajnym programem. U¿ywa fontów z zasobów X Window.
%{!?with_protections:Ta wersja ignoruje blokady zarówno drukowania jak i kopiowania.}

%description -l pt_BR
Xpdf é um visualizador de arquivos PDF (Portable Document Format).
(Estes são algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padrão X.

%description -l ru
Xpdf - ÜÔÏ ÐÒÏÇÒÁÍÍÁ ÄÌÑ ÐÒÏÓÍÏÔÒÁ ÆÁÊÌÏ× × ÆÏÒÍÁÔÅ Portable Document
Format (PDF). ïÎÁ ÂÙÓÔÒÁÑ É ÜÆÆÅËÔÉ×ÎÁÑ É ÉÓÐÏÌØÚÕÅÔ ÓÔÁÎÄÁÒÔÎÙÅ
ÛÒÉÆÔÙ X Window.

%description -l uk
Xpdf - ÃÅ ÐÒÏÇÒÁÍÁ ÄÌÑ ÐÅÒÅÇÌÑÄÕ ÆÁÊÌ¦× × ÆÏÒÍÁÔ¦ Portable Document
Format (PDF). ÷ÏÎÁ Û×ÉÄËÁ Ê ÅÆÅËÔÉ×ÎÁ ÔÁ ×ÉËÏÒÉÓÔÏ×Õ¤ ÓÔÁÎÄÁÒÔÎ¦
ÛÒÉÆÔÉ X Window.

%package tools
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl):	Zestaw narzêdzi do wy¶wietlania informacji i konwertowania plików PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml-pdftops

%description tools
Set of utilities for displaying information about PDF-files (pdfinfo,
pdffonts, pdfimages) and converting them (pdftopbm, pdftops,
pdftotext).

%description tools -l pl
Zestaw programów do wy¶wietlania informacji o plikach PDF (pdfinfo,
pdffonts, pdfimages) i konwertowania ich do innych formatów (pdftopbm,
pdftops, pdftotext).

%prep
%setup -q
%{!?with_protections:%patch0 -p1}
%patch1 -p1
%patch3 -p1

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--enable-a4-paper \
	--enable-freetype2 \
	--enable-multithreaded \
	--enable-opi \
	--enable-wordlist \
	--with-freetype2-includes=/usr/include/freetype2 \
	--with-gzip

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/xpdf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README
%attr(755,root,root) %{_bindir}/xpdf
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/xpdf
%{_mandir}/man1/xpdf.1*
%{_mandir}/man5/xpdfrc.5*
%{_desktopdir}/*
%{_pixmapsdir}/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*
