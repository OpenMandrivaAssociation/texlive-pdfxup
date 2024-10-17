Name:		texlive-pdfxup
Version:	59001
Release:	2
Summary:	Create n-up PDF pages with minimal margins
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pdfxup
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfxup.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfxup.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
pdfxup is a Unix/Linux shell script that creates a PDF document
where each page is obtained by combining several pages of a PDF
file given as output. pdfxup uses ghostscript for computing the
maximal bounding box of (some of) the pages of the document,
and then uses pdflatex (with the graphicx package) in order to
produce the new document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/pdfxup
%{_texmfdistdir}/texmf-dist/scripts/pdfxup
%doc %{_texmfdistdir}/texmf-dist/doc/support/pdfxup
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfxup.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdfxup.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
