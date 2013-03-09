# -*- coding: utf-8 -*-

"""
    Events
    ~~~~~~

    Implements C#-Style Events.

    Derived from the original work by Zoran Isailovski:
    http://code.activestate.com/recipes/410686/ - Copyright (c) 2005

    :copyright: (c) 2013 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""


class EventsException(Exception):
    pass


class Events:
    """
    Encapsulates the core to event subscription and event firing, and feels
    like a "natural" part of the language.

    The class Events is there mainly for 3 reasons:

        - Events (Slots) are added automatically, so there is no need to
        declare/create them separately. This is great for prototyping. (Note
        that `__events__` is optional and should primarilly help detect
        misspelled event names.)
        - To provide (and encapsulate) some level of introspection.
        - To "steel the name" and hereby remove unneeded redundancy in a call
        like:

            xxx.OnChange = event('OnChange')
    """
    def __getattr__(self, name):
        if hasattr(self.__class__, '__events__'):
            if name not in self.__class__.__events__:
                raise EventsException("Event '%s' is not declared" % name)
        self.__dict__[name] = ev = _EventSlot(name)
        return ev

    def __repr__(self):
        return 'Events' + str(list(self))

    __str__ = __repr__

    def __len__(self):
        return NotImplemented

    def __iter__(self):
        def gen(dictitems=self.__dict__.items()):
            for attr, val in dictitems:
                if isinstance(val, _EventSlot):
                    yield val
        return gen()


class _EventSlot:
    def __init__(self, name):
        self.targets = []
        self.__name__ = name

    def __repr__(self):
        return 'event ' + self.__name__

    def __call__(self, *a, **kw):
        for f in self.targets:
            f(*a, **kw)

    def __iadd__(self, f):
        self.targets.append(f)
        return self

    def __isub__(self, f):
        while f in self.targets:
            self.targets.remove(f)
        return self
