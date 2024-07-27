# Reshma Sri Murakonda
# 101282055

import sys

A = sys.argv[1] == '1'
B = sys.argv[2] == '1'
C = sys.argv[3] == '1'
D = sys.argv[4] == '1'
E = sys.argv[5] == '1'
F = sys.argv[6] == '1'
G = sys.argv[7] == '1'
H = sys.argv[8] == '1'
I = sys.argv[9] == '1'
J = sys.argv[10] == '1'
K = sys.argv[11] == '1'
L = sys.argv[12] == '1'

one = (not F) or E
one = one or C
one = one or (not D)

two = (not G) or L
two = two or J
two = two or (not G)

print(f"<{one},{two}>")