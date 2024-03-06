"""
    Mandelbrot Script
"""
import argparse
import numpy as np


def mandelbrot(c, max_iter):
    """
    Mandelbrot Iterator.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


def generate_mandelbrot(width, height, x_minmax, y_minmax, max_iter):
    """
    Generates the Mandelbrot set.
    """
    x_min, x_max = x_minmax
    y_min, y_max = y_minmax
    mandelbrot_set = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            real = x_min + (x_max - x_min) * j / (width - 1)
            imag = y_min + (y_max - y_min) * i / (height - 1)
            c = complex(real, imag)
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_set


def draw_mandelbrot(mandelbrot_set, characters=" #@"):
    """
    Prints the Mandelbrot set to stdout.
    """
    max_iter = np.max(mandelbrot_set)
    for row in mandelbrot_set:
        for col in row:
            index = int(col / max_iter * (len(characters) - 1))
            print(characters[index], end="")
        print()


def save_mandelbrot_pdf(mandelbrot_set, filename="mandelbrot.pdf"):
    """
    Saves the Mandelbrot set as a PDF.
    """
    import matplotlib.pyplot as plt

    plt.imshow(mandelbrot_set, cmap="hot", origin="lower")
    # plt.colorbar(label='Iterations')
    plt.axis("off")
    plt.savefig(filename, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Mandelbrot set")
    parser.add_argument("--pdf", action="store_true", help="Save as PDF")
    args = parser.parse_args()

    WIDTH = 120
    HEIGHT = 50
    X_MINMAX = (-2, 1)
    Y_MINMAX = (-1, 1)
    MAX_ITER = 50
    CHARACTERS = " .:-=+*#%@"
    if args.pdf:
        WIDTH = 800
        HEIGHT = 600

    mandelbrot_array = generate_mandelbrot(
        WIDTH, HEIGHT, X_MINMAX, Y_MINMAX, MAX_ITER
    )

    if args.pdf:
        save_mandelbrot_pdf(mandelbrot_array)
        print("Mandelbrot set saved as 'mandelbrot.pdf'")
    else:
        draw_mandelbrot(mandelbrot_array, CHARACTERS)
