#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Inter
%include	/usr/lib/rpm/macros.perl
Summary:	Test::Inter - framework for more readable interactive test scripts
Summary(pl.UTF-8):	Test::Inter - szkielet dla bardziej czytelnych, interaktywnych skryptów testowych
Name:		perl-Test-Inter
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	02705664dc874bc8b59b9b313a7572f5
URL:		http://search.cpan.org/dist/Test-Inter/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/Inter.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE TODO
%{perl_vendorlib}/Test/Inter.pm
%{_mandir}/man3/Test::Inter.3pm*
%{_examplesdir}/%{name}-%{version}
