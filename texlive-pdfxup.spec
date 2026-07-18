%global tl_name pdfxup
%global tl_revision 71513
%global tl_bin_links pdfxup:%{_texmfdistdir}/scripts/pdfxup/pdfxup

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.12
Release:	%{tl_revision}.1
Summary:	Create n-up PDF pages with minimal margins
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pdfxup
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfxup.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfxup.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pdfxup.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
pdfxup is a Unix/Linux shell script that creates a PDF document where
each page is obtained by combining several pages of a PDF file given as
output. pdfxup uses ghostscript for computing the maximal bounding box
of (some of) the pages of the document, and then uses pdflatex (with the
graphicx package) in order to produce the new document.

