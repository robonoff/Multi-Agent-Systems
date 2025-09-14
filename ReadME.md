# Multi-Agent Systems - exam project 2024-2025

A comprehensive repository containing various multi-agent system simulations, project developed for the Multi Agents Systems course held at University of Trieste by professors Tatjana Petrov and Tommaso Padoan. The contributors to this project are  [@Tanja Derin](https://github.com/tanjaderin) & [@Roberta Lamberti](https://github.com/robonoff).

## 📁 Project Structure

```
Multi-Agent-Systems/
├── ctmc_parameter_synthesis/        # CTMC parameter synthesis studies
│   ├── notebook/
│   │   └── ctmc_synthesis.ipynb    # CTMC parameter synthesis notebook
│   ├── src/
│   │   └── ctmc.py                 # CTMC implementation
│   └── requirements.txt            # Python dependencies
├── lts_behavior/                    # LTS behavior analysis and simulations
│   └── prison_simulation.ipynb     # Prisoner protocol Monte Carlo simulation
```


### 1. CTMC Parameter Synthesis (`ctmc_parameter_synthesis/`)

Continuous-Time Markov Chain parameter synthesis tools and analysis.

**Components:**
- CTMC model implementation
- Parameter synthesis algorithms
- Jupyter notebook for interactive analysis


### 2. Prisoner Protocol Simulation (`lts_behavior/`)

A Monte Carlo simulation study comparing different prisoner signaling protocols based on formal LTS specifications.

**Key Features:**
- **Case 1**: Known initial light state (OFF) - each signaler signals once
- **Case 3**: Unknown initial light state - each signaler signals twice  
- Statistical comparison of expected termination times
- Theoretical vs simulation validation
- Comprehensive visualization and analysis

**Results:**
- Case 1 (known OFF): ~10.6 days average termination
- Case 3 (unknown): ~18.8 days average termination  
- Performance degradation: 77% increase for unknown initial state
- Theoretical formula validation within 1.3% error


## Prerequisites
Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
# Python 3.8+
pip install -r requirements.txt
```

### Running the Simulations

1.**CTMC Analysis:**
```bash
cd ctmc_parameter_synthesis/
pip install -r requirements.txt
jupyter notebook notebook/ctmc_synthesis.ipynb
```

2. **Prisoner Protocol Simulation:**
```bash
cd lts_behavior/
jupyter notebook prison_simulation.ipynb
```

## License

This project is open source and available under standard academic use terms.
