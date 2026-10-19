import argparse
import requests
import plotext as plt

from datetime import datetime

def get_location():
	r = requests.get("https://ipinfo.io/json", timeout=10)
	r.raise_for_status()
	lat, lon = r.json()["loc"].split(",")
	return float(lat), float(lon)

def cloud_cover(lat=None, lon=None):
	if lat is None or lon is None:
		lat, lon = get_location()
	r = requests.get(
		"https://api.open-meteo.com/v1/forecast",
		params={"latitude": lat, "longitude": lon, "current": "cloud_cover"},
		timeout=10,
	)
	r.raise_for_status()
	return r.json()["current"]["cloud_cover"]

def cloud_series(lat=None, lon=None):
	if lat is None or lon is None:
		lat, lon = get_location()
	r = requests.get(
		"https://api.open-meteo.com/v1/forecast",
		params={
			"latitude": lat, 
			"longitude": lon, 
			"current": "cloud_cover",
			"hourly": "cloud_cover",
			"past_days": 1,
			"forecast_days": 3,
			"timezone": "auto",
			},
		timeout=10,
	)
	r.raise_for_status()
	data = r.json()
	now = datetime.fromisoformat(data["current"]["time"])
	times = [datetime.fromisoformat(t) for t in data["hourly"]["time"]]
	return times, data["hourly"]["cloud_cover"], now

def plot(lat=None, lon=None):
	times, values, now = cloud_series(lat, lon)
	xs = [(t - now).total_seconds() / 3600 for t in times]
	past = [(x, v) for x, v in zip(xs, values) if -24 <= x <= 0]
	future = [(x, v) for x, v in zip(xs, values) if 0 <= x <= 48]

	figure = plt.figure
	figure.clear()
	figure.draw(
		figure.signal(
			[x for x, _ in past], [v for _, v in past]
		).label("Past 24h")
	)
	figure.draw(
		figure.signal(
			[x for x, _ in future], [v for _, v in future]
		).label("Next 48h")
	)
	figure.title("Cloud Cover Forecast")
	figure.label("Hours from now", axis="x")
	figure.label("Cloud Cover (%)", axis="y")
	figure.ruler("x").lim(-24, 48)
	figure.ruler("y").lim(0, 100)
	figure.legend(x=-24, y=0, ha="left", va="bottom", relative=True)
	figure.show()

def main():
	p = argparse.ArgumentParser(description="Current cloud cover")
	p.add_argument("--lat", type=float)
	p.add_argument("--lon", type=float)
	p.add_argument("--plot", 
	               action="store_true", 
	               help="also show the last 24h and next 48h as a chart")
	args = p.parse_args()
	try:
		print(f"Cloud cover: {cloud_cover(args.lat, args.lon)}%")
		if args.plot:
			plot(args.lat, args.lon)
	except requests.RequestException as e:
		raise SystemExit(f"Could not fetch cloud cover: {e}")