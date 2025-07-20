%global tag 0.79.10-pl5

Name: dvdisaster
Version: %(echo %{tag} | tr -d '-')
Release: %autorelease
Summary: Dvdisaster provides additional ECC protection for optical media

License: GPL-3.0
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

%prep
%autosetup -n %{name}-%{tag}
%configure

%build
%make_build

%install
%make_install


%check


%files
%license
%doc

%{_bindir}/%{name}
%{_datadir}/doc/%{name}-%{tag}/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/man/de/man1/%{name}.1.gz
%{_datadir}/man/man1/%{name}.1.gz

%exclude %{_bindir}/%{name}-uninstall.sh

%changelog
%autochangelog
