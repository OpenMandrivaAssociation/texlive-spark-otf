Name:		texlive-spark-otf
Version:	62481
Release:	2
Summary:	Support OpenType Spark fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spark-otf
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spark-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spark-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports the free fonts from "After the Flood"
which are available from AtF Spark. The following fonts are
supported: Spark -- Bar -- Medium Spark -- Bar -- Narrow Spark
-- Bar -- Thin Spark -- Dot-line -- Medium Spark -- Dot --
Medium Spark -- Dot -- Small

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/spark-otf
%{_texmfdistdir}/fonts/opentype/public/spark-otf
%doc %{_texmfdistdir}/doc/fonts/spark-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
