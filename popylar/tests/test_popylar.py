import popylar


def test_track_event():
    """
    Test that event tracking goes through
    """
    r = popylar.track_event("UA-86484662-2", 'test', 'test_track_event',
                            thread=False)
    # When not threading, we can can check the status of the request:
    assert r.status_code == 200, "response is not OK"

    r = popylar.track_event("UA-86484662-2", 'test', 'test_track_event',
                            thread=True)
    # Otherwise the return value is none
    assert r is None, "There should be nothing to see here"


def test_track_event_with_version():
    """
    Test recording the software version (in this case, popylar version)
    """
    from popylar.version import VERSION
    r = popylar.track_event("UA-86484662-2", 'test',
                            'test_track_event_with_version',
                            software_version=VERSION, thread=False)
    # When not threading, we can can check the status of the request:
    assert r.status_code == 200, "response is not OK"

    r = popylar.track_event("UA-86484662-2", 'test',
                            'test_track_event_with_version',
                            software_version=VERSION, thread=True)
    # Otherwise the return value is none
    assert r is None, "There should be nothing to see here"


def test_opt():
    popylar.opt_out()
    parser = popylar.get_or_create_config()
    assert parser['user']['track'] == "False"
    popylar.opt_in()
    parser = popylar.get_or_create_config()
    assert parser['user']['track'] == "True"
