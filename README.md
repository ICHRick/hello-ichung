## Problem Statement

You're given the history price data for several crypto currencies.
The data indicate the prices of the currency for a given time.

Given a crypto currency and a time window, if you can only buy/sell it one time,
find the best timing for the buy/sell within the time window so that we can make the greatest profit.

For example, if we have the following data for a certain currency:

```
t1, 35.3
t2, 32.5
t3, 33.8
t4, 38.2
t5, 31.0
t6, 40.5
t7, 42.9
t8, 41.0
```

Given the time window `t1` to `t8`, the best timing would be `t5 to t7`

## Data Description

The data are all in CSV format with headers that look like this:

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
1577837280000,2020-01-01 00:08:00,BTCUSD,7155.22,7155.74,7155.22,7155.74,0.02724249
1577837220000,2020-01-01 00:07:00,BTCUSD,7155.23,7157.29,7155.22,7155.22,0.00080131
1577837160000,2020-01-01 00:06:00,BTCUSD,7155.0,7161.56,7155.0,7155.23,0.0304940988
1577837100000,2020-01-01 00:05:00,BTCUSD,7163.0,7163.59,7155.0,7155.0,28.19484272
1577837040000,2020-01-01 00:04:00,BTCUSD,7163.6,7163.6,7163.0,7163.0,1.75184352
1577836980000,2020-01-01 00:03:00,BTCUSD,7163.0,7163.6,7163.0,7163.6,0.00270608
1577836920000,2020-01-01 00:02:00,BTCUSD,7163.3,7164.22,7163.0,7163.0,0.06390411
1577836860000,2020-01-01 00:01:00,BTCUSD,7163.3,7164.23,7163.3,7163.3,0.00264583
1577836800000,2020-01-01 00:00:00,BTCUSD,7165.9,7170.79,7163.3,7163.3,0.00793095
```

## Submission

Your submission should have clear instructions on how to run your code. Please put the instruction in a file named `INSTRUCTION.md`.
You can assume that the code will be tested on a fresh installation of Ubuntu 16.04 and will not have any other editors/compilers/modules installed.
Any additional packages needed need to be specified in your documentation.

### 1. Please wrap your application as a command-line executable with the following parameters:

```
$ ./suggest-time <window-start-time>, <window-end-time>, <currency-name>
```

for example:

```
$ ./suggest-time '2020-01-01 00:00:00' '2020-01-01 00:13:00' BTC
```

The application should output the suggestion for the following format:

```
buy time: 2020-01-01 00:05:00
sell time: 2020-01-01 00:12:00
profit: 7.56
```

Please create a pull-request once you've done and let us know!

## Sample Test case:

```
$ ./suggest-time '2020-01-01 00:00:00' '2021-01-01 00:13:00' BTC

buy time: 2020-03-13 02:15:00
sell time: 2020-12-31 00:20:00
profit: 25369.71
```

### 2. Please compute and explain the Time/Space complexities of your algorithm in the file `INSTRUCTION.md`

## Evaluation

Your submission will be evaluated by:
- Correctness of the timing suggestions
- code quality and architecture
- Good programming practices such as clean code, clear comments, tests
- Description including algorithm explanation, project structure, API design (Feel free to replace this file with the Description one)
