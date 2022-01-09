#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Monadic let-bindings
Summary(pl.UTF-8):	Monadowe wiązania let
Name:		ocaml-ppx_let
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_let/tags
Source0:	https://github.com/janestreet/ppx_let/archive/v%{version}/ppx_let-%{version}.tar.gz
# Source0-md5:	6ded2e26e4207d0c9bf38ee71b4940c7
URL:		https://github.com/janestreet/ppx_let
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx rewriter for monadic and applicative let bindings, match
expressions, and if expressions.

This package contains files needed to run bytecode executables using
ppx_let library.

%description -l pl.UTF-8
Moduł przepisujący ppx do monadowych oraz aplikatywnych wiązań let,
wyrażeń match i wyrażeń if.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_let.

%package devel
Summary:	Monadic let-bindings - development part
Summary(pl.UTF-8):	Monadowe wiązania let - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_let library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_let.

%prep
%setup -q -n ppx_let-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_let/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_let/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_let

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_let
%attr(755,root,root) %{_libdir}/ocaml/ppx_let/ppx.exe
%{_libdir}/ocaml/ppx_let/META
%{_libdir}/ocaml/ppx_let/*.cma
%dir %{_libdir}/ocaml/ppx_let/expander
%{_libdir}/ocaml/ppx_let/expander/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_let/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_let/expander/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_let/*.cmi
%{_libdir}/ocaml/ppx_let/*.cmt
%{_libdir}/ocaml/ppx_let/*.cmti
%{_libdir}/ocaml/ppx_let/*.mli
%{_libdir}/ocaml/ppx_let/expander/*.cmi
%{_libdir}/ocaml/ppx_let/expander/*.cmt
%{_libdir}/ocaml/ppx_let/expander/*.cmti
%{_libdir}/ocaml/ppx_let/expander/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_let/ppx_let.a
%{_libdir}/ocaml/ppx_let/*.cmx
%{_libdir}/ocaml/ppx_let/*.cmxa
%{_libdir}/ocaml/ppx_let/expander/ppx_let_expander.a
%{_libdir}/ocaml/ppx_let/expander/*.cmx
%{_libdir}/ocaml/ppx_let/expander/*.cmxa
%endif
%{_libdir}/ocaml/ppx_let/dune-package
%{_libdir}/ocaml/ppx_let/opam
