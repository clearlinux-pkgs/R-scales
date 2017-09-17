#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-scales
Version  : 0.5.0
Release  : 41
URL      : https://cran.r-project.org/src/contrib/scales_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/scales_0.5.0.tar.gz
Summary  : Scale Functions for Visualization
Group    : Development/Tools
License  : MIT
Requires: R-scales-lib
Requires: R-RColorBrewer
Requires: R-Rcpp
Requires: R-dichromat
Requires: R-labeling
Requires: R-munsell
Requires: R-plyr
Requires: R-viridisLite
BuildRequires : R-RColorBrewer
BuildRequires : R-Rcpp
BuildRequires : R-dichromat
BuildRequires : R-labeling
BuildRequires : R-munsell
BuildRequires : R-plyr
BuildRequires : R-viridisLite
BuildRequires : clr-R-helpers

%description
methods for automatically determining breaks and labels
    for axes and legends.

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
export LANG=C
export SOURCE_DATE_EPOCH=1505674954

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1505674954
export LANG=C
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
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scales
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library scales|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/scales/help/paths.rds
/usr/lib64/R/library/scales/help/scales.rdb
/usr/lib64/R/library/scales/help/scales.rdx
/usr/lib64/R/library/scales/html/00Index.html
/usr/lib64/R/library/scales/html/R.css
/usr/lib64/R/library/scales/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/scales/libs/scales.so
/usr/lib64/R/library/scales/libs/scales.so.avx2
