# CTMC Parameter Synthesis

This project solves a parameter synthesis problem for a Continuous-Time Markov Chain (CTMC) with 3 states.

- **Symbolic solution**: closed-form expression for reachability of state C.
- **Numerical solution**: matrix exponential using `scipy.linalg.expm`.
- **Plots**: feasible regions of (r, s), sensitivity curves, and comparison symbolic vs numeric.

## Structure
- `src/ctmc.py`: functions for Q-matrix, probabilities, and plotting.
- `notebook/ctmc_synthesis.ipynb`: main exploration and results.
- `CTMC.pdf`: theoretical background and formal specification.

## Key Results
- **Symbolic solution**: Closed-form expression for P(X(t) = C) derived analytically
- **Numerical validation**: Matrix exponential computations using scipy
- **Parameter feasibility**: Identified valid regions for (r, s) parameter space
- **Sensitivity analysis**: Performance curves showing parameter impact on reachability
- **Convergence verification**: Symbolic vs numerical solutions match within numerical precision

