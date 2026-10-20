# cloudcover

A small command-line tool that reports the current cloud cover at your location or at coordinates you choose. It can also display a terminal chart of the previous 24 hours and the next 48 hours.

## What the code does

Cloudcover gets your approximate location from [ipinfo.io](https://ipinfo.io/) when you don't provide coordinates, then requests cloud-cover data from [Open-Meteo](https://open-meteo.com/). The current cloud cover is reported as a percentage. The optional chart shows recent and forecast hourly cloud cover.

The tool needs an internet connection. When using automatic location detection, your IP address is sent to ipinfo.io to determine your approximate coordinates.

## How to use the code

Run the command with no options to look up your approximate location and show the current cloud cover:

```console
cloudcover
```

Example output:

```text
Cloud cover: 42%
```

Provide both latitude and longitude to check another location:

```console
cloudcover --lat 47.6062 --lon -122.3321
```

Add `--plot` to show the recent history and forecast chart:

```console
cloudcover --lat 47.6062 --lon -122.3321 --plot
```

Run `cloudcover --help` to see the available options.

## How to download the code

Clone this repository and install the project locally. Python 3.10 or newer is required.

```console
git clone https://github.com/nawderstokes/cloudcover.git
cd cloudcover
python -m pip install -e .
```

After installation, run `cloudcover` from your terminal.
