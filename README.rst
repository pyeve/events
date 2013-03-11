Python Events C#-Style
~~~~~~~~~~~~~~~~~~~~~~

The C# language provides a handy way to declare, subscribe to and fire
events. Technically, an event is a "slot" where callback functions (event
handlers) can be attached to - a process referred to as subscribing to an
event. Here is a handy class that encapsulates the core to event subscription
and event firing and feels like a “natural” part of the language. 
   
.. code-block:: python
 
    >>> def something_changed(reason):
    ...     print "something changed because %s" % reason
    ...

    >>> from events import Events
    >>> events = Events()
    >>> events.on_change += something_changed

Multiple callback functions can subscribe to the same event. When the event is
fired, all attached event handlers are invoked in sequence. To fire the event,
perform a call on the slot: 

.. code-block:: python

    >>> events.on_change('it had to happen')
    'something changed because it had to happen'

Documentation
-------------
Complete documentation is available at http://events.readthedocs.org

Testing
-------
Just run: ::

    python setup.py test

License
-------
Events is BSD licensed. See the LICENSE_ for details.

Attribution
-----------
Based on the excellent recipe by `Zoran Isailovski`_, Copyright (c) 2005.

.. _LICENSE: https://github.com/nicolaiarocci/events/blob/master/LICENSE 
.. _`Zoran Isailovski`: http://code.activestate.com/recipes/410686/
