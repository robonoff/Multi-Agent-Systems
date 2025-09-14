# CTMC Parameter Synthesis

This project solves a parameter synthesis problem for a Continuous-Time Markov Chain (CTMC) with 3 states.

- **Symbolic solution**: closed-form expression for reachability of state C.
- **Numerical solution**: matrix exponential using `scipy.linalg.expm`.
- **Plots**: feasible regions of (r, s), sensitivity curves, and comparison symbolic vs numeric.

## Structure
- `src/ctmc.py`: functions for Q-matrix, probabilities, and plotting.
- `notebooks/01_ctmc_synthesis.ipynb`: main exploration and results.
- `report`: CTMC.pdf

