Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System での PDF ファイルヴューア
Summary(pl):	Przegl�darka plik�w w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Summary(ru):	靤惑卅様� 通� 侑腕溶墟� PDF 徳別��
Summary(uk):	靤惑卅輿 通� 佚凖婆冂� PDF 徳別ψ
Name:		xpdf
Version:	1.01
Release:	2
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
PDF del Adobe. Xpdf fue proyectado para ser peque�o y eficiente. Usa
fuentes padr�n X y no necesita de las bibliotecas Motif el Xt.

%description -l ja
xpdf は Portable Document Format (PDF) ファイルの X Window System
上での ヴューアです。PDF ファイルは Adobe Acrobat (Adobe の PDF
ヴューア) にちなんで、 時々 Acrobat ファイルと呼ばれます。xpdf
は小さく、標準的な X のフォントを 使う効果的なプログラムです。 PDF
ファイルのヴューアが必要ならば、xpdf
パッケージをインストールしましょう。

%description -l pl
Xpdf jest przegl�dark� plik�w zapisanych w formacie PDF (Portable
Document Format). Xpdf jest zaprojektowany tak, by by� ma�ym i
wydajnym programem. Nie u�ywa bibliotek Motif czy Xt u�ywaj�cym font�w
z zasob�w X Window.

%description -l pt_BR
Xpdf � um visualizador de arquivos PDF (Portable Document Format).
(Estes s�o algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padr�o X e n�o precisa das bibliotecas Motif
ou Xt.

%description -l ru
Xpdf - 榑� 侑惑卅様� 通� 侑腕溶墟� 徳別�� � 届厖壮� Portable Document
Format (PDF). 鑪� 泰嘖卅� � 榮禿穆夫料� � 瓶佻蒙旁都 嘖僧珍參隣�
柢鋲壅 X Window.

%description -l uk
Xpdf - 壇 侑惑卅輿 通� 佚凖婆冂� 徳別ψ � 届厖壮� Portable Document
Format (PDF). �藁� 柧苗冒 � 兎屠塢徇� 堊 徂墨夘嘖�徼� 嘖僧珍參陸
柢鋲塢 X Window.

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
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_applnkdir}/Graphics/Viewers/*
%{_pixmapsdir}/*
