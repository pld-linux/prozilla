Summary: An advanced download manager
Name: prozilla
Version: 1.06pre0
Release: 2
Copyright: GNU
Group: Applications/Internet
Source0: prozilla-1.06pre0.tar.gz
Distribution: Build For Redhat 7.0
Url: http://www.lintux.cx/~kalum/prozilla.html
Packager: Ralph Slooten <axllent@axllent.cjb.net>

%description
ProZilla is a new download accellerator program written for
Linux to speed up the normal file download process. It often
gives speed increases of around 200% to 300%. It supports
both FTP and HTTP protocols, and the theory behind it is
very simple. The program opens multiple connections to a
server, and each of the connections downloads a part of the
file, thus defeating existing internet congestion prevention
methods which slow down a single connection based download.



%prep
rm -rf $RPM_BUILD_ROOT

%setup -n prozilla-1.06pre0
./configure --prefix=/usr







%build
make







%install
make install




%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/*





%files
/usr/bin/proz
/usr/bin/gproz
%doc ANNOUNCE
%doc AUTHORS
%doc CHANGES
%doc COPYING
%doc CREDITS
%doc ChangeLog
%doc FAQ
%doc NEWS
%doc README
%doc TODO
