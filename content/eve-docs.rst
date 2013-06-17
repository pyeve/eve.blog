Auto generate API docs
======================

:slug: eve-docs
:date: 2013-06-17
:category: tools
:tags: documentation, tools
:author: Charles Flynn

Eve provides powerful capabilities for quickly building RESTful APIs. The
`Eve-docs`_ blueprint extends these capabilities with API documentation. You
activate the blueprint in your launch script, and Eve-docs creates the
documentation from your existing Eve configuration file, with no additional
configuration required.

.. image:: static/images/evedocs-example.png
   :alt: An example of eve-docs auto generated API documentation

Eve-docs generates documentation in HTML using `Twitter Bootstrap`_. You can
expand each domain to show available endpoints and methods, and further expand
each method to show parameter details. Eve-docs also publishes the
documentation data as JSON for programmatic consumption.

For more detail see the `project repo`_ on Github.

.. _`Eve-docs`: https://github.com/charlesflynn/eve-docs
.. _`project repo`: https://github.com/charlesflynn/eve-docs
.. _`Twitter Bootstrap`: http://twitter.github.io/bootstrap/
