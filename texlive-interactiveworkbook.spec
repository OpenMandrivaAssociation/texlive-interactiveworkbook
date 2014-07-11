# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/interactiveworkbook
# catalog-date 2006-10-06 13:44:13 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-interactiveworkbook
Version:	20061006
Release:	8
Summary:	latex-based interactive PDF on the web
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/interactiveworkbook
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/interactiveworkbook.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/interactiveworkbook/interactiveworkbook-web.sty
%{_texmfdistdir}/tex/latex/interactiveworkbook/interactiveworkbook.sty
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/documentation/interactiveworkbookmanual.tex
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/WS_FTP.LOG
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/buttonappearance.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/checkclear.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/checksubmit.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques1.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques10.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques11.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques12.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques13.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques14.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques15.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques16.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques17.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques18.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques19.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques2.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques20.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques3.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques4.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques5.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques6.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques7.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques8.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/exerques9.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/fieldclear.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/fieldsubmit.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/ndex.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/next.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonecheckthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonechecktwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonefieldtwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopupthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageonepopuptwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiofive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiofour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradioone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiothree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pageoneradiotwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreecheckthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreechecktwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreefieldtwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopupthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreepopuptwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiofour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradioone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiothree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagethreeradiotwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwocheckthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwochecktwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwofieldtwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupfour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopupthree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetwopopuptwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiofive.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiofour.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadioone.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiothree.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/pagetworadiotwo.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/popupclear.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/popupsubmit.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/prev.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/radioclear.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/radiosubmit.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/return.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightcheckcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightfieldcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightpopupcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/rightradiocorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongcheckcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongfieldcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongpopupcorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/epsfiles/wrongradiocorrect.eps
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/check.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/check.tex
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/field.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/field.tex
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/ndex.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/ndex.tex
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/popup.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/popup.tex
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/radio.pdf
%doc %{_texmfdistdir}/doc/latex/interactiveworkbook/samplefiles/radio.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061006-2
+ Revision: 752798
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061006-1
+ Revision: 718724
- texlive-interactiveworkbook
- texlive-interactiveworkbook
- texlive-interactiveworkbook
- texlive-interactiveworkbook

