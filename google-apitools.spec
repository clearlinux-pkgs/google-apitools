#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-apitools
Version  : 0.5.30
Release  : 39
URL      : https://files.pythonhosted.org/packages/2f/b9/76bd1fdac6bdf60eec829f8e2aa61ed029f82bdec312eedae5b4139ec56b/google-apitools-0.5.30.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/b9/76bd1fdac6bdf60eec829f8e2aa61ed029f82bdec312eedae5b4139ec56b/google-apitools-0.5.30.tar.gz
Summary  : client libraries for humans
Group    : Development/Tools
License  : Apache-2.0
Requires: google-apitools-bin = %{version}-%{release}
Requires: google-apitools-python = %{version}-%{release}
Requires: google-apitools-python3 = %{version}-%{release}
Requires: fasteners
Requires: httplib2
Requires: oauth2client
Requires: python-gflags
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : fasteners
BuildRequires : httplib2
BuildRequires : oauth2client
BuildRequires : python-gflags
BuildRequires : six

%description
google-apitools
===============
|pypi| |build| |coverage|
``google-apitools`` is a collection of utilities to make it easier to build
client-side tools, especially those that talk to Google APIs.

%package bin
Summary: bin components for the google-apitools package.
Group: Binaries

%description bin
bin components for the google-apitools package.


%package python
Summary: python components for the google-apitools package.
Group: Default
Requires: google-apitools-python3 = %{version}-%{release}

%description python
python components for the google-apitools package.


%package python3
Summary: python3 components for the google-apitools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the google-apitools package.


%prep
%setup -q -n google-apitools-0.5.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561601809
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gen_client

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
