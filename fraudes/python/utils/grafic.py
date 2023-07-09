import numpy as np
import matplotlib.pyplot as plt


def raincloud_image(data_x: list, feats: list, value: str, title: str):
    """Crea grafica tipo RainCloud.

    Args:
        data_x: valores númericos a gráficas, por el momento esta implementado
         para que la lista posea dos elementos.
        feats: nombres de los valores a graficar.
        value: nombre de la data_x
        title:  titulo de la gráfica.
    """
    fig, ax = plt.subplots(figsize=(8, 4))

    boxplots_colors = ["green", "blue"]

    # Boxplot data
    bp = ax.boxplot(data_x, patch_artist=True, vert=False)

    # Change to the desired color and add transparency
    for patch, color in zip(bp["boxes"], boxplots_colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.4)

    # Create a list of colors for the violin plots based on the number of features you have
    violin_colors = ["green", "blue"]

    # Violinplot data
    vp = ax.violinplot(
        data_x,
        points=500,
        showmeans=False,
        showextrema=False,
        showmedians=False,
        vert=False,
    )

    for idx, b in enumerate(vp["bodies"]):
        # Get the center of the plot
        m = np.mean(b.get_paths()[0].vertices[:, 0])
        # Modify it so we only see the upper half of the violin plot
        b.get_paths()[0].vertices[:, 1] = np.clip(
            b.get_paths()[0].vertices[:, 1], idx + 1, idx + 2
        )
        # Change to the desired color
        b.set_color(violin_colors[idx])

    # Create a list of colors for the scatter plots based on the number of features you have
    scatter_colors = ["darksalmon", "darksalmon"]

    # Scatterplot data
    for idx, features in enumerate(data_x):
        # Add jitter effect so the features do not overlap on the y-axis
        y = np.full(len(features), idx + 0.8)
        idxs = np.arange(len(y))
        out = y.astype(float)
        out.flat[idxs] += np.random.uniform(low=-0.05, high=0.05, size=len(idxs))
        y = out
        plt.scatter(features, y, s=0.4, c=scatter_colors[idx])

    plt.yticks(np.arange(1, 3, 1), feats)  # Set text labels.
    plt.xlabel(value)
    plt.title(title)
    plt.show()
