Name:           test_task
Version:        1.0
Release:        1%{?dist}
Summary:        Internship test task

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        https://www.example.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
Devops internship test task for RAIDIX.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/%{name}

%changelog
* Mon Nov 14 2022 Alexey Fonarev <avf.2016@yandex.ru> - 1.0-1
- First package