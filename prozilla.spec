Summary:	An advanced download manager
Summary(pl.UTF-8):	Zaawansowany program do ściągania plików
Name:		prozilla
Version:	2.0.4
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.bz2
# Source0-md5:	220f03968ddac79c2d6b48a507cd9c71
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-Oopt.patch
Patch2:		%{name}-man.patch
Patch3:		%{name}-gcc4.patch
Patch4:		%{name}-opt.patch
URL:		http://prozilla.genesys.ro/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProZilla is a new download accellerator program written for Linux to
speed up the normal file download process. It often gives speed
increases of around 200% to 300%. It supports both FTP and HTTP
protocols, and the theory behind it is very simple. The program opens
multiple connections to a server, and each of the connections
downloads a part of the file, thus defeating existing internet
congestion prevention methods which slow down a single connection
based download.

%description -l pl.UTF-8
ProZilla jest programem typu "download accellerator" dla Linuksa
napisanym, aby przyspieszyć proces ściągania plików. Często daje
zwiększenie prędkości do 200-300%. Wspiera protokoły HTTP i FTP, a
jego teoretyczne działanie jest bardzo proste. Program otwiera wiele
połączeń do serwera i każde z nich ściąga tylko część programu. Dzięki
temu możliwe jest ominięcie ograniczeń transferu nakładanych na
pojedyncze połączenie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# kill AC_PROG_LIBTOOL
head -n 667 libprozilla/acinclude.m4 > tmp
mv tmp libprozilla/acinclude.m4

%build
cd libprozilla
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="-I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}

install src/proz 	$RPM_BUILD_ROOT%{_bindir}
#install prozrc.sample	$RPM_BUILD_ROOT%{_sysconfdir}/prozilla.conf
install man/proz.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog docs/FAQ README TODO
# %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prozilla.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
