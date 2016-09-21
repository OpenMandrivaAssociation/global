Summary:	GNU GLOBAL source code tag system for all hackers
Name:		global
Version:	6.5.5
Release:	1
License:	GPLv3
Group:		Development/Other
Url:		http://www.gnu.org/software/global/
Source0:	http://ftp.gnu.org/gnu/global/%{name}-%{version}.tar.gz
Patch0:		global-6.2.7-fix-str-fmt.patch

BuildRequires:	pkgconfig(ncurses)

%description
GNU GLOBAL is a source code tag system that works the same way across
diverse environments. It supports C, C++, Yacc, Java, PHP4 and assembler
source code.

Sample quick usage:
$ tar -zxf foo-0.3.4.tar.gz && cd foo-0.3.4
$ gtags && htags -a -s -n
$ www-browser ./HTML/files.html

%prep
%setup -q
%apply_patches

%build
%configure \
	--enable-shared \
	--disable-static

%make

%install
%makeinstall_std
install -d %{buildroot}%{_datadir}/emacs/site-lisp
mv %{buildroot}%{_datadir}/gtags/gtags.el %{buildroot}%{_datadir}/emacs/site-lisp/
install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF >%{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el
(autoload 'gtags-mode "gtags" "GNU GLOBAL tags mode." t) ;;;'
EOF

pushd %{buildroot}%{_datadir}/gtags/
rm -f AUTHORS BOKIN_MODEL BOKIN_MODEL_FAQ COPYING ChangeLog DONORS \
      FAQ INSTALL LICENSE NEWS README THANKS gtags.conf BUILD_TOOLS \
      head.in
popd
# at least Lynx can work with *.html.gz, not with .ghtml
sed -e 's/gzipped_suffix=ghtml/gzipped_suffix=html.gz/' <gtags.conf >%{buildroot}%{_sysconfdir}/gtags.conf

%files
%doc AUTHORS BOKIN_MODEL BOKIN_MODEL_FAQ DONORS FAQ
%doc LICENSE NEWS README THANKS gtags.conf
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
%config(noreplace) %{_sysconfdir}/gtags.conf
%{_bindir}/global
%{_bindir}/globash
%{_bindir}/gozilla
%{_bindir}/gtags
%{_bindir}/gtags-cscope
%{_bindir}/htags
%{_datadir}/emacs/site-lisp/gtags.el
%dir %{_datadir}/gtags
%dir %{_datadir}/gtags/icons
%{_datadir}/gtags/*.dox
%{_datadir}/gtags/elvis-2.2_0.patch
%{_datadir}/gtags/*.pl
%{_datadir}/gtags/*.rc
%{_datadir}/gtags/*.tmpl
%{_datadir}/gtags/*.vim
%{_datadir}/gtags/icons/*
%{_datadir}/gtags/jquery
%{_datadir}/gtags/script
%{_mandir}/man1/global.1*
%{_mandir}/man1/globash.1*
%{_mandir}/man1/gozilla.1*
%{_mandir}/man1/gtags-cscope.1*
%{_mandir}/man1/gtags.1*
%{_mandir}/man1/htags.1*
%{_infodir}/global.info.*
%{_libdir}/gtags/exuberant-ctags.so
%{_libdir}/gtags/user-custom.so
