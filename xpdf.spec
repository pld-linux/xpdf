# Conditional build:
%bcond_with	protections	# protections against fair use (printing and copying)
%bcond_without	x		# X-based browser

Summary:	Portable Document Format (PDF) file viewer
Summary(es.UTF-8):	Visualizador de archivos PDF
Summary(ja.UTF-8):	X Window System での PDF ファイルヴューア
Summary(pl.UTF-8):	Przeglądarka plików w formacie PDF
Summary(pt_BR.UTF-8):	Visualizador de arquivos PDF
Summary(ru.UTF-8):	Программа для просмотра PDF файлов
Summary(uk.UTF-8):	Програма для перегляду PDF файлів
Name:		xpdf
Version:	4.01
Release:	1
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://www.xpdfreader.com/dl/%{name}-%{version}.tar.gz
# Source0-md5:	80c8ce77acf1d36de93cecb82bd64a0f
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}rc
Patch0:		%{name}-remove_protections.patch
Patch1:		%{name}-fontdirs.patch
Patch2:		dynamic_private.patch
URL:		http://www.xpdfreader.com/
BuildRequires:	cmake >= 2.8.8
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libpaper-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?with_x:BuildRequires:	QtCore-devel}
%{?with_x:BuildRequires:	QtGui-devel}
%{?with_x:BuildRequires:	qt4-qmake}
BuildRequires:	rpmbuild(macros) >= 1.596
Requires:	desktop-file-utils
Suggests:	ghostscript-fonts-std
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package common
Summary:	Common xpdf files
Summary(pl.UTF-8):	Wspólne pliki xpdf
Group:		Applications/Publishing

%description common
Private libraries used by xpdf GUI and CLI tools and xpdfrc file.

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
%setup -q -n %{name}-4.00
%{!?with_protections:%patch0 -p1}
%patch1 -p1
%patch2 -p1
sed -e 's|DESTINATION man/|DESTINATION share/man/|g' -i xpdf{,-qt}/CMakeLists.txt

%build
%cmake . \
	-DA4_PAPER=ON \
	-DSPLASH_CMYK=ON \
	-DOPI_SUPPORT=ON \
	-DSYSTEM_XPDFRC="%{_sysconfdir}/%{name}rc" \
	-DCMAKE_DISABLE_FIND_PACKAGE_Qt5Widgets=1 \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}" \
	-DCMAKE_INSTALL_RPATH="%{_libexecdir}/%{name}" \
	-DCMAKE_EXE_LINKER_FLAGS="-lpaper %{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_desktopdir},%{_pixmapsdir},{%{_datadir},%{_libexecdir}}/%{name}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install {fofi/libfofi,goo/libgoo,splash/libsplash}.so $RPM_BUILD_ROOT%{_libexecdir}/%{name}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%if %{with x}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xpdf
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/xpdf.1*
%endif

%files common
%doc ANNOUNCE CHANGES README
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/%{name}rc
%dir %{_libexecdir}/%{name}
%attr(755,root,root) %{_libexecdir}/%{name}/lib*.so
%{_datadir}/xpdf
%{_mandir}/man5/xpdfrc.5*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfdetach
%attr(755,root,root) %{_bindir}/pdffonts
%attr(755,root,root) %{_bindir}/pdfimages
%attr(755,root,root) %{_bindir}/pdfinfo
%attr(755,root,root) %{_bindir}/pdftohtml
%attr(755,root,root) %{_bindir}/pdftopng
%attr(755,root,root) %{_bindir}/pdftoppm
%attr(755,root,root) %{_bindir}/pdftops
%attr(755,root,root) %{_bindir}/pdftotext
%{_mandir}/man1/pdfdetach.1*
%{_mandir}/man1/pdffonts.1*
%{_mandir}/man1/pdfimages.1*
%{_mandir}/man1/pdfinfo.1*
%{_mandir}/man1/pdftohtml.1*
%{_mandir}/man1/pdftopng.1*
%{_mandir}/man1/pdftoppm.1*
%{_mandir}/man1/pdftops.1*
%{_mandir}/man1/pdftotext.1*
