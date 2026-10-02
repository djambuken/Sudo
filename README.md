# Sudo [PLANET] ^@^ ! // A code for a tracker and machine for weather for a green-water filled planet named Sudo.

It simulates precipitation, wind, humidity, thunderstorm days, and lightning events for a 7-day cycle.

## Features
- 7-day rainfall and weather analysis
- Extreme storm mode triggered by `0000`
- Reset command to restore normal conditions
- Weekly totals and daily metrics

## Commands
- `YY` — show the past 7 days of baseline weather, including after a storm forecast
- `0000` — show a separate extreme-weather forecast for the next 7 days
- `RESET` — clear the storm state and reset the weather system
- `HELP` — display the command list
- `EXIT` — leave the app

## Weather scale used
This simulator uses a realistic reference range for an extreme storm world:
- Humidity: 94% to 100% during storm mode
- Rainfall: about 1,950 mm to 4,250 mm per day during extreme storm conditions, increasing with humidity
- Wind: 1,000 to 2,000 mph in baseline weeks; 3,000 to 3,500 mph in storm mode
- Thunderstorms and lightning can appear several times per week during extreme conditions

## Make it available to users

Make the GitHub repository public, then share this link:
[https://github.com/djambuken/Sudo](https://github.com/djambuken/Sudo)

Users need Python 3 and Git. To download and start the app, they can run:
```bash
git clone https://github.com/djambuken/Sudo.git
cd Sudo
python3 sudo.py
```

Alternatively, users can select **Code > Download ZIP** on GitHub, extract the archive, open a terminal in the extracted `Sudo` folder, and run `python3 sudo.py`.

## Run it

From the project folder, run:
```bash
python3 sudo.py
```

Enter `0000` to display the extreme-weather forecast. Enter `YY` to display baseline weather.
