%global tl_name interactiveworkbook
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX-based interactive PDF on the Web
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/interactiveworkbook
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package interactiveworkbook gives the user the ability to write
LaTeX documents which, ultimately, create interactive question-and-
answer Portable Document Format (PDF) tutorials meant to be used by
Internet students and that, in particular, freely use mathematical
notation.

