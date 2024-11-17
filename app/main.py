import geocoder

from app import QiblaDirection, PrayerTimes, IslamicCalendar
from app.logger import Logger


class MainApp:
    def __init__(self):
        self.city = None
        self.country = None
        self.logger = Logger()

    def set_city_and_country(self):
        """
        Set the city and country for the application.
        """
        self.city = input('Enter the city name: ')
        self.country = input('Enter the country:')

    def get_current_position(self):
        """
        Get the current user position (latitude and longitude).
        """
        self.logger.info('Getting current position...')
        g = geocoder.ip('me')

        return g.latlng

    def get_hijri_date(self):
        """
        Display the current Islamic (Hijri) date.
        """
        self.logger.info('Getting Hijri date...')
        calendar = IslamicCalendar(self.logger)
        calendar.display_hijri_date()

    def get_prayer_times(self):
        """
        Display prayer times in a human-readable format
        """
        self.logger.info('Fetching prayer times...')
        prayer_times = PrayerTimes(self.city, self.country, self.logger)
        prayer_times.get_prayer_times()

    def get_qibla_direction(self):
        """
        Display the Qibla direction in a human-readable format
        """
        self.logger.info('Getting Qibla direction...')
        qibla = QiblaDirection(self.city, self.country, self.logger)
        qibla.display_qibla_direction()

    def run(self):
        self.set_city_and_country()

        while True:
            self.logger.info('\nSelect an option:')
            self.logger.info('1. Change city and country')
            self.logger.info('2. Get Hijri date')
            self.logger.info('3. Get prayer times')
            self.logger.info('4. Get Qibla direction')
            self.logger.info('5. Exit')

            choice = input('Enter your choice (1-5): ')

            if choice == '1':
                self.set_city_and_country()
                self.logger.info("City and country updated.")
            elif choice == '2':
                self.get_hijri_date()
            elif choice == '3':
                self.get_prayer_times()
            elif choice == '4':
                self.get_qibla_direction()
            elif choice == '5':
                self.logger.info('Exiting...')
                break
            else:
                self.logger.error('Invalid choice. Please try again.')


if __name__ == '__main__':
    app = MainApp()
    app.run()
