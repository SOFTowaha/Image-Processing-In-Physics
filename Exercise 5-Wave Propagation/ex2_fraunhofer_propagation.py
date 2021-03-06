"""
24.05.2018
Image Processing Physics TU Muenchen
Julia Herzen, Klaus Achterhold, (Maximilian Teuffenbach, Juanjuan Huang)

ex1_fraunhofer_propagation.py

Using numpy, matplotlib

Script to generate a speckle pattern from an atmospheric phase screen
using Fraunhofer propagation.
You need to replace the ??? in the code with the required commands.
"""

import numpy as np
import matplotlib.pylab as plt

N = 1024  # Square dimension of phase screen

radius = 128  # Radius of the circular aperture in pixels

# Generate an NxN array of zeros for the aperture

aperture = np.zeros([N, N])

# Calculate the aperture magnitude: 1's of radius given above centered
# in the NxN array of zeros
# Functions of interest include np.meshgrid, np.linspace, range ...
# Hint eq of circle x^2 + y^2 = r^2
xx, yy =np.meshgrid(np.linspace(-N/2, N/2, N), np.linspace(-N/2, N/2, N)) 
circle = xx**2 + yy**2
aperture[circle < radius**2] = 1

# Plot your aperture function

plt.figure(1)
plt.imshow(aperture, cmap='gray', interpolation='none')
plt.colorbar()

# Load in the wavefront phase screen and plot it.

screen = np.loadtxt('wavefront.txt')
plt.figure(2)
plt.imshow(screen, cmap='jet', interpolation='none')
plt.colorbar()

# Propagate the phase screen from the aperture to the focal plane using
# Fraunhofer propagation.
# Hints - aperture is the magnitude, and screen is the phase
# Fraunhofer propagation - wave at focal plane is FT of wave at aperture plane
# You may need to use an fftshift here!
# Intensity is the absolute value of field at the focal plane squared

speckle = np.abs(np.fft.fftshift(np.fft.fft2(aperture * np.exp(screen * -1j))))**2

# Plot the speckle image (zoomed in to show the centre)

plt.figure(3)
plt.imshow(speckle[int(N/2-64):int(N/2+64), int(N/2-64):int(N/2+64)],
           cmap='jet', aspect='auto', interpolation='none')
plt.colorbar()
plt.title('Intensity') 
