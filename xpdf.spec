Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System ╓г╓н PDF ╔у╔║╔╓╔К╔Т╔Е║╪╔╒
Summary(pl):	Przegl╠darka plikСw w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Summary(ru):	Программа для просмотра PDF файлов
Summary(uk):	Програма для перегляду PDF файл╕в
Name:		xpdf
Version:	1.01
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
PDF del Adobe. Xpdf fue proyectado para ser pequeЯo y eficiente. Usa
fuentes padrСn X y no necesita de las bibliotecas Motif el Xt.

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
wydajnym programem. Nie u©ywa bibliotek Motif czy Xt u©ywaj╠cym fontСw
z zasobСw X Window.

%description -l pt_BR
Xpdf И um visualizador de arquivos PDF (Portable Document Format).
(Estes sЦo algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padrЦo X e nЦo precisa das bibliotecas Motif
ou Xt.

%description -l ru
Xpdf - это программа для просмотра файлов в формате Portable Document
Format (PDF). Она быстрая и эффективная и использует стандартные
шрифты X Window.

%description -l uk
Xpdf - це програма для перегляду файл╕в в формат╕ Portable Document
Format (PDF). Вона швидка й ефективна та використову╓ стандартн╕
шрифти X Window.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
%configure \
	--with-gzip \
	--enable-a4-paper \
	--enable-opi \
	--enable-freetype2 \
	--with-freetype2-includes=/usr/include/freetype2 \
	--with-freetype-includes=/usr/include/freetype

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics/Viewers,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers/xpdf.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*
