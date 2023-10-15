import numpy as np
import matplotlib.pyplot as plt

def frequency_analysis(mismatch):
    """
    Perform Fourier Transform on the mismatch time-series and visualize the results.
    """
    # Fourier Transform
    sp = np.fft.fft(mismatch)
    freq = np.fft.fftfreq(mismatch.index.size, d=1)  # Assuming hourly data

    # Visualization
    plt.figure(figsize=(14, 7))
    for col in mismatch.columns:
        plt.plot(freq, np.abs(sp[col]), label=col)
    
    plt.title('Frequency Analysis of Mismatch (Demand - Generation)')
    plt.xlabel('Frequency (1/hour)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
