[![Build Status](https://travis-ci.com/prodekan/smhi-primitive.svg?branch=master)](https://travis-ci.com/prodekan/smhi-primitive)
# smhi-primitive-query

## Basic setup

Install the requirements:
```
$ pip install -r requirements.txt
```

Run the application:
```
$ python -m smhi_primitive_query --help
```
## Intro

This application provides 2 options:
1. *forecast* data for for which it expects the longitude and latitude parameters
2. *history* data which can be obtained without parameters

- The `forecast` data is taken for a fixed forcasting model (pmp3g). We take the provided URL from SMHI
to query for a 10 day forecast. `'/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json'`
The data response is in json.
Running the `--help` command gives u this:
```
> python -m smhi-primitive-query forecast --help
Usage: smhi-primitive-query.py forecast [OPTIONS]

  Forecast on smhi_primitive_query

Options:
  --lon FLOAT  Longitude
  --lat FLOAT  Latitude
  --help       Show this message and exit.

```

- For the `historic` data the we get is in `CSV` format (crazy, I know). Because the API on SMHI 
is structured the way it is (it is kind of zooming in on the data from left to right [looking at the URL]) 
we first loop over all possible paramters (values that are measured by stations) and create for a single station the csv file with historic data.
Running the `--help` command gives u this:
``` 
> python -m smhi-primitive-query history --help 
Usage: smhi-primitive-query.py history [OPTIONS]

  History on smhi_primitive_query We took the default station id to be
  "Skillinge" https://www.smhi.se/en/weather/sweden-weather/observations#ws=
  wpt-a,proxy=wpt-a,tab=all,stationid=54290,type=weather I think this is the
  nearest weather station to Simris

Options:
  --station INTEGER  Station ID for which to get the data
  --help             Show this message and exit.

```
### Parameters
The list of parameters is in the file `all_paramaters.json`. 


| key | title                               | summary                                                                        |
|-----|-------------------------------------|--------------------------------------------------------------------------------|
| 1   | air temperature                     | instantaneous value            1 time / hour                                   |
| 2   | air temperature                     | average 1 day                  1 time / day                      at 00         |
| 3   | wind direction                      | average 10 min                 1 time / h                                      |
| 4   | wind speed                          | average 10 min                 1 time / h                                      |
| 5   | precipitation                       | sum 1 day                      1 time / day                      at 06         |
| 6   | relative humidity                   | instantaneous value            1 time / hour                                   |
| 7   | precipitation                       | sum 1 hour                     1 time / hour                                   |
| 8   | snow depth                          | instant value                  1 time / day                      at 06         |
| 9   | Air pressure reduced sea level      | at sea level                   instantaneous value               1 time / hour |
| 10  | Sunshine                            | sum 1 hour                     1 time / hour                                   |
| 11  | Global Irradians (Swedish stations) | average 1 hour                 1 time / hour                                   |
| 12  | Vision                              | instantaneous value            1 time / hour                                   |
| 13  | present weather                     | instantaneous value            1 time / hour and 8 times / day                 |
| 14  | precipitation                       | sum 15 min                     4 times / hr                                    |
| 15  | precipitation intensity             | max during 15 min              4 times / h                                     |
| 16  | Total cloud amount                  | instantaneous value            1 time / hour                                   |
| 17  | precipitation                       | 2 times / day                  at 06 and 18                                    |
| 18  | precipitation                       | 1 time / day                   at 18                                           |
| 19  | air temperature                     | mine                           once a day                                      |
| 20  | air temperature                     | max                            once a day                                      |
| 21  | Byvind                              | max                            1 time / hour                                   |
| 22  | air temperature                     | funds                          once a month                                    |
| 23  | precipitation                       | sum                            once a month                                    |
| 24  | Long-wave Irradians                 | Long-wave radiation            average 1 hour                    every hour    |
| 25  | Max of Average Wind Speed           | maximum of average 10 minutes  for 3 hours                       1 time / hour |
| 26  | air temperature                     | mine                           2 times a day                     at 06 and 18  |
| 27  | air temperature                     | max                            2 times a day                     at 06 and 18  |
| 28  | Molnbas                             | lowest cloud layer             instantaneous value               1 time / hour |
| 29  | cloud amount                        | lowest cloud layer             instantaneous value               1 time / hour |
| 30  | Molnbas                             | other cloud layers             instantaneous value               1 time / hour |
| 31  | cloud amount                        | other cloud layers             instantaneous value               1 time / hour |
| 32  | Molnbas                             | third cloud layer              instantaneous value               1 time / hour |
| 33  | cloud amount                        | third cloud layer              instantaneous value               1 time / hour |
| 34  | Molnbas                             | fourth cloud layer             instantaneous value               1 time / hour |
| 35  | cloud amount                        | fourth cloud layer             instantaneous value               1 time / hour |
| 36  | Molnbas                             | lowest cloud base              instantaneous value               1 time / hour |
| 37  | Molnbas                             | lowest cloud base              mine under 15 minutes             1 time / hour |

### Example:
Get the history. The default station is 54290 which is near *Simris*.
```
python -m smhi-primitive-query history

```

Get forecasts. Here we provide longitude and latitude that are *Simris*
```
python -m smhi-primitive-query forecast --lon 14.31 --lat 55.53

```
