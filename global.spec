Name:    global
Version: 5.7.5
Release: %mkrel 2
Summary: GNU GLOBAL source code tag system for all hackers
Source0: http://tamacom.com/global/%{name}-%{version}.tar.gz
Patch0:  global-5.7.5-fix-str-fmt.patch
License: GPLv3
Group:   Development/Other
Url:     http://www.gnu.org/software/global/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post): info-install
Requires(preun): info-install


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
%patch0 -p1


%build
%configure2_5x
%make


%install
rm -rf %{buildroot}
%makeinstall_std
install -d %{buildroot}%_datadir/emacs/site-lisp
mv %{buildroot}%_datadir/gtags/gtags.el %{buildroot}%_datadir/emacs/site-lisp/
install -d %{buildroot}%_sysconfdir/emacs/site-start.d
cat <<EOF >%{buildroot}%_sysconfdir/emacs/site-start.d/%name.el
(autoload 'gtags-mode "gtags" "GNU GLOBAL tags mode." t) ;;;'
EOF

pushd %{buildroot}%_datadir/gtags/
rm -f AUTHORS BOKIN_MODEL BOKIN_MODEL_FAQ COPYING ChangeLog DONORS \
      FAQ INSTALL LICENSE NEWS README THANKS gtags.conf
popd
# at least Lynx can work with *.html.gz, not with .ghtml
sed -e 's/gzipped_suffix=ghtml/gzipped_suffix=html.gz/' <gtags.conf >%{buildroot}%_sysconfdir/gtags.conf


%clean
rm -rf %{buildroot}


%post
%_install_info %name.info

%preun
%_remove_install_info %name.info


%files
%defattr(-,root,root)
%doc AUTHORS BOKIN_MODEL BOKIN_MODEL_FAQ COPYING ChangeLog DONORS FAQ
%doc INSTALL LICENSE NEWS README THANKS gtags.conf
%_bindir/global
%_bindir/gozilla
%_bindir/gtags
%_bindir/gtags-cscope
%_bindir/gtags-parser
%_bindir/htags
%_mandir/man1/global.1.*
%_mandir/man1/gozilla.1.*
%_mandir/man1/gtags-cscope.1.*
%_mandir/man1/gtags-parser.1.*
%_mandir/man1/gtags.1.*
%_mandir/man1/htags.1.*
%_infodir/global.info.lzma
%config(noreplace) %_sysconfdir/emacs/site-start.d/%name.el
%config(noreplace) %_sysconfdir/gtags.conf
%_datadir/emacs/site-lisp/gtags.el
%dir %_datadir/gtags
%_datadir/gtags/bless.sh.tmpl
%_datadir/gtags/global.cgi.tmpl
%_datadir/gtags/ghtml.cgi.tmpl
%_datadir/gtags/globash.rc
%_datadir/gtags/gtags.pl
%_datadir/gtags/gtags.vim
%_datadir/gtags/icons/*
%_datadir/gtags/style.css

