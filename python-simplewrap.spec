%global modname simplewrap

Name:           python-%{modname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        Easy to use wrappers generator for C libraries based on ctypes

# https://github.com/spedemon/simplewrap/pull/2
# not license text in PyPi archive
License:        BSD
URL:            https://pypi.python.org/pypi/simplewrap
Source0:        https://pypi.python.org/packages/source/s/simplewrap/%{modname}-%{version}.tar.gz

BuildRequires:  gcc

%description
%{summary}.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy
Requires:       python2-numpy
%else
BuildRequires:  numpy
Requires:       numpy
%endif

%description -n python2-%{modname}
%{summary}.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  /usr/bin/2to3
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-numpy
Requires:       python3-numpy

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
%autosetup -c
mv %{modname}-%{version} python2
rm -rf python2/*.egg-info

cp -a python2 python3
2to3 --write --nobackups python3

%build
pushd python2
  %py2_build
popd

pushd python3
  %py3_build
popd

%install
pushd python2
  %py2_install
popd

pushd python3
  %py3_install
popd

%check
pushd python2
  %{__python2} setup.py test
popd

pushd python3
  %{__python2} setup.py test
popd

%files -n python2-%{modname}
%doc python2/README.rst
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%doc python3/README.rst
%{python3_sitearch}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
