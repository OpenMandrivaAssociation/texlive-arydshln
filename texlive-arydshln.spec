# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/arydshln
# catalog-date 2007-04-06 18:29:05 +0200
# catalog-license lppl
# catalog-version 1.71
Name:		texlive-arydshln
Version:	1.71
Release:	7
Summary:	Horizontal and vertical dashed lines in arrays and tabulars
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arydshln
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arydshln.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.71-2
+ Revision: 749350
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.71-1
+ Revision: 717857
- texlive-arydshln
- texlive-arydshln
- texlive-arydshln
- texlive-arydshln
- texlive-arydshln

