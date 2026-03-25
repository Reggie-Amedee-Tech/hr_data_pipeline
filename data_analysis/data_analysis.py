import math
import numpy as np

def average(data: list) -> float:
    sum_of_hr = sum(data)
    avg_of_hr = sum_of_hr / len(data)
    return avg_of_hr


def median(data: list) -> float:
    med = 0
    halfway_point = len(data) / 2
    if(halfway_point % 1):
        floored_hwp = math.floor(halfway_point)
        med = int((data[floored_hwp] + data[floored_hwp + 1]) / 2)
        return med
    med = data[int(halfway_point)]
    return med


def range(data: list) -> float:
    sorted_hrs = sorted(data)
    range = sorted_hrs[-1] - sorted_hrs[0]
    return range

def variance(data: list) -> float:
    var = np.var(data)
    return var