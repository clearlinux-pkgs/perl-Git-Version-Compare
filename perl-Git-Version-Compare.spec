#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Git-Version-Compare
Version  : 1.005
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/B/BO/BOOK/Git-Version-Compare-1.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BO/BOOK/Git-Version-Compare-1.005.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgit-version-compare-perl/libgit-version-compare-perl_1.004-1.debian.tar.xz
Summary  : 'Functions to compare Git versions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Git-Version-Compare-license = %{version}-%{release}
Requires: perl-Git-Version-Compare-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::NoWarnings)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Git::Version::Compare - Functions to compare Git versions
SYNOPSIS
use Git::Version::Compare qw( cmp_git );

%package dev
Summary: dev components for the perl-Git-Version-Compare package.
Group: Development
Provides: perl-Git-Version-Compare-devel = %{version}-%{release}
Requires: perl-Git-Version-Compare = %{version}-%{release}

%description dev
dev components for the perl-Git-Version-Compare package.


%package license
Summary: license components for the perl-Git-Version-Compare package.
Group: Default

%description license
license components for the perl-Git-Version-Compare package.


%package perl
Summary: perl components for the perl-Git-Version-Compare package.
Group: Default
Requires: perl-Git-Version-Compare = %{version}-%{release}

%description perl
perl components for the perl-Git-Version-Compare package.


%prep
%setup -q -n Git-Version-Compare-1.005
cd %{_builddir}
tar xf %{_sourcedir}/libgit-version-compare-perl_1.004-1.debian.tar.xz
cd %{_builddir}/Git-Version-Compare-1.005
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Git-Version-Compare-1.005/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Git-Version-Compare
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Git-Version-Compare/3d9b88fe8680fe3a0c6ab15e5770128d7881393e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Git::Version::Compare.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Git-Version-Compare/3d9b88fe8680fe3a0c6ab15e5770128d7881393e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
