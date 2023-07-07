greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(a,b):
    a,b=greek_alphabet.index(a),greek_alphabet.index(b)
    return -1 if a<b else 0 if a==b else 1

print(greek_comparator('alpha','beta'))