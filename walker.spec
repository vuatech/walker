%global debug_package %{nil}

Name:           walker
Version:        2.6.2
Release:        1
Source0:        https://github.com/abenz1267/walker/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
Summary:        Multi-Purpose Launcher with a lot of features. Highly Customizable and fast
URL:            https://github.com/abenz1267/walker
License:        GPL
Group:          Window Manager/Utils

#BuildRequires:  cargo
#BuildRequires:  pkgconfig(graphene-gobject-1.0)
#BuildRequires:  pkgconfig(gtk4)
#BuildRequires:  pkgconfig(gtk4-layer-shell-0)
#BuildRequires:  pkgconfig(poppler-glib)
#BuildRequires:  pkgconfig(protobuf)

Requires:       elephant

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
install -Dm 644 resources/config.toml -t "%{buildroot}/etc/xdg/walker"
install -Dm 644 resources/themes/default/item.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_calc.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_clipboard.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_dmenu.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_files.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_providerlist.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_symbols.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_archlinuxpkgs.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_todo.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/item_unicode.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/layout.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/keybind.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/preview.xml -t "%{buildroot}/etc/xdg/walker/themes/default"
install -Dm 644 resources/themes/default/style.css -t "%{buildroot}/etc/xdg/walker/themes/default"



%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_sysconfdir}/xdg/walker
