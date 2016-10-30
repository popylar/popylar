import os
import os.path as op
import uuid

import requests

popylar_path = op.join(op.expanduser('~'), '.popylar')


def get_uid():
    if op.exists(popylar_path):
        return open(popylar_path).read()
    else:
        return False


def track_event(tracking_id, category, action, uid=None, label=None, value=0):
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
        uid = get_uid()

    # If it's stil None, assume that the user has opted out (by removing that
    # file):
    if not uid:
        return False

    data = {'v': '1',  # API version.
            'tid': tracking_id,  # GA tracking ID
            'cid': uid,  # User unique ID, stored in `popylar_path`
            't': 'event',  # Event hit type.
            'ec': category,  # Event category.
            'ea': action,  # Event action.
            'el': label,  # Event label.
            'ev': value}  # Event value, must be an integer
    try:
        response = requests.post('http://www.google-analytics.com/collect',
                                 data=data)

        return response
    except:
        return False
