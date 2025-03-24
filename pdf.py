from fpdf import FPDF

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Set font and size
pdf.set_font(\"Arial\", size=12)

# Title
pdf.cell(0, 10, \"Correction - Mathématiques S2-B3-APEF\", ln=True, align='C', border=False)

# Exercice 1
pdf.set_font(\"Arial\", 'B', 12)
pdf.cell(0, 10, \"Exercice 1 : Polynômes 1 (6,5 points)\", ln=True)

pdf.set_font(\"Arial\", size=12)
pdf.multi_cell(0, 10, \"On considère P(X) = X^5 + 4X^4 + 7X^3 + 6X^2 + 2X.\")

# Question 1
pdf.multi_cell(0, 10, \"1. Montrer que 0 est une racine d'ordre de multiplicité exactement 1 de P :\")

pdf.multi_cell(0, 10, \"Pour montrer que 0 est une racine de P, on évalue P(0) :\")

pdf.multi_cell(0, 10, \"P(0) = 0^5 + 4 * 0^4 + 7 * 0^3 + 6 * 0^2 + 2 * 0 = 0\")

pdf.multi_cell(0, 10, \"Donc, 0 est une racine de P.\")

# Question 2
pdf.multi_cell(0, 10, \"2. Montrer que -1 est une racine d'ordre de multiplicité exactement 2 de P :\")

pdf.multi_cell(0, 10, \"On évalue P(-1) et P'(-1) :\")

pdf.multi_cell(0, 10, \"P(-1) = (-1)^5 + 4(-1)^4 + 7(-1)^3 + 6(-1)^2 + 2(-1) = -1 + 4 - 7 + 6 - 2 = 0\")

pdf.multi_cell(0, 10, \"P'(-1) = 5(-1)^4 + 16(-1)^3 + 21(-1)^2 + 12(-1) + 2 = 5 - 16 + 21 - 12 + 2 = 0\")

# Question 3
pdf.multi_cell(0, 10, \"3. En déduire que X^3 + 2X^2 + X | P :\")

pdf.multi_cell(0, 10, \"Puisque 0 est une racine de multiplicité 1 et -1 est une racine de multiplicité 2, on peut écrire :\")

pdf.multi_cell(0, 10, \"P(X) = (X)(X+1)^2 * Q(X)\")

pdf.multi_cell(0, 10, \"En développant, on trouve que Q(X) = X^3 + 2X^2 + X.\")

# Question 4
pdf.multi_cell(0, 10, \"4. Écrire P comme produit de polynômes irréductibles dans R[X] et C[X] :\")

pdf.multi_cell(0, 10, \"En effectuant la division euclidienne de P(X) par X^3 + 2X^2 + X, on trouve :\")

pdf.multi_cell(0, 10, \"P(X) = (X)(X+1)^2(X^2+2)\")

pdf.multi_cell(0, 10, \"Dans R[X], X^2 + 2 est irréductible. Dans C[X], X^2 + 2 = (X + i√2)(X - i√2).\")

# Exercice 2
pdf.add_page()
pdf.set_font(\"Arial\", 'B', 12)
pdf.cell(0, 10, \"Exercice 2 : Polynômes 2 (2,5 points)\", ln=True)

pdf.set_font(\"Arial\", size=12)
pdf.multi_cell(0, 10, \"On considère P(X) = Q(X) * (X-1)^n avec Q un polynôme de degré 2.\")

# Conditions
pdf.multi_cell(0, 10, \"Les conditions données sont :\")

pdf.multi_cell(0, 10, \"Q(0) = 0, Q(-1) = 0, Q(1) = 2, P(1) = P'(1) = P''(1) = 0, P^(3)(1) ≠ 0\")

# Solution
pdf.multi_cell(0, 10, \"Puisque Q est un polynôme de degré 2 avec Q(0) = 0 et Q(-1) = 0, on peut écrire :\")

pdf.multi_cell(0, 10, \"Q(X) = aX(X+1)\")

# Utilisation de Q(1) = 2
pdf.multi_cell(0, 10, \"En utilisant Q(1) = 2 :\")

pdf.multi_cell(0, 10, \"2 = a * 1 * (1+1) ⇒ a = 1\")

pdf.multi_cell(0, 10, \"Donc, Q(X) = X(X+1).\")

# P(X)
pdf.multi_cell(0, 10, \"Pour P(X), on a :\")

pdf.multi_cell(0, 10, \"P(X) = X(X+1)(X-1)^n\")

# Utilisation des dérivées
pdf.multi_cell(0, 10, \"En utilisant P(1) = P'(1) = P''(1) = 0 et P^(3)(1) ≠ 0, on déduit que n = 3.\")

pdf.multi_cell(0, 10, \"Donc, P(X) = X(X+1)(X-1)^3.\")

# Exercice 3
pdf.add_page()
pdf.set_font(\"Arial\", 'B', 12)
pdf.cell(0, 10, \"Exercice 3 : Équations différentielles (9 points)\", ln=True)

pdf.set_font(\"Arial\", size=12)

# Solutions particulières
pdf.multi_cell(0, 10, \"1. Solutions particulières :\")

pdf.multi_cell(0, 10, \"(a) 2y' + 6y = -3 :\")

pdf.multi_cell(0, 10, \"yp = -1/2\")

# (b)
pdf.multi_cell(0, 10, \"(b) y' + y = e^x :\")

pdf.multi_cell(0, 10, \"yp = xe^x\")

# (c)
pdf.multi_cell(0, 10, \"(c) y'' + y' + y = x + 1 :\")

pdf.multi_cell(0, 10, \"yp = x + 1\")

# Résolution de y'' + y' + y = x + 1
pdf.multi_cell(0, 10, \"2. Résolution de y'' + y' + y = x + 1 :\")

pdf.multi_cell(0, 10, \"La solution générale est :\")

pdf.multi_cell(0, 10, \"y = C1 * e^(-x/2) * cos(√3/2 * x) + C2 * e^(-x/2) * sin(√3/2 * x) + x + 1\")

# Résolution de (e^x + 1)y' + e^x y = cos(3x)
pdf.multi_cell(0, 10, \"3. Résolution de (e^x + 1)y' + e^x y = cos(3x) :\")