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

To run the tests:
```
    $ pytest
```

## Intro

This application provides 2 options:
1. *forecast* data for for which it expects the longitude and latitude parameters
2. *history* data which can be obtained without parameters

The forecast data is taken for a fixed forcasting model (pmp3g). We take the provided URL from SMHI
to query for a 10 day forecast. `'/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json'`
The data response is in json.

For the historic data the we get is in CSV format (crazy, I know). Because the API on SMHI 
is structured the way it is (it is kind of zooming in on the data from left to right [looking at the URL]) 
we first loop over all possible paramters (values that are measured by stations) and create for a single station the csv file with historic data.

### Example:
Get the history. The default station is 54290 which is near *Simris*.
```
python -m smhi-primitive-query history

```

Get forecasts. Here we provide longitude and latitude that are *Simris*
```
python -m smhi-primitive-query forecast --lon 14.31 --lat 55.53
```
