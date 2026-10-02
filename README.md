# Sudo Weather Tracker

This project adds a terminal app for a green-water planet called Sudo. It simulates precipitation, wind, humidity, thunderstorm days, and lightning events for a 7-day cycle.

## Features
- 7-day rainfall and weather analysis
- Random-but-planet-appropriate values for Sudo
- Extreme storm mode triggered by `0000`
- Reset command to restore normal conditions
- Weekly totals and daily metrics

## Commands
- `YY` — show a 7-day realistic forecast for Sudo
- `0000` — trigger extreme weather for the next 7 days
- `RESET` — clear the storm state and reset the weather system
- `HELP` — display the command list
- `EXIT` — leave the app

## Weather scale used
This simulator uses a realistic reference range for an extreme storm world:
- Humidity: 90% to 100% during storm mode
- Rainfall: 500 mm to 2500 mm per day during extreme storm conditions
- Wind: up to 3500 mph in severe storm cycles
- Thunderstorms and lightning can appear several times per week during extreme conditions

## Run it
```bash
python3 sudo.py
```
