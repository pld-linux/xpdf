#
# Conditional build:
%bcond_without	protections	# remove protections against fair use (printing and copying)
#
Summary:	Portable Document Format (PDF) file viewer
Summary(es):	Visualizador de archivos PDF
Summary(ja):	X Window System �Ǥ� PDF �ե�������塼��
Summary(pl):	Przegl�darka plik�w w formacie PDF
Summary(pt_BR):	Visualizador de arquivos PDF
Summary(ru):	��������� ��� ��������� PDF ������
Summary(uk):	�������� ��� ��������� PDF ���̦�
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
PDF del Adobe. Xpdf fue proyectado para ser peque�o y eficiente. Usa
fuentes padr�n X.

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
wydajnym programem. U�ywa font�w z zasob�w X Window.
%{!?with_protections:Ta wersja ignoruje blokady zar�wno drukowania jak i kopiowania.}

%description -l pt_BR
Xpdf � um visualizador de arquivos PDF (Portable Document Format).
(Estes s�o algumas vezes chamados de arquivos 'Acrobat', nome do
software PDF da Adobe. Xpdf foi projetado para ser pequeno e
eficiente. Ele usa fontes padr�o X.

%description -l ru
Xpdf - ��� ��������� ��� ��������� ������ � ������� Portable Document
Format (PDF). ��� ������� � ����������� � ���������� �����������
������ X Window.

%description -l uk
Xpdf - �� �������� ��� ��������� ���̦� � �����Ԧ Portable Document
Format (PDF). ���� ������ � ��������� �� ����������դ ��������Φ
������ X Window.

%package tools
Summary:	Set of tools for viewing information and converting PDF files
Summary(pl):	Zestaw narz�dzi do wy�wietlania informacji i konwertowania plik�w PDF
Group:		Applications/Publishing
Provides:	pdftops
Obsoletes:	pdftohtml-pdftops

%description tools
Set of utilities for displaying information about PDF-files (pdfinfo,
pdffonts, pdfimages) and converting them (pdftopbm, pdftops,
pdftotext).

%description tools -l pl
Zestaw program�w do wy�wietlania informacji o plikach PDF (pdfinfo,
pdffonts, pdfimages) i konwertowania ich do innych format�w (pdftopbm,
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
