'''
Created on May 06, 2012

@author: mindrunner
'''

import xbmc
import xbmcgui
import xbmcaddon

if __name__ == '__main__':
    
    addon_id = "service.partymode.autostart"
    Addon = xbmcaddon.Addon(addon_id)
    __is_enabled__ = Addon.getSetting('enable')
    
    if __is_enabled__:
    	xbmc.executebuiltin("XBMC.PlayerControl(PartyMode)")

