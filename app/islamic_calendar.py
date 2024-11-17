from datetime import datetime

from convertdate import islamic


class IslamicCalendar:
    def __init__(self, logger):
        """
        Initializes the Islamic (Hijri) calendar.

        Args:
            logger (Logger): Logger object to log messages.
        """
        self.logger = logger
        self.gregorian_today = datetime.today()
        self.hijri_today = islamic.from_gregorian(self.gregorian_today.year, self.gregorian_today.month,
                                                  self.gregorian_today.day)

    def get_hijri_date(self):
        """
        Returns the current Islamic (Hijri) date in the format (Day, Month, Year).
        """
        hijri_day, hijri_month, hijri_year = self.hijri_today
        return hijri_day, hijri_month, hijri_year

    def display_hijri_date(self):
        """
        Display the current Islamic (Hijri) date.
        """
        hijri_day, hijri_month, hijri_year = self.get_hijri_date()
        self.logger.info(
            f"Today's Islamic (Hijri) date is: {hijri_day} {self.get_hijri_month_name(hijri_month)} {hijri_year}")

    @staticmethod
    def get_hijri_month_name(month_number):
        """
        Convert the numeric month (1-12) to the Islamic month name.

        Args:
            month_number (int): The numeric month (1-12).

        Returns:
            month (str): The name of the Islamic month.
        """
        hijri_month_names = [
            'Muharram', 'Safar', 'Rabi\' al-Awwal', 'Rabi\' al-Thani', 'Jumada al-Awwal', 'Jumada al-Thani',
            'Rajab', 'Sha\'ban', 'Ramadan', 'Shawwal', 'Dhul-Qi\'dah', 'Dhul-Hijjah'
        ]
        return hijri_month_names[month_number - 1]
