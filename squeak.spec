%global imagefile Squeak6.1-23976-64bit

Summary:	Squeak Smalltalk environment
Name:		squeak
Version:	6.1.23976
Release:	1
License:	MIT
Group:		Development/Languages
Url:		https://squeak.org/
# https://files.squeak.org/6.1/Squeak6.1-23976-64bit/Squeak6.1-23976-64bit.zip
Source0:	%{imagefile}.zip
Source1:	squeak-image.sh
Source2:	squeak.desktop
Source3:	squeak.xml
Source4:	squeak.png
BuildArch:	noarch
BuildRequires:	desktop-file-utils
Requires:	opensmalltalk-vm >= 202606270913
Provides:	squeak3-vm = %{version}-%{release}
Obsoletes:	squeak3-vm < %{version}

%description
Squeak is a Smalltalk-80 environment. This package contains the Squeak 6.1
image, update 23976. It runs on the OpenSmalltalk Cog Spur virtual machine
and replaces the Squeak 3.10 virtual machine.

The image and changes file are copied into the user data directory on first
launch, because a running image writes to both.

%prep
%setup -q -c -n %{name}-%{version}

%build
# Data package. Nothing to compile.

%install
install -d %{buildroot}%{_datadir}/squeak
install -m 644 %{imagefile}.image %{imagefile}.changes SqueakV60.sources \
	%{buildroot}%{_datadir}/squeak/
install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/squeak-image
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/mime/packages/squeak.xml
install -D -m 644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/squeak.png

%check
test -s %{imagefile}.image
test -s %{imagefile}.changes
test -s SqueakV60.sources

%files
%{_bindir}/squeak-image
%{_datadir}/squeak
%{_datadir}/applications/squeak.desktop
%{_datadir}/mime/packages/squeak.xml
%{_datadir}/pixmaps/squeak.png
