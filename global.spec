Summary:	GNU GLOBAL source code tag system for all hackers
Name:		global
Version:	6.6.5
Release:	1
License:	GPLv3
Group:		Development/Other
Url:		https://www.gnu.org/software/global/
Source0:	https://ftp.gnu.org/pub/gnu/global/%{name}-%{version}.tar.gz

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
%autopatch -p1

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
%doc AUTHORS DONORS FAQ
%doc NEWS README THANKS gtags.conf
%license LICENSE COPYING.LIB
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}.el
%config(noreplace) %{_sysconfdir}/gtags.conf
%{_bindir}/global
%{_bindir}/globash
%{_bindir}/gozilla
%{_bindir}/gtags
%{_bindir}/gtags-cscope
%{_bindir}/htags
%{_bindir}/htags-server
%{_datadir}/emacs/site-lisp/gtags.el
%{_datadir}/gtags/COPYING.LIB
%{_datadir}/gtags/PLUGIN_HOWTO
%{_datadir}/gtags/PLUGIN_HOWTO.pygments
%{_datadir}/gtags/README.PATCHES
%{_datadir}/gtags/SERVERSIDE_HOWTO
%{_datadir}/gtags/completion.cgi
%{_datadir}/gtags/dot_htaccess
%{_datadir}/gtags/global.cgi
%{_datadir}/gtags/jscode_suggest
%{_datadir}/gtags/jscode_treeview
%{_datadir}/gtags/style.css
%{_datadir}/gtags/vim74-gtags-cscope.patch
%dir %{_datadir}/gtags
%dir %{_datadir}/gtags/icons
%{_datadir}/gtags/elvis-2.2_0.patch
%{_datadir}/gtags/*.pl
%{_datadir}/gtags/*.rc
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
%{_mandir}/man1/htags-server.1*
%{_mandir}/man5/gtags.conf.5*
%{_infodir}/global.info.*
%{_libdir}/gtags/exuberant-ctags.so
%{_libdir}/gtags/user-custom.so
%{_libdir}/gtags/pygments-parser.so
%{_libdir}/gtags/universal-ctags.so
