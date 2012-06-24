Summary:	Portable Document Format (PDF) file viewer
Summary(ja):	X Window System �Ǥ� PDF �ե�������塼��
Summary(pl):	Przegl�darka plik�w w formacie PDF
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
