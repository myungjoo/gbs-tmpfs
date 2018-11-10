Name:        gbs-tmpfs
Summary:     Create tmpfs /tmp for faster I/O in gbs build
Version:     1.0
Release:     1rc1
Group:       Development/Tools
Packager:    MyungJoo Ham <myungjoo.ham@samsung.com>
License:     Apache-2.0
Source0:     gbs-tmpfs-%{version}.tar.gz

Requires:    mount

%description
gbs-tmpfs creates tmpfs at /tmp for gbs build in order to
accelerate gbs's QEMU I/O.
An rpm package may use this by addinng
BuildRequires: gbs-tmpfs

%files

%post
mkdir -p /tmp
mount -t tmpfs tmpfs /tmp

%changelog
* Sat Nov 10 2018 MyungJoo Ham <myungjoo.ham@samsung.com>
- The first version is implemented
