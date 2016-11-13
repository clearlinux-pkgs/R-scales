#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-scales
Version  : 0.4.1
Release  : 32
URL      : http://cran.r-project.org/src/contrib/scales_0.4.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/scales_0.4.1.tar.gz
Summary  : Scale Functions for Visualization
Group    : Development/Tools
License  : MIT
Requires: R-scales-lib
Requires: R-Rcpp
Requires: R-RColorBrewer
Requires: R-labeling
Requires: R-munsell
Requires: R-dichromat
Requires: R-plyr
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : R-dichromat
BuildRequires : R-labeling
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : clr-R-helpers

%description
# Scales
[![Build Status](https://travis-ci.org/hadley/scales.png?branch=master)](https://travis-ci.org/hadley/scales)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/scales/master.svg)](https://codecov.io/github/hadley/scales?branch=master)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/scales)](https://cran.r-project.org/package=scales)

%package lib
Summary: lib components for the R-scales package.
Group: Libraries

%description lib
lib components for the R-scales package.


%prep
%setup -q -c -n scales

%build
export LANG=C

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library scales
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library scales


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/scales/DESCRIPTION
/usr/lib64/R/library/scales/INDEX
/usr/lib64/R/library/scales/LICENSE
/usr/lib64/R/library/scales/Meta/Rd.rds
/usr/lib64/R/library/scales/Meta/hsearch.rds
/usr/lib64/R/library/scales/Meta/links.rds
/usr/lib64/R/library/scales/Meta/nsInfo.rds
/usr/lib64/R/library/scales/Meta/package.rds
/usr/lib64/R/library/scales/NAMESPACE
/usr/lib64/R/library/scales/NEWS.md
/usr/lib64/R/library/scales/R/scales
/usr/lib64/R/library/scales/R/scales.rdb
/usr/lib64/R/library/scales/R/scales.rdx
/usr/lib64/R/library/scales/help/AnIndex
/usr/lib64/R/library/scales/help/aliases.rds
/usr/lib64/R/library/scales/help/paths.rds
/usr/lib64/R/library/scales/help/scales.rdb
/usr/lib64/R/library/scales/help/scales.rdx
/usr/lib64/R/library/scales/html/00Index.html
/usr/lib64/R/library/scales/html/R.css
/usr/lib64/R/library/scales/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/scales/libs/scales.so
