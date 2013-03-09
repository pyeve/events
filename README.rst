Events: C#-Style Events in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Documentation
-------------
Complete documentation is available at http://events.readthedocs.org

License
-------
Events is BSD licensed. See the LICENSE_ for details.

Attribution
-----------
Based on the work done by `Zoran Isailovski`_ (Copyright 2005).

.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/
