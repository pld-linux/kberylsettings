#
%define	_snap	20070101
#
Summary:	KDE beryl settings
Summary(pl):	Mened¿er ustawieñ beryla dla KDE
Name:		kberylsettings
Version:	0.1
Release:	1
License:	LGPL
Group:		X11
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	982b2696816441906378626db2d3725b
URL:		http://beryl-project.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	beryl-core
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Beryl Settings Manager for KDE.

%description -l pl
Mened¿er ustawieñ beryla dla KDE.

%prep
%setup -q -n %{name}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/html
%{py_sitescriptdir}/%{name}/pixmaps
%{py_sitescriptdir}/*.egg-info
