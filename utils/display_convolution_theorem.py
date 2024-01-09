import matplotlib.pyplot as plt
import numpy as np


def display_convolution_theorem(img, kernel, img_filtered, img_ft, kernel_ft, kernel_label):
    fig, axes = plt.subplots(2, 3, figsize=(15,10))

    axes[0, 0].imshow(img, cmap='gray')
    axes[0, 0].axis('off')
    axes[0, 0].set_title('Original Image')

    axes[0, 1].imshow(kernel, cmap='gray')
    axes[0, 1].axis('off')
    axes[0, 1].set_title(kernel_label)

    axes[0, 2].imshow(img_filtered.real, cmap='gray')
    axes[0, 2].axis('off')
    axes[0, 2].set_title('Convolution in Spatial Domain')

    axes[1, 0].imshow(np.log(1 + np.abs(img_ft)), cmap='gray')
    axes[1, 0].axis('off')
    axes[1, 0].set_title('Fourier Transform of Image')

    axes[1, 1].imshow(np.log(1 + np.abs(kernel_ft)), cmap='gray')
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Fourier Transform of Kernel')

    axes[1, 2].imshow(np.log(1 + np.abs(img_ft * kernel_ft)), cmap='gray')
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Multiplication in Fourier Domain')

    plt.show()
