# -*- coding: utf-8 -*-

import unittest
import events
from events import Events, EventsException


class TestBase(unittest.TestCase):
    def setUp(self):
        self.events = Events()

    def callback1(self):
        pass

    def callback2(self):
        pass

    def callback3(self):
        pass


class TestEvents(TestBase):
    def test_getattr(self):
        class MyEvents(Events):
            __events__ = ('on_eventOne', )

        try:
            MyEvents().on_eventNotOne += self.callback1
        except EventsException:
            pass
        else:
            self.fail("'EventsException' excpected and not raised.")

        try:
            self.events.on_eventNotOne += self.callback1
        except:
            self.fail("Exception raised but not expected.")

    def test_len(self):
        self.events.on_change += self.callback1
        self.events.on_get += self.callback2
        self.assertEqual(len(self.events), 2)

    def test_iter(self):
        self.events.on_change += self.callback1
        self.events.on_change += self.callback2
        self.events.on_edit += self.callback1
        i = 0
        for event in self.events:
            i += 1
            self.assertTrue(isinstance(event, events.events._EventSlot))
        self.assertEqual(i, 2)


class TestEventSlot(TestBase):
    def setUp(self):
        super(TestEventSlot, self).setUp()
        self.events.on_change += self.callback1
        self.events.on_change += self.callback2
        self.events.on_change += self.callback3
        self.events.on_edit += self.callback3

    def test_type(self):
        ev = self.events.on_change
        self.assertTrue(isinstance(ev, events.events._EventSlot))
        self.assertEqual(ev.__name__, 'on_change')

    def test_len(self):
        self.assertEqual(len(self.events.on_change), 3)
        self.assertEqual(len(self.events.on_edit), 1)

    def test_repr(self):
        ev = self.events.on_change
        self.assertEqual(ev.__repr__(), "event 'on_change'")

    def test_iter(self):
        ev = self.events.on_change
        self.assertEqual(len(ev), 3)
        i = 0
        for target in ev:
            i += 1
            self.assertEqual(target.__name__, 'callback%d' % i)

    def test_getitem(self):
        ev = self.events.on_edit
        self.assertEqual(len(ev), 1)
        self.assertTrue(ev[0].__name__, 'callback3')
        try:
            ev[1]
        except IndexError:
            pass
        else:
            self.fail("IndexError expected.")

    def test_isub(self):
        self.events.on_change -= self.callback1
        ev = self.events.on_change
        self.assertEqual(len(ev), 2)
        self.assertEqual(ev[0].__name__, 'callback2')
        self.assertEqual(ev[1].__name__, 'callback3')


class TestInstanceEvents(TestBase):

    def test_getattr(self):

        MyEvents = Events(('on_eventOne', ))

        try:
            MyEvents.on_eventOne += self.callback1
        except:
            self.fail("Exception raised but not expected.")

        try:
            MyEvents.on_eventNotOne += self.callback1
        except EventsException:
            pass
        else:
            self.fail("'EventsException' excpected and not raised.")

        try:
            self.events.on_eventNotOne += self.callback1
        except:
            self.fail("Exception raised but not expected.")

    def test_instance_restriction(self):

        class MyEvents(Events):
            __events__ = ('on_eventOne', 'on_eventTwo')

        MyRestrictedInstance = MyEvents(('on_everyTwo', ))

        try:
            MyRestrictedInstance.on_everyTwo += self.callback1
        except:
            self.fail("Exception raised but not expected.")

        try:
            MyRestrictedInstance.on_everyOne += self.callback1
        except:
            pass
        else:
            self.fail("'EventsException' excpected and not raised.")
