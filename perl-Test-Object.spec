%define modname	Test-Object
%define modver	0.07

Summary:	Thoroughly testing objects via registered handlers 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description 
In situations where you have deep trees of classes, there is a common situation
in which you test a module 4 or 5 subclasses down, which should follow the
correct behaviour of not just the subclass, but of all the parent classes.

This should be done to ensure that the implementation of a subclass has not
somehow "broken" the object's behaviour in a more general sense.

Test::Object is a testing package designed to allow you to easily test what you
believe is a valid object against the expected behaviour of all of the classes
in its inheritance tree in one single call.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
%make test

%files
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/*

