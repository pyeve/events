Events: C#-Style Events in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The concept of events is heavily used in GUI libraries and is the foundation
for most implementations of the MVC (Model, View, Controller) design pattern.
Another prominent use of events is in communication protocol stacks, where
lower protocol layers need to inform upper layers of incoming data and the
like. Here is a handy class that encapsulates the core to event subscription
and event firing and feels like a "natural" part of the language.

Usage
-----
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions (event
handlers) can be attached to - a process referred to as subscribing to an
event. To subscribe to an event: ::

    from events import Events

    events = Events()
    events.on_change += my_event_handler

As you can see, multiple callback functions can suscribe to the same
event. When the event is fired, all attached event handlers are invoked in
sequence. To fire the event, perform a call on the slot: ::

    events.on_change()

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

The :class:`~events.Events` and :class:`~events._EventSlot` classes provide
some introspection support, too:

    - Every event (aka event slot) has a :attr:`__name__` attribute
    - You can get the number of events registered in :class:`~events.Events`.
    - You can iterate through all registered events in :class:`~events.Events`
      instances
    - You can get the number of callbacks registered to a single event.
    - You can iterate through all registered callbacks for an event, or
      retrieve them by index.


This is usefull for ex. for an atomatic event subscription based on method
name patterns.

Note that by default :class:`~events.Events` does not check if an event that is
being subscribed to can actually be fired, unless the class attribute
:attr:`__events__` is defined.  This can cause a problem if an event name is
slightly misspelled. If this is an issue, subclass Events and list the possible
events, like: ::

    class MyEvents(Events):
        __events__ = ('on_this', 'on_that', ...)


Attribution
-----------
Based on the excellent recipe by `Zoran Isailovski`_ (Copyright 2005).

Source Code
-----------
Source code is available at `GitHub
<https://github.com/nicolaiarocci/events>`_.

Copyright Notice
----------------
This is an open source project by `Nicola Iarocci
<http://nicolaiarocci.com>`_. See the original `LICENSE
<https://github.com/nicolaiarocci/events/blob/master/LICENSE>`_ for more
informations.

.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/ 
