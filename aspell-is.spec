%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.51.1-0
%define languageenglazy Icelandic
%define languagecode is
%define lc_ctype is_IS
%define aspellrelease 0.60

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.51.1.0
Release:	3
Group:		System/Internationalization
License:	GPLv2
Url:		https://aspell.net/
Source0:	http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Autoreqprov:	no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
# don't use configure macro
./configure

%make_build

%install
%make_install
mv $RPM_BUILD_ROOT/%{_libdir}/aspell-%{aspellrelease}/*slenska.alias $RPM_BUILD_ROOT/%{_libdir}/aspell-%{aspellrelease}/íslenska.alias

mkdir -p %{buildroot}/%{_datadir}/aspell
mkdir -p %{buildroot}/%{_libdir}/aspell

chmod 644 Copyright README* 

%files
%doc README* Copyright 
%{_libdir}/aspell-*/*

