def clean_heartrate_data(data: list) -> tuple:
    poor_data_quality_capture = 0
    for i,hr in enumerate(data['cleaned_data']):
        if (hr == "" or hr == "NO DATA"):
            poor_data_quality_capture += 1
            data['cleaned_data'].remove(hr)
        data['cleaned_data'][i] = int(data['cleaned_data'][i])
    return {"data": data, "poor_data_quality_capture": poor_data_quality_capture}