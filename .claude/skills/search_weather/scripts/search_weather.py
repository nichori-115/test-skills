import sys
def main(city_name: str, date: str) -> None:
    print(f"Searching weather for {city_name} on {date}")
    print("Weather search completed.")
    print(f"city_name: {city_name}, date: {date}, weather: sunny, 25C")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python search_weather.py <city_name> <date>")
    else:
        main(sys.argv[1], sys.argv[2])