Summary:	Portable Document Format (PDF) file viewer
Summary(pl):	Przegl±darka plików w formacie PDF
Name:		xpdf
Version:	0.80
Release:	1
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Copyright:	freeware
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}-%{version}.tar.gz
Source1:	xpdf.wmconfig
Patch1:		xpdf-0.7a-patch1
Patch2:		xpdf-0.7a-type3.patch
URL:		http://www.foolabs.com/xpdf/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Xpdf is a viewer for Portable Document Format (PDF) files.  (These are also
sometimes also called 'Acrobat' files, from the name of Adobe's PDF
software.) Xpdf is designed to be small and efficient.  It does not use the
Motif or Xt libraries.  It uses standard X fonts.  Xpdf is quite usable on a
486-66 PC running Linux.

%description -l pl
Xpdf jest przegl±dark± plików zapisanych w formacie PDF (nazywanych równie¿
czasami plikami 'Acrobata', od nazwy programu firmy Adobe). Xpdf jest 
zaprojektowany tak, by byæ ma³ym i wydajnym. Nie u¿ywa bibliotek Motif czy Xt.
Wykorzystuje standardowe fonty ¶rodowiska X. By móc u¿ywaæ Xpdf wystarczy
komputer klasy PC 486-66 z Linuxem na pok³adzie.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{usr/X11R6/{bin,man/man1},etc/X11/wmconfig}

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xpdf

gzip -9nf ANNOUNCE CHANGES README \
	$RPM_BUILD_ROOT/usr/X11R6/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,CHANGES,README}.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*
%config(missingok) /etc/X11/wmconfig/xpdf

%changelog
* Thu Apr  1 1999 Piotr Czerwiñski <pius@pld.org.pl>
  
- changed BuildRoot to /tmp/%%{name}-%%{version}-root,
- added pl translation,
- added -q %setup parameter,
- simplifications in %install,
- added gzipping documentation,
- rewritten %files,
- added full %defattr description,
- moved %changelog at the end of spec,
- major changes.

* Sun Mar 15 1998 Joel Young <jyoung@erols.com>
- modified to use BuildRoot, %attr, to gzip the manpages, and moved
  into the X11R6 hierarchy (since it is an X app).
- released as new version with go-ahead from Michal Jaegermann

* Thu Mar 12 1998 Michal Jaegermann <michal@ellpspace.math.ualberta.ca>
- corrections to Type3 fonts handling code from the author
  (Derek B. Noonburg <derekn@aimnet.com>) remove a need for -mieee
  workaround

* Thu Mar  5 1998 Michal Jaegermann <michal@ellpspace.math.ualberta.ca>
- recompiled from a new release 0-7a including xpdf-0.7a-patch1 for
  Makefiles from the author.
- added -mieee to compilation flags to avoid Alpha floating point problems

* Wed Feb 18 1998 Michal Jaegermann <michal@ellpspace.math.ualberta.ca>
- fixed off-by-one error in Stream.cc; nasty stack kill on Alpha

* Thu Nov 20 1997 Otto Hammersmith <otto@redhat.com>
- added changelog
- added wmconfig
