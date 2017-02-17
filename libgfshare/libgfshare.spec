Name:		libgfshare
Version:	2.0.0
Release:	1%{?dist}
Summary:	Shamir's secret-sharing method in the Galois Field GF(2**8)

Group:		Applications/Communications
License:	BSD
URL:		http://www.digital-scurf.org/software/libgfshare
Source0:	https://git.gitano.org.uk/libgfshare.git/snapshot/libgfshare-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool

%description
This library implements what is known as Shamir Secret Sharing. This
entails encoding a secret as an integer and then constructing a
polynomial whose coefficients are random and calculating coordinate
pairs along the resultant curve. These coordinate pairs are considered
'shares' and by controlling the order of the polynomial we can control
the number of shares required to be able to recover the secret.

%package devel
Summary:	Development files for %{name}

%description devel
Static libraries and header files for %{name}



%prep
%setup -q


%build
./prep-fresh.sh
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/gfcombine
%{_bindir}/gfsplit
%{_libdir}/libgfshare.so*
%{_mandir}/man1/*

%files devel
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_mandir}/man5/*
%{_mandir}/man7/*


%changelog
* Wed Feb 08 2017 RJ Bergeron - 2.0.0-1
- initial build
