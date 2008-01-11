Summary:	A native client application to configure the Kolab groupware server
Name:		kolabadmin
Version:	0
Release:	%mkrel 0.r74.2
License:	GPL
Group:		Graphical desktop/KDE
URL:		http://wgess16.dyndns.org/~tobias/qt/kolabadmin/
# svn://wgess16.dyndns.org/kolabadmin/trunk
Source0:	%{name}.tar.bz2
BuildRequires:	kdelibs-devel
BuildRequires:	qt4-devel
BuildRequires:	openldap-devel
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
KolabAdmin is a native client application to configure the Kolab groupware
server. It is written in C++/Qt4, which makes it portable to all platforms
(*nix, MacOSX, Windows) and allows a clean and easy installation.

%prep

%setup -q -n %{name}

%build
/usr/lib/qt4/bin/qmake

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/

# Mandriva Icons
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}

convert pics/kolab_logo.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert pics/kolab_logo.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png
convert pics/kolab_logo.png -resize 48x48 %{buildroot}%{_liconsdir}/%{name}.png

# install menu entry.

# XDG menu
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Kolabadmin
Comment=The kolab2 administrator
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Configuration-Networking;
EOF

%post
%update_menus
 
%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*.desktop
