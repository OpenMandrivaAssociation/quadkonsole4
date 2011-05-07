%define name	quadkonsole4
%define version	0.2.1
Summary:	QuadKonsole - multiple Konsoles in one window
Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
License:	GPLv2+
Group:		Terminals
URL:		http://kde-apps.org/content/show.php/QuadKonsole4?content=141069&PHPSESSID=0d2c6837c693192c7a288f988e6cfb21
Source0:	quadkonsole4-%{version}.tar.lzma
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	kdelibs4-devel


%description
QuadKonsole embeds Konsole kparts in a grid layout. 


%prep
%setup -q

%build

%cmake_kde4 
%make


%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall_std} -C build



%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif 

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc INSTALL COPYING NEWS AUTHORS ChangeLog 
%_kde_datadir/doc/HTML/en/quadkonsole4/common  
%_kde_datadir/doc/HTML/en/quadkonsole4/index.cache.bz2  
%_kde_datadir/doc/HTML/en/quadkonsole4/index.docbook
%{_bindir}/%{name}
%_kde_datadir/applications/kde4/*.desktop
%_kde_datadir/apps/%{name}/quadkonsole4ui.rc
%_kde_datadir/config.kcfg/*
%_kde_iconsdir/*/*/*/*

