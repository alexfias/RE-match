# Renewable Matching Index (RMI)

This repository provides a framework to compute the Renewable Matching Index (RMI) for energy system models. The goal is to assess how well an energy model matches renewable generation with demand in both space and time. It builds upon and extends the adequacy indicators defined by ENTSO-E, such as loss of load duration, loss of load expectation, and energy not served.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Basic RMI Method](#basic-rmi-method)
- [Methods](#methods)
- [Utilities](#utilities)
- [Contribute](#contribute)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/renewable-matching-index.git

2. Install the required packages:
   pip install -r requirements.txt

## Usage
   After installation, you can use the main script to compute the RMI based on different methods:
   python main.py --method basic_rmi --network_path path/to/your/network.nc

### Basic RMI Method
   This method computes the RMI based on spatial and temporal correlations between nodes and hours, respectively. The results are then normalized and combined to   
   produce an overall index. Check methods/basic_rmi.py for more details.

## Methods
   basic_rmi: Computes the RMI based on spatial and temporal correlations.

## Utilities
   Utilities provide helper functions for data processing, file input/output operations, and visualizations. Check the utils directory for more details.

## Contribute
   Contributions are welcome!  

## License
   MIT License
