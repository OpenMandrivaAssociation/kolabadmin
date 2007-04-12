Summary:	The kolab2 administrator
Name:		kolabadmin
Version:	0
Release:	%mkrel 0.r23.2
License:	GPL
Group:		Graphical desktop/KDE
URL:		svn://wgess16.dyndns.org/kolabadmin/trunk
Source0:	%{name}.tar.bz2
Patch0:		kolabadmin-build_fix.diff
BuildRequires:	kdelibs-devel
BuildRequires:	qt4-devel
BuildRequires:	openldap-devel
BuildRequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The kolab2 administrator

%prep

%setup -q -n %{name}
%patch0 -p0

%build
export CFLAGS="%{optflags} -DLDAP_DEPRECATED"
export CXXFLAGS="%{optflags} -DLDAP_DEPRECATED"

/usr/lib/qt4/bin/qmake

%make \
    CFLAGS="$CFLAGS %{optflags} -DLDAP_DEPRECATED" \
    CXXFLAGS="$CXXFLAGS %{optflags} -DLDAP_DEPRECATED"

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
install -d %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}): needs=X11 \
section="More Applications/Servers" \
title="%{name}" \
longtitle="%{summary}." \
command="%{_bindir}/%{name}" \
icon="%{name}.png"
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus
 
%postun
%clean_menus

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %{_bindir}/%{name}
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

