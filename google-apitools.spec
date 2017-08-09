#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-apitools
Version  : 0.5.12
Release  : 4
URL      : https://pypi.python.org/packages/d9/a9/4914ccb93f8e236b7f773572cd3ade47d88c9b3e923ffbe3e794684a906f/google-apitools-0.5.12.tar.gz
Source0  : https://pypi.python.org/packages/d9/a9/4914ccb93f8e236b7f773572cd3ade47d88c9b3e923ffbe3e794684a906f/google-apitools-0.5.12.tar.gz
Summary  : client libraries for humans
Group    : Development/Tools
License  : Apache-2.0
Requires: google-apitools-bin
Requires: google-apitools-python
Requires: httplib2
Requires: oauth2client
Requires: python-mock
Requires: six
Requires: unittest2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
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

%description python
python components for the google-apitools package.


%prep
%setup -q -n google-apitools-0.5.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502288153
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1502288153
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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
/usr/lib/python2*/*
/usr/lib/python3*/*
