Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System �Ǥ� PDF �ե�������塼��
Summary(pl):	Przegl�darka plik�w w formacie PDF
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
PDF del Adobe. Xpdf fue proyectado para ser peque�o y eficiente. Usa
fuentes padr�n X y no necesita de las bibliotecas Motif el Xt.

%description -l ja
xpdf �� Portable Document Format (PDF) �ե������ X Window System
��Ǥ� ���塼���Ǥ���PDF �ե������ Adobe Acrobat (Adobe �� PDF
���塼��) �ˤ��ʤ�ǡ� ���� Acrobat �ե�����ȸƤФ�ޤ���xpdf
�Ͼ�������ɸ��Ū�� X �Υե���Ȥ� �Ȥ�����Ū�ʥץ����Ǥ��� PDF
�ե�����Υ��塼����ɬ�פʤ�С�xpdf
�ѥå������򥤥󥹥ȡ��뤷�ޤ��礦��

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
