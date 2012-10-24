'''
Created on May 06, 2012
Last change on Oct 25, 2012
v0.0.2

@author: mindrunner
'''

import xbmc
import xbmcgui
import xbmcaddon
import time

if __name__ == '__main__':
    addon_id = "service.partymode.autostart"
    Addon = xbmcaddon.Addon(addon_id)
    enable = Addon.getSetting('enable')
    delay = Addon.getSetting('delay')
    fullscreen = Addon.getSetting('fullscreen')
    fullscreendelay = Addon.getSetting('fullscreendelay')
    if enable:
        time.sleep(int(delay))
        xbmc.executebuiltin("XBMC.PlayerControl(PartyMode)")
        if fullscreen:
            time.sleep(int(fullscreendelay))
            xbmc.executebuiltin("XBMC.ActivateWindow(visualisation)")
