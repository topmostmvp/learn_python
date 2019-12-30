import csv
from datetime import datetime
import matplotlib.pyplot as plt 


filename = 'Beijing_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(current_date, 'missing date')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

fig = plt.figure(figsize=(10,6), dpi=128)
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperatures', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)


plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()