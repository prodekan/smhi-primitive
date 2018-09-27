import click
import requests
available_parameters = [21, 11, 22, 26, 27, 19, 1, 2, 20, 9, 24, 25, 28, 30, 32,
                        34, 36, 37, 29, 31, 33, 35, 17, 18, 15, 23, 14, 5, 7,
                        13, 6, 12, 8, 10, 16, 4, 3]

avalialbe_periods = {'hour': 'latest-hour',
                     'day': 'latest-day',
                     'last-months': 'latest-months',
                     'all': 'corrected-archive'}
observation = {
    'base_url': 'https://opendata-download-metobs.smhi.se',
    'api_version': '1.0',
    'path': '/api/version/1.0/parameter/{param}/station/{station}/period/{period}/data.csv'
}

forecasts = {
    'base_url': 'https://opendata-download-metfcst.smhi.se',
    'api_version': '2',
    'path': '/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json'
}


def save_to_csv(name, content):
    print('Writing {}'.format(name))
    with open(name, 'w') as f:
        f.write(content)


def query(url):
    return requests.get(url)


@click.group(invoke_without_command=True)
@click.option('--version', '-v', is_flag=True, help='Print application version')
def smhi_primitive_query(version):
    if version:
        click.echo('Version: {}'.format('0.1.0'))


@smhi_primitive_query.command()
@click.option('--station', default=54290, help='Station ID for which to get the data')
def history(station):
    """History on smhi_primitive_query
    We took the default station id to be "Skillinge"
    https://www.smhi.se/en/weather/sweden-weather/observations#ws=wpt-a,proxy=wpt-a,tab=all,stationid=54290,type=weather
    I think this is the nearest weather station to Simris
    """
    click.echo(
        'Historical CSV data. All parameters')
    click.echo('For Station ID: {}'.format(station))
    for param in available_parameters:
        url = observation['base_url'] + \
            observation['path'].format(
                param=param, station=station, period=avalialbe_periods['all'])
        print(url)
        content = query(url)
        save_to_csv(
            'station_{station}-param{param}_{period}.csv'.format(station=str(station),
                                                                 param=str(
                                                                     param),
                                                                 period=avalialbe_periods['all']),
            content.text)

    for param in available_parameters:
        url = observation['base_url'] + \
            observation['path'].format(
                param=param, station=station, period=avalialbe_periods['last-months'])
        print(url)
        content = query(url)
        save_to_csv(
            'station_{station}-param{param}_{period}.csv'.format(station=str(station),
                                                                 param=str(
                                                                     param),
                                                                 period=avalialbe_periods['last-months']),
            content.text)


@smhi_primitive_query.command()
@click.option('--lon',
              default=14.31,
              help='Longitude')
@click.option('--lat',
              default=55.53,
              help='Latitude')
def forecast(lon, lat):
    '''Forecast on smhi_primitive_query'''
    click.echo('smhi_primitive_query forecast for ({},{})'.format(lon, lat))
    url = forecasts['base_url'] + forecasts['path'].format(lon=lon, lat=lat)
    print(url)
    print(query(url).json())


if __name__ == '__main__':
    smhi_primitive_query()
