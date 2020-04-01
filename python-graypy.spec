# For different distributions and versions
%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif


# Define macros py2_* for rhel versions less then 7.2
%if 0%{?rhel} && 0%{?dist_raw} <= 72
%{!?py2_build: %global py2_build %py_build}
%{!?py2_install: %global py2_install %py_install}
%endif


%global dist_raw %(%{__grep} -oP "release \\K[0-9]+\\.[0-9]+" /etc/system-release | tr -d ".")

%if 0%{?fedora} > 12 || 0%{?rhel} && 0%{?dist_raw} >= 75
%bcond_without python3
%else
%bcond_with python3
%endif


%global pkgname graypy

Name:		python-%{pkgname}
Version:	2.1.0
Release:	CROC1%{?dist}
Summary:	Python library for logging handlers that send log messages in the GELF

Group:		Development/Python
License:	ASL 2.0
URL:		https://github.com/severb/graypy
Source0:	python-%{pkgname}-2.1.0.tar.gz
BuildArch:	noarch


BuildRequires:  python2-devel
BuildRequires:	python-setuptools


%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%endif

%global _description\
Python logging handlers that send log messages in the Graylog Extended Log Format (GELF).\
graypy supports sending GELF logs to both Graylog2 and Graylog3 servers.\

%description %_description


%package -n python2-%{pkgname}
Summary: %summary
%description -n python2-%{pkgname} %_description


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary: %summary
%description -n python%{python3_pkgversion}-%{pkgname} %_description
%endif


%prep
%setup -q -n %{pkgname}-%{version}


%build
%py2_build

%if %{with python3}
%py3_build
%endif


%install
%py2_install

%if %{with python3}
%py3_install
%endif


%files -n python2-%{pkgname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%endif


%changelog
* Mon Mar 23 2020 Evgenii Kovalev <evgkovalev@croc.ru>
- Build rpm package graypy.
