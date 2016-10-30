import popylar


def test_track_event():
    """
    Test that event tracking
    """
    r = popylar.track_event("UA-86484662-2", 'test', 'test_track_event')
    assert r.status_code == 200, "response is not OK"
