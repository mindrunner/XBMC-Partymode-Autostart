'''
Created on May 06, 2012
Last change on Oct 25, 2012
v0.0.2

@author: mindrunner
'''

import xbmc
import xbmcgui
import xbmcaddon

if __name__ == '__main__':
    addon_id = "service.partymode.autostart"
    Addon = xbmcaddon.Addon(addon_id)
    if Addon.getSetting('enable'):
        sleep(Addon.getSetting('delay'))
        xbmc.executebuiltin("XBMC.PlayerControl(PartyMode)")
        if Addon.getSetting('fullscreen'):
            sleep(20)
            xbmc.executebuiltin("XBMC.ActivateWindow(visualisation)")

