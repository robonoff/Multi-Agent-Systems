# CTMC Parameter Synthesis

This project solves a parameter synthesis problem for a Continuous-Time Markov Chain (CTMC) with 3 states.

- **Symbolic solution**: closed-form expression for reachability of state C.
- **Numerical solution**: matrix exponential using `scipy.linalg.expm`.
- **Plots**: feasible regions of (r, s), sensitivity curves, and comparison symbolic vs numeric.

## Structure
- `src/ctmc.py`: functions for Q-matrix, probabilities, and plotting.
- `notebook/ctmc_synthesis.ipynb`: main exploration and results.
- `CTMC.pdf`: theoretical background and formal specification.

## Key features
- **Symbolic solution**: closed-form expression for reachability of state C.
- **Numerical validation**: Matrix exponential computations `scipy.linalg.expm`.
- **Plots**: feasible regions of (r, s), sensitivity curves, and comparison symbolic vs numeric.

**Results:**
- Analytical reachability formula derived and validated
- Symbolic vs numerical solutions match within precision
- Feasible parameter regions identified and visualized
- Convergence verification completed successfully

