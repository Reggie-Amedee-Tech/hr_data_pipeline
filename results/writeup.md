1) Which file appears to represent the most active period? Explain using at least two metrics. Consider that this is a 30 year old participant and compare your output to the column titled "Target HR Zone 50-85%" within this link: https://www.heart.org/en/healthy-living/fitness/fitness-basics/target-heart-rates

### Most Active Period
- I'd say the most active period would be phase one. This is the case because:
    - Average heart rate, **87.3** is the highest across all phases
    - Median heart rate, **89** is also the highest across all phases
    - According to the article provided in the first question, our average heart rate is actually lower then the national average.

2) Which file had the **poorest** data quality? How do you know?

### File with poorest data quality
- Phase/file 0 had the poorest data quality. This is the case because it had the most data that was considered "poor" quality, which in this case, is "NO DATA" or null.
- I captured this data by adding a counter in my clean_data function which returns an object, which would allow me to print it in our run function.

3) Suppose one heart-rate file contains the following cleaned values: `68, 70, 71, 72, 72, 73, 74, 75, 180`. The value 180 was recorded during a sensor glitch.

a) Calculate the range of this dataset.
- The range for this data set is 112!



b) Explain how the extreme value affects the range.
- This extreme value is an outlier and skews our data which doesnt accuratley represent our range.



c) Identify a different statistic that would better represent the typical variability of the dataset. Why would this measure be better?
- I would say the average is the better metric because average is **slightly** more resistent with outliers as opposed to ranges.
- A strong second measure that we can use is median, as it gets the middle of the data set which more accuratley represent the data we're looking for.

