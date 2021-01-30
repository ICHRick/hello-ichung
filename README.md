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

## Quick Start
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

### For example:

```
$ ./suggest-time '2020-01-01 00:00:00' '2021-01-01 00:13:00' BTC
```

The application should output the suggestion for the following format:

```
buy time: 2020-03-13 02:15:00
sell time: 2020-12-31 00:20:00
profit: 25369.71
```
## Source Code
The folder `Source Code` includes the original code script and files that would pack as the executable file (i.e., suggest-time).
