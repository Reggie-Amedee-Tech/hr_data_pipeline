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
    
    data_payload = {"cleaned_data": data, "filename": filename}

    cleaned_list = data_cleaning.clean_heartrate_data(data_payload)

    list_of_hrs = cleaned_list["data"]["cleaned_data"]


    avg = data_analysis.average(list_of_hrs)
    med = data_analysis.median(list_of_hrs)
    ran = data_analysis.range(list_of_hrs)
    var = data_analysis.variance(list_of_hrs)
    
    data_visualizations.plotLineChart(cleaned_list)

    return f'{file} metrics: \n Average: {avg} \n Median: {med} \n Range: {ran} \n Amount of poor data quality captured: {cleaned_list["poor_data_quality_capture"]}  \n Variance: {var}'


for phase in list_of_phases:
    run(f'./data/{phase}')

# if __name__ == "__main__":
#     run("data/phase0.txt")
#     run("data/phase1.txt")
#     run("data/phase2.txt")
#     run("data/phase3.txt")
#     run("data/phase4.txt")


