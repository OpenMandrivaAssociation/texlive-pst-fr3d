# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fr3d
# catalog-date 2007-02-28 00:07:21 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-pst-fr3d
Version:	1.10
Release:	10
Summary:	Draw 3-dimensional framed boxes using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fr3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package using PSTricks to draw three dimensional framed boxes
using a macro \PstFrameBoxThreeD. The macro is especially
useful for drawing 3d-seeming buttons.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-fr3d/pst-fr3d.tex
%{_texmfdistdir}/tex/latex/pst-fr3d/pst-fr3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/README
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/pst-fr3d.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-fr3d/pst-fr3d.dtx
%doc %{_texmfdistdir}/source/generic/pst-fr3d/pst-fr3d.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-2
+ Revision: 755272
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.10-1
+ Revision: 719350
- texlive-pst-fr3d
- texlive-pst-fr3d
- texlive-pst-fr3d
- texlive-pst-fr3d

