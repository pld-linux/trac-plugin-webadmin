
%define		dev_r	dev_r3158
Summary:	Plugin for administering Trac projects through the web interface
Summary(pl.UTF-8):	Wtyczka do administracji projektami Traca przez interfejs WWW
Name:		trac-plugin-webadmin
Version:	0.1.2
Release:	0.%{dev_r}.1
Group:		Application/WWW
License:	distributable
Source0:	http://rakin.eu.org/trac-plugins/trac-plugin-webadmin-%{version}%{dev_r}.tar.gz
# Source0-md5:	2635ffb44e2e342cec17e9d87710f558
URL:		http://projects.edgewall.com/trac/wiki/WebAdmin
BuildRequires:	python-devel
%pyrequires_eq  python-modules
Requires:	trac
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for administering your Trac projects through the web interface.
This plugin is still under development, but it already supports most of
the tasks performed by trac-admin.

%description -l pl.UTF-8
Wtyczka dla Traca służąca do administracji projektami poprzez
interfejs WWW. Jest ciągle rozwijana, jednak udostepnia już większą
część funkcjonalości programu trac-admin.

%prep
%setup -q -n webadmin

%build
python setup.py build
python setup.py	egg_info

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
        --single-version-externally-managed \
        --optimize 2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%{py_sitescriptdir}/webadmin
%{py_sitescriptdir}/TracWebAdmin-0.1.2dev_r3129-py2.4.egg-info
