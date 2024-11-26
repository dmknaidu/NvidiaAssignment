# Evaluation Framework for Synthetic Human Action Recognition

This project provides a framework for evaluating the quality of synthetic human action videos using **FID-VID** and **FVD** metrics. Users can upload videos to perform quantitative evaluations, visualize results, and generate comparative graphs.

## Features
- Upload real and synthetic videos for comparison.
- Compute **FID-VID** and **FVD** metrics dynamically.
- Generate visualization plots for performance evaluation.

## Prerequisites
1. **Python 3.7+** installed.
2. ### Prerequisite: Clone the fid-metrics Repository
   This project uses the `fid-metrics` repository for FID and FVD computations. Clone the repository and set up the environment before running the project:
      # Clone the repository
        git clone https://github.com/npurson/fid-metrics.git
      # Navigate into the directory
        cd fid-metrics
      # Set the environment variable for PYTHONPATH
        export PYTHONPATH=$(pwd):$PYTHONPATH
3. Install dependencies using:
   ```bash
         pip install -r requirements.txt

# How to Use

1. **Download Sample Videos**:  
2. **Launch the Gradio Interface**:  
   Run the following command to start the interface:
   ```bash
   python main.py
3. **Use the Interface**:
    . Select a metric (FID-VID or FVD).
    . Upload two videos (one real and one synthetic) for evaluation.
    . View the computed metric values and visualization.

#Outputs
1. Metric Results: Example - FID-VID,FVD
2. Visualization: Scatter plot comparing FID-VID and FVD values.
