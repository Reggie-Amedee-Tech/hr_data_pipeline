import os
from data_cleaning import data_cleaning
from data_analysis import data_analysis
from data_visualizations import data_visualizations

list_of_phases = os.listdir("./data/")

def run(file: str):
    data = []
    with open(file, "r") as file:
        for line in file:
            data.append(line.replace('\n', ""))

    cleaned_list = data_cleaning.clean_heartrate_data(data)

    avg = data_analysis.average(cleaned_list)
    med = data_analysis.median(cleaned_list)
    ran = data_analysis.range(cleaned_list)
    var = data_analysis.variance(cleaned_list)
    
    line_plot = data_visualizations.plotLineChart(cleaned_list)

    print(f'{file} metrics: \n Average: {avg} \n Median: {med} \n Range: {ran} \n Amount of poor data quality captured: {cleaned_list["poor_data_quality_capture"]} \n Variance: {var}')
    return line_plot


for phase in list_of_phases:
    print(phase)
    run(f'./data/{phase}')


