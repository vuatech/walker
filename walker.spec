%global debug_package %{nil}

Name:           walker
Version:        1.0.0
Release:        1
Source0:        https://github.com/abenz1267/walker/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
Summary:        Multi-Purpose Launcher with a lot of features. Highly Customizable and fast
URL:            https://github.com/abenz1267/walker
License:        GPL
Group:          Window Manager/Utils

BuildRequires:  cargo
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-layer-shell-0)
BuildRequires:  pkgconfig(poppler-glib)

%description
A fast, customizable application launcher built with GTK4 and Rust, designed for Linux desktop environments. Walker provides a clean, modern interface for launching applications, running commands, performing c>

%prep
%autosetup -p1
tar -zxf %{SOURCE1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --release --offline --frozen

%install
install -Dpm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
