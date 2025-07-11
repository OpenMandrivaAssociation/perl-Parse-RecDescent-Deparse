%define real_name Parse-RecDescent-Deparse

Summary:	Turn a Parse::RecDescent object back into its grammar
Name:		perl-%{real_name}
Version:	1.00
Release:	9
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Parse/RecDescent/Deparse.pm
%{_mandir}/*/*
