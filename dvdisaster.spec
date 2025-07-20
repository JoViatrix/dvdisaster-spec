%global tag 0.79.10-pl5
%global shortname dvdisaster

Name: %{shortname}-gtk3
Version: %(echo %{tag} | tr -d '-')
Release: %autorelease
Summary: Dvdisaster provides additional ECC protection for optical media

License: GPL-3.0-only
URL: https://github.com/speed47/dvdisaster.git
Source0: https://github.com/speed47/dvdisaster/archive/refs/tags/v%{tag}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconf
BuildRequires: pkgconf-pkg-config
BuildRequires: gettext
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: gtk3-devel >= 3.4.0

%description
Dvdisaster provides additional ECC protection for optical media. If a medium gets damaged, dvdisaster can recover it as long as the amount of damage is smaller than the amount of ECC data you added to protect it.
It can loosely be compared to .par2 files, but the protection works at the iso level instead of working at the file level. This way, even if metadata from the optical medium filesystem is damaged, dvdisaster can still work flawlessly.
This is the unofficial version from %{url}.
%prep
%autosetup -n %{shortname}-%{tag}
%configure

%build
%make_build

%install
%make_install


%check


%files
%{_bindir}/%{shortname}
%{_datadir}/locale/*/LC_MESSAGES/%{shortname}.mo
%{_datadir}/man/de/man1/%{shortname}.1.gz
%{_datadir}/man/man1/%{shortname}.1.gz

%exclude %{_bindir}/%{shortname}-uninstall.sh

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This subpackage contains documentation files for %{name}

%files doc
%doc
%{_datadir}/doc/%{shortname}-%{tag}/*

%changelog
%autochangelog
