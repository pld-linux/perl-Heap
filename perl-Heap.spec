#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Heap perl module
Summary(pl):	Modu³ perla Heap
Name:		perl-Heap
Version:	0.50
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
# Source0-md5:	f23fc81b84101719e88c66a872611e78
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap module is a collection of routines for managing a heap data
structure.

%description -l pl
Modu³ Heap to kolekcja procedur do zarz±dzania struktur± danych
sterty.

%prep
%setup -q -n Heap-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/Heap
# empty autosplit.ix files
#%%{perl_vendorlib}/auto/Heap
%{_mandir}/man3/*
