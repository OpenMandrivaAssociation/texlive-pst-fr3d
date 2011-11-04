# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fr3d
# catalog-date 2007-02-28 00:07:21 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-pst-fr3d
Version:	1.10
Release:	1
Summary:	Draw 3-dimensional framed boxes using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fr3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package using PSTricks to draw three dimensional framed boxes
using a macro \PstFrameBoxThreeD. The macro is especially
useful for drawing 3d-seeming buttons.

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
%{_texmfdistdir}/tex/generic/pst-fr3d/pst-fr3d.tex
%{_texmfdistdir}/tex/latex/pst-fr3d/pst-fr3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/README
%doc %{_texmfdistdir}/doc/generic/pst-fr3d/pst-fr3d.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-fr3d/pst-fr3d.dtx
%doc %{_texmfdistdir}/source/generic/pst-fr3d/pst-fr3d.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
