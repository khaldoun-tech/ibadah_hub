import math

import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim


class QiblaDirection:
    def __init__(self, city, country, logger):
        """
        Initializes the Qibla direction calculation.
        """
        self.logger = logger
        self.city_lat, self.city_lon = self._get_latitude_and_longitude(city, country)

        # Coordinates of the Kaaba in Mecca (in degrees)
        self.kaaba_lat = 21.4225
        self.kaaba_lon = 39.8262

    @staticmethod
    def _get_latitude_and_longitude(city, country):
        """
        Get the latitude and longitude of a city using the geopy library.

        Args:
            city (str): The name of the city.
            country (str): The name of the country.

        Return:
            result (tuple): A tuple containing the latitude and longitude of the city.
        """

        geolocator = Nominatim(user_agent='Geopy Library')
        location = geolocator.geocode(f'{city}, {country}')

        return location.latitude, location.longitude

    def calculate_qibla(self):
        """
        Calculates the Qibla direction from the given city coordinates to the Kaaba.

        Returns:
            qibla_angle (float): The Qibla direction in degrees (clockwise from true north).
        """
        delta_lon = math.radians(self.kaaba_lon - self.city_lon)
        city_lat_rad = math.radians(self.city_lat)
        kaaba_lat_rad = math.radians(self.kaaba_lat)

        # Qibla direction calculation formula
        x = math.sin(delta_lon) * math.cos(kaaba_lat_rad)
        y = math.cos(city_lat_rad) * math.sin(kaaba_lat_rad) - (
                math.sin(city_lat_rad) * math.cos(kaaba_lat_rad) * math.cos(delta_lon))

        # Calculate the direction in radians
        qibla_angle = math.atan2(x, y)
        qibla_angle = math.degrees(qibla_angle)  # Convert to degrees
        qibla_angle = (qibla_angle + 360) % 360  # Normalize the angle to [0, 360]

        return qibla_angle

    def display_qibla_direction(self):
        """
        Display the Qibla direction in a human-readable format and draw a compass.
        """
        qibla_angle = self.calculate_qibla()
        self.logger.info(f'The Qibla direction from your location is: {qibla_angle:.2f} '
                         f'degrees (clockwise from North).')

        # Draw the compass
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)

        # Draw the compass circle
        compass_circle = plt.Circle((0, 0), 1, color='black', fill=False)
        ax.add_artist(compass_circle)

        # Draw the North arrow
        ax.arrow(0, 0, 0, 1, head_width=0.1, head_length=0.1, fc='blue', ec='blue')
        ax.text(0, 1.1, 'N', ha='center', va='center', fontsize=12, color='blue')

        # Draw the Qibla direction arrow
        qibla_radians = np.radians(qibla_angle)
        ax.arrow(0, 0, np.sin(qibla_radians), np.cos(qibla_radians), head_width=0.1, head_length=0.1, fc='red',
                 ec='red')
        ax.text(np.sin(qibla_radians) * 1.1, np.cos(qibla_radians) * 1.1, 'Qibla', ha='center', va='center',
                fontsize=12, color='red')

        plt.title('Qibla Direction')
        plt.show()
