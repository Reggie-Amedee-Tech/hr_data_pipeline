import math
import os

# with open("./data/phase0.txt", "r") as file:
#     phase_zero_hr = []
#     for line in file:
#         phase_zero_hr.append(line.replace('\n', ""))

# with open("./data/phase1.txt", "r") as file:
#     phase_one_hr = []
#     for line in file:
#         phase_one_hr.append(line.replace('\n', ""))

# with open("./data/phase2.txt", "r") as file:
#     phase_two_hr = []
#     for line in file:
#         phase_two_hr.append(line.replace('\n', ""))

# with open("./data/phase3.txt", "r") as file:
#     phase_three_hr = []
#     for line in file:
#         phase_three_hr.append(line.replace('\n', ""))

list_of_phases = os.listdir("../data")

# print(list_of_phases)
    


def clean_heartrate_data(data: list) -> tuple:
    poor_data_quality_capture = 0
    for i,hr in enumerate(data):
        if (hr == "" or hr == "NO DATA"):
            poor_data_quality_capture += 1
            data.remove(hr)
        data[i] = int(data[i])
    return {"data": data, "poor_data_quality_capture": poor_data_quality_capture}

# c0 = clean_heartrate_data(phase_zero_hr)
# c1 = clean_heartrate_data(phase_one_hr)
# c2 = clean_heartrate_data(phase_two_hr)
# c3 = clean_heartrate_data(phase_three_hr)


def average(data: list) -> float:
    sum_of_hr = sum(data["data"])
    avg_of_hr = sum_of_hr / len(data['data'])
    return avg_of_hr

# average(c0)
# average(c1)
# average(c2)
# average(c3)


def median(data: list) -> float:
    med = 0
    halfway_point = len(data["data"]) / 2
    if(halfway_point % 1):
        floored_hwp = math.floor(halfway_point)
        med = int((data['data'][floored_hwp] + data['data'][floored_hwp + 1]) / 2)
        return med
    med = data['data'][int(halfway_point)]
    return med

# median(c0)
# median(c1)
# median(c2)
# median(c3)


def range(data: list) -> float:
    sorted_hrs = sorted(data["data"])
    range = sorted_hrs[-1] - sorted_hrs[0]
    return range



# def rolling_avg(data: list, k: int) -> float:
#     """
#     CHALLENGE FUNCTION (Optional)
#     """
#     pass


def run(file: str):
    data = []
    with open(file, "r") as file:
        for line in file:
            data.append(line.replace('\n', ""))

    cleaned_list = clean_heartrate_data(data)

    avg = average(cleaned_list)
    med = median(cleaned_list)
    ran =range(cleaned_list)

    print(f'{file} metrics: \n Average: {avg} \n Median: {med} \n Range: {ran} \n Amount of poor data quality captured: {cleaned_list["poor_data_quality_capture"]}')



# if __name__ == "__main__":
#     run("data/phase0.txt")
#     run("data/phase1.txt")
#     run("data/phase2.txt")
#     run("data/phase3.txt")
#     run("data/phase4.txt")

for phase in list_of_phases:
    run(f'./data/{phase}')



# Loop through list
