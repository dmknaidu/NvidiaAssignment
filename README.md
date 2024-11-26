#Evaluation Framework for Synthetic Human Action Recognition
This project provides a framework for evaluating the quality of synthetic human action videos using FID-VID and FVD metrics. Users can upload videos to perform quantitative evaluations, visualize results, and generate comparative graphs.

Project Overview
Purpose:

To set up a local workflow with Gradio to evaluate synthetic data quality using FID-VID and FVD metrics.
Users can easily upload two videos (real and synthetic) for comparison and generate result plots and tables.
Metrics:

FID-VID (Fréchet Inception Distance for Videos): Evaluates video fidelity.
FVD (Fréchet Video Distance): Measures temporal coherence in videos.
Outputs:

Numerical metrics (FID-VID and FVD scores).
Graphical plots showing the metric performance.
Features
File Upload: Supports drag-and-drop or file selection for video inputs.
Metric Computation: Dynamically updates the configuration file and computes FID-VID and FVD metrics.
Visualization: Generates scatter plots to compare the results visually.
Interactive Interface: Uses Gradio for a user-friendly GUI.
Workflow
Upload two videos (e.g., one real and one synthetic) to compare.
Choose the evaluation metric (FID-VID or FVD).
Run the evaluation and view the results:
Computed metric values.
Visualization as a scatter plot.
Compare results for 5 Sims4Action videos and 5 sample synthetic videos. Fill the results in a table as shown below.
