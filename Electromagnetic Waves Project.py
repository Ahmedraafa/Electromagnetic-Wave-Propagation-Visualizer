import matplotlib.pyplot as plt
import numpy as np

# ==================== Input ====================
c = 3e8  
f = float(input("Enter frequency in Hz: "))

# ==================== Wavelength ====================
wavelength = c / f
print("\n--- Wavelength Result ---")
print(f"Wavelength = {wavelength:.3e} meters")

# ==================== Frequency Classification ====================
if f < 3e5:
    band = "LF (Low Frequency)"
    mode = "Ground Wave"
elif f < 3e6:
    band = "MF (Medium Frequency)"
    mode = "Ground Wave"
elif f < 3e7:
    band = "HF (High Frequency)"
    mode = "Sky Wave"
elif f < 3e8:
    band = "VHF (Very High Frequency)"
    mode = "Line-of-Sight"
elif f < 3e9:
    band = "UHF (Ultra High Frequency)"
    mode = "Line-of-Sight"
else:
    band = "Microwave"
    mode = "Line-of-Sight"

print("\n--- Frequency Classification ---")
print("Frequency Band:", band)
print("Suggested Propagation Mode:", mode)

# ==================== Wavelength vs Frequency Plot ====================
frequencies = np.logspace(5, 10, 100)
wavelengths = c / frequencies

plt.figure(figsize=(12, 8))
plt.plot(frequencies, wavelengths, linewidth=2, label='Wavelength vs Frequency')
plt.scatter([f], [wavelength], s=100, zorder=5,
            label=f'Input Frequency = {f:.2e} Hz')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", linestyle='--', alpha=0.7)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Wavelength (meters)")
plt.title("Frequency vs Wavelength Relationship")

bands = {
    'LF': (3e4, 3e5),
    'MF': (3e5, 3e6),
    'HF': (3e6, 3e7),
    'VHF': (3e7, 3e8),
    'UHF': (3e8, 3e9),
    'Microwave': (3e9, 1e10)
}

colors = ['purple', 'blue', 'green', 'orange', 'red', 'brown']
for (band_name, (f_min, f_max)), color in zip(bands.items(), colors):
    plt.axvspan(
        max(f_min, frequencies[0]),
        min(f_max, frequencies[-1]),
        alpha=0.2,
        color=color,
        label=band_name
    )

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()


# -------- 1) Ground Wave  ------------
x = np.linspace(0, 100, 400)
earth = -0.002 * (x - 50)**2
ground_wave = earth + 1
plt.figure()
plt.plot(x, earth, label="Earth Surface")
plt.plot(x, ground_wave, label="Ground Wave")
plt.text(5, 0.5, "Tx")
plt.text(90, 0.5, "Rx")
plt.title("Ground Wave Curving Along Earth")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend()
plt.grid(True)
plt.show()

# -------- 2) Sky Wave  --------
x = np.linspace(0, 100, 400)
ground = np.zeros_like(x)
plt.figure()
plt.plot(x, ground, label="Earth")
plt.plot([10, 50], [0, 20], label="Incident Wave")
plt.plot([50, 90], [20, 0], label="Reflected Wave")
plt.axhline(20, linestyle='--', label="Ionosphere")
plt.text(10, 0.5, "Tx")
plt.text(85, 0.5, "Rx")
plt.title("Sky Wave Reflection from Ionosphere")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend()
plt.grid(True)
plt.show()

# -------- 3) Line of Sight  -------------
x = np.linspace(0, 100, 400)
los = np.ones_like(x) * 2
plt.figure()
plt.plot(x, los, label="LOS Signal")
plt.plot(x, np.zeros_like(x), label="Ground")
plt.plot([50, 50], [0, 4], linewidth=4, label="Obstacle")
plt.text(5, 2.2, "Tx")
plt.text(90, 2.2, "Rx")
plt.title("LOS Signal Blocked by an Obstacle")
plt.xlabel("Distance")
plt.ylabel("Height")
plt.legend()
plt.grid(True)
plt.show()

# ==================== ENERGY ====================
h = 6.626e-34  
energy = h * f  

print("\n--- Propagation Mode & Photon Energy ---")
print(f"Propagation Mode: {mode} | LOS Possible: {'Yes' if mode=='Line-of-Sight' else 'No'}")
print(f"Photon Energy: {energy:.3e} Joules")
