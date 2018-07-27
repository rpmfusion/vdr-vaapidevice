# https://github.com/pesintta/vdr-plugin-vaapidevice/commit/a17c11072e7f9465f12830e6d3045956d4cb2776
%global commit0 a17c11072e7f9465f12830e6d3045956d4cb2776
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global sname vdr-plugin-vaapi
%global gitdate 20180401

Name:           vdr-vaapidevice
Version:        0.7.0
Release:        7.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        A VA-API output device plugin for VDR

License:        AGPLv3
URL:            https://github.com/pesintta/vdr-plugin-vaapidevice
Source0:        %{url}/archive/%{commit0}/%{sname}-%{shortcommit0}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vdr) >= 2.2.0
BuildRequires:  gettext
BuildRequires:  libva-devel >= 2.0.0
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gl)
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       (vdr-vaapidevice if libva-intel-driver)

Conflicts:      vdr-softhddevice

%description
A VA-API output device plugin for VDR.

    Based on softhddevice by Johns:
    http://projects.vdr-developer.org/projects/plg-softhddevice
    Video decoder CPU / VAAPI
    Video output VAAPI
    Audio FFMpeg / Alsa / Analog / Digital
    HDMI/SPDIF pass-through
    VDR ScaleVideo API
    Autocrop
    Grab image (no OSD!)
    Suspend / Detach
    Letterbox, Stretch and Center cut-out video display modes


%prep
%setup -qn vdr-plugin-vaapidevice-%{commit0}

# remove .git files
rm -f .indent.pro .gitignore .dependencies

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} \
     LDFLAGS="%{?__global_ldflags}"

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/vaapidevice.conf
%find_lang %{name}

%files -f %{name}.lang
%doc HISTORY README
%license AGPL-3.0.txt
%{vdr_plugindir}/libvdr-vaapidevice.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/vaapidevice.conf

%changelog
* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-7.20180401gita17c110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-6.20180401gita17c110
- Rebuilt for vdr-2.4.0

* Wed Apr 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-5.20180401gita17c110
- Update to 0.7.0-5.20180401gita17c110
- Use url macro in Source0
- Remove RR xorg-x11-server-Xorg

* Tue Mar 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-4.20180312git53d44aa
- Add Obsoletes vdr-softhddevice
- Remove BR: xorg-x11-drv-intel It's unneeded when using va-api enabled 
- Add Suggests libva-intel-driver

* Mon Mar 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-3.20180312git53d44aa
- Update to 0.7.0-3.20180312git53d44aa

* Tue Feb 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-2.20180220git6372704
- Add BR gcc
- Add BR gcc-c++
- Simplify the Source0 URL
- Use pkgconfig for BR
- Add LDFLAGS to make

* Sun Feb 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-1.20180220git6372704
- Initial build
