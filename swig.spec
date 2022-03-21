#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swig
Version  : 4.0.2
Release  : 25
URL      : https://github.com/swig/swig/archive/rel-4.0.2.tar.gz
Source0  : https://github.com/swig/swig/archive/rel-4.0.2.tar.gz
Summary  : Compiler Cache
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: swig-bin = %{version}-%{release}
Requires: swig-data = %{version}-%{release}
Requires: swig-license = %{version}-%{release}
BuildRequires : R
BuildRequires : bison
BuildRequires : buildreq-golang
BuildRequires : go
BuildRequires : guile-dev
BuildRequires : lua-dev
BuildRequires : nodejs
BuildRequires : openjdk-dev
BuildRequires : pcre-dev
BuildRequires : php-dev
BuildRequires : python3-dev
BuildRequires : ruby-dev
BuildRequires : tcl-dev
BuildRequires : zlib-dev

%description
ccache caches gcc output files

%package bin
Summary: bin components for the swig package.
Group: Binaries
Requires: swig-data = %{version}-%{release}
Requires: swig-license = %{version}-%{release}

%description bin
bin components for the swig package.


%package data
Summary: data components for the swig package.
Group: Data

%description data
data components for the swig package.


%package license
Summary: license components for the swig package.
Group: Default

%description license
license components for the swig package.


%prep
%setup -q -n swig-rel-4.0.2
cd %{_builddir}/swig-rel-4.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647839639
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto -std=gnu++98"
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1647839639
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/swig
cp %{_builddir}/swig-rel-4.0.2/CCache/COPYING %{buildroot}/usr/share/package-licenses/swig/075d599585584bb0e4b526f5c40cb6b17e0da35a
cp %{_builddir}/swig-rel-4.0.2/LICENSE-GPL %{buildroot}/usr/share/package-licenses/swig/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ccache-swig
/usr/bin/swig

%files data
%defattr(-,root,root,-)
/usr/share/swig/4.0.2/allkw.swg
/usr/share/swig/4.0.2/attribute.i
/usr/share/swig/4.0.2/carrays.i
/usr/share/swig/4.0.2/cdata.i
/usr/share/swig/4.0.2/cmalloc.i
/usr/share/swig/4.0.2/constraints.i
/usr/share/swig/4.0.2/cpointer.i
/usr/share/swig/4.0.2/csharp/arrays_csharp.i
/usr/share/swig/4.0.2/csharp/boost_intrusive_ptr.i
/usr/share/swig/4.0.2/csharp/boost_shared_ptr.i
/usr/share/swig/4.0.2/csharp/complex.i
/usr/share/swig/4.0.2/csharp/csharp.swg
/usr/share/swig/4.0.2/csharp/csharphead.swg
/usr/share/swig/4.0.2/csharp/csharpkw.swg
/usr/share/swig/4.0.2/csharp/director.swg
/usr/share/swig/4.0.2/csharp/enums.swg
/usr/share/swig/4.0.2/csharp/enumsimple.swg
/usr/share/swig/4.0.2/csharp/enumtypesafe.swg
/usr/share/swig/4.0.2/csharp/std_array.i
/usr/share/swig/4.0.2/csharp/std_auto_ptr.i
/usr/share/swig/4.0.2/csharp/std_common.i
/usr/share/swig/4.0.2/csharp/std_complex.i
/usr/share/swig/4.0.2/csharp/std_deque.i
/usr/share/swig/4.0.2/csharp/std_except.i
/usr/share/swig/4.0.2/csharp/std_list.i
/usr/share/swig/4.0.2/csharp/std_map.i
/usr/share/swig/4.0.2/csharp/std_pair.i
/usr/share/swig/4.0.2/csharp/std_set.i
/usr/share/swig/4.0.2/csharp/std_shared_ptr.i
/usr/share/swig/4.0.2/csharp/std_string.i
/usr/share/swig/4.0.2/csharp/std_vector.i
/usr/share/swig/4.0.2/csharp/std_wstring.i
/usr/share/swig/4.0.2/csharp/stl.i
/usr/share/swig/4.0.2/csharp/swiginterface.i
/usr/share/swig/4.0.2/csharp/swigtype_inout.i
/usr/share/swig/4.0.2/csharp/typemaps.i
/usr/share/swig/4.0.2/csharp/wchar.i
/usr/share/swig/4.0.2/cstring.i
/usr/share/swig/4.0.2/cwstring.i
/usr/share/swig/4.0.2/d/boost_shared_ptr.i
/usr/share/swig/4.0.2/d/carrays.i
/usr/share/swig/4.0.2/d/cpointer.i
/usr/share/swig/4.0.2/d/d.swg
/usr/share/swig/4.0.2/d/dclassgen.swg
/usr/share/swig/4.0.2/d/ddirectives.swg
/usr/share/swig/4.0.2/d/denums.swg
/usr/share/swig/4.0.2/d/dexception.swg
/usr/share/swig/4.0.2/d/dhead.swg
/usr/share/swig/4.0.2/d/director.swg
/usr/share/swig/4.0.2/d/dkw.swg
/usr/share/swig/4.0.2/d/dmemberfunctionpointers.swg
/usr/share/swig/4.0.2/d/doperators.swg
/usr/share/swig/4.0.2/d/dprimitives.swg
/usr/share/swig/4.0.2/d/dstrings.swg
/usr/share/swig/4.0.2/d/dswigtype.swg
/usr/share/swig/4.0.2/d/dvoid.swg
/usr/share/swig/4.0.2/d/std_common.i
/usr/share/swig/4.0.2/d/std_deque.i
/usr/share/swig/4.0.2/d/std_except.i
/usr/share/swig/4.0.2/d/std_map.i
/usr/share/swig/4.0.2/d/std_pair.i
/usr/share/swig/4.0.2/d/std_shared_ptr.i
/usr/share/swig/4.0.2/d/std_string.i
/usr/share/swig/4.0.2/d/std_vector.i
/usr/share/swig/4.0.2/d/stl.i
/usr/share/swig/4.0.2/d/typemaps.i
/usr/share/swig/4.0.2/d/wrapperloader.swg
/usr/share/swig/4.0.2/director_common.swg
/usr/share/swig/4.0.2/exception.i
/usr/share/swig/4.0.2/go/cdata.i
/usr/share/swig/4.0.2/go/director.swg
/usr/share/swig/4.0.2/go/exception.i
/usr/share/swig/4.0.2/go/go.swg
/usr/share/swig/4.0.2/go/gokw.swg
/usr/share/swig/4.0.2/go/goruntime.swg
/usr/share/swig/4.0.2/go/gostring.swg
/usr/share/swig/4.0.2/go/std_common.i
/usr/share/swig/4.0.2/go/std_deque.i
/usr/share/swig/4.0.2/go/std_except.i
/usr/share/swig/4.0.2/go/std_list.i
/usr/share/swig/4.0.2/go/std_map.i
/usr/share/swig/4.0.2/go/std_pair.i
/usr/share/swig/4.0.2/go/std_string.i
/usr/share/swig/4.0.2/go/std_vector.i
/usr/share/swig/4.0.2/go/stl.i
/usr/share/swig/4.0.2/go/typemaps.i
/usr/share/swig/4.0.2/guile/common.scm
/usr/share/swig/4.0.2/guile/cplusplus.i
/usr/share/swig/4.0.2/guile/guile.i
/usr/share/swig/4.0.2/guile/guile_scm.swg
/usr/share/swig/4.0.2/guile/guile_scm_run.swg
/usr/share/swig/4.0.2/guile/guilemain.i
/usr/share/swig/4.0.2/guile/interpreter.i
/usr/share/swig/4.0.2/guile/list-vector.i
/usr/share/swig/4.0.2/guile/pointer-in-out.i
/usr/share/swig/4.0.2/guile/ports.i
/usr/share/swig/4.0.2/guile/std_common.i
/usr/share/swig/4.0.2/guile/std_deque.i
/usr/share/swig/4.0.2/guile/std_except.i
/usr/share/swig/4.0.2/guile/std_map.i
/usr/share/swig/4.0.2/guile/std_pair.i
/usr/share/swig/4.0.2/guile/std_string.i
/usr/share/swig/4.0.2/guile/std_vector.i
/usr/share/swig/4.0.2/guile/stl.i
/usr/share/swig/4.0.2/guile/swigrun.i
/usr/share/swig/4.0.2/guile/typemaps.i
/usr/share/swig/4.0.2/intrusive_ptr.i
/usr/share/swig/4.0.2/inttypes.i
/usr/share/swig/4.0.2/java/arrays_java.i
/usr/share/swig/4.0.2/java/boost_intrusive_ptr.i
/usr/share/swig/4.0.2/java/boost_shared_ptr.i
/usr/share/swig/4.0.2/java/director.swg
/usr/share/swig/4.0.2/java/enums.swg
/usr/share/swig/4.0.2/java/enumsimple.swg
/usr/share/swig/4.0.2/java/enumtypesafe.swg
/usr/share/swig/4.0.2/java/enumtypeunsafe.swg
/usr/share/swig/4.0.2/java/java.swg
/usr/share/swig/4.0.2/java/javahead.swg
/usr/share/swig/4.0.2/java/javakw.swg
/usr/share/swig/4.0.2/java/std_array.i
/usr/share/swig/4.0.2/java/std_auto_ptr.i
/usr/share/swig/4.0.2/java/std_common.i
/usr/share/swig/4.0.2/java/std_deque.i
/usr/share/swig/4.0.2/java/std_except.i
/usr/share/swig/4.0.2/java/std_list.i
/usr/share/swig/4.0.2/java/std_map.i
/usr/share/swig/4.0.2/java/std_pair.i
/usr/share/swig/4.0.2/java/std_set.i
/usr/share/swig/4.0.2/java/std_shared_ptr.i
/usr/share/swig/4.0.2/java/std_string.i
/usr/share/swig/4.0.2/java/std_unordered_map.i
/usr/share/swig/4.0.2/java/std_unordered_set.i
/usr/share/swig/4.0.2/java/std_vector.i
/usr/share/swig/4.0.2/java/std_wstring.i
/usr/share/swig/4.0.2/java/stl.i
/usr/share/swig/4.0.2/java/swiginterface.i
/usr/share/swig/4.0.2/java/typemaps.i
/usr/share/swig/4.0.2/java/various.i
/usr/share/swig/4.0.2/javascript/jsc/arrays_javascript.i
/usr/share/swig/4.0.2/javascript/jsc/ccomplex.i
/usr/share/swig/4.0.2/javascript/jsc/cdata.i
/usr/share/swig/4.0.2/javascript/jsc/complex.i
/usr/share/swig/4.0.2/javascript/jsc/exception.i
/usr/share/swig/4.0.2/javascript/jsc/javascript.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptcode.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptcomplex.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptfragments.swg
/usr/share/swig/4.0.2/javascript/jsc/javascripthelpers.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptinit.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptkw.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptprimtypes.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptrun.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptruntime.swg
/usr/share/swig/4.0.2/javascript/jsc/javascriptstrings.swg
/usr/share/swig/4.0.2/javascript/jsc/javascripttypemaps.swg
/usr/share/swig/4.0.2/javascript/jsc/std_common.i
/usr/share/swig/4.0.2/javascript/jsc/std_complex.i
/usr/share/swig/4.0.2/javascript/jsc/std_deque.i
/usr/share/swig/4.0.2/javascript/jsc/std_except.i
/usr/share/swig/4.0.2/javascript/jsc/std_map.i
/usr/share/swig/4.0.2/javascript/jsc/std_pair.i
/usr/share/swig/4.0.2/javascript/jsc/std_string.i
/usr/share/swig/4.0.2/javascript/jsc/std_vector.i
/usr/share/swig/4.0.2/javascript/jsc/stl.i
/usr/share/swig/4.0.2/javascript/jsc/typemaps.i
/usr/share/swig/4.0.2/javascript/v8/arrays_javascript.i
/usr/share/swig/4.0.2/javascript/v8/ccomplex.i
/usr/share/swig/4.0.2/javascript/v8/cdata.i
/usr/share/swig/4.0.2/javascript/v8/complex.i
/usr/share/swig/4.0.2/javascript/v8/exception.i
/usr/share/swig/4.0.2/javascript/v8/javascript.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptcode.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptcomplex.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptfragments.swg
/usr/share/swig/4.0.2/javascript/v8/javascripthelpers.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptinit.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptkw.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptprimtypes.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptrun.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptruntime.swg
/usr/share/swig/4.0.2/javascript/v8/javascriptstrings.swg
/usr/share/swig/4.0.2/javascript/v8/javascripttypemaps.swg
/usr/share/swig/4.0.2/javascript/v8/std_common.i
/usr/share/swig/4.0.2/javascript/v8/std_complex.i
/usr/share/swig/4.0.2/javascript/v8/std_deque.i
/usr/share/swig/4.0.2/javascript/v8/std_except.i
/usr/share/swig/4.0.2/javascript/v8/std_map.i
/usr/share/swig/4.0.2/javascript/v8/std_pair.i
/usr/share/swig/4.0.2/javascript/v8/std_string.i
/usr/share/swig/4.0.2/javascript/v8/std_vector.i
/usr/share/swig/4.0.2/javascript/v8/stl.i
/usr/share/swig/4.0.2/javascript/v8/typemaps.i
/usr/share/swig/4.0.2/lua/_std_common.i
/usr/share/swig/4.0.2/lua/carrays.i
/usr/share/swig/4.0.2/lua/factory.i
/usr/share/swig/4.0.2/lua/lua.swg
/usr/share/swig/4.0.2/lua/lua_fnptr.i
/usr/share/swig/4.0.2/lua/luakw.swg
/usr/share/swig/4.0.2/lua/luarun.swg
/usr/share/swig/4.0.2/lua/luaruntime.swg
/usr/share/swig/4.0.2/lua/luatypemaps.swg
/usr/share/swig/4.0.2/lua/std_common.i
/usr/share/swig/4.0.2/lua/std_deque.i
/usr/share/swig/4.0.2/lua/std_except.i
/usr/share/swig/4.0.2/lua/std_map.i
/usr/share/swig/4.0.2/lua/std_pair.i
/usr/share/swig/4.0.2/lua/std_string.i
/usr/share/swig/4.0.2/lua/std_vector.i
/usr/share/swig/4.0.2/lua/stl.i
/usr/share/swig/4.0.2/lua/typemaps.i
/usr/share/swig/4.0.2/lua/wchar.i
/usr/share/swig/4.0.2/math.i
/usr/share/swig/4.0.2/mzscheme/mzrun.swg
/usr/share/swig/4.0.2/mzscheme/mzscheme.swg
/usr/share/swig/4.0.2/mzscheme/std_common.i
/usr/share/swig/4.0.2/mzscheme/std_deque.i
/usr/share/swig/4.0.2/mzscheme/std_map.i
/usr/share/swig/4.0.2/mzscheme/std_pair.i
/usr/share/swig/4.0.2/mzscheme/std_string.i
/usr/share/swig/4.0.2/mzscheme/std_vector.i
/usr/share/swig/4.0.2/mzscheme/stl.i
/usr/share/swig/4.0.2/mzscheme/typemaps.i
/usr/share/swig/4.0.2/ocaml/carray.i
/usr/share/swig/4.0.2/ocaml/class.swg
/usr/share/swig/4.0.2/ocaml/cstring.i
/usr/share/swig/4.0.2/ocaml/director.swg
/usr/share/swig/4.0.2/ocaml/ocaml.i
/usr/share/swig/4.0.2/ocaml/ocaml.swg
/usr/share/swig/4.0.2/ocaml/ocamlkw.swg
/usr/share/swig/4.0.2/ocaml/ocamlrun.swg
/usr/share/swig/4.0.2/ocaml/ocamlrundec.swg
/usr/share/swig/4.0.2/ocaml/preamble.swg
/usr/share/swig/4.0.2/ocaml/std_common.i
/usr/share/swig/4.0.2/ocaml/std_complex.i
/usr/share/swig/4.0.2/ocaml/std_deque.i
/usr/share/swig/4.0.2/ocaml/std_except.i
/usr/share/swig/4.0.2/ocaml/std_list.i
/usr/share/swig/4.0.2/ocaml/std_map.i
/usr/share/swig/4.0.2/ocaml/std_pair.i
/usr/share/swig/4.0.2/ocaml/std_string.i
/usr/share/swig/4.0.2/ocaml/std_vector.i
/usr/share/swig/4.0.2/ocaml/stl.i
/usr/share/swig/4.0.2/ocaml/swig.ml
/usr/share/swig/4.0.2/ocaml/swig.mli
/usr/share/swig/4.0.2/ocaml/swigp4.ml
/usr/share/swig/4.0.2/ocaml/typecheck.i
/usr/share/swig/4.0.2/ocaml/typemaps.i
/usr/share/swig/4.0.2/ocaml/typeregister.swg
/usr/share/swig/4.0.2/octave/attribute.i
/usr/share/swig/4.0.2/octave/boost_shared_ptr.i
/usr/share/swig/4.0.2/octave/carrays.i
/usr/share/swig/4.0.2/octave/cdata.i
/usr/share/swig/4.0.2/octave/cmalloc.i
/usr/share/swig/4.0.2/octave/director.swg
/usr/share/swig/4.0.2/octave/exception.i
/usr/share/swig/4.0.2/octave/factory.i
/usr/share/swig/4.0.2/octave/implicit.i
/usr/share/swig/4.0.2/octave/octave.swg
/usr/share/swig/4.0.2/octave/octcomplex.swg
/usr/share/swig/4.0.2/octave/octcontainer.swg
/usr/share/swig/4.0.2/octave/octfragments.swg
/usr/share/swig/4.0.2/octave/octheaders.hpp
/usr/share/swig/4.0.2/octave/octiterators.swg
/usr/share/swig/4.0.2/octave/octopers.swg
/usr/share/swig/4.0.2/octave/octprimtypes.swg
/usr/share/swig/4.0.2/octave/octrun.swg
/usr/share/swig/4.0.2/octave/octruntime.swg
/usr/share/swig/4.0.2/octave/octstdcommon.swg
/usr/share/swig/4.0.2/octave/octtypemaps.swg
/usr/share/swig/4.0.2/octave/octuserdir.swg
/usr/share/swig/4.0.2/octave/std_alloc.i
/usr/share/swig/4.0.2/octave/std_basic_string.i
/usr/share/swig/4.0.2/octave/std_carray.i
/usr/share/swig/4.0.2/octave/std_char_traits.i
/usr/share/swig/4.0.2/octave/std_common.i
/usr/share/swig/4.0.2/octave/std_complex.i
/usr/share/swig/4.0.2/octave/std_container.i
/usr/share/swig/4.0.2/octave/std_deque.i
/usr/share/swig/4.0.2/octave/std_except.i
/usr/share/swig/4.0.2/octave/std_list.i
/usr/share/swig/4.0.2/octave/std_map.i
/usr/share/swig/4.0.2/octave/std_pair.i
/usr/share/swig/4.0.2/octave/std_shared_ptr.i
/usr/share/swig/4.0.2/octave/std_string.i
/usr/share/swig/4.0.2/octave/std_vector.i
/usr/share/swig/4.0.2/octave/std_wstring.i
/usr/share/swig/4.0.2/octave/stl.i
/usr/share/swig/4.0.2/octave/typemaps.i
/usr/share/swig/4.0.2/perl5/Makefile.pl
/usr/share/swig/4.0.2/perl5/attribute.i
/usr/share/swig/4.0.2/perl5/carrays.i
/usr/share/swig/4.0.2/perl5/cdata.i
/usr/share/swig/4.0.2/perl5/cmalloc.i
/usr/share/swig/4.0.2/perl5/cpointer.i
/usr/share/swig/4.0.2/perl5/cstring.i
/usr/share/swig/4.0.2/perl5/director.swg
/usr/share/swig/4.0.2/perl5/exception.i
/usr/share/swig/4.0.2/perl5/factory.i
/usr/share/swig/4.0.2/perl5/noembed.h
/usr/share/swig/4.0.2/perl5/perl5.swg
/usr/share/swig/4.0.2/perl5/perlerrors.swg
/usr/share/swig/4.0.2/perl5/perlfragments.swg
/usr/share/swig/4.0.2/perl5/perlhead.swg
/usr/share/swig/4.0.2/perl5/perlinit.swg
/usr/share/swig/4.0.2/perl5/perlkw.swg
/usr/share/swig/4.0.2/perl5/perlmacros.swg
/usr/share/swig/4.0.2/perl5/perlmain.i
/usr/share/swig/4.0.2/perl5/perlopers.swg
/usr/share/swig/4.0.2/perl5/perlprimtypes.swg
/usr/share/swig/4.0.2/perl5/perlrun.swg
/usr/share/swig/4.0.2/perl5/perlruntime.swg
/usr/share/swig/4.0.2/perl5/perlstrings.swg
/usr/share/swig/4.0.2/perl5/perltypemaps.swg
/usr/share/swig/4.0.2/perl5/perluserdir.swg
/usr/share/swig/4.0.2/perl5/reference.i
/usr/share/swig/4.0.2/perl5/std_common.i
/usr/share/swig/4.0.2/perl5/std_deque.i
/usr/share/swig/4.0.2/perl5/std_except.i
/usr/share/swig/4.0.2/perl5/std_list.i
/usr/share/swig/4.0.2/perl5/std_map.i
/usr/share/swig/4.0.2/perl5/std_pair.i
/usr/share/swig/4.0.2/perl5/std_string.i
/usr/share/swig/4.0.2/perl5/std_vector.i
/usr/share/swig/4.0.2/perl5/stl.i
/usr/share/swig/4.0.2/perl5/typemaps.i
/usr/share/swig/4.0.2/php/const.i
/usr/share/swig/4.0.2/php/director.swg
/usr/share/swig/4.0.2/php/factory.i
/usr/share/swig/4.0.2/php/globalvar.i
/usr/share/swig/4.0.2/php/php.swg
/usr/share/swig/4.0.2/php/phpinit.swg
/usr/share/swig/4.0.2/php/phpkw.swg
/usr/share/swig/4.0.2/php/phppointers.i
/usr/share/swig/4.0.2/php/phprun.swg
/usr/share/swig/4.0.2/php/std_common.i
/usr/share/swig/4.0.2/php/std_deque.i
/usr/share/swig/4.0.2/php/std_map.i
/usr/share/swig/4.0.2/php/std_pair.i
/usr/share/swig/4.0.2/php/std_string.i
/usr/share/swig/4.0.2/php/std_vector.i
/usr/share/swig/4.0.2/php/stl.i
/usr/share/swig/4.0.2/php/typemaps.i
/usr/share/swig/4.0.2/php/utils.i
/usr/share/swig/4.0.2/pointer.i
/usr/share/swig/4.0.2/python/argcargv.i
/usr/share/swig/4.0.2/python/attribute.i
/usr/share/swig/4.0.2/python/boost_shared_ptr.i
/usr/share/swig/4.0.2/python/builtin.swg
/usr/share/swig/4.0.2/python/carrays.i
/usr/share/swig/4.0.2/python/ccomplex.i
/usr/share/swig/4.0.2/python/cdata.i
/usr/share/swig/4.0.2/python/cmalloc.i
/usr/share/swig/4.0.2/python/complex.i
/usr/share/swig/4.0.2/python/cpointer.i
/usr/share/swig/4.0.2/python/cstring.i
/usr/share/swig/4.0.2/python/cwstring.i
/usr/share/swig/4.0.2/python/defarg.swg
/usr/share/swig/4.0.2/python/director.swg
/usr/share/swig/4.0.2/python/embed.i
/usr/share/swig/4.0.2/python/exception.i
/usr/share/swig/4.0.2/python/factory.i
/usr/share/swig/4.0.2/python/file.i
/usr/share/swig/4.0.2/python/implicit.i
/usr/share/swig/4.0.2/python/pyabc.i
/usr/share/swig/4.0.2/python/pyapi.swg
/usr/share/swig/4.0.2/python/pybackward.swg
/usr/share/swig/4.0.2/python/pybuffer.i
/usr/share/swig/4.0.2/python/pyclasses.swg
/usr/share/swig/4.0.2/python/pycomplex.swg
/usr/share/swig/4.0.2/python/pycontainer.swg
/usr/share/swig/4.0.2/python/pydocs.swg
/usr/share/swig/4.0.2/python/pyerrors.swg
/usr/share/swig/4.0.2/python/pyfragments.swg
/usr/share/swig/4.0.2/python/pyhead.swg
/usr/share/swig/4.0.2/python/pyinit.swg
/usr/share/swig/4.0.2/python/pyiterators.swg
/usr/share/swig/4.0.2/python/pymacros.swg
/usr/share/swig/4.0.2/python/pyname_compat.i
/usr/share/swig/4.0.2/python/pyopers.swg
/usr/share/swig/4.0.2/python/pyprimtypes.swg
/usr/share/swig/4.0.2/python/pyrun.swg
/usr/share/swig/4.0.2/python/pyruntime.swg
/usr/share/swig/4.0.2/python/pystdcommon.swg
/usr/share/swig/4.0.2/python/pystrings.swg
/usr/share/swig/4.0.2/python/python.swg
/usr/share/swig/4.0.2/python/pythonkw.swg
/usr/share/swig/4.0.2/python/pythreads.swg
/usr/share/swig/4.0.2/python/pytuplehlp.swg
/usr/share/swig/4.0.2/python/pytypemaps.swg
/usr/share/swig/4.0.2/python/pyuserdir.swg
/usr/share/swig/4.0.2/python/pywstrings.swg
/usr/share/swig/4.0.2/python/std_alloc.i
/usr/share/swig/4.0.2/python/std_array.i
/usr/share/swig/4.0.2/python/std_auto_ptr.i
/usr/share/swig/4.0.2/python/std_basic_string.i
/usr/share/swig/4.0.2/python/std_carray.i
/usr/share/swig/4.0.2/python/std_char_traits.i
/usr/share/swig/4.0.2/python/std_common.i
/usr/share/swig/4.0.2/python/std_complex.i
/usr/share/swig/4.0.2/python/std_container.i
/usr/share/swig/4.0.2/python/std_deque.i
/usr/share/swig/4.0.2/python/std_except.i
/usr/share/swig/4.0.2/python/std_ios.i
/usr/share/swig/4.0.2/python/std_iostream.i
/usr/share/swig/4.0.2/python/std_list.i
/usr/share/swig/4.0.2/python/std_map.i
/usr/share/swig/4.0.2/python/std_multimap.i
/usr/share/swig/4.0.2/python/std_multiset.i
/usr/share/swig/4.0.2/python/std_pair.i
/usr/share/swig/4.0.2/python/std_set.i
/usr/share/swig/4.0.2/python/std_shared_ptr.i
/usr/share/swig/4.0.2/python/std_sstream.i
/usr/share/swig/4.0.2/python/std_streambuf.i
/usr/share/swig/4.0.2/python/std_string.i
/usr/share/swig/4.0.2/python/std_unordered_map.i
/usr/share/swig/4.0.2/python/std_unordered_multimap.i
/usr/share/swig/4.0.2/python/std_unordered_multiset.i
/usr/share/swig/4.0.2/python/std_unordered_set.i
/usr/share/swig/4.0.2/python/std_vector.i
/usr/share/swig/4.0.2/python/std_vectora.i
/usr/share/swig/4.0.2/python/std_wios.i
/usr/share/swig/4.0.2/python/std_wiostream.i
/usr/share/swig/4.0.2/python/std_wsstream.i
/usr/share/swig/4.0.2/python/std_wstreambuf.i
/usr/share/swig/4.0.2/python/std_wstring.i
/usr/share/swig/4.0.2/python/stl.i
/usr/share/swig/4.0.2/python/typemaps.i
/usr/share/swig/4.0.2/python/wchar.i
/usr/share/swig/4.0.2/r/boost_shared_ptr.i
/usr/share/swig/4.0.2/r/cdata.i
/usr/share/swig/4.0.2/r/exception.i
/usr/share/swig/4.0.2/r/r.swg
/usr/share/swig/4.0.2/r/rcontainer.swg
/usr/share/swig/4.0.2/r/rfragments.swg
/usr/share/swig/4.0.2/r/rkw.swg
/usr/share/swig/4.0.2/r/ropers.swg
/usr/share/swig/4.0.2/r/rrun.swg
/usr/share/swig/4.0.2/r/rstdcommon.swg
/usr/share/swig/4.0.2/r/rtype.swg
/usr/share/swig/4.0.2/r/srun.swg
/usr/share/swig/4.0.2/r/std_alloc.i
/usr/share/swig/4.0.2/r/std_common.i
/usr/share/swig/4.0.2/r/std_container.i
/usr/share/swig/4.0.2/r/std_deque.i
/usr/share/swig/4.0.2/r/std_except.i
/usr/share/swig/4.0.2/r/std_list.i
/usr/share/swig/4.0.2/r/std_map.i
/usr/share/swig/4.0.2/r/std_pair.i
/usr/share/swig/4.0.2/r/std_shared_ptr.i
/usr/share/swig/4.0.2/r/std_string.i
/usr/share/swig/4.0.2/r/std_vector.i
/usr/share/swig/4.0.2/r/stl.i
/usr/share/swig/4.0.2/r/typemaps.i
/usr/share/swig/4.0.2/ruby/Makefile.swig
/usr/share/swig/4.0.2/ruby/argcargv.i
/usr/share/swig/4.0.2/ruby/attribute.i
/usr/share/swig/4.0.2/ruby/boost_shared_ptr.i
/usr/share/swig/4.0.2/ruby/carrays.i
/usr/share/swig/4.0.2/ruby/cdata.i
/usr/share/swig/4.0.2/ruby/cmalloc.i
/usr/share/swig/4.0.2/ruby/cpointer.i
/usr/share/swig/4.0.2/ruby/cstring.i
/usr/share/swig/4.0.2/ruby/director.swg
/usr/share/swig/4.0.2/ruby/embed.i
/usr/share/swig/4.0.2/ruby/exception.i
/usr/share/swig/4.0.2/ruby/extconf.rb
/usr/share/swig/4.0.2/ruby/factory.i
/usr/share/swig/4.0.2/ruby/file.i
/usr/share/swig/4.0.2/ruby/progargcargv.i
/usr/share/swig/4.0.2/ruby/ruby.swg
/usr/share/swig/4.0.2/ruby/rubyapi.swg
/usr/share/swig/4.0.2/ruby/rubyautodoc.swg
/usr/share/swig/4.0.2/ruby/rubyclasses.swg
/usr/share/swig/4.0.2/ruby/rubycomplex.swg
/usr/share/swig/4.0.2/ruby/rubycontainer.swg
/usr/share/swig/4.0.2/ruby/rubycontainer_extended.swg
/usr/share/swig/4.0.2/ruby/rubydef.swg
/usr/share/swig/4.0.2/ruby/rubyerrors.swg
/usr/share/swig/4.0.2/ruby/rubyfragments.swg
/usr/share/swig/4.0.2/ruby/rubyhead.swg
/usr/share/swig/4.0.2/ruby/rubyinit.swg
/usr/share/swig/4.0.2/ruby/rubyiterators.swg
/usr/share/swig/4.0.2/ruby/rubykw.swg
/usr/share/swig/4.0.2/ruby/rubymacros.swg
/usr/share/swig/4.0.2/ruby/rubyopers.swg
/usr/share/swig/4.0.2/ruby/rubyprimtypes.swg
/usr/share/swig/4.0.2/ruby/rubyrun.swg
/usr/share/swig/4.0.2/ruby/rubyruntime.swg
/usr/share/swig/4.0.2/ruby/rubystdautodoc.swg
/usr/share/swig/4.0.2/ruby/rubystdcommon.swg
/usr/share/swig/4.0.2/ruby/rubystdcommon_forward.swg
/usr/share/swig/4.0.2/ruby/rubystdfunctors.swg
/usr/share/swig/4.0.2/ruby/rubystrings.swg
/usr/share/swig/4.0.2/ruby/rubytracking.swg
/usr/share/swig/4.0.2/ruby/rubytypemaps.swg
/usr/share/swig/4.0.2/ruby/rubyuserdir.swg
/usr/share/swig/4.0.2/ruby/rubywstrings.swg
/usr/share/swig/4.0.2/ruby/std_alloc.i
/usr/share/swig/4.0.2/ruby/std_array.i
/usr/share/swig/4.0.2/ruby/std_auto_ptr.i
/usr/share/swig/4.0.2/ruby/std_basic_string.i
/usr/share/swig/4.0.2/ruby/std_char_traits.i
/usr/share/swig/4.0.2/ruby/std_common.i
/usr/share/swig/4.0.2/ruby/std_complex.i
/usr/share/swig/4.0.2/ruby/std_container.i
/usr/share/swig/4.0.2/ruby/std_deque.i
/usr/share/swig/4.0.2/ruby/std_except.i
/usr/share/swig/4.0.2/ruby/std_functors.i
/usr/share/swig/4.0.2/ruby/std_ios.i
/usr/share/swig/4.0.2/ruby/std_iostream.i
/usr/share/swig/4.0.2/ruby/std_list.i
/usr/share/swig/4.0.2/ruby/std_map.i
/usr/share/swig/4.0.2/ruby/std_multimap.i
/usr/share/swig/4.0.2/ruby/std_multiset.i
/usr/share/swig/4.0.2/ruby/std_pair.i
/usr/share/swig/4.0.2/ruby/std_queue.i
/usr/share/swig/4.0.2/ruby/std_set.i
/usr/share/swig/4.0.2/ruby/std_shared_ptr.i
/usr/share/swig/4.0.2/ruby/std_sstream.i
/usr/share/swig/4.0.2/ruby/std_stack.i
/usr/share/swig/4.0.2/ruby/std_streambuf.i
/usr/share/swig/4.0.2/ruby/std_string.i
/usr/share/swig/4.0.2/ruby/std_unordered_map.i
/usr/share/swig/4.0.2/ruby/std_unordered_multimap.i
/usr/share/swig/4.0.2/ruby/std_unordered_multiset.i
/usr/share/swig/4.0.2/ruby/std_unordered_set.i
/usr/share/swig/4.0.2/ruby/std_vector.i
/usr/share/swig/4.0.2/ruby/std_vectora.i
/usr/share/swig/4.0.2/ruby/std_wstring.i
/usr/share/swig/4.0.2/ruby/stl.i
/usr/share/swig/4.0.2/ruby/timeval.i
/usr/share/swig/4.0.2/ruby/typemaps.i
/usr/share/swig/4.0.2/runtime.swg
/usr/share/swig/4.0.2/scilab/boost_shared_ptr.i
/usr/share/swig/4.0.2/scilab/carrays.i
/usr/share/swig/4.0.2/scilab/cmalloc.i
/usr/share/swig/4.0.2/scilab/cpointer.i
/usr/share/swig/4.0.2/scilab/exception.i
/usr/share/swig/4.0.2/scilab/matrix.i
/usr/share/swig/4.0.2/scilab/sciarray.swg
/usr/share/swig/4.0.2/scilab/scibool.swg
/usr/share/swig/4.0.2/scilab/scichar.swg
/usr/share/swig/4.0.2/scilab/scicontainer.swg
/usr/share/swig/4.0.2/scilab/scidouble.swg
/usr/share/swig/4.0.2/scilab/scienum.swg
/usr/share/swig/4.0.2/scilab/sciexception.swg
/usr/share/swig/4.0.2/scilab/scifloat.swg
/usr/share/swig/4.0.2/scilab/sciint.swg
/usr/share/swig/4.0.2/scilab/sciiterators.swg
/usr/share/swig/4.0.2/scilab/scilab.swg
/usr/share/swig/4.0.2/scilab/scilist.swg
/usr/share/swig/4.0.2/scilab/scilong.swg
/usr/share/swig/4.0.2/scilab/scilonglong.swg
/usr/share/swig/4.0.2/scilab/scimacros.swg
/usr/share/swig/4.0.2/scilab/scimatrixbool.swg
/usr/share/swig/4.0.2/scilab/scimatrixchar.swg
/usr/share/swig/4.0.2/scilab/scimatrixdouble.swg
/usr/share/swig/4.0.2/scilab/scimatrixint.swg
/usr/share/swig/4.0.2/scilab/scimisctypes.swg
/usr/share/swig/4.0.2/scilab/scipointer.swg
/usr/share/swig/4.0.2/scilab/sciprimtypes.swg
/usr/share/swig/4.0.2/scilab/scirun.swg
/usr/share/swig/4.0.2/scilab/sciruntime.swg
/usr/share/swig/4.0.2/scilab/scisequence.swg
/usr/share/swig/4.0.2/scilab/scisequencebool.swg
/usr/share/swig/4.0.2/scilab/scisequencedouble.swg
/usr/share/swig/4.0.2/scilab/scisequencefloat.swg
/usr/share/swig/4.0.2/scilab/scisequenceint.swg
/usr/share/swig/4.0.2/scilab/scisequencepointer.swg
/usr/share/swig/4.0.2/scilab/scisequencestring.swg
/usr/share/swig/4.0.2/scilab/scishort.swg
/usr/share/swig/4.0.2/scilab/scisignedchar.swg
/usr/share/swig/4.0.2/scilab/scistdcommon.swg
/usr/share/swig/4.0.2/scilab/scitypemaps.swg
/usr/share/swig/4.0.2/scilab/sciunsignedchar.swg
/usr/share/swig/4.0.2/scilab/sciunsignedint.swg
/usr/share/swig/4.0.2/scilab/sciunsignedlong.swg
/usr/share/swig/4.0.2/scilab/sciunsignedshort.swg
/usr/share/swig/4.0.2/scilab/std_alloc.i
/usr/share/swig/4.0.2/scilab/std_basic_string.i
/usr/share/swig/4.0.2/scilab/std_char_traits.i
/usr/share/swig/4.0.2/scilab/std_common.i
/usr/share/swig/4.0.2/scilab/std_container.i
/usr/share/swig/4.0.2/scilab/std_deque.i
/usr/share/swig/4.0.2/scilab/std_except.i
/usr/share/swig/4.0.2/scilab/std_list.i
/usr/share/swig/4.0.2/scilab/std_map.i
/usr/share/swig/4.0.2/scilab/std_multiset.i
/usr/share/swig/4.0.2/scilab/std_pair.i
/usr/share/swig/4.0.2/scilab/std_set.i
/usr/share/swig/4.0.2/scilab/std_shared_ptr.i
/usr/share/swig/4.0.2/scilab/std_string.i
/usr/share/swig/4.0.2/scilab/std_vector.i
/usr/share/swig/4.0.2/scilab/stl.i
/usr/share/swig/4.0.2/scilab/typemaps.i
/usr/share/swig/4.0.2/shared_ptr.i
/usr/share/swig/4.0.2/std/_std_deque.i
/usr/share/swig/4.0.2/std/std_alloc.i
/usr/share/swig/4.0.2/std/std_array.i
/usr/share/swig/4.0.2/std/std_basic_string.i
/usr/share/swig/4.0.2/std/std_carray.swg
/usr/share/swig/4.0.2/std/std_char_traits.i
/usr/share/swig/4.0.2/std/std_common.i
/usr/share/swig/4.0.2/std/std_container.i
/usr/share/swig/4.0.2/std/std_deque.i
/usr/share/swig/4.0.2/std/std_except.i
/usr/share/swig/4.0.2/std/std_ios.i
/usr/share/swig/4.0.2/std/std_iostream.i
/usr/share/swig/4.0.2/std/std_list.i
/usr/share/swig/4.0.2/std/std_map.i
/usr/share/swig/4.0.2/std/std_multimap.i
/usr/share/swig/4.0.2/std/std_multiset.i
/usr/share/swig/4.0.2/std/std_pair.i
/usr/share/swig/4.0.2/std/std_queue.i
/usr/share/swig/4.0.2/std/std_set.i
/usr/share/swig/4.0.2/std/std_sstream.i
/usr/share/swig/4.0.2/std/std_stack.i
/usr/share/swig/4.0.2/std/std_streambuf.i
/usr/share/swig/4.0.2/std/std_string.i
/usr/share/swig/4.0.2/std/std_unordered_map.i
/usr/share/swig/4.0.2/std/std_unordered_multimap.i
/usr/share/swig/4.0.2/std/std_unordered_multiset.i
/usr/share/swig/4.0.2/std/std_unordered_set.i
/usr/share/swig/4.0.2/std/std_vector.i
/usr/share/swig/4.0.2/std/std_vectora.i
/usr/share/swig/4.0.2/std/std_wios.i
/usr/share/swig/4.0.2/std/std_wiostream.i
/usr/share/swig/4.0.2/std/std_wsstream.i
/usr/share/swig/4.0.2/std/std_wstreambuf.i
/usr/share/swig/4.0.2/std/std_wstring.i
/usr/share/swig/4.0.2/std_except.i
/usr/share/swig/4.0.2/stdint.i
/usr/share/swig/4.0.2/stl.i
/usr/share/swig/4.0.2/swig.swg
/usr/share/swig/4.0.2/swigarch.i
/usr/share/swig/4.0.2/swigerrors.swg
/usr/share/swig/4.0.2/swigfragments.swg
/usr/share/swig/4.0.2/swiginit.swg
/usr/share/swig/4.0.2/swiglabels.swg
/usr/share/swig/4.0.2/swigrun.i
/usr/share/swig/4.0.2/swigrun.swg
/usr/share/swig/4.0.2/swigwarn.swg
/usr/share/swig/4.0.2/swigwarnings.swg
/usr/share/swig/4.0.2/tcl/attribute.i
/usr/share/swig/4.0.2/tcl/carrays.i
/usr/share/swig/4.0.2/tcl/cdata.i
/usr/share/swig/4.0.2/tcl/cmalloc.i
/usr/share/swig/4.0.2/tcl/cpointer.i
/usr/share/swig/4.0.2/tcl/cstring.i
/usr/share/swig/4.0.2/tcl/cwstring.i
/usr/share/swig/4.0.2/tcl/exception.i
/usr/share/swig/4.0.2/tcl/factory.i
/usr/share/swig/4.0.2/tcl/std_common.i
/usr/share/swig/4.0.2/tcl/std_deque.i
/usr/share/swig/4.0.2/tcl/std_except.i
/usr/share/swig/4.0.2/tcl/std_map.i
/usr/share/swig/4.0.2/tcl/std_pair.i
/usr/share/swig/4.0.2/tcl/std_string.i
/usr/share/swig/4.0.2/tcl/std_vector.i
/usr/share/swig/4.0.2/tcl/std_wstring.i
/usr/share/swig/4.0.2/tcl/stl.i
/usr/share/swig/4.0.2/tcl/tcl8.swg
/usr/share/swig/4.0.2/tcl/tclapi.swg
/usr/share/swig/4.0.2/tcl/tclerrors.swg
/usr/share/swig/4.0.2/tcl/tclfragments.swg
/usr/share/swig/4.0.2/tcl/tclinit.swg
/usr/share/swig/4.0.2/tcl/tclinterp.i
/usr/share/swig/4.0.2/tcl/tclkw.swg
/usr/share/swig/4.0.2/tcl/tclmacros.swg
/usr/share/swig/4.0.2/tcl/tclopers.swg
/usr/share/swig/4.0.2/tcl/tclprimtypes.swg
/usr/share/swig/4.0.2/tcl/tclresult.i
/usr/share/swig/4.0.2/tcl/tclrun.swg
/usr/share/swig/4.0.2/tcl/tclruntime.swg
/usr/share/swig/4.0.2/tcl/tclsh.i
/usr/share/swig/4.0.2/tcl/tclstrings.swg
/usr/share/swig/4.0.2/tcl/tcltypemaps.swg
/usr/share/swig/4.0.2/tcl/tcluserdir.swg
/usr/share/swig/4.0.2/tcl/tclwstrings.swg
/usr/share/swig/4.0.2/tcl/typemaps.i
/usr/share/swig/4.0.2/tcl/wish.i
/usr/share/swig/4.0.2/typemaps/attribute.swg
/usr/share/swig/4.0.2/typemaps/carrays.swg
/usr/share/swig/4.0.2/typemaps/cdata.swg
/usr/share/swig/4.0.2/typemaps/cmalloc.swg
/usr/share/swig/4.0.2/typemaps/cpointer.swg
/usr/share/swig/4.0.2/typemaps/cstring.swg
/usr/share/swig/4.0.2/typemaps/cstrings.swg
/usr/share/swig/4.0.2/typemaps/cwstring.swg
/usr/share/swig/4.0.2/typemaps/enumint.swg
/usr/share/swig/4.0.2/typemaps/exception.swg
/usr/share/swig/4.0.2/typemaps/factory.swg
/usr/share/swig/4.0.2/typemaps/fragments.swg
/usr/share/swig/4.0.2/typemaps/implicit.swg
/usr/share/swig/4.0.2/typemaps/inoutlist.swg
/usr/share/swig/4.0.2/typemaps/misctypes.swg
/usr/share/swig/4.0.2/typemaps/primtypes.swg
/usr/share/swig/4.0.2/typemaps/ptrtypes.swg
/usr/share/swig/4.0.2/typemaps/std_except.swg
/usr/share/swig/4.0.2/typemaps/std_string.swg
/usr/share/swig/4.0.2/typemaps/std_strings.swg
/usr/share/swig/4.0.2/typemaps/std_wstring.swg
/usr/share/swig/4.0.2/typemaps/string.swg
/usr/share/swig/4.0.2/typemaps/strings.swg
/usr/share/swig/4.0.2/typemaps/swigmacros.swg
/usr/share/swig/4.0.2/typemaps/swigobject.swg
/usr/share/swig/4.0.2/typemaps/swigtype.swg
/usr/share/swig/4.0.2/typemaps/swigtypemaps.swg
/usr/share/swig/4.0.2/typemaps/typemaps.swg
/usr/share/swig/4.0.2/typemaps/valtypes.swg
/usr/share/swig/4.0.2/typemaps/void.swg
/usr/share/swig/4.0.2/typemaps/wstring.swg
/usr/share/swig/4.0.2/wchar.i
/usr/share/swig/4.0.2/windows.i
/usr/share/swig/4.0.2/xml/typemaps.i
/usr/share/swig/4.0.2/xml/xml.swg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swig/075d599585584bb0e4b526f5c40cb6b17e0da35a
/usr/share/package-licenses/swig/8624bcdae55baeef00cd11d5dfcfa60f68710a02
