Summary:	An advanced download manager
Name:		prozilla
Version:	1.3.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.lintux.cx/~kalum/%{name}-%{version}.tar.gz
URL:		http://www.lintux.cx/~kalum/prozilla.html
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ProZilla is a new download accellerator program written for Linux to
speed up the normal file download process. It often gives speed
increases of around 200% to 300%. It supports both FTP and HTTP
protocols, and the theory behind it is very simple. The program opens
multiple connections to a server, and each of the connections
downloads a part of the file, thus defeating existing internet
congestion prevention methods which slow down a single connection
based download.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}

%{__install} src/proz 	$RPM_BUILD_ROOT%{_bindir}
%{__install} prozrc.sample	$RPM_BUILD_ROOT%{_sysconfdir}/prozilla.conf 
%{__install} man/prozilla.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ANNOUNCE AUTHORS CREDITS ChangeLog FAQ NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/prozilla.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
