.. Popylar documentation master file, created by
   sphinx-quickstart on Sun Oct 30 09:16:27 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Popylar: Tracking software use with Google Analytics
====================================================

Popylar is a small Python package that allows tracking execution of Python
code (such as imports) via the Google Analytics API.
For example, once you have `set up a google analytics account <https://support.google.com/analytics/answer/1008015>`_, you could track
the import of your package by adding this to the package ``__init__.py`` file::

  import popylar
  popylar.track_event(google_analytics_id, 'import', 'import_mypackage')

With this setup, every time the package is imported it will be tracked on
Google analytics.


.. toctree::
   :maxdepth: 2

   FAQ


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
