Name:         xpdf
Version:      0.7a
Release:      6
Summary:      Portable Document Format (PDF) file viewer
Group:        X11/Applications
Copyright:    freeware
Vendor:       Derek B. Noonburg <derekn@aimnet.com>
Packager:     Red Hat Contrib-Net <rhcn-bugs@redhat.com>
Distribution: Red Hat Contrib-Net
URL:          http://www.aimnet.com/~derekn/xpdf/
Source:       ftp://ftp.aimnet.com/pub/users/derekn/xpdf/xpdf-0.7a.tar.gz
Source2:      xpdf.wmconfig
Patch1:       xpdf-0.7a-patch1
Patch2:       xpdf-0.7a-type3.patch
BuildRoot:    /var/tmp/xpdf

%description
Xpdf is a viewer for Portable Document Format (PDF) files.  (These are also
sometimes also called 'Acrobat' files, from the name of Adobe's PDF
software.) Xpdf is designed to be small and efficient.  It does not use the
Motif or Xt libraries.  It uses standard X fonts.  Xpdf is quite usable on a
486-66 PC running Linux.

%changelog

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

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
env CFLAGS="$RPM_OPT_FLAGS" \
    CXXFLAGS="$RPM_OPT_FLAGS" \
    ./configure --prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/man/man1
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

gzip $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

install $RPM_SOURCE_DIR/xpdf.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/xpdf

%files
%attr(0644,root,root) %doc ANNOUNCE
%attr(0644,root,root) %doc CHANGES
%attr(0644,root,root) %doc README
%attr(0755,root,root) /usr/X11R6/bin/*
%attr(0644,root,root) /usr/X11R6/man/man1/*
%attr(0644,root,root) /etc/X11/wmconfig/xpdf

%clean
rm -rf $RPM_BUILD_ROOT
