#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Inter
Summary:	Test::Inter - framework for more readable interactive test scripts
Summary(pl.UTF-8):	Test::Inter - szkielet dla bardziej czytelnych, interaktywnych skryptów testowych
Name:		perl-Test-Inter
Version:	1.09
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4e9bbe25e28d2453a6c63a1e675cc484
URL:		https://metacpan.org/release/Test-Inter
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-Test-Pod >= 1.00
BuildRequires:	perl-Test-Pod-Coverage >= 1.00
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is another framework for writing test scripts. It is loosely
inspired by Test::More, and has most of it's functionality, but it is
not a drop-in replacement.

%description -l pl.UTF-8
Ten moduł to jeszcze jeden szkielet do tworzenia skryptów testowych.
Jest luźno inspirowany modułem Test::More i ma większość jego
funkcjonalności, ale nie jest bezpośrednim zamiennikiem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/Inter.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%{perl_vendorlib}/Test/Inter.pm
%{_mandir}/man3/Test::Inter.3pm*
%{_examplesdir}/%{name}-%{version}
