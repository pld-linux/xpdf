#
# TODO:
#	- separate subpackage with /etc/xpdfrc file; pdftotext
#	  from xpdf-tools or poppler-progs can use language
#	  support files but don't require entire xpdf
#
# Conditional build:
%bcond_without	protections	# remove protections against fair use (printing and copying)
%bcond_without	x		# X-based browser
#
Summary:	Portable Document Format (PDF) file viewer
Summary(es.UTF-8):	Visualizador de archivos PDF
Summary(ja.UTF-8):	X Window System での PDF ファイルヴューア
Summary(pl.UTF-8):	Przeglądarka plików w formacie PDF
Summary(pt_BR.UTF-8):	Visualizador de arquivos PDF
Summary(ru.UTF-8):	Программа для просмотра PDF файлов
Summary(uk.UTF-8):	Програма для перегляду PDF файлів
Name:		xpdf
Version:	3.02
Release:	7
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tar.gz
# Source0-md5:	599dc4cc65a07ee868cf92a667a913d2
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}rc
Patch0:		%{name}-remove_protections.patch
Patch1:		%{name}-fontdirs.patch
Patch2:		%{name}-%{version}pl1.patch
Patch3:		%{name}-%{version}pl2.patch
Patch4:		%{name}-%{version}pl3.patch
Patch5:		%{name}-%{version}pl4.patch
URL:		http://www.foolabs.com/xpdf/
%{?with_x:BuildRequires:	xorg-lib-libX11-devel}
BuildRequires:	autoconf
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libpaper-devel
BuildRequires:	libstdc++-devel
%{?with_x:BuildRequires:	motif-devel}
BuildRequires:	t1lib-devel >= 1.3.0
Suggests:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libXm.so.1 libXm.so.2
%define		specflags_ia32	 -fomit-frame-pointer 

%description
Xpdf is an X Window System based viewer for Portable Document Format
(PDF) files. PDF files are sometimes called Acrobat files, after Adobe
Acrobat (Adobe's PDF viewer). Xpdf is a small and efficient program
which uses standard X fonts.
%{!?with_protections:This version ignores protections for both: printing and copying.}

%description -l es.UTF-8
Xpdf es un visor de archivos PDF (Portable Document Format). (Estos
son algunas veces llamados de archivos 'Acrobat', nombre del software
PDF del Adobe. Xpdf fue proyectado para ser pequeño y eficiente. Usa
fuentes padrón X.

%description -l ja.UTF-8
xpdf は Portable Document Format (PDF) ファイルの X Window System
上での ヴューアです。PDF ファイルは Adobe Acrobat (Adobe の PDF
ヴューア) にちなんで、 時々 Acrobat ファイルと呼ばれます。xpdf
は小さく、標準的な X のフォントを 使う効果的なプログラムです。 PDF
ファイルのヴューアが必要ならば、xpdf
パッケージをインストールしましょう。

%description -l pl.UTF-8
Xpdf jest przeglądarką plików zapisanych w formacie PDF (Portable
Document Format). Xpdf jest zaprojektowany tak, by być małym i
wydajnym programem. Używa fontów z zasobów X Window.
%{!?with_protections:Ta wersja ignoruje blokady zarówno drukowania jak i kopiowania.}

%description -l pt_BR.UTF-8
Xpdf é um visualizador de arquivos PDF (Portable Document Format).
(Estes são algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padrão X.

%description -l ru.UTF-8
Xpdf - это программа для просмотра файлов в формате Portable Document
Format (PDF). Она быстрая и эффективная и использует стандартные
шрифты X Window.

%description -l uk.UTF-8
Xpdf - це програма для перегляду файлів в форматі Portable Document
Format (PDF). Вона швидка й ефективна та використовує стандартні
шрифти X Window.

%package tools
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl.UTF-8):	Zestaw narzędzi do wyświetlania informacji i konwertowania plików PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml-pdftops

%description tools
Set of utilities for displaying information about PDF-files (pdfinfo,
pdffonts, pdfimages) and converting them (pdftopbm, pdftops,
pdftotext).

%description tools -l pl.UTF-8
Zestaw programów do wyświetlania informacji o plikach PDF (pdfinfo,
pdffonts, pdfimages) i konwertowania ich do innych formatów (pdftopbm,
pdftops, pdftotext).

%prep
%setup -q
%{!?with_protections:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__autoconf}
%{!?with_x:export no_x=yes}
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

%if %{with x}
%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES README
%attr(755,root,root) %{_bindir}/xpdf
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_datadir}/xpdf
%{_mandir}/man1/xpdf.1*
%{_mandir}/man5/xpdfrc.5*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdf*
%{_mandir}/man1/pdf*
