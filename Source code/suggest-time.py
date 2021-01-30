"""
The implement of the program to find the best trade time for the maximum profit. 
Given a tradable time window and currency name, one buy time, one sell time, and the maximum profit would be output based on the currency's historical price data. Besides, the buy time is before the sell time.

Parameters 
<window-start-time>: Year-Month-Day Hour:Minute:Second  with leading zeros (e.g., '2020-01-01 00:00:00')
<window-end-time>: Year-Month-Day Hour:Minute:Second  with leading zeros (e.g., '2020-01-01 00:13:00')
<currency-name>: Currency name that is same as the data name (e.g., BTC)

Data:
The data are all in CSV format (e.g., BTC.csv) with headers:
```
Unix Timestamp,Date,Symbol,Open,High,Low,Close,Volume
```
Note:
(1) The time and price are referred to the columns with headers `Unix Timestamp`(or `Date`) and `Close`, respectively.
(2) Please place data in the folder 'assets'.

Quick start:
```
python suggest-time.py  '2020-01-01 00:00:00' '2021-01-01 00:13:00' BTC
```

"""

import sys
from os import path
import dask.dataframe as dd
import datetime
import re

def check_format(date_time):
    '''
    Check if the format of date_time is correct
    '''
    r = re.compile('.{4}-.{2}-.{2} .{2}:.{2}:.{2}')
    return len(date_time) == 19 and r.match(date_time)!= None
    

def Load_data(Currency_name):
    '''
    Load data according to the currency name in the folder 'assets'
    '''
    data = None
    try:
        price_data_path = './assets/{0}.csv'.format(Currency_name)
        data = dd.read_csv(price_data_path)[['Unix Timestamp', 'Date', 'Close']]
    except:
        assert data, 'Load Error, the file {0} is not found in the folder \'assets\' '.format(Currency_name+'.csv')

    return data


def date_to_Unix(date_time):
    '''
    Convert intput (date and clock time) to unix timestamp
    '''
    date, clock = date_time.split(' ')
    date, clock = list(map(int, date.split('-'), )), list(map(int, clock.split(':'), ))
    year, minute, day, hh, mm, ss = date+clock
    date_datetime = datetime.datetime(year, minute, day, hh, mm, ss)
    difference = date_datetime - datetime.datetime(1970,1,1)

    return (difference.microseconds + (difference.seconds + difference.days * 86400) * 10**3)


def find_suggest_time(Time_from, Time_to, data):
    '''
    Find the best trade time for the maximum profit
    '''
    # Convert time in the form of Unix Timestamp
    Time_from_Unix = date_to_Unix(Time_from)
    Time_to_Unix = date_to_Unix(Time_to)

    # Filter data for the valid period and select price and time
    df = data[(Time_from_Unix<=data['Unix Timestamp']) & (data['Unix Timestamp']<=Time_to_Unix)]
    assert len(df)>1, 'The time interval invalid. The records are less than 2.'
    Prices = df['Close'].compute().values
    Date = df['Date'].compute().values

    # Algorithm for the comparison of best max-profit time
    # # Only ascent price trend would increase the profit.
    # # The max-profit can be found by saving the lowest price and update profit iteratively. 
    # Initial 
    min_price = float('inf')
    max_profit = 0
    min_index = -1
    max_set = None

    for i in range(len(Prices)-1, -1, -1):
        cur_profit = (Prices[i]-min_price).round(2)
        # Update the lowest time
        if Prices[i] < min_price:
            min_price = Prices[i] 
            min_index = i
        # Update the profit
        elif cur_profit > max_profit:
            max_profit = cur_profit
            max_set = (min_index, i)

    # Output
    if max_set:
        print('buy time:', Date[max_set[0]])
        print('sell time:',  Date[max_set[1]])
        print('profit:', max_profit)
    else:
        print('The prices are decreasing or same in the given window, which would not generate the profit.')


if __name__ == '__main__':
    # Parameters:
    try:
        Time_from, Time_to, Currency_name = sys.argv[1], sys.argv[2], sys.argv[3]
    except:
        print('Expected 3 parameters instead of {0} (given)'.format(len(sys.argv)-1))
    assert check_format(Time_from), 'Wrong date format!'
    assert check_format(Time_to), 'Wrong date format!'

    # Data
    data = Load_data(Currency_name)

    # find the suggest time
    find_suggest_time(Time_from, Time_to, data)