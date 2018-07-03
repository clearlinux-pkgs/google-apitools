#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-apitools
Version  : 0.5.23
Release  : 26
URL      : https://pypi.debian.net/google-apitools/google-apitools-0.5.23.tar.gz
Source0  : https://pypi.debian.net/google-apitools/google-apitools-0.5.23.tar.gz
Summary  : client libraries for humans
Group    : Development/Tools
License  : Apache-2.0
Requires: google-apitools-bin
Requires: google-apitools-python3
Requires: google-apitools-python
Requires: fasteners
Requires: httplib2
Requires: oauth2client
Requires: python-gflags
Requires: six
BuildRequires : fasteners
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
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
Requires: google-apitools-python3

%description python
python components for the google-apitools package.


%package python3
Summary: python3 components for the google-apitools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the google-apitools package.


%prep
%setup -q -n google-apitools-0.5.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528564358
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
