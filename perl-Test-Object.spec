%define module  Test-Object
%define name    perl-%{module}
%define version 0.07
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Thoroughly testing objects via registered handlers 
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*


