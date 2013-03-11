Events in Python C#-Style 
~~~~~~~~~~~~~~~~~~~~~~~~~

The concept of events is heavily used in GUI libraries and is the foundation
for most implementations of the MVC (Model, View, Controller) design pattern.
Another prominent use of events is in communication protocol stacks, where
lower protocol layers need to inform upper layers of incoming data and the
like. Here is a handy class that encapsulates the core to event subscription
and event firing and feels like a "natural" part of the language.

The package has been tested under Python 2.6, Python 2.7 and Python 3.3.

Usage
=====
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions (event
handlers) can be attached to - a process referred to as subscribing to an
event. To subscribe to an event: ::

    >>> def something_changed(reason):
    ...     print "something changed because %s" % reason
    ...

    >>> from events import Events
    >>> events = Events()
    >>> events.on_change += something_changed

Multiple callback functions can subscribe to the same event. When the event is
fired, all attached event handlers are invoked in sequence. To fire the event,
perform a call on the slot: ::

    >>> events.on_change('it had to happen')
    something changed because it had to happen

Usually, instances of :class:`~events.Events` will not hang around loosely like
above, but will typically be embedded in model objects, like here: ::

    class MyModel(object):
        def __init__(self):
            self.events = Events()
            ...

Similarly, view and controller objects will be the prime event subscribers: ::

    class MyModelView(SomeWidget):
        def __init__(self, model):
            ...
            self.model = model
            model.events.on_change += self.display_value
            ...

        def display_value(self):
            ...

Introspection
-------------
The :class:`~events.Events` and :class:`~events._EventSlot` classes provide
some introspection support. This is usefull for example for automatic event
subscription based on method name patterns. ::

    >>> from events import Events
    >>> events = Events()
    >>> print events
    <events.events.Events object at 0x104e5d5f0>

    >>> def changed():
    ...     print "something changed"
    ...

    >>> def another_one():
    ...     print "something changed here too"
    ...

    >>> def deleted():
    ...     print "something got deleted!"
    ...

    >>> events.on_change += changed
    >>> events.on_change += another_one
    >>> events.on_delete += deleted

    >>> print len(events)
    2

    >>> for event in events:
    ...     print event.__name__
    ...
    on_change
    on_delete

    >>> event = events.on_change
    >>> print event
    event 'on_change'

    >>> print len(event)
    2

    >>> for handler in event:
    ...     print handler.__name__
    ...
    changed
    another_one

    >>> print event[0]
    <function changed at 0x104e5c230>

    >>> print event[0].__name__
    changed

    >>> print len(events.on_delete)
    1

    >>> events.on_change()
    something changed
    somethind changed here too

    >>> events.on_delete()
    something got deleted!


Event names
-----------
Note that by default :class:`~events.Events` does not check if an event that is
being subscribed to can actually be fired, unless the class attribute
:attr:`__events__` is defined.  This can cause a problem if an event name is
slightly misspelled. If this is an issue, subclass :class:`~events.Events` and
list the possible events, like: ::

    class MyEvents(Events):
        __events__ = ('on_this', 'on_that', )

    events = MyEvents()

    # this will raise a EventsException as `on_change` is unknown to MyEvents:
    events.on_change += changed     

Source Code
===========
Source code is available at GitHub_.

Attribution
===========
Based on the excellent recipe by `Zoran Isailovski`_, Copyright (c) 2005.

Copyright Notice
================
This is an open source project by `Nicola Iarocci`_. See the original LICENSE_
for more informations.

.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/ 
.. _GitHub: https://github.com/nicolaiarocci/events
.. _`Nicola Iarocci`: http://nicolaiarocci.com
.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
