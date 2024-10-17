Name:		texlive-pst-fr3d
Version:	15878
Release:	2
Summary:	Draw 3-dimensional framed boxes using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fr3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
