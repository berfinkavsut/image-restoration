import matplotlib.pyplot as plt
import numpy as np


def display_deconvolution(img_blurry_noisy, h_inv, img_restored, img_blurry_noisy_ft, h_inv_ft, img_restored_ft):

    fig, axes = plt.subplots(2, 3, figsize=(15,10))

    axes[0, 0].imshow(img_blurry_noisy, cmap='gray')
    axes[0, 0].axis('off')
    axes[0, 0].set_title('Original Image')

    axes[0, 1].imshow(h_inv.real, cmap='gray')
    axes[0, 1].axis('off')
    axes[0, 1].set_title('Inverse Filter')

    axes[0, 2].imshow(img_restored.real, cmap='gray')
    axes[0, 2].axis('off')
    axes[0, 2].set_title('Deconvolution Solution')

    axes[1, 0].imshow(np.log(1 + np.abs(img_blurry_noisy_ft)), cmap='gray')
    axes[1, 0].axis('off')
    axes[1, 0].set_title('Fourier Transform of Image')

    axes[1, 1].imshow(np.log(1 + np.abs(h_inv_ft)), cmap='gray')
    axes[1, 1].axis('off')
    axes[1, 1].set_title('Fourier Transform of Inverse Filter')

    axes[1, 2].imshow(np.log(1 + np.abs(img_restored_ft)), cmap='gray')
    axes[1, 2].axis('off')
    axes[1, 2].set_title('Multiplication in Fourier Domain')