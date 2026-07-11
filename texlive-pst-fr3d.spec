%global tl_name pst-fr3d
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Draw 3-dimensional framed boxes using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fr3d
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fr3d.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package using PSTricks to draw three dimensional framed boxes using a
macro \PstFrameBoxThreeD. The macro is especially useful for drawing
3d-seeming buttons.

