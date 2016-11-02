# popylar : track software use with Google Analytics

Popylar is a small Python package that allows tracking execution of Python
code (such as imports) via the Google Analytics API.
For example, once you have [set up a google analytics account](https://support.google.com/analytics/answer/1008015), you could track
the import of your package by adding this to the ``__init__.py`` file:

```python
# In package __init__.py
import popylar
popylar.track_event(google_analytics_id, 'import', 'import_mypackage')
```

With this setup, every time the package is imported it will be tracked on
Google analytics.

## Why this Package?

Tracking the use of open software is, in general, very difficult, and with many
open source projects being supported by private and public funding agencies, a
means of more quantitative reporting would be beneficial.
Current tracking options exist, but are relatively limited:

- [PyPI](https://pypi.python.org/) tracks downloads, but cannot track when
  packages are installed with downstream package managers like
  [conda](http://conda.pydata.org/docs/),
  [brew](http://brew.sh/), [apt](https://wiki.debian.org/Apt), and others.
- Software hosting services like [GitHub](http://github.com) provide information
  about project forks, but no information about number of downloads or clones.
- Other means of tracking (mailing list traffic, bug report traffic, StackOverflow
  questions) are helpful but difficult to quantify and compare between projects.

More fine-grained user tracking is accepted practice for blogs and other websites,
and ``popylar`` seeks to add that capability to software packages.

## Wait... is this really OK?

Short answer: we're not sure. We agree that this feels a bit icky at first-blush,
and we are open to feedback about the ethical issues or potential abuse of such
a setup.
That being said, the information tracked by popylar is identical to that tracked
by any site using Google Analytics, including likely your favorite independent
blogs, and popylar solves a real problem faced by many developers of the open
source tools you probably depend on.

## What information is tracked?

The tracked information is exactly that stored by Google Analytics when you visit
a website, with the addition of [a few pieces of metadata](https://github.com/popylar/popylar/blob/master/popylar/popylar.py#L73-L82)
that can be configured by the package.
In particular, the only identifying information provided by the Python package is
a randomly-generated unique ID.

## Can a user opt-out?

Yes. If a user runs ``popylar.opt_out()``, popylar will never track usage for
that system/user, and this opt-out state is preserved between sessions.

## Can I still use packages off-line?

Yes. If no internet connection is detected, no information will be reported
by popylar and the script will continue to execute as normal.

## Where can I give feedback or offer ideas?

If you would like to weigh-in on this idea, please use Popylar's [Github Issues](https://github.com/popylar/popylar/issues). We'd love to hear your
thoughts, particularly on any ethical or technical issues we may be overlooking.
