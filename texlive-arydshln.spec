Name:		texlive-arydshln
Version:	50084
Release:	1
Summary:	Horizontal and vertical dashed lines in arrays and tabulars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arydshln
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Definitions of horizontal and vertical dashed lines for the
array and tabular environment. Horizontal lines are drawn by
\hdashline and \cdashline while vertical ones can be specified
as a part of preamble using ':'. The shape of dashed lines may
be controlled through style parameters or optional arguments.
The package is compatible with array and colortab.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/arydshln/arydshln.sty
%doc %{_texmfdistdir}/doc/latex/arydshln/README
%doc %{_texmfdistdir}/doc/latex/arydshln/arydshln-man.pdf
%doc %{_texmfdistdir}/doc/latex/arydshln/arydshln-man.tex
%doc %{_texmfdistdir}/doc/latex/arydshln/arydshln.pdf
#- source
%doc %{_texmfdistdir}/source/latex/arydshln/arydshln.dtx
%doc %{_texmfdistdir}/source/latex/arydshln/arydshln.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
