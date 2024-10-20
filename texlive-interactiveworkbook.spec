Name:		texlive-interactiveworkbook
Version:	15878
Release:	2
Summary:	latex-based interactive PDF on the web
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/interactiveworkbook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package interactiveworkbook gives the user the ability to
write LaTeX documents which, ultimately, create interactive
question-and-answer Portable Document Format (PDF) tutorials
meant to be used by Internet students and that, in particular,
freely use mathematical notation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/interactiveworkbook
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
