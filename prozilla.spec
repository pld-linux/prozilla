Summary:	An advanced download manager
Summary(pl):	Zaawansowany program do ¶ci±gania plików
Name:		prozilla
Version:	1.3.7.3	
Release:	1	
Epoch:		1
License:	GPL
Group:		Applications/Networking
Source0:	http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	88f0d9d88aa7628239dae08804dcd550
Patch0:		%{name}-ac_fixes.patch
URL:		http://prozilla.genesys.ro/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
ProZilla jest programem typu "download accellerator" dla Linuksa
napisanym, aby przyspieszyæ proces ¶ci±gania plików. Czêsto daje
zwiêkszenie prêdko¶ci do 200-300%. Wspiera protoko³y HTTP i FTP, a
jego teoretyczne dzia³anie jest bardzo proste. Program otwiera wiele
po³±czeñ do serwera i ka¿de z nich ¶ci±ga tylko czê¶æ programu. Dziêki
temu mo¿liwe jest ominiêcie ograniczeñ transferu nak³adanych na
pojedyncze po³±czenie.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}

install src/proz 	$RPM_BUILD_ROOT%{_bindir}
install prozrc.sample	$RPM_BUILD_ROOT%{_sysconfdir}/prozilla.conf
install man/prozilla.1	$RPM_BUILD_ROOT%{_mandir}/man1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS CREDITS ChangeLog FAQ NEWS README TODO
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/prozilla.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
