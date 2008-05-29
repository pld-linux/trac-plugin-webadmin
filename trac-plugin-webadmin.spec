%define		subver	dev_r3158
%define		rel		2
Summary:	Plugin for administering Trac projects through the web interface
Summary(pl.UTF-8):	Wtyczka do administracji projektami Traca przez interfejs WWW
Name:		trac-plugin-webadmin
Version:	0.1.2
Release:	0.%{subver}.%{rel}
License:	distributable
Group:		Applications/WWW
Source0:	http://rakin.eu.org/trac-plugins/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	2635ffb44e2e342cec17e9d87710f558
URL:		http://projects.edgewall.com/trac/wiki/WebAdmin
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.194
%pyrequires_eq  python-modules
Requires:	trac
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for administering your Trac projects through the web interface.
This plugin is still under development, but it already supports most
of the tasks performed by trac-admin.

%description -l pl.UTF-8
Wtyczka dla Traca służąca do administracji projektami poprzez
interfejs WWW. Jest ciągle rozwijana, jednak udostepnia już większą
część funkcjonalości programu trac-admin.

%prep
%setup -q -n webadmin

%build
%{__python} setup.py build
%{__python} setup.py	egg_info

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = "1" ]; then
	%banner -e %{name} <<-'EOF'
	Don't forget to enable webadmin in conf/trac.ini:

	[components]
	webadmin.* = enabled
#'
EOF
fi

%files
%defattr(644,root,root,755)
%doc COPYING
%{py_sitescriptdir}/webadmin
%{py_sitescriptdir}/TracWebAdmin-*.egg-info
