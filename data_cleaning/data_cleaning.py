def clean_heartrate_data(data: list) -> tuple:
    poor_data_quality_capture = 0
    for i,hr in enumerate(data):
        if (hr == "" or hr == "NO DATA"):
            poor_data_quality_capture += 1
            data.remove(hr)
        data[i] = int(data[i])
    return {"data": data, "poor_data_quality_capture": poor_data_quality_capture}