#!/usr/bin/env python3
"""Sudo Planet Weather Tracker

A terminal-based simulator for a green-water world named Sudo.
Displays the past 7 days of the calendar week in order and supports
extreme weather commands for the next 7-day simulation.

Commands:
    YY      = show the past 7 days of rainfall and storm data
    0000    = trigger extreme storm conditioning for the next 7 days
    RESET   = clear storm effects and restore baseline conditions
    HELP    = show commands
    EXIT    = close the application
"""

import random

RED = "\033[31m"
RESET = "\033[0m"


def red_label(text):
    return f"{RED}{text}{RESET}"


class SudoWeatherTracker:
    def __init__(self):
        self.storm_mode = False
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def baseline_day(self, day_index):
        wind = round(random.uniform(1000, 2000), 1)
        humidity = round(random.uniform(58, 84), 1)
        rainfall = round(random.uniform(80, 520), 1)
        thunderstorm = random.randint(0, 2)
        lightning = random.randint(0, 2)
        return {
            "day": day_index,
            "wind_mph": wind,
            "humidity_pct": humidity,
            "rainfall_mm": rainfall,
            "thunderstorms": thunderstorm,
            "lightning_storms": lightning,
            "storm_mode": False,
        }

    def extreme_day(self, day_index):
        humidity = round(random.uniform(94, 100), 1)
        wind = round(random.uniform(3000, 3500), 1)
        humidity_intensity = (humidity - 94) / 6
        rainfall = round(2200 + (1800 * humidity_intensity) + random.uniform(-250, 250), 1)
        thunderstorm = random.randint(2, 6)
        lightning = random.randint(1, 6)
        return {
            "day": day_index,
            "wind_mph": wind,
            "humidity_pct": humidity,
            "rainfall_mm": rainfall,
            "thunderstorms": thunderstorm,
            "lightning_storms": lightning,
            "storm_mode": True,
        }

    def generate_day(self, day_index):
        if self.storm_mode:
            return self.extreme_day(day_index)
        return self.baseline_day(day_index)

    def generate_week(self):
        return [self.generate_day(i + 1) for i in range(7)]

    def print_week(self, heading, period_label):
        week = self.generate_week()
        total_rain = sum(day["rainfall_mm"] for day in week)
        avg_wind = sum(day["wind_mph"] for day in week) / len(week)
        avg_humidity = sum(day["humidity_pct"] for day in week) / 7
        total_thunder = sum(day["thunderstorms"] for day in week)
        total_lightning = sum(day["lightning_storms"] for day in week)

        print()
        print(heading)
        print("--------------------------------------------------")
        print(period_label)
        print("--------------------------------------------------")

        for i, day in enumerate(week):
            name = self.days_of_week[i]
            print(
                f"{name:>10} | Wind: {day['wind_mph']:>8.1f} mph | "
                f"Humidity: {day['humidity_pct']:>5.1f}% | "
                f"Rain: {day['rainfall_mm']:>7.1f} mm | "
                f"Thunderstorms: {day['thunderstorms']:>2} | "
                f"Lightning: {day['lightning_storms']:>2}"
            )

        print("--------------------------------------------------")
        print(
            f"WEEKLY TOTALS | Avg Wind: {avg_wind:>7.1f} mph | "
            f"Avg Humidity: {avg_humidity:>5.1f}% | "
            f"Rain: {total_rain:>9.1f} mm | "
            f"Thunderstorms: {total_thunder:>2} | "
            f"Lightning: {total_lightning:>2}"
        )
        print("--------------------------------------------------")
        print()

    def command_yy(self):
        period_label = "Next 7 Days of Extreme Storm Forecast" if self.storm_mode else "Past 7 Days of the Current Calendar Week"
        self.print_week("7-DAY RAINFALL & STORM DATA FOR PLANET SUDO", period_label)

    def command_0000(self):
        self.storm_mode = True
        print()
        print("0000 ENGAGED")
        print("EXTREME WEATHER SYSTEM ACTIVATED FOR THE NEXT 7 DAYS")
        print("Expect humidity-driven severe rainfall and violent winds up to 3500 MPH,")
        print("frequent thunderstorms, and lightning storms.")
        print()

    def command_reset(self):
        self.storm_mode = False
        print()
        print("RESET COMPLETE")
        print("Storm patterns cleared. Planet Sudo weather has returned to baseline conditions.")
        print()

    def command_help(self):
        print()
        print("SUDO COMMANDS")
        print("YY     => Show the past 7 days of rainfall and weather data")
        print("0000   => Trigger extreme weather conditions for the next 7 days")
        print("RESET  => Disable storm mode and return to baseline")
        print("HELP   => Show this command list")
        print("EXIT   => Close the Sudo weather app")
        print()


def main():
    tracker = SudoWeatherTracker()

    print()
    print(red_label("# Sudo [PLANET]"))
    print()
    print("Weather tracker online.")
    print("Enter 'YY' to show the current 7-day weather data.")
    print("Enter '0000' to activate extreme weather, then 'YY' to show it.")
    print("Type 'HELP' for command options.")
    print()

    while True:
        try:
            command = input("ENTER THE COMMAND ; ").strip().upper()
        except KeyboardInterrupt:
            print()
            print("App interrupted. Exiting.")
            break

        if command == "YY":
            tracker.command_yy()
        elif command == "0000":
            tracker.command_0000()
        elif command == "RESET":
            tracker.command_reset()
        elif command == "HELP":
            tracker.command_help()
        elif command in ("EXIT", "QUIT"):
            print("SYSTEM OFFLINE")
            break
        else:
            print("Unknown command. Type HELP for available commands.")
            print()


if __name__ == "__main__":
    main()
