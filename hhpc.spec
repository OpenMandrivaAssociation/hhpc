%define debug_package %nil

Name: hhpc
Version: 1.0
Release: 1
Source0: %{name}-%{version}.tar.xz
Summary: Tool to hide the mouse pointer while it is inactive
URL: https://github.com/aktau/hhpc
License: MIT
Group: System/X11
BuildRequires: pkgconfig(x11)

%description
Tool to hide the mouse pointer while it is inactive

%prep
%setup -q

%build
%make

%install
%makeinstall_std PREFIX=%{_prefix}

%files
%{_bindir}/hhpc
