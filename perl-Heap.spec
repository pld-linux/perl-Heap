#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	Heap - Perl extensions for keeping data partially sorted
Summary(pl.UTF-8):	Heap - rozszerzenie Perla do przechowywania danych częściowo posortowanych
Name:		perl-Heap
Version:	0.80
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Heap/Heap-%{version}.tar.gz
# Source0-md5:	05fed19a7552dadee11c780cd68c0116
URL:		http://search.cpan.org/dist/Heap/
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl.UTF-8
Zestaw modułów Heap to udostępnia procedury do zarządzania strukturą
danych sterty. Sterta to częściowo posortowana struktura danych, która
umożliwia łatwe znalezienie elementu najmniejszego (lub największego w
przypadku podania odwrotnej funkcji porównującej).

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
