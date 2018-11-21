# pylint: disable=C0111,R0903

"""Displays the current date and time, from UTC (or other) time zone.

Parameters:
    * tztime.format: strftime()-compatible formatting string
    * tztime.locale: locale to use rather than the system default
    * tztime.tz:     Time zone to use (see pytz.timezone)
"""

from __future__ import absolute_import
import datetime
import locale
import bumblebee.engine
import pytz

class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        super(Module, self).__init__(engine, config,
            bumblebee.output.Widget(full_text=self.get_time))
        self._fmt = self.parameter("format", "%H:%M")
        l = locale.getdefaultlocale()
        if not l:
            l = ('en_US', 'UTF-8')
        lcl = self.parameter("locale", ".".join(l))
        locale.setlocale(locale.LC_TIME, lcl.split("."))

        tz = self.parameter("tz", "UTC")
        self._timezone = pytz.timezone(tz)

    def get_time(self, widget):
        enc = locale.getpreferredencoding()
        now=pytz.utc.localize(datetime.datetime.utcnow())
        local=now.astimezone(self._timezone)
        retval = local.strftime(self._fmt)
        if hasattr(retval, "decode"):
            return retval.decode(enc)
        return retval

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
