Eve + ORM? Eve-Mongoengine! 
===========================

:date: 2013-12-20
:category: extensions
:tags: eve-mongoengine
:author: Stanislav Heller

Eve-Mongoengine_ is an Eve extension, which enables Mongoengine_ ORM models to
be used as eve schema. 

If you use mongoengine in your application and simultaneously want to use Eve_,
instead of writing schema again in Cerberus_ format (DRY!), you can use this
extension, which takes your mongoengine models and auto-transforms them into
Cerberus schema under the hood.

Features
--------
- **Auto-generated schema out of your mongoengine models**. Even if you did not specify ``updated`` and ``created`` fields in your model, Eve-Mongoengine adds them into the model class. But beware, if you update your document using mongoengine model (i.e. by calling ``save()`` on the model object), the ``updated`` field wont be updated to current time. This is because there arent any hooks bound to ``save()`` or ``update()`` methods at default.
- **Every operation goes through mongoengine**. You do not loose your mongoengine hooks!
- **Support for most of mongoengine fields**.
- **Mongoengine validation layer not disconnected**. If you define some validators on top of regular mongoengine validation spec, you have got them in eve too!

How it works?
-------------
.. code-block:: python

    import mongoengine
    from eve import Eve
    from eve_mongoengine import EveMongoengine

    # create some dummy model class
    class Person(mongoengine.Document):
        name = mongoengine.StringField()
        age = mongoengine.IntField()

    # default eve settings
    my_settings = {
        'MONGO_HOST': 'localhost',
        'MONGO_PORT': 27017,
        'MONGO_DBNAME': 'eve_mongoengine_test'
        # You have to give Eve some dummy domain to shut him up. Without this
        # setting it will complain about empty domain.
        'DOMAIN': {'eve-mongoengine': {}}
    }

    # init application
    app = Eve(settings=my_settings)
    # init extension
    ext = EveMongoengine(app)
    # register model to eve
    ext.add_model(Person)
    # let's roll
    app.run()

So you just give Eve some general settings, initialize EveMongoengine
extension and then register a bunch of mongoengine models as you wish.

If you ask, what's the name of resource in case of ``Person`` class, it will be
lowercase name of given class, in this example it will be `person`, so the
request URL could be ``/person`` (but you can use ``lowercase`` param to get the
original name of class as resource name: ``add_model(Person, lowercase=False)``).

In ``add_model()`` method you can add into resource settings every possible
parameter, which is accepted by Eve. Even if you want to overwrite some
settings, which generates eve-mongoengine under the hood, you can do it this
way: 

.. code-block:: python

    ext.add_model(Person,                                       # model or models 
                  resource_methods=['GET'],                     # allow only GET 
                  cache_control="max-age=600; must-revalidate") # set max-age 

Need more? Check out official documentation_ !

.. _Eve-Mongoengine: https://github.com/hellerstanislav/eve-mongoengine
.. _mongoengine: http://mongoengine.org/
.. _documentation: http://eve-mongoengine.readthedocs.org/en/latest/
.. _Cerberus: http://cerberus.readthedocs.org/en/latest/
.. _Eve: http://python-eve.org
