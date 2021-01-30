## Suggest Time for Crypto Currencies

The implement of the program to find the best trade time for the maximum profit. 

Given a tradable a time window and currency name, one buy time, one sell time, and the maximum profit would be output based on the currency's historical price data. Besides, the buy time is before the sell time.

## Data Description
The data are all in CSV format (e.g., BTC.csv) with headers:

```
Unix Timestamp,Date,Symbol,Open,High,Low,Close,Volume
```

For the price, we only care about `Close` in this assignment.

Some sample data look like this:

```
1577837580000,2020-01-01 00:13:00,BTCUSD,7162.56,7162.56,7157.78,7157.78,3e-05
1577837520000,2020-01-01 00:12:00,BTCUSD,7162.88,7165.85,7161.64,7162.56,0.3269290054
1577837460000,2020-01-01 00:11:00,BTCUSD,7157.79,7167.82,7157.79,7162.88,0.25267007
1577837400000,2020-01-01 00:10:00,BTCUSD,7157.29,7169.27,7157.29,7157.79,0.27973615
1577837340000,2020-01-01 00:09:00,BTCUSD,7155.74,7157.3,7155.74,7157.29,4.49
```
Note:

(1) The time and price are referred to the columns with headers `Unix Timestamp`(or `Date`) and `Close`, respectively.

(2) Please place data in the folder 'assets'.

## Usage
Please wrap your application as a command-line executable with the following parameters:

```
$ ./suggest-time <window-start-time>, <window-end-time>, <currency-name>
```
### Parameters 
Three parameters indicate window-start-time, window-end-time, and currency-name. Their format are listed follows:
```
<window-start-time>: Year-Month-Day Hour:Minute:Second  with leading zeros (e.g., '2020-01-01 00:00:00')
<window-end-time>: Year-Month-Day Hour:Minute:Second  with leading zeros (e.g., '2020-01-01 00:13:00')
<currency-name>: Currency name that is same as the data name (e.g., BTC)
```

## Algorithm 

1. For the given parameters (currency name), the program read data with `Unix Timestamp`, `Date`, and `Close` corresponding to time and price.

2. According to the given time (start and end time), we select data in the valid time period in the form of the example of the problem.

3. To find the best two trade time (buy/sell) for the maximum profit, we need to find an increasing trend with a maximum difference. If we find that a point starts from a lower price and the price is increasing, we can compare the profit for each point and the past one. Therefore, we only need to set two variables `min_price` and `max_profit` to record the new low-price point and check if the profit is higher in the following timestamps.

4. After we check each timestamp, we return `max_profit`, start/end time point corresponding to `max_profit` as the buy/sell time.

## Complexity Analysis

Time complexity: 

The valid timestamp would be check once, and the time complexity is O(n).

Space complexity: 

We storage `min_price`, `max_profit`, and the corresponding timestamps, only constant-number variables are used. That is O(1).

## Development Environment
The algorithm is implemented by Python3.6 with requirements: 

  * dask==2021.1.1

  * numpy==1.19.5

  * pandas==1.1.5

  * pyinstaller==4.2

The usage of the scipt `suggest-time.py` is like follows:
```
python suggest-time.py <window-start-time> <window-end-time> <currency-name>
```

To pack the script and some dependencies, the module `pyinstaller` can build `suggest-time.py` as an executable file.
```
pyinstaller -F suggest-time.py
```

Besides the `suggest-time.py`, the files in the folder `source code` are log and debug files for `pyinstaller`.

Note that the folder 'suggest-time' is the unpacked version of the program including the main program `suggest-time` and dependencies.
