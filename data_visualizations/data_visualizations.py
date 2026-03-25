import matplotlib.pyplot as plt

def plotLineChart(data: list):
    plot = plt.plot(data["data"])
    # plt.savefig(f'./images/my_plot.png', dpi=300, bbox_inches="tight")
    return plot