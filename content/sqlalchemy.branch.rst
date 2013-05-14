SQLAlchemy and Eve
==================

:date: 2013-05-10 15:39
:tags: sqlalchemy
:category: develop
:author: Nicola Iarocci

There is an ongoing effort to develop a SQLAlchemy data layer for Eve. This is
interesting because it will allow the use of a wide range of SQL databases
(PostgreSQL, MySQL, Oracle, etc.) as storage backends for Eve-powered REST
APIs. 

The current early prototype resides in its own `sqlalchemy branch`_. We are in
the early stages of development and contributors are invited to join the ranks.
There is a lot of room for improvement at all levels: features, tests,
documentation, you name it.

If you want to lend a hand please come visit us on IRC_ so we can better
coordinate efforts. **Jezier** has been working on the SQL features while
**beatpanic** has been playing around with the test suite. Get in touch with
them or with me (I’m **iaro** on IRC). If IRC is not your cup of tea feel free to
open a ticket_, `email me`_ or submit a pull requests: just make sure it is
against the sqlalchemy branch.

.. _`sqlalchemy branch`: https://github.com/nicolaiarocci/eve/tree/sqlalchemy
.. _IRC: irc://irc.freenode.net/evehq
.. _ticket: https://github.com/nicolaiarocci/eve/issues
.. _`email me`: mailto:eve@nicolaiarocci.com
