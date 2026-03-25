import matplotlib.pyplot as plt

def plotLineChart(data: list):
    list_of_hr = data["data"]["cleaned_data"]
    filename = data["data"]["filename"]
    plot = plt.plot(list_of_hr)
    plt.savefig(f'./images/{filename}.jpg', dpi=300, bbox_inches="tight")
    plt.close()
    return plot