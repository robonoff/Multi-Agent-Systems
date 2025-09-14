# LTS Behavior Analysis

This project analyzes prisoner protocol behavior using Labelled Transition Systems (LTS) and Monte Carlo simulation with 3 prisoners.

- **Monte Carlo simulation**: Statistical validation of prisoner signaling protocols (Case 1 vs Case 3).
- **Theoretical analysis**: Mathematical formulation using summation series Σ(i=1 to n-1) 1/i.
- **Comparative study**: Performance impact of known vs unknown initial light state.
- **Visualization**: Distribution plots, CDF analysis, and statistical validation charts.

## Structure
- `prison_simulation.ipynb`: Monte Carlo simulation comparing Case 1 (known initial light OFF) vs Case 3 (unknown initial light state)
- `LTS.pdf`: Formal LTS specification and theoretical background

## Key Results
- **Case 1** (known OFF): ~10.6 days average termination
- **Case 3** (unknown): ~18.8 days average termination  
- **Performance degradation**: 77% increase for unknown initial state
- **Theoretical validation**: Simulation matches analytical formula within 1.3% error
