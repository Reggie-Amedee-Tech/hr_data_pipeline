import os
import matplotlib.pyplot as plt
from data_cleaning import data_cleaning
from data_analysis import data_analysis
from data_visualizations import data_visualizations

list_of_phases = os.listdir("./data/")

def run(file: str):
    filename = file[7:]

    data = []
    with open(file, "r") as file:
        for line in file:
            data.append(line.replace('\n', ""))

    cleaned_list = data_cleaning.clean_heartrate_data(data)

    avg = data_analysis.average(cleaned_list)
    med = data_analysis.median(cleaned_list)
    ran = data_analysis.range(cleaned_list)
    var = data_analysis.variance(cleaned_list)
    
    data_visualizations.plotLineChart(cleaned_list)
    plt.savefig(f'./images/{filename}.jpg', dpi=300, bbox_inches="tight")
    plt.close()

    return f'{file} metrics: \n Average: {avg} \n Median: {med} \n Range: {ran} \n Amount of poor data quality captured: {cleaned_list["poor_data_quality_capture"]} \n Variance: {var}'


for phase in list_of_phases:
    run(f'./data/{phase}')

# if __name__ == "__main__":
#     run("data/phase0.txt")
#     run("data/phase1.txt")
#     run("data/phase2.txt")
#     run("data/phase3.txt")
#     run("data/phase4.txt")


