import argparse
import requests

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

def main():
	p = argparse.ArgumentParser(description="Current cloud cover")
	p.add_argument("--lat", type=float)
	p.add_argument("--lon", type=float)
	args = p.parse_args()
	try:
		print(f"Cloud cover: {cloud_cover(args.lat, args.lon)}%")
	except requests.RequestException as e:
		raise SystemExit(f"Error fetching cloud cover: {e}")
