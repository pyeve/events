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

By default, Events does not check if an event can be subscribed to and fired. 
You can predefine events by subclassing Events and listing them. Attempts to
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

You can define default arguments for events

.. code-block:: pycon

    >>> from events import Events
    >>> class MyClass(object):
    ...     def __init__(self):
    ...         self.events = Events(default=[str(self) + ": "])
    ...         self.events.on_change += print
    ...     def __str__(self):
    ...         return self.__class__.__name__
    >>> inst = MyClass()
    >>> inst.events.on_change("Hello world!")
    >>> inst.events.on_change("Bye world!")

You can also declare a global wrap function that allows to insert all the events a 
use is at the time of debugging or avoiding the execution of an event under certain 
circumstances

.. code-block:: pycon

    >>> from events import Events
    >>> def debug(func, *args, **kwargs):
    ...     logging.debug("Trigger event: " + func.__name__)
    ...     func(*args, **kwargs)
    >>> class MyClass(object):
    ...     def __init__(self):
    ...         self.events = Events(wrapper=debug)
    ...         self.events.on_change += print
    ...     def __str__(self):
    ...         return self.__class__.__name__
    >>> inst = MyClass()
    >>> inst.events.on_change("Hello world!")
    >>> inst.events.on_change("Bye world!")

Do not worry about sending exact parameters or fill your functions with * args, * 
kwargs the functions are only calls with the parameters they need

.. code-block:: pycon

    >>> from events import Events
    >>> class MyClass(object):
    ...     def __init__(self):
    ...         self.events = Events(default=[self])
    ...         self.events.on_change += self.destroy
    ...         self.events.on_change += self.paint
    ...     def destroy(self):
    ...         pass
    ...     def paint(self):
    ...         pass
    ...     def __str__(self):
    ...         return self.__class__.__name__
    >>> def need1(arg):
    ...    print(f"need1 {arg}")
    >>> def need2(arg, arg2):
    ...    print(f"need2 {arg} {arg2}")
    >>> def need3(arg, arg3, named):
    ...    print(f"need3 {arg} {arg3} {named}")
    >>> def function(sender):
    ...    print(sender)
    ...    sender.paint()
    >>> my_class = MyClass()
    >>> my_class.events.on_change()
    >>> my_class.events.on_change += function
    >>> my_class.events.on_change()
    >>> my_class.events.on_key += need1
    >>> my_class.events.on_key += need2
    >>> my_class.events.on_key += need3
    >>> my_class.events.on_key('arg', 'arg2', arg3='arg3', named='named')

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
