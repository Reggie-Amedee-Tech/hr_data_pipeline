import matplotlib.pyplot as plt

def plotLineChart(data: list):
    plt.plot(data["data"])
    return plt.show()