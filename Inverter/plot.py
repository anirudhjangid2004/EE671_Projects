import numpy as np
import matplotlib.pyplot as plt

# Constants
VDD = 1.8  # Supply voltage_out
V_LOW = 0.2 * VDD  # 20% of VDD
V_HIGH = 0.8 * VDD  # 80% of VDD

# Load data from file
data = np.loadtxt('output1_1.txt')
time = data[:, 0]  # First column: time
voltage_out = data[:, 1]  # Second column: voltage_out
voltage_in = data[:, 3]   # Third column is applied voltage input

# Load data from files (replace 'V_in.txt' and 'V_out.txt' with your actual file names)
data = np.loadtxt('output1_2.txt')
V_out = data[:, 1]  # Second column: voltage_out
V_in = data[:, 3]   # Third column is applied voltage input

# Plot the data
plt.plot(time, voltage_out, label="Signal")
plt.axhline(V_LOW, color='red', linestyle='--', label="20% of VDD")
plt.axhline(V_HIGH, color='green', linestyle='--', label="80% of VDD")
plt.xlabel('Time (s)')
plt.ylabel('voltage_out (V)')
plt.title('Signal with Rise and Fall Time')
plt.legend()
plt.grid(True)
plt.savefig("plot_2.png")

# Debugging: Print min and max values of voltage_out
print(f"Min voltage_out: {np.min(voltage_out)} V")
print(f"Max voltage_out: {np.max(voltage_out)} V")


i = 50000
while(voltage_out[i] < V_LOW):
    i += 1
tr1 = time[i]*1e12

while(voltage_out[i] < V_HIGH):
    i +=1 
tr2 = time[i]*1e12

t_rise = tr2 - tr1
print(f"Rise Time : {t_rise}ps")


i = 150000
while(voltage_out[i] > V_HIGH):
    i +=1 
tf1 = time[i]*1e12
while(voltage_out[i] > V_LOW):
    i += 1
tf2 = time[i]*1e12

t_fall = tf2 - tf1
print(f"Fall Time: {t_fall}ps")


j = 50000
while(voltage_in[j] > 0.9):
    j+=1
t_input = time[j]

j = 60000
while(voltage_out[j] < 0.9):
    j+=1
t_output = time[j]

prop_delay = t_output-t_input
print(f"Propagation delay :{prop_delay*1e12} ps")

# For Other half

# Ensure both arrays are of the same length
assert len(V_in) == len(V_out), "V_in and V_out must be of the same length"

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(V_in, V_out, label='V_out vs V_in')
plt.xlabel('V_in')
plt.ylabel('V_out')
plt.title('Plot of V_out vs V_in')

# Calculate slopes between adjacent points
slopes = np.diff(V_out) / np.diff(V_in)

# Find indices where slope is approximately -1
indices = np.where(np.isclose(slopes, -1, atol=1e-2))[0]

min_slope_idx = np.argmin(slopes)

# Get the coordinates where the slope is -1
# Note: Use indices and indices + 1 to get the corresponding points
coordinates = [(V_in[i], V_out[i]) for i in indices]
min_slope_coord = [V_in[min_slope_idx], V_out[min_slope_idx]]

# Plot the points where slope is -1
for coord in coordinates:
    plt.plot(coord[0], coord[1], 'ro')  # Red dots for points with slope -1

plt.plot(min_slope_coord[0], min_slope_coord[1], 'bo')

# Show the plot with the points marked
plt.legend()
plt.grid(True)
plt.savefig("Characteristic_2.png")

# Print the coordinates
print("Coordinates where the slope is approximately -1:")
for coord in coordinates:
    print(f"V_in: {coord[0]:.2f}, V_out: {coord[1]:.2f}")

NoiseMarginH = coordinates[0][1] - coordinates[1][0]
NoiseMarginL = coordinates[0][0] - coordinates[1][1]

print(f"Noise Margin High : {NoiseMarginH}")
print(f"Noise Margin Low  : {NoiseMarginL}")

with open("ReportPart2.txt", 'w') as file:
    file.write(f"Min voltage_out: {np.min(voltage_out)} V\n")
    file.write(f"Max voltage_out: {np.max(voltage_out)} V\n")
    file.write(f"Rise Time : {t_rise}ps\n")
    file.write(f"Fall Time : {t_fall}ps\n")
    file.write(f"Propagation delay :{prop_delay*1e12} ps\n")
    file.write(f"VIL : {coordinates[0][0]}\n")
    file.write(f"VIH : {coordinates[1][0]}\n")
    file.write(f"Noise Margin High : {NoiseMarginH}\n")
    file.write(f"Noise Margin Low  : {NoiseMarginL}\n")
    file.write(f"Switching Voltage : {min_slope_coord[0]}")
    file.close()
