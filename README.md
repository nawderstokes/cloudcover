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

## Installation

Requires Python 3.9 or newer, and is currently only available on macOS.

### Recommended: pipx or uv

These install `cloudcover` into its own isolated environment, so you don't need to create or activate a virtual environment, either with pipx:

```bash
brew install pipx && pipx ensurepath    
pipx install --index-url https://test.pypi.org/simple/ \
  --pip-args="--extra-index-url https://pypi.org/simple/" \
  cloudcover-nawder
```
or with uv
```bash
# install with homebrew
brew install uv
# or in the case homebrew cannot install `uv` (e.g. on older intel macs), install it directly
curl -LsSf https://astral.sh/uv/install.sh | sh

uv tool install --index https://test.pypi.org/simple/ \
  --index-strategy unsafe-best-match cloudcover-nawder
```

Then run it with:

```bash
cloudcover
```

> The package is currently on TestPyPI. Once it is published on PyPI, the
> install will simply be `pipx install cloudcover-nawder`.

## Development

To work on the code, clone the repo and use a virtual environment:

```bash
git clone https://github.com/USERNAME/cloudcover.git
cd cloudcover
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```