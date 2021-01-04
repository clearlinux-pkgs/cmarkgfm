#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmarkgfm
Version  : 0.5.2
Release  : 10
URL      : https://files.pythonhosted.org/packages/21/5d/86d7959a7c9eaf70653d0e72cf7e00e604aa2b3bdbbfcfec365ab0002deb/cmarkgfm-0.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/5d/86d7959a7c9eaf70653d0e72cf7e00e604aa2b3bdbbfcfec365ab0002deb/cmarkgfm-0.5.2.tar.gz
Summary  : Minimal bindings to GitHub's fork of cmark
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: cmarkgfm-license = %{version}-%{release}
Requires: cmarkgfm-python = %{version}-%{release}
Requires: cmarkgfm-python3 = %{version}-%{release}
Requires: cffi
BuildRequires : buildreq-distutils3
BuildRequires : cffi

%description
============================================
        
        Minimalist Python bindings to GitHub's fork of cmark.
        
        Installation
        ------------

%package license
Summary: license components for the cmarkgfm package.
Group: Default

%description license
license components for the cmarkgfm package.


%package python
Summary: python components for the cmarkgfm package.
Group: Default
Requires: cmarkgfm-python3 = %{version}-%{release}

%description python
python components for the cmarkgfm package.


%package python3
Summary: python3 components for the cmarkgfm package.
Group: Default
Requires: python3-core
Provides: pypi(cmarkgfm)
Requires: pypi(cffi)

%description python3
python3 components for the cmarkgfm package.


%prep
%setup -q -n cmarkgfm-0.5.2
cd %{_builddir}/cmarkgfm-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609774539
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cmarkgfm
cp %{_builddir}/cmarkgfm-0.5.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/cmarkgfm/592ea524450874d50778dd5db4a8dd176a0261e2
cp %{_builddir}/cmarkgfm-0.5.2/third_party/cmark/COPYING %{buildroot}/usr/share/package-licenses/cmarkgfm/fa524e3e5b56232fdada455ba84c938f5a1487d2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cmarkgfm/592ea524450874d50778dd5db4a8dd176a0261e2
/usr/share/package-licenses/cmarkgfm/fa524e3e5b56232fdada455ba84c938f5a1487d2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
