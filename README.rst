Events
~~~~~~

The concept of events is heavily used in GUI libraries and is the foundation
for most implementations of the MVC (Model, View, Controller) design pattern
(the latter being my prime motivation for this recipe). Another prominent use
of events is in communication protocol stacks, where lower protocol layers need
to inform upper layers of incoming data and the like. Here is a handy class
that encapsulates the core to event subscription and event firing and feels
like a "natural" part of the language.

Usage
-----
The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions (event
handlers) can be attached to - a process referred to as subscribing to an
event. To subscribe to an event: ::

    from events import Events

    events = Events()
    events.on_change += my_event_handler_for_on_change

When the event is fired, all attached event handlers are invoked in
sequence. To fire the event, perform a call on the slot: ::

    events.on_change()

Usually, instances of Events will not hang around loosely like above, but
will typically be embedded in model objects, like here: ::

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

The Events and _EventSlot classes provide some introspection support, too:

    - Every event (aka event slot) has a __name__ attribute
    - You can iterate through all registered events in Events instances

This is usefull for ex. for an atomatic event subscription based on method
name patterns.

Note that the recipe does not check if an event that is being subscribed to
can actually be fired, unless the class attribute __events__ is defined.
This can cause a problem if an event name is slightly misspelled. If this
is an issue, subclass Events and list the possible events, like: ::

    class MyEvents(Events):
        __events__ = ('on_this', 'on_that', ...)


License
-------
Events is BSD licensed. See the LICENSE_ for details.

Attribution
-----------
Based on the work done by `Zoran Isailovski`_ (Copyright 2005).

.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/
