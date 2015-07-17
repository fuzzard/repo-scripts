
import sys
import xbmc
import xbmcgui
import xbmcaddon
import json as json
import urllib

ACTION_PLAYER_STOP = 13
    
class StillWatchingInfo(xbmcgui.WindowXMLDialog):

    item = None
    cancel = False
    stillwatching = False
    
    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

    def onInit(self):
        self.action_exitkeys_id = [10, 13]
    
        image = self.item['art'].get('tvshow.poster','')
        thumb = self.item['art'].get('thumb','')
        landscape = self.item['art'].get('tvshow.landscape','')
        fanartimage = self.item['art'].get('tvshow.fanart','')
        clearartimage = self.item['art'].get('tvshow.clearart','')
        name = self.item['label']
        rating = str(round(float(self.item['rating'])))
        year = self.item['firstaired']
        overview = self.item['plot']
        season = self.item['season']
        episodeNum = self.item['episode']
        title = self.item['title']
        # set the dialog data
        self.getControl(4000).setLabel(name)
        self.getControl(4006).setText(overview)
        self.getControl(4001).setImage(image)
        try:
            thumbControl = self.getControl(4002)
            if(thumbControl != None):
                self.getControl(4002).setImage(thumb)
        except:
            pass
        self.getControl(4003).setLabel(rating)
        self.getControl(4004).setLabel(year)
        
        try:
            landscapeControl = self.getControl(4005)
            if(landscapeControl != None):
                self.getControl(4005).setImage(landscape)
        except:
            pass
        
        try:
            fanartControl = self.getControl(4007)
            if(fanartControl != None):
                fanartControl.setImage(fanartimage)
        except:
            pass
        
        try:
            seasonControl = self.getControl(4008)
            if(seasonControl != None):
                seasonControl.setLabel(str(season))
        except:
            pass
        
        try:
            episodeControl = self.getControl(4009)
            if(episodeControl != None):
                episodeControl.setLabel(str(episodeNum))
        except:
            pass
        
        try:
            titleControl = self.getControl(4010)
            if(titleControl != None):
                titleControl.setLabel(title)
        except:
            pass
        
        try:
            resolutionControl = self.getControl(4011)
            if(resolutionControl != None):
                resolution1 =  self.item['streamdetails'].get('video')
                resolution = resolution1[0].get('height')    
                resolutionControl.setLabel(str(resolution))
        except:
            pass
        
        try:
            clearartControl = self.getControl(4014)
            if(clearartControl != None):
                clearartControl.setImage(clearartimage)
        except:
            pass
        
    def setItem(self, item):
        self.item = item
    
    def setCancel(self, cancel):
        self.cancel = cancel
        
    def isCancel(self):
        return self.cancel
            
    def setStillWatching(self, stillwatching):
        self.stillwatching = stillwatching
    
    def isStillWatching(self):
        return self.stillwatching
    
    def onFocus(self, controlId):
        pass
        
    def doAction(self):
        pass

    def closeDialog(self):
        self.close()        
        
    def onClick(self, controlID):
        
        xbmc.log("still watching info onclick: "+str(controlID))

        if(controlID == 4012):
            # still watching
            self.setStillWatching(True)
            self.close()
        
        elif(controlID == 4013):
            #cancel
            self.setCancel(True)
            self.close()

        pass
    
    def onAction(self, action):
        
        xbmc.log("still watching info action: "+str(action.getId()))
        if action == ACTION_PLAYER_STOP:
            self.close()
     
