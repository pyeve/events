Events
~~~~~~
.. image:: https://secure.travis-ci.org/pyeve/events.png?branch=master 
        :target: https://secure.travis-ci.org/pyeve/events

The C# language provides a handy way to declare, subscribe to and fire events.
Technically, an event is a "slot" where callback functions (event handlers) can
be attached to - a process referred to as subscribing to an event. Here is
a handy package that encapsulates the core to event subscription and event
firing and feels like a "natural" part of the language.

.. code-block:: pycon
 
    >>> def something_changed(reason): 
    ...     print "something changed because %s" % reason 
    ...

    >>> from events import Events
    >>> events = Events()
    >>> events.on_change += something_changed

Multiple callback functions can subscribe to the same event. When the event is
fired, all attached event handlers are invoked in sequence. To fire the event,
perform a call on the slot: 

.. code-block:: pycon

    >>> events.on_change('it had to happen')
    'something changed because it had to happen'

By default, event.Events does not check if an event can be subscribed to and fired. 
You can predefine these events by subclassing event.Events and listing them. Attempts to
subscribe to or fire an undefined event will raise an EventsException.

.. code-block:: pycon
 
    >>> class MyEvents(Events):
    ...     __events__ = ('on_this', 'on_that', )

    >>> events = MyEvents()

    # this will raise an EventsException as `on_change` is unknown to MyEvents:
    >>> events.on_change += something_changed

You can also predefine events for a single Events instance by passing an iterator to the constructor.

.. code-block:: pycon

    >>> events = Events(('on_this', 'on_that'))

    # this will raise an EventsException as `on_change` is unknown to events:
    >>> events.on_change += something_changed


Documentation
-------------
Complete documentation is available at http://events.readthedocs.org

Installing
----------
Events is on PyPI so all you need to do is: ::

    pip install events

Testing
-------
Just run: ::

    python setup.py test

Or use tox to test the package under all supported Pythons: 2.6, 2.7, 3.3, 3.4, 3.5 and 3.6. 

License
-------
Events is BSD licensed. See the LICENSE_ for details.

Contributing
------------
Please see the `Contribution Guidelines`_.

Attribution
-----------
Based on the excellent recipe by `Zoran Isailovski`_, Copyright (c) 2005.

.. _LICENSE: https://github.com/pyeve/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/
.. _`Contribution Guidelines`: https://github.com/pyeve/events/blob/master/CONTRIBUTING.rst
