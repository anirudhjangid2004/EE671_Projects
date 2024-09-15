import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load the file
    data = np.loadtxt(file_path)
    
    # Extract time, input, and output columns
    time = data[:, 0]   # First column for time
    input_signal = data[:, 1]   # Second column for input signal
    output_signal = data[:, 3]  # Fourth column for output signal
    
    return time, input_signal, output_signal

def calculate_rise_fall_time(time, signal):
    # Calculate the 10% and 90% thresholds of the signal
    min_val = 0
    max_val = 1.8
    range_val = max_val - min_val
    low_threshold = min_val + 0.1 * range_val
    high_threshold = min_val + 0.9 * range_val

    i = 50
    if (signal[i] <= low_threshold):
        while(signal[i] <= low_threshold):
            i += 1
        time_step1 = time[i]*(10e9)
        while(signal[i] <= high_threshold):
            i += 1
        time_step2 = time[i]*(10e9)

        rise_time = time_step2 - time_step1

        while(signal[i] >= high_threshold):
            i += 1
        time_step1 = time[i]*(10e9)
        while(signal[i] >= low_threshold):
            i += 1
        time_step2 = time[i]*(10e9)

        fall_time = time_step2 - time_step1

    else:
        while(signal[i] >= high_threshold):
            i += 1
        time_step1 = time[i]*(10e9)
        while(signal[i] >= low_threshold):
            i += 1
        time_step2 = time[i]*(10e9)

        fall_time = time_step2 - time_step1

        while(signal[i] <= low_threshold):
            i += 1
        time_step1 = time[i]*(10e9)
        while(signal[i] <= high_threshold):
            i += 1
        time_step2 = time[i]*(10e9)

        rise_time = time_step2 - time_step1

    return rise_time, fall_time

def plot_signals(time, input_signal, output_signal, save_path='output_plot.png'):
    # Plot input signal
    plt.figure(figsize=(10, 6))
    plt.plot(time, input_signal, label='Input Signal', color='b')
    plt.plot(time, output_signal, label='Output Signal', color='r')
    plt.xlabel('Time')
    plt.ylabel('Signal')
    plt.title('Input and Output Signals vs Time')
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path, format='png')
    # plt.show()
  

def main(file_path):
    # Load data from the file
    time, input_signal, output_signal = load_data(file_path)

    # Plot the input and output signals
    plot_signals(time, input_signal, output_signal, save_path='random.png')

    # Calculate rise time and fall time for the output signal
    rise_time, fall_time = calculate_rise_fall_time(time, output_signal)

    print(f"Rise Time: {rise_time} units")
    print(f"Fall Time: {fall_time} units")

# file_path = 'output_B1_t.txt'
# print("For B1")
# main(file_path)

file_path = 'data_A1.txt'
print("\nFor A1")
main(file_path)

# file_path = 'output_A2_t.txt'
print("\n")
# main(file_path)