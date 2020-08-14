Name:      aml-acuity-ovxlib
Summary:   Acuity OVX Library
Version:   6.4.0.10
Release:   0
Group:     System/Libraries
License:   Apache-2.0
Source0:   %{name}-%{version}.tar.gz
Source1:   %{name}.manifest

BuildRequires: cmake
Requires: aml-npu-sdk
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%define _pcdir  %{_libdir}/pkgconfig

%description
Amlogic Acuity OVX Library for NN Applications.

%package devel
Summary:   Amlogic Acuity OVX Library (development)
Group:    System/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header and Configuration for Amlogic Acuity OVX Library.

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
	-DPCDIR=%{_pcdir}

make %{?jobs:-j%jobs}

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%manifest %{name}.manifest
%attr(755, root, root)
%{_libdir}/*.so*

%files devel
%{_includedir}/ovx/*
%{_libdir}/pkgconfig/*.pc

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
