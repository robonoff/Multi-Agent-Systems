import numpy as np
from scipy.linalg import expm
import matplotlib.pyplot as plt

# Q-matrices

def Q_matrix(r, s):
    """Generator matrix of the original CTMC."""
    return np.array([
        [-r,   r,   0.0],
        [ s, -r-s,  r  ],
        [0.0,  s,  -s ]
    ], dtype=float)

def Q_absorbC(r, s):
    """Generator matrix with state C absorbing for reachability."""
    return np.array([
        [-r,   r,   0.0],
        [ s, -r-s,  r  ],
        [0.0, 0.0,  0.0]
    ], dtype=float)

# Probabilities (numerical)

def prob_in_state_at_t(state_index, r, s, t=5.0, pi0=np.array([1.0,0.0,0.0])):
    """Occupancy: P[X(t)=state] in the original CTMC."""
    Pt = expm(Q_matrix(r, s) * t)
    return float((pi0 @ Pt)[state_index])

def prob_reach_C_by_t(r, s, t=5.0, pi0=np.array([1.0,0.0,0.0])):
    """Reachability: P[τ_C ≤ t] via absorbing-C trick."""
    Pt = expm(Q_absorbC(r, s) * t)
    return float((pi0 @ Pt)[2])  # index 2 = state C

# Wrappers for convenience
prob_B = lambda r,s,t=5.0: prob_in_state_at_t(1, r, s, t)
prob_C = lambda r,s,t=5.0: prob_in_state_at_t(2, r, s, t)
prob_reachC = lambda r,s,t=5.0: prob_reach_C_by_t(r, s, t)



# Symbolic closed form for pC(t)

def pC_symbolic(r, s, t=5.0):
    """
    Closed form expression for reachability of C by time t.
    Derived via eigen-decomposition of the 2x2 subsystem (A,B).
    """
    Delta = np.sqrt(s**2 + 4*r*s)
    lam1 = -(2*r + s - Delta) / 2
    lam2 = -(2*r + s + Delta) / 2

    # Closed form (from derivation in report)
    term1 = (Delta + s)**2 * np.exp(lam1 * t)
    term2 = (Delta - s)**2 * np.exp(lam2 * t)
    return 1.0 - (term1 - term2) / (4 * s * Delta)





# Plotting helpers

def grid_values(prob_fn, r_range=(0.1, 3.0), s_range=(0.1, 3.0), n=100, t=5.0):
    """Evaluate probability function on a grid of r,s values."""
    rs = np.linspace(*r_range, n)
    ss = np.linspace(*s_range, n)
    Z = np.zeros((n, n))
    for i, r in enumerate(rs):
        for j, s in enumerate(ss):
            Z[j, i] = prob_fn(r, s, t)
    return rs, ss, Z

def plot_region(prob_fn, title, theta=0.8, t=5.0):
    """Plot heatmap + contour for a probability function."""
    rs, ss, Z = grid_values(prob_fn, t=t)
    plt.figure(figsize=(6,5))
    im = plt.imshow(Z, origin='lower', 
                    extent=[rs.min(), rs.max(), ss.min(), ss.max()], 
                    aspect='auto')
    CS = plt.contour(rs, ss, Z, levels=[theta], colors='red', linewidths=1.5)
    plt.clabel(CS, inline=True, fontsize=8)
    plt.xlabel("r"); plt.ylabel("s")
    plt.title(f"{title} (red contour = {theta})")
    plt.colorbar(im, label="Probability")
    plt.show()
