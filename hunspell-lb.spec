Name: hunspell-lb
Summary: Luxembourgish hunspell dictionaries
%define upstreamid 20121128
Version: 0.%{upstreamid}
Release: 1%{?dist}
Source: http://downloads.spellchecker.lu/packages/OOo3/SpellcheckerLu.oxt
Group: Applications/Text
URL: http://spellchecker.lu
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: EUPL 1.1
BuildArch: noarch
Requires: hunspell

%description
Luxembourgish hunspell dictionaries.

%package -n mythes-lb
Summary: Luxembourgish thesaurus
Group: Applications/Text
Requires: mythes

%description -n mythes-lb
Luxembourgish thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_lb_LU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc registration/README_lb_LU.txt
%{_datadir}/myspell/*

%files -n mythes-lb
%defattr(-,root,root,-)
%doc registration/README_lb_LU.txt
%{_datadir}/mythes/th_lb_LU_v2.*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20110821-1
- Resolves: rhbz#905966 latest version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110821-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110821-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 26 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110821-1
- latest version

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110709-1
- latest version

* Sat Apr 16 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110412-1
- latest version

* Tue Apr 11 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110411-1
- latest version

* Fri Mar 1 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110313-1
- latest version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110107-1
- latest version

* Wed Sep 15 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100914-1
- latest version

* Mon Jul 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100704-1
- latest version

* Tue Jun 29 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100628-1
- latest version

* Tue May 11 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100509-1
- latest version

* Thu Apr 22 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100420-1
- latest version

* Mon Apr 12 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100408-1
- latest version

* Thu Apr 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100407-2
- latest version

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100301-2
- mythes now owns /usr/share/mythes

* Tue Mar 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100301-1
- latest version

* Wed Feb 17 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100216-1
- latest version

* Wed Jan 27 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100120-1
- initial version
