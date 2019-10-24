#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-scales
Version  : 1.0.0
Release  : 73
URL      : https://cran.r-project.org/src/contrib/scales_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/scales_1.0.0.tar.gz
Summary  : Tools for Splitting, Applying and Combining Data
Group    : Development/Tools
License  : MIT
Requires: R-scales-lib = %{version}-%{release}
Requires: R-R6
Requires: R-RColorBrewer
Requires: R-Rcpp
Requires: R-labeling
Requires: R-munsell
Requires: R-viridisLite
BuildRequires : R-R6
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : R-dichromat
BuildRequires : R-labeling
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : R-viridisLite
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# Scales <img src="man/figures/logo.png" align="right" />
[![Build
Status](https://travis-ci.org/r-lib/scales.svg?branch=master)](https://travis-ci.org/r-lib/scales)
[![Coverage
Status](https://img.shields.io/codecov/c/github/r-lib/scales/master.svg)](https://codecov.io/github/r-lib/scales?branch=master)
[![CRAN\_Status\_Badge](http://www.r-pkg.org/badges/version/scales)](https://cran.r-project.org/package=scales)

%package lib
Summary: lib components for the R-scales package.
Group: Libraries

%description lib
lib components for the R-scales package.


%prep
%setup -q -c -n scales

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571906601

%install
export SOURCE_DATE_EPOCH=1571906601
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scales
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scales
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scales
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc scales || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/scales/DESCRIPTION
/usr/lib64/R/library/scales/INDEX
/usr/lib64/R/library/scales/LICENSE
/usr/lib64/R/library/scales/Meta/Rd.rds
/usr/lib64/R/library/scales/Meta/features.rds
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
/usr/lib64/R/library/scales/help/figures/README-palettes-1.png
/usr/lib64/R/library/scales/help/figures/README-squish-1.png
/usr/lib64/R/library/scales/help/figures/README-transforms-1.png
/usr/lib64/R/library/scales/help/figures/logo.png
/usr/lib64/R/library/scales/help/paths.rds
/usr/lib64/R/library/scales/help/scales.rdb
/usr/lib64/R/library/scales/help/scales.rdx
/usr/lib64/R/library/scales/html/00Index.html
/usr/lib64/R/library/scales/html/R.css
/usr/lib64/R/library/scales/tests/testthat.R
/usr/lib64/R/library/scales/tests/testthat/test-alpha.r
/usr/lib64/R/library/scales/tests/testthat/test-bounds.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks-extended.R
/usr/lib64/R/library/scales/tests/testthat/test-breaks-log.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks-minor.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks.r
/usr/lib64/R/library/scales/tests/testthat/test-colors.r
/usr/lib64/R/library/scales/tests/testthat/test-colour-ramp.R
/usr/lib64/R/library/scales/tests/testthat/test-discrete.R
/usr/lib64/R/library/scales/tests/testthat/test-formatter.r
/usr/lib64/R/library/scales/tests/testthat/test-manual-pal.R
/usr/lib64/R/library/scales/tests/testthat/test-pal-hue.r
/usr/lib64/R/library/scales/tests/testthat/test-range.r
/usr/lib64/R/library/scales/tests/testthat/test-rescale.R
/usr/lib64/R/library/scales/tests/testthat/test-round-any.R
/usr/lib64/R/library/scales/tests/testthat/test-scale.r
/usr/lib64/R/library/scales/tests/testthat/test-trans-date.r
/usr/lib64/R/library/scales/tests/testthat/test-trans-numeric.r
/usr/lib64/R/library/scales/tests/testthat/test-trans.r
/usr/lib64/R/library/scales/tests/testthat/test-zero-range.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/scales/libs/scales.so
/usr/lib64/R/library/scales/libs/scales.so.avx2
