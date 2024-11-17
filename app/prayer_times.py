from datetime import datetime

import requests
from tabulate import tabulate


class PrayerTimes:
    def __init__(self, city, country, logger, method=2):
        """
        Initialize the PrayerTimes object.

        Args:
            city (str): Name of the city.
            country (str): Name of the country.
            logger (Logger): Logger object to log messages.
            method (int): Calculation method for prayer times (default is 2).
        """
        self.city = city
        self.country = country
        self.logger = logger
        self.method = method
        self.base_url = 'http://api.aladhan.com/v1/timingsByCity'
        self.timings = {}

    def get_prayer_times(self):
        """
        Return the prayer times
        """
        self._fetch_prayer_times()
        self._display_prayer_times()
        self.logger.info(self._get_next_prayer())

    def _fetch_prayer_times(self):
        """
        Fetch prayer times from Aladhan API
        """
        params = {
            'city': self.city,
            'country': self.country,
            'method': self.method
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data['code'] == 200:
                self.timings = data['data']['timings']
            else:
                self.logger.error(f"Error: {data['status']}")
        except requests.exceptions.RequestException as e:
            self.logger.error(f'Error fetching data: {e}')

    def _display_prayer_times(self):
        """
        Display prayer times in a human-readable format
        """
        if not self.timings:
            self.logger.warning('No prayer times available.')
            return

        self.logger.info(f'Prayer times for {self.city}, {self.country}:')
        self._print_prayer_times()

    def _print_prayer_times(self):
        """
        Print the prayer times in a tabular format
        """
        current_time = datetime.now().strftime('%H:%M')
        current_time_dt = datetime.strptime(current_time, '%H:%M')

        prayers_to_print = ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']
        table = []
        for prayer, time in self.timings.items():
            if prayer in prayers_to_print:
                prayer_time_dt = datetime.strptime(time, '%H:%M')
                time_difference = prayer_time_dt - current_time_dt
                table.append([prayer, time, current_time, str(time_difference)])

        headers = ['Prayer', 'Time', 'Current Time', 'Time Difference']
        self.logger.info(tabulate(table, headers, tablefmt='grid'))

    def _get_next_prayer(self):
        """
        Return the next prayer time after the current time
        """
        if not self.timings:
            return None

        current_time = datetime.now().strftime('%H:%M')
        next_prayer = None
        next_prayer_time = None

        for prayer, time in self.timings.items():
            if time > current_time:
                next_prayer = prayer
                next_prayer_time = time
                break

        if next_prayer:
            # calculate the time difference
            current_time_dt = datetime.strptime(current_time, '%H:%M')
            next_prayer_time_dt = datetime.strptime(next_prayer_time, '%H:%M')
            time_difference = next_prayer_time_dt - current_time_dt

            return f'Next prayer: {next_prayer} at {next_prayer_time} in {time_difference}'
        else:
            return 'No more prayers for today.'
