%include	/usr/lib/rpm/macros.perl
Summary:	Heap perl module
Summary(pl):	Modu³ perla Heap
Name:		perl-Heap
Version:	0.50
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Heap/Heap-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heap module is a collection of routines for managing a heap data
structure.

%description -l pl
Modu³ Heap to kolekcja rutyn do zarz±dzania struktur± danych sterty.

%prep
%setup -q -n Heap-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Heap.pm
%{perl_sitelib}/Heap
%{perl_sitelib}/auto/Heap
%{_mandir}/man3/*
