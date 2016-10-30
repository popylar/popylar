import popylar


def test_track_event():
    """
    Test that event tracking goes through
    """
    r = popylar.track_event("UA-86484662-2", 'test', 'test_track_event')
    assert r.status_code == 200, "response is not OK"


def test_track_event_with_version():
    """
    Test recording the software version (in this case, popylar version)
    """
    from popylar.version import VERSION
    r = popylar.track_event("UA-86484662-2", 'test',
                            'test_track_event_with_version',
                            software_version=VERSION)
    assert r.status_code == 200, "response is not OK"
