Name:		graypy
Version:	2.1.0
Release:	1%{?dist}
Summary:	Python library for logging handlers that send log messages in the GELF

Group:		Development/Python
License:	LICENSE
URL:		https://github.com/severb/graypy
Source0:	graypy-2.1.0.tar.gz
BuildArch:	noarch

BuildRequires:	gcc
BuildRequires:  python2-tools
BuildRequires:  python2-devel
BuildRequires:	python-setuptools


# %if %{with python3}
# BuildRequires:  python%{python3_pkgversion}-devel
# BuildRequires:  python%{python3_pkgversion}-setuptools
# %endif


%description
Python logging handlers that send log messages in the Graylog Extended Log Format (GELF).
graypy supports sending GELF logs to both Graylog2 and Graylog3 servers.


%prep
%setup -q


%build
%py2_build


%install
%py2_install
# rm -rf $RPM_BUILD_ROOT


%files
%doc LICENSE README.rst
%{python_sitelib}/*egg-info
%{python_sitelib}/graypy
%{python_sitelib}/tests


%changelog
* Mon Mar 23 2020 Evgenii Kovalev <evgkovalev@croc.ru>
- First try build rpm graypy.
