# CMSC 137 Laboratory: Data Signals
# Prepared by: Reah Mae Sardañas
########################################################################

import numpy as np
import matplotlib.pyplot as plt


def main():
    while True:
        wave_type = input("\n    Enter the function type (sine or cosine): ")               # input for selecting function to calculate
    
        omega = 2 * np.pi                                                                   # angular frequency
        t = np.linspace(0, 2, 1000)                                                         # value of time using numpy's linspace function

        if wave_type.lower() == "sine":                                                     # choosing sine wave function 
            N = int(input("    Enter the number of terms in the series: "))                 # input for the value of N
            plt.plot(t, calculate_sine_wave(N, omega, t))                                   # plot the sine wave

        elif wave_type.lower() == "cosine":                                                 # choosing cosine wave function 
            N = int(input("    Enter the number of terms in the series: "))                 # input for the value of N
            plt.plot(t, calculate_cosine_wave(N, omega, t))                                 # plot the cosine wave

        else:
            print("    Invalid function type. Please enter either 'sine' or 'cosine'.")
            continue
        
        plt.xlabel('Time')                                                                  # label for the x-axis
        plt.ylabel('Amplitude')                                                             # label for the y-axis
        plt.title('{} Wave with {} Terms'.format(wave_type.capitalize(), N))                # title for the wave graph
        plt.show()                                                                          # displays the plot

        exit = input("    Do you want to exit? (y/n): ")                             
        if exit.lower() == "y":
            print("\n")
            break
            
def calculate_sine_wave(N, omega, t):                                                       # function to calculate the sine wave
    result = 0  
    for n in range(1, N+1):                                                                 # loops to calculate every term of the series using the general(sine) formula
        result += np.sin((2*n-1)*omega*t) / (2*n-1)
    return result


def calculate_cosine_wave(N, omega, t):                                                     # function to calculate the sine wave
    result = 0
    for n in range(1, N+1):
        m = (2*n-1)                                                                         # loops to calculate every term of the series using the given cosine formula
        result += (1/(m**2)) * np.cos(m*omega*t)
    return (8/np.pi**2) * result

if __name__ == "__main__":
=======

# CMSC 137 Laboratory: Data Signals
# Prepared by: Reah Mae Sardañas
########################################################################

import numpy as np
import matplotlib.pyplot as plt


def main():
    while True:
        wave_type = input("\n    Enter the function type (sine or cosine): ")               # input for selecting function to calculate
    
        omega = 2 * np.pi                                                                   # angular frequency
        t = np.linspace(0, 2, 1000)                                                         # value of time using numpy's linspace function

        if wave_type.lower() == "sine":                                                     # choosing sine wave function 
            N = int(input("    Enter the number of terms in the series: "))                 # input for the value of N
            plt.plot(t, calculate_sine_wave(N, omega, t))                                   # plot the sine wave

        elif wave_type.lower() == "cosine":                                                 # choosing cosine wave function 
            N = int(input("    Enter the number of terms in the series: "))                 # input for the value of N
            plt.plot(t, calculate_cosine_wave(N, omega, t))                                 # plot the cosine wave

        else:
            print("    Invalid function type. Please enter either 'sine' or 'cosine'.")
            continue
        
        plt.xlabel('Time')                                                                  # label for the x-axis
        plt.ylabel('Amplitude')                                                             # label for the y-axis
        plt.title('{} Wave with {} Terms'.format(wave_type.capitalize(), N))                # title for the wave graph
        plt.show()                                                                          # displays the plot

        exit = input("    Do you want to exit? (y/n): ")                             
        if exit.lower() == "y":
            print("\n")
            break
            
def calculate_sine_wave(N, omega, t):                                                       # function to calculate the sine wave
    result = 0  
    for n in range(1, N+1):                                                                 # loops to calculate every term of the series using the general(sine) formula
        result += np.sin((2*n-1)*omega*t) / (2*n-1)
    return result


def calculate_cosine_wave(N, omega, t):                                                     # function to calculate the sine wave
    result = 0
    for n in range(1, N+1):
        m = (2*n-1)                                                               # loops to calculate every term of the series using the given cosine formula
        result += (1/(m**2)) * np.cos(m*omega*t)
    return (8/np.pi**2) * result

if __name__ == "__main__":
    main()
