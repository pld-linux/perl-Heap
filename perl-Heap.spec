#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
Summary:	Heap - Perl extensions for keeping data partially sorted
Summary(pl):	Heap - rozszerzenie Perla do przechowywania dznych czê¶ciowo posortowanych
Name:		perl-Heap
Version:	0.70
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
# Source0-md5:	51538c57b26ca2fa1afba16a75d90b5b
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap module is a collection of routines for managing a heap data
structure.

The Heap collection of modules provide routines that manage a heap of
elements.  A heap is a partially sorted structure that is always able
to easily extract the smallest of the elements in the structure (or
the largest if a reversed compare routine is provided).

%description -l pl
Zestaw modu³ów Heap to udostêpnia procedury do zarz±dzania struktur±
danych sterty. Sterta to czê¶ciowo posortowana struktura danych, która
umo¿liwia ³atwe znalezienie elementu najmniejszego (lub najwiêkszego w
przypadku podania odwrotnej funkcji porównuj±cej).

%prep
%setup -q -n Heap-%{version}

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
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/Heap
# empty autosplit.ix files
#%%{perl_vendorlib}/auto/Heap
%{_mandir}/man3/*
