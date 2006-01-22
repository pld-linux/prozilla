Summary:	An advanced download manager
Summary(pl):	Zaawansowany program do ¶ci±gania plików
Name:		prozilla
Version:	2.0.3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.bz2
# Source0-md5:	0a3b9c179ffd7390e52a2b6f6f98111d
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-Oopt.patch
Patch2:		%{name}-man.patch
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
%patch1 -p1
%patch2 -p1

%build
rm -f missing
CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses"
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
