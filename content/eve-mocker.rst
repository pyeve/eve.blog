Mocking tool for Eve APIs
=========================

:slug: eve-mocker
:date: 2013-08-01
:category: tools
:tags: documentation, tools
:author: Thomas Sileo

`EveMocker <https://github.com/tsileo/eve-mocker>`_ is a mocking tool for `Eve
powered REST API <http://python-eve.org>`_, based on the excellent `HTTPretty
<http://falcao.it/HTTPretty>`_, and aimed to be used in your unit tests, when
you rely on an Eve API. It mimics the behavior of an Eve API in a controlled
way. Why would you want to mock Eve when writing unit tests?

- Your test suite will run faster.
- You don't need to bundle an Eve app exclusively for testing purposes (you can
  spend more time on the actual task).
- You don't need to worry about having a real Eve server running when running
  the test cases.

Let's say you want to test the following class stored in ``remote_items.py``
that need to call an Eve powered REST API:

.. code-block:: python

    from urlparse import urljoin
    from functools import partial
    import requests

    API_URL = "http://my-eve-api.com/api/"


    class RemoteItems(object):
        def __init__(self, api_url=API_URL):
            self.api_url = api_url
            self.endpoint_url = partial(urljoin, self.api_url)

        def get_latest(self):
            r = requests.get(self.endpoint_url("items"))
            r.raise_for_status()
            return r.json().get("_items", [])


Here is how you can do it with Eve-Mocker:

.. code-block:: python

    from eve_mocker import EveMocker
    import unittest
    from remote_items import RemoteItems, API_URL

    class TestRemoteItems(unittest.TestCase):
        def testGetLatestItems(self):
            items = [{"_id": "fakeid", "content": "my content"},
                     {"_id": "fakeid2", "content": "another_content"}]
            with EveMocker(API_URL) as eve_mocker:
                # We feed EveMocker DB with some items
                eve_mocker.set_resource("items", items)

                remote_items = RemoteItems()
                latest_items = remote_items.get_latest()

                self.assertEqual(sorted(latest_items), sorted(items))

    if __name__ == '__main__':
        unittest.main()

Check out `the repository <https://github.com/tsileo/eve-mocker>`_ on GitHub.
