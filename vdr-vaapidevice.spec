# https://github.com/pesintta/vdr-plugin-vaapidevice/commit/d19657bae399e79df107e316ca40922d21393f80
%global commit0 d19657bae399e79df107e316ca40922d21393f80
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global sname vdr-plugin-vaapi
%global gitdate 20190526

Name:           vdr-vaapidevice
Version:        0.7.0
Release:        25.%{gitdate}git%{shortcommit0}%{?dist}
Summary:        A VA-API output device plugin for VDR

License:        AGPLv3
URL:            https://github.com/pesintta/vdr-plugin-vaapidevice
Source0:        %{url}/archive/%{commit0}/%{sname}-%{shortcommit0}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
Patch0:         %{name}-undefined-symbol.patch

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
%autosetup -p0 -n vdr-plugin-vaapidevice-%{commit0}

# remove .git files
rm -f .indent.pro .gitignore .dependencies

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" \
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
* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> -  0.7.0-25.20190526gitd19657b
- Rebuilt for new VDR API version

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-24.20190526gitd19657b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-23.20190526gitd19657b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-22.20190526gitd19657b
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-21.20190526gitd19657b
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-20.20190526gitd19657b
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-19.20190526gitd19657b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-18.20190526gitd19657b
- Add patch %%{name}-undefined-symbol.patch fixes (BZ#5686)

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.7.0-17.20190526gitd19657b
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-16.20190526gitd19657b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.7.0-15.20190526gitd19657b
- Rebuild for new ffmpeg version

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-14.20190526gitd19657b
- Rebuilt for new VDR API version 2.4.1

* Sun Jun 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-13.20190526gitd19657b
- Rebuilt for new VDR API version

* Fri Jun 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-12.20190526gitd19657b
- Update to 0.7.0-12.20190526gitd19657b

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-11.20180401gita17c110
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.7.0-10.20180401gita17c110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.7.0-9.20180401gita17c110
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.7.0-8.20180401gita17c110
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

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
