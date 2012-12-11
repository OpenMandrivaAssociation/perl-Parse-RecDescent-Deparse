%define real_name Parse-RecDescent-Deparse

Summary:	Parse::RecDescent::Deparse - Turn a Parse::RecDescent object back into its grammar
Name:		perl-%{real_name}
Version:	1.00
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module adds the deparse method to the Parse::RecDescent
class, which returns a textual description of the grammar.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Parse/RecDescent/Deparse.pm
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.00-6mdv2010.0
+ Revision: 430520
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.00-5mdv2009.0
+ Revision: 258192
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.00-4mdv2009.0
+ Revision: 246271
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-2mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.00-2mdv2008.0
+ Revision: 86769
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdk
- initial Mandriva package

