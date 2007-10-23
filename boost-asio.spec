Summary:	Boost ASIO - a cross-platform C++ library for network programming
Name:		boost-asio
Version:	0.3.7
Release:	1
License:	Boost Software License
Group:		Libraries
Source0:	http://dl.sourceforge.net/asio/asio-%{version}.tar.bz2
# Source0-md5:	5481c9764ece613d8e099c1a9b32ded2
URL:		http://asio.sourceforge.net/
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	openssl-devel
Requires:	boost-devel
Requires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
asio is a cross-platform C++ library for network programming that
provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%prep
%setup -q -n asio-%{version}

%build
cp -a src src-example
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING LICENSE* THANKS TODO doc/*
%doc src-example/examples
%{_includedir}/asio
%{_includedir}/*.hpp
