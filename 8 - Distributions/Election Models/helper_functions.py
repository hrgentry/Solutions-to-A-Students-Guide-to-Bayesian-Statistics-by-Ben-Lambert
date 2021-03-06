import matplotlib.pyplot as plt


def plotter(parameter1_range, parameter2_range, value_grid, title_string, x_label, y_label, colormap = plt.cm.viridis):
    """
        Creates a 2D contour plot over two parameters.
    """

    plt.contourf(parameter1_range, parameter2_range, value_grid, cmap=colormap)
    plt.colorbar()

    plt.title(title_string)

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.show()
