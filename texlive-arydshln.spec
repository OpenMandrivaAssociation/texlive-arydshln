%global tl_name arydshln
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.76
Release:	%{tl_revision}.1
Summary:	Draw dash-lines in array/tabular
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arydshln
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is to draw dash-lines in array/tabular environments.
Horizontal lines are drawn by \hdashline and \cdashline while vertical
ones can be specified as a part of the preamble using ':'. The shape of
dash-lines may be controlled through style parameters or optional
arguments. The package is compatible with array, colortab, longtable,
and colortbl.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arydshln
%dir %{_datadir}/texmf-dist/source/latex/arydshln
%dir %{_datadir}/texmf-dist/tex/latex/arydshln
%doc %{_datadir}/texmf-dist/doc/latex/arydshln/README
%doc %{_datadir}/texmf-dist/doc/latex/arydshln/arydshln-man.pdf
%doc %{_datadir}/texmf-dist/doc/latex/arydshln/arydshln-man.tex
%doc %{_datadir}/texmf-dist/doc/latex/arydshln/arydshln.pdf
%doc %{_datadir}/texmf-dist/source/latex/arydshln/arydshln.dtx
%doc %{_datadir}/texmf-dist/source/latex/arydshln/arydshln.ins
%{_datadir}/texmf-dist/tex/latex/arydshln/arydshln.sty
