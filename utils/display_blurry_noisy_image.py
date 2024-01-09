import matplotlib.pyplot as plt


def display_blurry_noisy_image(img, img_blurry, img_blurry_noisy):
    fig, axes = plt.subplots(1, 3, figsize=(20, 10))

    axes[0].imshow(img, cmap='gray')
    axes[0].axis('off')
    axes[0].set_title('Original Image')

    axes[1].imshow(img_blurry, cmap='gray')
    axes[1].axis('off')
    axes[1].set_title(f'Blurry Image')

    axes[2].imshow(img_blurry_noisy, cmap='gray')
    axes[2].axis('off')
    axes[2].set_title(f'Blurry + Noisy image')