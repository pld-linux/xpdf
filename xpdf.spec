#
# Conditional build:
# _without_protections	- remove protections against fair use (printing and copying)
#
Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System ╓г╓н PDF ╔у╔║╔╓╔К╔Т╔Е║╪╔╒
Summary(pl):	Przegl╠darka plikСw w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Summary(ru):	Программа для просмотра PDF файлов
Summary(uk):	Програма для перегляду PDF файл╕в
Name:		xpdf
Version:	2.02
Release:	1
License:	GPL
Group:		X11/Applications
#Source0-md5:	fb54402d98fb834e5778163cfc238b44
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}rc
Patch0:		%{name}-remove_protections.patch
Patch1:		%{name}-nonumericlocale.patch
URL:		http://www.foolabs.com/xpdf/
Icon:		xpdfIcon.gif
BuildRequires:	XFree86-devel
BuildRequires:	freetype-devel >= 2.0.6
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	t1lib-devel >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libXm.so.1 libXm.so.2

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. PDF files are sometimes called Acrobat files, after Adobe
Acrobat (Adobe's PDF viewer). Xpdf is a small and efficient program
which uses standard X fonts.
%{?_without_protections:This version ignores protections for both: printing and copying.}

%description -l es
Xpdf es un visor de archivos PDF (Portable Document Format). (Estos
son algunas veces llamados de archivos 'Acrobat', nombre del software
PDF del Adobe. Xpdf fue proyectado para ser pequeЯo y eficiente. Usa
fuentes padrСn X.

%description -l ja
xpdf ╓о Portable Document Format (PDF) ╔у╔║╔╓╔К╓н X Window System
╬Е╓г╓н ╔Т╔Е║╪╔╒╓г╓╧║ёPDF ╔у╔║╔╓╔К╓о Adobe Acrobat (Adobe ╓н PDF
╔Т╔Е║╪╔╒) ╓к╓а╓й╓С╓г║╒ ╩Ч║╧ Acrobat ╔у╔║╔╓╔К╓х╦ф╓п╓Л╓ч╓╧║ёxpdf
╓о╬╝╓╣╓╞║╒и╦╫Юе╙╓й X ╓н╔у╔╘╔С╔х╓Р ╩х╓╕╦З╡ле╙╓й╔в╔М╔╟╔И╔Ю╓г╓╧║ё PDF
╔у╔║╔╓╔К╓н╔Т╔Е║╪╔╒╓╛и╛мв╓й╓И╓п║╒xpdf
╔я╔ц╔╠║╪╔╦╓Р╔╓╔С╔╧╔х║╪╔К╓╥╓ч╓╥╓Г╓╕║ё

%description -l pl
Xpdf jest przegl╠dark╠ plikСw zapisanych w formacie PDF (Portable
Document Format). Xpdf jest zaprojektowany tak, by byФ maЁym i
wydajnym programem. U©ywa fontСw z zasobСw X Window.
%{?_without_protections:Ta wersja ignoruje blokady zarСwno drukowania jak i kopiowania.}

%description -l pt_BR
Xpdf И um visualizador de arquivos PDF (Portable Document Format).
(Estes sЦo algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padrЦo X.

%description -l ru
Xpdf - это программа для просмотра файлов в формате Portable Document
Format (PDF). Она быстрая и эффективная и использует стандартные
шрифты X Window.

%description -l uk
Xpdf - це програма для перегляду файл╕в в формат╕ Portable Document
Format (PDF). Вона швидка й ефективна та використову╓ стандартн╕
шрифти X Window.

%package tools
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl):	Zestaw narzЙdzi do wy╤wietlania informacji i konwertowania plikСw PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml-pdftops

%description tools
Set of utilities for displaying information about PDF-files (pdfinfo,
pdffonts, pdfimages) and converting them (pdftopbm, pdftops,
pdftotext).

%description tools -l pl
Zestaw programСw do wy╤wietlania informacji o plikach PDF (pdfinfo,
pdffonts, pdfimages) i konwertowania ich do innych formatСw (pdftopbm,
pdftops, pdftotext).

%prep
%setup -q
%{?_without_protections:%patch0 -p1}
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--with-gzip \
	--enable-a4-paper \
	--enable-opi \
	--enable-freetype2 \
	--with-freetype2-includes=/usr/include/freetype2 \
	--with-freetype-includes=/usr/include/freetype \
	--with-Xm-includes=/usr/X11R6/include

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/xpdf

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README
%attr(755,root,root) %{_bindir}/xpdf
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/*
%{_datadir}/xpdf
%{_mandir}/man1/xpdf.1*
%{_mandir}/man5/xpdfrc.5*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*
