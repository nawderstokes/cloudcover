import cloudcover


class FakeResponse:
    def __init__(self, data):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


def test_cloud_cover_with_coordinates(monkeypatch):
    def fake_get(url, params=None, timeout=None):
        assert params["latitude"] == 41.39
        return FakeResponse({"current": {"cloud_cover": 42}})

    monkeypatch.setattr(cloudcover.requests, "get", fake_get)
    assert cloudcover.cloud_cover(41.39, 2.17) == 42


def test_get_location_parses_loc(monkeypatch):
    monkeypatch.setattr(
        cloudcover.requests, "get",
        lambda *a, **k: FakeResponse({"loc": "41.39,2.17"}),
    )
    assert cloudcover.get_location() == (41.39, 2.17)