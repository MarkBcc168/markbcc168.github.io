title: Research
menu-position: 1
--------
# Research

Here is a list of my papers and preprints. 
Click on each title to view the abstract.

Last updated: **{{last_updated("input/research.md")}}**.

{{paper("Extremal $t$-intersecting Families of Permutations for Large $t$", 
    [], 
    {"arXiv": "https://arxiv.org/abs/2605.26051",
    "JMM": "https://meetings.ams.org/math/jmm2026/meetingapp.cgi/Paper/55074",
    "Slides": "static/slides/permutations_slides.pdf"},
    "<p>Research conducted through the <a href=https://sites.google.com/view/gallian-reu/home>Duluth REU program</a> in 2025. A partial result was presented at JMM 2026.</p>",
    "A set of permutations of $\\{1,2,\\dots,n\\}$ is $t$-intersecting if any two permutations agree on at least $t$ inputs. A recent work by Kupavskii, in the spirit of the Erdős--Ko--Rado Theorem, shows that for all $t\\leq n-O\\left(\\frac{n\\log\\log n}{\\log n}\\right)$, every $t$-intersecting family of permutations of $\\{1,2,\\dots,n\\}$ with the maximum size must be isomorphic to the set $$\\mathcal A_k = \\{\\sigma : \\sigma(i)=i\\text{ for at least } t+k \\text{ indices } i\\in\\{1,2,\\dots,t+2k\\}\\}$$ for some $k$. By refining Kupavskii's spread approximation technique, we prove that this conclusion holds for a wider range of $t\\leq n-n^{5/7+\\varepsilon}$."
)     
}}

{{paper("Improved Bounds on Rainbow $k$-partite Matching", 
    [], 
    {"arXiv": "https://arxiv.org/abs/2508.07331"},
    "<p>Research conducted through the <a href=https://sites.google.com/view/gallian-reu/home>Duluth REU program</a> in 2025.</p>",
    "Let $n$, $s$, and $k$ be positive integers. We say that a sequence $f_1, \\dots,f_s$ of nonnegative integers is <i>satisfying</i> if for any collection of $s$ families $\\mathcal F_1,\\dots,\\mathcal F_s\\subseteq [n]^k$ such that $|\\mathcal F_i|=f_i$ for all $i$, there exists a rainbow matching, i.e., a list of pairwise disjoint tuples  $F_1\\in\\mathcal F_1$, $\\dots$, $F_s\in\mathcal F_s$. We investigate the question, posed by Kupavskii  and Popova, of determining the smallest $c=c(n,s,k)$ such that the arithmetic progression  $c$, $n^{k-1}+c$, $2n^{k-1}+c$, $\\dots$, $(s-1)n^{k-1}+c$ is satisfying. We prove that the sequence is satisfying for $c=\\Omega_k(\\max(s^2n^{k-2}, sn^{k-3/2}\\sqrt{\\log s}))$, improving the previous result by Kupavskii and Popova. We also study satisfying sequences for $k=2$ using the polynomial method, extending the previous result by Kupavskii and Popova  to when $n$ is not prime."
)     
}}

{{paper("Gluing Genus 1 and Genus 2 Curves Along $\ell$-torsion",
    ["Noah Walsh"],
    {"arXiv": "https://arxiv.org/abs/2508.07331",
    "LuCaNT": "https://lucant.org/",
    "JMM": "https://meetings.ams.org/math/jmm2026/meetingapp.cgi/Paper/55066",
    "LuCaNT Slides": "https://app.icerm.brown.edu/assets/515/9289/9289_5350_Saengrungkongka_071020251600_Slides.pdf",
    "JMM Slides": "static/slides/gluing_curves_slides.pdf",
    "LuCaNT Recording": "https://icerm.brown.edu/video_archive/4213"},
    "<p>in <i>LMFDB, Computation, and Number Theory (LuCaNT 2025)</i>, July 7-11, 2025.</p>" +
    "<p>Research conducted through the MIT Math Department's <a href=https://math.mit.edu/research/undergraduate/spur/index.html>SPUR program</a>. My mentors were Sam Schiavone and Edgar Costa. I presented this paper in LuCaNT 2025 and in JMM 2026.</p>",
    "Let $Y$ be a genus $2$ curve over $\\mathbb Q$. We provide a method to systematically search for possible candidates of a prime $\\ell\\geq 3$ and a genus $1$ curve $X$ for which there exists a genus $3$ curve $Z$ over $\\mathbb Q$ whose Jacobian is, up to quadratic twist, $(\\ell, \\ell, \\ell)$-isogenous to the product of Jacobians of $X$ and $Y$, building on the work by Hanselman, Schiavone, and Sijsling for $\\ell=2$. We find several such pairs $(X,Y)$ for prime $\\ell$ up to $13$. We also improve their numerical gluing algorithm, allowing us to successfully glue genus $1$ and genus $2$ curves along their $13$-torsion."
)
}}

{{paper("Complexity of 2D Snake Cube Puzzles", 
["Nithid Anchaleenukoon", "Alex Dang", "Erik D. Demaine", "Kaylee Ji"],
{"arXiv" : "https://arxiv.org/abs/2407.10323",
"Conference" : "https://brocku.ca/mathematics-science/canadian-conference-on-computational-geometry-2024/"},
"<p>in <i>Proceedings of the 36th Canadian Conference on Computational Geometry (CCCG 2024)</i>, July 17-19, 2024.</p>" + 
"<p>Research conducted during open problem sessions in <a href=https://courses.csail.mit.edu/6.5440/fall23/>MIT 6.5440</a> (Algorithmic Lower Bounds).</p>",
'Given a chain of $HW$ cubes where each cube is marked "turn $90^\\circ$" or "go straight", when can it fold into a $1 \\times H \\times W$ rectangular box? We prove several variants of this (still) open problem NP-hard:' + 
    "<br> (1) allowing some cubes to be wildcard (can turn or go straight);" + 
    "<br> (2) allowing a larger box with empty spaces (simplifying a proof from CCCG 2022);" +
    "<br> (3) growing the box (and the number of cubes) to $2 \\times H \\times W$ (improving a prior 3D result from height $8$ to $2$);" + 
    "<br> (4) with hexagonal prisms rather than cubes, each specified as going straight, turning $60^\\circ$, or turning $120^\\circ$; and" + 
    "<br> (5) allowing the cubes to be encoded implicitly to compress exponentially large repetitions."
)}}
