%define upstream_name    Test-Object
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Thoroughly testing objects via registered handlers 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-4mdv2012.0
+ Revision: 765735
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-3
+ Revision: 764249
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.70.0-2
+ Revision: 676733
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 405589
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.07-4mdv2009.0
+ Revision: 258573
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.07-3mdv2009.0
+ Revision: 246543
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.07-1mdv2008.1
+ Revision: 123718
- kill re-definition of %%buildroot on Pixel's request


* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.0
+ Revision: 84382
- Import perl-Test-Object

* Wed Nov 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2007.1
- first mdv release

