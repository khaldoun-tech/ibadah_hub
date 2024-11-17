# IbadahHub

IbadahHub is an AI-powered assistant for prayer times, notifications, Qibla direction, and Islamic calendar services. It
provides accurate prayer times, real-time Qibla directions, and Islamic calendar conversions based on the location of
your choice.

## Features

- **Prayer Time Calculations**: Calculates prayer times based on the user's input.
- **Notifications**: Sends notifications for upcoming prayer times.
- **Qibla Direction**: Calculates the Qibla direction using Geopy Library.
- **Islamic Calendar**: Converts Gregorian dates to Islamic (Hijri) dates.

## Installation

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```sh
python main.py
```

## Configuration

### Setting City and Country

You can set the city and country for which you want to calculate prayer times and Qibla direction by following the
prompts in the application.

### Notifications

The application will send desktop notifications for upcoming prayer times. You can configure the notification interval
in the PrayerNotifications class.

## Dependencies

geocoder: For getting the current location.
plyer: For sending desktop notifications.
tabulate: For displaying options in a table format.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## Acknowledgements

- [Geopy](https://geopy.readthedocs.io/en/stable/) for calculating the Qibla direction.
- [PrayTimes](http://praytimes.org/) for calculating prayer times.
- [Hijri Converter](https://pypi.org/project/convertdate/) for converting Gregorian dates to Islamic (Hijri) dates.
