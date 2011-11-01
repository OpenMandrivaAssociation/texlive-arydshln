Name:		texlive-arydshln
Version:	1.71
Release:	1
Summary:	Horizontal and vertical dashed lines in arrays and tabulars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arydshln
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Definitions of horizontal and vertical dashed lines for the
array and tabular environment. Horizontal lines are drawn by
\hdashline and \cdashline while vertical ones can be specified
as a part of preamble using ':'. The shape of dashed lines may
be controlled through style parameters or optional arguments.
The package is compatible with array and colortab.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
