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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is to draw dash-lines in array/tabular environments.
Horizontal lines are drawn by \hdashline and \cdashline while vertical
ones can be specified as a part of the preamble using ':'. The shape of
dash-lines may be controlled through style parameters or optional
arguments. The package is compatible with array, colortab, longtable,
and colortbl.

