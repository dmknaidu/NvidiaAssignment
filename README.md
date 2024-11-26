# Evaluation Framework for Synthetic Human Action Recognition

This project provides a framework for evaluating the quality of synthetic human action videos using **FID-VID** and **FVD** metrics. Users can upload videos to perform quantitative evaluations, visualize results, and generate comparative graphs.

## Features
- Upload real and synthetic videos for comparison.
- Compute **FID-VID** and **FVD** metrics dynamically.
- Generate visualization plots for performance evaluation.

## Prerequisites
1. **Python 3.7+** installed.
2. Install dependencies using:
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
