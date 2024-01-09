import matplotlib.pyplot as plt

def display_lsi_system(imgs, kernel, imgs_conv):
    fig, axes = plt.subplots(3, 3, figsize=(10, 10))

    labels = [['Input', 'Shifted Input', 'Linear Combination of Inputs'],
              ['Point Spread Function', 'Shift-Invariance', 'Linearity'],
              ['Output', 'Shifted Output', 'Linear Combination of Outputs']]

    for i in range(3):
        for j, data in enumerate([imgs[i], kernel, imgs_conv[i]]):
            axes[i, j].imshow(data, cmap='gray')
            axes[i, j].axis('off')
            axes[i, j].set_title(labels[i][j])  # Fix the indexing here

    plt.tight_layout()
    plt.show()
