#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-scales
Version  : 1.1.0
Release  : 76
URL      : https://cran.r-project.org/src/contrib/scales_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/scales_1.1.0.tar.gz
Summary  : Scale Functions for Visualization
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-RColorBrewer
Requires: R-farver
Requires: R-labeling
Requires: R-lifecycle
Requires: R-munsell
Requires: R-plyr
Requires: R-viridisLite
BuildRequires : R-R6
BuildRequires : R-RColorBrewer
BuildRequires : R-farver
BuildRequires : R-labeling
BuildRequires : R-lifecycle
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : R-viridisLite
BuildRequires : buildreq-R

%description
provide methods for automatically determining breaks and labels for
    axes and legends.

%prep
%setup -q -c -n scales

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574319434

%install
export SOURCE_DATE_EPOCH=1574319434
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
/usr/lib64/R/library/scales/help/figures/README-labels-1.png
/usr/lib64/R/library/scales/help/figures/README-labels-2.png
/usr/lib64/R/library/scales/help/figures/README-palettes-1.png
/usr/lib64/R/library/scales/help/figures/README-transforms-1.png
/usr/lib64/R/library/scales/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/scales/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/scales/help/figures/logo.png
/usr/lib64/R/library/scales/help/paths.rds
/usr/lib64/R/library/scales/help/scales.rdb
/usr/lib64/R/library/scales/help/scales.rdx
/usr/lib64/R/library/scales/html/00Index.html
/usr/lib64/R/library/scales/html/R.css
/usr/lib64/R/library/scales/tests/testthat.R
/usr/lib64/R/library/scales/tests/testthat/test-bounds.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks-extended.R
/usr/lib64/R/library/scales/tests/testthat/test-breaks-log.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks-minor.r
/usr/lib64/R/library/scales/tests/testthat/test-breaks.r
/usr/lib64/R/library/scales/tests/testthat/test-colour-manip.r
/usr/lib64/R/library/scales/tests/testthat/test-colour-mapping.r
/usr/lib64/R/library/scales/tests/testthat/test-colour-ramp.R
/usr/lib64/R/library/scales/tests/testthat/test-discrete.R
/usr/lib64/R/library/scales/tests/testthat/test-label-bytes.R
/usr/lib64/R/library/scales/tests/testthat/test-label-date-short.txt
/usr/lib64/R/library/scales/tests/testthat/test-label-date.R
/usr/lib64/R/library/scales/tests/testthat/test-label-dollar.R
/usr/lib64/R/library/scales/tests/testthat/test-label-expression.R
/usr/lib64/R/library/scales/tests/testthat/test-label-number-auto.R
/usr/lib64/R/library/scales/tests/testthat/test-label-number-auto.txt
/usr/lib64/R/library/scales/tests/testthat/test-label-number-si.R
/usr/lib64/R/library/scales/tests/testthat/test-label-number.r
/usr/lib64/R/library/scales/tests/testthat/test-label-ordinal.R
/usr/lib64/R/library/scales/tests/testthat/test-label-percent.R
/usr/lib64/R/library/scales/tests/testthat/test-label-pvalue.R
/usr/lib64/R/library/scales/tests/testthat/test-label-scientific.R
/usr/lib64/R/library/scales/tests/testthat/test-label-wrap.R
/usr/lib64/R/library/scales/tests/testthat/test-labels-retired.R
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
