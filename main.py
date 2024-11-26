import gradio as gr
import re
import yaml
import subprocess
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

# Function to dynamically update config.yaml and compute metrics
def compute_metrics(metric_type, file1, file2):
    try:
        # Get paths of the uploaded files
        path1 = file1.name  # File 1 path
        path2 = file2.name  # File 2 path

        # Read existing config.yaml
        with open("configs/config.yaml", "r") as file:
            config = yaml.safe_load(file)

        # Update the `paths` field with the new file paths
        config["paths"] = [path1, path2]

        # Update the `metrics` type in the config based on the selected metric type
        if metric_type == "fid":
            config["metrics"][0]["type"] = "fid"
        elif metric_type == "fvd":
            config["metrics"][1]["type"] = "fvd"
        else:
            raise ValueError("Invalid metric type specified.")

        # Write back updated config.yaml
        with open("configs/config.yaml", "w") as file:
            yaml.safe_dump(config, file)

        # Build the command to call main.py without using Hydra overrides
        cmd = [
            "python", "fid_metrics/main.py"
        ]

        # Execute the command
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Check for errors and return results
        if result.returncode == 0:


            fid_match = re.search(r"FID:\s*([\d.]+)", result.stdout)
            fvd_match = re.search(r"FVD:\s*([\d.]+)", result.stdout)
            fig, ax = plt.subplots()
            x_values = ["fid value", "fvd value"]
            y_values = [float(fid_match.group(1)), float(fvd_match.group(1))]

    # Plot the circles
            ax.scatter(x_values, y_values, marker='o', s=100, color='blue', label='Metrics')  # Scatter plot with circles

    # Annotate the values on the graph
            for i, value in enumerate(y_values):
              ax.text(x_values[i], value + 0.05, f"{value:.2f}", ha='center', fontsize=10, color='black')  # Display value above each circle
 # Title at its location
            ax.set_title(f'{metric_type.upper()} Metric')
            ax.set_ylabel('Score')
            ax.set_xlabel('Metric Type')
            ax.legend()

    # Save the plot to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            plt.close(fig)  # Close the figure to avoid memory issues

    # Convert BytesIO object to PIL Image
            image = Image.open(buf)
            if metric_type=="fid":
                t=fid_match.group(1)
            elif metric_type=="fvd":
                t=fvd_match.group(1)
            else:
                t="None"
            return f"Metric Computed Successfully:\n{result.stdout}",t,image
        else:
            return f"Error:\n{result.stderr}", None
    except Exception as e:
        return f"An error occurred: {str(e)}", None

# Gradio Interface
def gradio_interface(metric_type, file1, file2):
    # Call compute_metrics and pass the uploaded files and metric type
    return compute_metrics(metric_type, file1, file2)

# Define Gradio UI
metric_options = ["fid", "fvd"]
gr.Interface(
    fn=gradio_interface,
    inputs=[
        gr.Dropdown(metric_options, label="Metric Type"),  # Metric type dropdown
        gr.File(label="Upload File 1"),                   # First file uploader
        gr.File(label="Upload File 2")                    # Second file uploader
    ],
    outputs=[gr.Textbox(label="Total Output"),gr.Textbox(label="Metric Result"),gr.Image(label="Metric Plot")],  # Output as text and plot
    title="FID/FVD Metric Evaluation",
    description="Upload two files (images/videos) to compute FID/FVD metrics dynamically."
).launch()
