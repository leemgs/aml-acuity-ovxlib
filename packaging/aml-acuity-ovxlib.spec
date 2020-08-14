Name:      aml-acuity-ovxlib
Summary:   Amlogic Acuity OpenVX Library
Version:   6.4.0.10
Release:   0
Group:     System/Libraries
License:   GPLv2
URL:       https://www.khadas.com/post/npu-toolkit-v6-4-0-10-for-vim3---vim3l-released
Source0:   %{name}-%{version}.tar.gz
Source1:   %{name}.manifest

BuildRequires: cmake

ExclusiveArch: %{arm} aarch64

Requires: aml-npu-sdk
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
Amlogic Acuity OpenVX Library to run neural network applications.

%package devel
Summary:   Amlogic Acuity OVX Library (development)
Group:    System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header and Configuration for Amlogic Acuity OpenVX Library.

%prep
%setup -q

%build
cp %{SOURCE1} .
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
cmake \
	-DCMAKE_INSTALL_PREFIX=/usr \
%ifarch aarch64
     -DARCH=arm64 \
%else
     -DARCH=arm \
%endif
	-DFULLVER=%{version} \
	-DBINDIR=%{_bindir} \
	-DLIBDIR=%{_libdir} \
	-DINCDIR=%{_includedir}/ovx \
	-DPCDIR=%{_libdir}/pkgconfig

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%manifest %{name}.manifest
%attr(0755, root, root)
%license LICENSE
%{_libdir}/*.so*

%files devel
%{_includedir}/ovx/*
%{_libdir}/pkgconfig/*.pc


%changelog

* Fri Aug 14 2020 Geunsik Lim <geunsik.lim@samsung.com>
- Added the spec file to generate a Tizen RPM package
