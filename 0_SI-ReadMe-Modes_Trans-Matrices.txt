This is a common ReadMe file for the Supplementary Information documents related to the derivations and expressions 
for gamete mode probabilities, as well as genotype to gamete transition matrices.

[1] Notational Changes

To aid either the reading of the main paper or to aid derivations, some notational changes are made between the main paper 
and the python files, notebooks and txt files.

p_pair: This is used in place of 1 - p[pref] (from the main text) to simplify algebra in the python and txt files

ppc: This corresponds to p[cp] in the main text.
pmp: This corresponds to p[pm] in the main text.
pdm: This corresponds to p[md] in the main text.

vp: This is v' in the main text.
qp: This is q' in the main text.
rp: This is r' in the main text.

p_0: This is p[0] in the main text.
p_1: This is p[1] in the main text.

[2] Function definitions in python script (.py) files

swap_r1 - performs a recombination event between the middle and distal loci 
swap_r2 - performs a recombination event between the proximal and middel loci
swap_r3 - performs a recombination event between the centromere and the proximal locus

biv_D - generates all meiotic products and associated probabilities up to metaphase 1 for bivalents
quad_A_D - generates all meiotic products and associated probabilities up to metaphase 1 for tetravalents and a synaptic
partner switch between the centromere and proximal locus
quad_B_D - generates all meiotic products and associated probabilities up to metaphase 1 for tetravalents and a synaptic
partner switch between the middle and distal loci
qual_C_D - generates all meiotic products and associated probabilities up to metaphase 1 for tetravalents and a synaptic
partner switch between the proximal and middle loci

ana - generates all meiotic products and associated probabilities during metaphase 1 through anaphase 2
total_list - sums up probabilities for meiotic products across prophase 1 to anaphase 2

get_mode_gametes - generates a list of all of the gametes for a mode in terms of a1b1c1/a2b2c2/a3b3c3/a4b4c4
gam_mode - generates the probability of a gamete mode by checking if a gamete corresponds to the mode and sums up the
probabilities of gametes that correspond to a mode
mode_prob - a function that calls a series of functions that generates the probability of a mode for a given pairing
arrangement and synaptic partner switch

Note that gamete mode probabilities are generated for a particular pairing arrangement and synaptic partner switch.  The
python notebooks that compile gamete mode probabilities then put together mode probabilites across pairing arrangements
and synaptic partner switchs into a single expression giving the overall probability for a gamete mode.

[3] Python notebook (.ipynb) files

[a] Compilation of gamete mode probabilities

These files put together mode probabilites across pairing arrangements and synaptic partner switches into a single 
expression giving the overall probability for a gamete mode (comb_lst).

[b] Genotype - gamete transition matrices

These files generate unique unordered tetraploid parent and diploid gamete genotypes.  It then uses the get_mode_gametes()
function (see above) to generate a transition matrix between parental genotypes and gamete genotypes at the level of 
gamete modes (trans_matrix).  In trans_matrix, p(i) corresponds to the probability of gamete mode i. 

[c] Substitute algebraic probabilities

These files substitute specific values for p(i) in terms of complicated functions of the probabilities of synaptic
partner switches, recombination rates, preferential pairing and probabilities of bi versus tetravalency.

[d] Double reduction

Provides expressions for probabilities of double reduction across models of gamete formation.

[4] Lists of gamete mode probabilities (.txt) files

The element in each sublist is the number for a gamete mode and corresponds to Appendices 1 or 2 in Griswold & Asif.
The second element is the gamete mode probability (no preferential cross-over formation) or a list of gamete
mode probabilities (preferential cross-over formation).  In the latter case the first element in the list 
of probabilities is for a GGGG parent, the second a GGGg parent, the third a GGgg parent and the fourth a GGG,G&&g
parent.

[5] Matrices of genotype-gamete transition probabilities (.txt) files

These are outputs of the .ipynb files which generate genotype-gamete transition probabilities (see above).  Output the
probability of a gamete mode is written as p(i) for gamete mode i.  The Substitute algebraic probabilities .pynb files 
are then used to substitute in complicated expressions for p(i).




