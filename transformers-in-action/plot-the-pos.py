import numpy as np
import matplotlib.pyplot as plt

# Transformer parameter configuration
d_model = 512
sequence_length = 1024

# Generate the X-axis (word positions from 0 to 1023)
positions = np.arange(sequence_length)

# Define the dimension indices (i) for the 5 selected rows
# We multiply by 2 in the formula because 'i' ranges from 0 to 255 (2*i corresponds to the row index)
selected_rows = {
    "Row 0 (Denom: 1)": 0,
    "Row 128 (Denom: 10)": 64,
    "Row 256 (Denom: 100)": 128,
    "Row 384 (Denom: 1000)": 192,
    "Row 510 (Denom: ~9646)": 255
}

# Select a high-contrast, vibrant color palette
colors = ["#FF1493", "#00BFFF", "#FF8C00", "#32CD32", "#9400D3"]

# Initialize the plot layout
plt.figure(figsize=(14, 7), facecolor='#111111') # Dark background to make colors pop
ax = plt.axes()
ax.set_facecolor('#111111')

# Calculate and plot each individual positional function
for (name, i), color in zip(selected_rows.items(), colors):
    # Apply the standard Transformer denominator formula
    denominator = 10000 ** ((2 * i) / d_model)
    
    # Calculate the Sine values for all 1024 positions
    y_values = np.sin(positions / denominator)
    
    # Plot the line. For Row 0, we use a thinner line combined with markers
    # to highlight the "chaotic" nature of its discrete sampling steps.
    if i == 0:
        plt.plot(positions, y_values, label=name, color=color, alpha=0.7, linewidth=0.8, linestyle='-', marker='o', markersize=2)
    else:
        plt.plot(positions, y_values, label=name, color=color, linewidth=2.5)

# Graph styling and titles
plt.title("Positional Encoding in Transformers: Holistic Row-Wise View", color='white', fontsize=16, pad=20, fontweight='bold')
plt.xlabel("Word Position in the Sentence (X)", color='white', fontsize=12, labelpad=10)
plt.ylabel("Positional Encoding Value (Y)", color='white', fontsize=12, labelpad=10)

# Grid and axis boundary configurations
plt.xlim(0, sequence_length)
plt.ylim(-1.1, 1.1)
plt.grid(True, color='#333333', linestyle='--', alpha=0.5)

# Style tick labels for dark mode visibility
ax.tick_params(colors='white', labelsize=10)

# Add a clean legend in the upper right corner
plt.legend(facecolor='#222222', edgecolor='#444444', labelcolor='white', fontsize=11, loc='upper right')

# Render the final plot
plt.tight_layout()
plt.show()

