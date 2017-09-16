# -*- coding: utf-8 -*-

"""
    Events
    ~~~~~~

    Implements C#-Style Events.

    Derived from the original work by Zoran Isailovski:
    http://code.activestate.com/recipes/410686/ - Copyright (c) 2005

    :copyright: (c) 2014-2017 by Nicola Iarocci.
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
    def __init__(self, events=None, default=None, wrapper=None):
        if not isinstance(default, (list, tuple)) and default is not None:
            raise AttributeError("type object %s is not list" % (type(default)))
        elif not callable(wrapper) and wrapper is not None:
            raise AttributeError("type object %s is not function" % (type(wrapper)))
        self._wrapper = wrapper
        self._default = default
        if events is not None:

            try:
                for _ in events:
                    break
            except:
                raise AttributeError("type object %s is not iterable" %
                                     (type(events)))
            else:
                self.__events__ = events

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError("type object '%s' has no attribute '%s'" %
                                 (self.__class__.__name__, name))

        if hasattr(self, '__events__'):
            if name not in self.__events__:
                raise EventsException("Event '%s' is not declared" % name)

        elif hasattr(self.__class__, '__events__'):
            if name not in self.__class__.__events__:
                raise EventsException("Event '%s' is not declared" % name)

        self.__dict__[name] = ev = _EventSlot(name, self._default, self._wrapper)
        return ev

    def __repr__(self):
        return '<%s.%s object at %s>' % (self.__class__.__module__,
                                         self.__class__.__name__,
                                         hex(id(self)))

    __str__ = __repr__

    def __len__(self):
        return len([x for x in self.__dict__ if not x.startswith('_')])

    def __iter__(self):
        def gen(dictitems=self.__dict__.items()):
            for _, val in dictitems:
                if isinstance(val, _EventSlot):
                    yield val
        return gen()


class _EventSlot:
    def __init__(self, name, default=None, wrapper=None):
        self._default = default or []
        self._wrapper = wrapper or (lambda func, *args, **kwargs: func(*args, **kwargs))
        self.targets = []
        self.__name__ = name

    def __repr__(self):
        return "event '%s'" % self.__name__

    def __call__(self, *args, **kwargs):
        for function in tuple(self.targets):
            self._wrapper(function, *self._default, *args, **kwargs)

    def __iadd__(self, function):
        self.targets.append(function)
        return self

    def __isub__(self, function):
        while function in self.targets:
            self.targets.remove(function)
        return self

    def __len__(self):
        return len(self.targets)

    def __iter__(self):
        def gen():
            for target in self.targets:
                yield target
        return gen()

    def __getitem__(self, key):
        return self.targets[key]
