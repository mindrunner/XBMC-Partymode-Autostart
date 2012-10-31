'''
Created on May 06, 2012
Last change on Oct 25, 2012
v0.0.2

@author: mindrunner
'''

import xbmc
import xbmcgui
import xbmcaddon
import sched
import time

s = sched.scheduler(time.time, time.sleep)

def ontimer():
    interval = Addon.getSetting('interval')
    isplaying = xbmc.Player().isPlaying()
    if isplaying == 0:
        xbmc.executebuiltin("XBMC.PlayerControl(PartyMode)")
    s.enter(int(interval), 1, ontimer, ())

if __name__ == '__main__':
    addon_id = "service.partymode.autostart"
    Addon = xbmcaddon.Addon(addon_id)
    enable = Addon.getSetting('enable')
    delay = Addon.getSetting('delay')
    fs = Addon.getSetting('fs')
    fsdelay = Addon.getSetting('fsdelay')
    idletimer = Addon.getSetting('idletimer')
    interval = Addon.getSetting('interval')
    if enable == "true":
        time.sleep(int(delay))
        xbmc.executebuiltin("XBMC.PlayerControl(PartyMode)")
        if fs == "true":
            time.sleep(int(fsdelay))
            xbmc.executebuiltin("XBMC.ActivateWindow(visualisation)")
        if idletimer == "true":
            s.enter(int(interval), 1, ontimer, ())
            s.run()
