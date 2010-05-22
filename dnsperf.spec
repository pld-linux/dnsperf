Summary:	DNS server query performance testing tool
Summary(pl.UTF-8):	Narzędzia do testowania wydajności serwera DNS
Name:		dnsperf
Version:	1.0.0.1
Release:	1
License:	BSD-like/distributable
Group:		Networking/Utilities
Source0:	ftp://ftp.nominum.com/pub/nominum/dnsperf/1.0.0.1/%{name}-%{version}-1.tar.gz
# Source0-md5:	db2e3f85fbe1f75d384f9b5c1ff0759a
URL:		http://www.nominum.com/services/measurement_tools.php
BuildRequires:	autoconf
BuildRequires:	bind-devel >= 9.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DNSPerf and ResPerf deliver accurate performance metrics of Domain
Name Services (DNS). These tools are easy-to-use andsimulate real
Internet workloads to provide the necessary insight that carriers need
to plan and deploy network services.

DNSPerf measures Authoritative Domain Name services and is designed to
simulate network conditions by self-pacing the query load.

Caching services performance and workload profile differ significantly
from Authoritative Domain services; therefore a different tool is
needed. ResPerf is designed specifically to simulate Caching Domain
Name services. To test a caching server, ResPerf systematically
increases the query rate and monitors the response rate.

%prep
%setup -q -n %{name}-%{version}-1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	mandir=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

install contrib/queryparse/queryparse $RPM_BUILD_ROOT%{_bindir}
install contrib/queryparse/queryparse.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES doc/*.pdf contrib/queryparse/{INSTALL,USAGE} common.h
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
