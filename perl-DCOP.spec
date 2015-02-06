%define upstream_name    DCOP
%define upstream_version 0.038

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Epoch:		2

Summary:	Extensible inheritable class to dcop
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This class is meant to be a base constructor for higher level of
abstraction on dcop clients.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 2:0.38.0-3mdv2011.0
+ Revision: 654905
- rebuild for updated spec-helper

* Sun Jul 26 2009 Jérôme Quelin <jquelin@mandriva.org> 2:0.38.0-2mdv2011.0
+ Revision: 400182
- bumping epoch

* Sat Jul 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.38.0-2mdv2010.0
+ Revision: 399738
- bumping mkrel
- bumping epoch to upgrade previous module provided by kdebindings-3.5.*
- import perl-DCOP


* Sat Jul 25 2009 cpan2dist 0.038-1mdv
- initial mdv release, generated with cpan2dist
