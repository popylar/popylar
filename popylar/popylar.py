import os.path as op
import requests
import uuid

popylar_path = op.join(op.expanduser('~'), '.popylar')
DO_NOT_TRACK = 'DO_NOT_TRACK'


def opt_out():
    """Permanently opt-out of Popylar tracking.

    To opt-in again, run ``popylar.reset_uid()``
    """
    with open(popylar_path, 'w') as fhandle:
        fhandle.write(DO_NOT_TRACK)


def reset_uid():
    """Opt-in to popylar tracking, and/or reset the user id"""
    uid = uuid.uuid1()
    with open(popular_path, 'w') as fhandle:
        fhandle.write(uid.hex)


def _get_uid():
    if op.exists(popylar_path):
        return open(popylar_path).read()
        if uid.strip() == DO_NOT_TRACK:
            return False
        else:
            return uid
    else:
        return False


def track_event(tracking_id, category, action, uid=None, label=None, value=0,
                software_version=None):
    """
    Record an event with Google Analytics

    Parameters
    ----------
    tracking_id : str
        Google Analytics tracking ID.
    category : str
        Event category.
    action : str
        Event action.
    uid : str
        User unique ID, assigned when popylar was installed.
    label : str
        Event label.
    value : int
        Event value.
    """
    # If no user unique ID provided, try to get one from popylar_path:
    if uid is None:
        uid = _get_uid()

    # If it's stil None, assume that the user has opted out
    # (either by removing the file or running popylar.opt_out())
    if not uid:
        return False

    # Based on https://cloud.google.com/appengine/docs/python/google-analytics
    # and:  https://developers.google.com/analytics/devguides/collection/protocol/v1/devguide  # noqa
    data = {'v': '1',  # API version.
            'tid': tracking_id,  # GA tracking ID
            'cid': uid,  # User unique ID, stored in `popylar_path`
            't': 'event',  # Event hit type.
            'ec': category,  # Event category.
            'ea': action,  # Event action.
            'el': label,  # Event label.
            'ev': value,  # Event value, must be an integer
            # We hijack "app version" to report the package version:
            'av': software_version}
    try:
        response = requests.post('http://www.google-analytics.com/collect',
                                 data=data)

        return response

    except:
        return False
