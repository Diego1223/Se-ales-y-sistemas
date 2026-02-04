import numpy as np
import matplotlib.pyplot as plt

# Parámetros de muestreo
fs = 1000            # Frecuencia de muestreo (Hz)
T = 1                # Duración de la señal (segundos)
t = np.linspace(0, T, fs, endpoint=False)

# Definición de la señal
f1 = 50               # Frecuencia de la primera señal (Hz)
f2 = 120              # Frecuencia de la segunda señal (Hz)

x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Transformada de Fourier
X = np.fft.fft(x)

# Vector de frecuencias
frecuencias = np.fft.fftfreq(len(X), 1/fs)

# Magnitud del espectro
magnitud = np.abs(X)


plt.figure(figsize=(12, 5))

# Dominio del tiempo
plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title("Señal en el dominio del tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()

# Dominio de la frecuencia (solo frecuencias positivas)
plt.subplot(1, 2, 2)
plt.stem(frecuencias[:len(frecuencias)//2],
         magnitud[:len(magnitud)//2],
         use_line_collection=True)
plt.title("Espectro de magnitud (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()

plt.tight_layout()
plt.show()


