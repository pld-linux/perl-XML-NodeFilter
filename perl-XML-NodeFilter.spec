#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	NodeFilter
Summary:	XML::NodeFilter - generic node-filter class
Summary(pl):	XML::NodeFilter - og�lna klasa do filtrowania w�z��w
Name:		perl-XML-NodeFilter
Version:	0.01
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a585cd03435fc51ead427aa2c82b40a3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::NodeFilter is a generic node-filter class for DOM traversal as
specified in the DOM Level 2 Traversal and Range specification. It
extends that specification so this class is more easy to use for Perl
programmers.

%description -l pl
XML::NodeFilter to og�lna klasa do filtrowania w�z��w przy
przechodzeniu DOM wg specyfikacji "DOM Level 2 Traversal and Range".
Rozszerza ona specyfikacj� w ten spos�b, �e ta klasa jest �atwiejsza w
u�yciu dla programist�w perlowych.
 
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/XML/NodeFilter.pm
%{_mandir}/man3/*
