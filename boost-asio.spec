Summary:	Boost ASIO - a cross-platform C++ library for network programming
Summary(pl.UTF-8):	Boost ASIO - wieloplatformowa biblioteka C++ do programowania sieciowego
Name:		boost-asio
Version:	1.2.0
Release:	1
License:	Boost Software License
Group:		Libraries
Source0:	http://dl.sourceforge.net/asio/asio-%{version}.tar.bz2
# Source0-md5:	9dbd5e04e015d02f5b072be5028c91b8
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

%description -l pl.UTF-8
asio to wieloplatformowa biblioteka C++ do programowania sieciowego
udostępniająca spójny, asynchroniczny model wejścia/wyjścia z
nowoczesnym podejściem C++.

%prep
%setup -q -n asio-%{version}

cp -a src src-example

%build
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
%doc COPYING LICENSE* doc/*
%doc src-example/examples
%{_includedir}/asio
%{_includedir}/*.hpp
