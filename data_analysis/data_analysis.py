import math
import numpy as np

def average(data: list) -> float:
    sum_of_hr = sum(data["data"])
    avg_of_hr = sum_of_hr / len(data['data'])
    return avg_of_hr


def median(data: list) -> float:
    med = 0
    halfway_point = len(data["data"]) / 2
    if(halfway_point % 1):
        floored_hwp = math.floor(halfway_point)
        med = int((data['data'][floored_hwp] + data['data'][floored_hwp + 1]) / 2)
        return med
    med = data['data'][int(halfway_point)]
    return med


def range(data: list) -> float:
    sorted_hrs = sorted(data["data"])
    range = sorted_hrs[-1] - sorted_hrs[0]
    return range

def variance(data: list) -> float:
    var = np.variance(data)
    return var