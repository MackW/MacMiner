'''
Created on Feb 23, 2014

@author: mack
'''
import os, sys,random
import pygame
from pygame.locals import *
from Helpers import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class MacMiner:
    sprPlayer=None
    msg="This is a test Scrolling message that will probably never really get read by anybody, but it looks cool anyway "
    def MainLoop(self): 
        self.CreatePlayerSprite()
        clock=pygame.time.Clock()
        font = pygame.font.Font(None, 72)                                                                                        
        text = font.render(self.msg, 1, (0, 255, 0))                               
        textpos = text.get_rect(x=self.width,centery=278)
        #self.screen.blit(text, textpos) 
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            self.screen.fill((0,0,0),self.sprPlayer.rect)
            self.sprPlayer.move()
            self.screen.blit(self.sprPlayer.image, self.sprPlayer.rect)
            self.screen.fill((0,0,0),textpos)
            self.screen.blit(text, textpos)
            textpos = text.get_rect(x=textpos.x-2,centery=278)
            pygame.display.flip()
            clock.tick(30)        
    
    def __init__(self, width=1024,height=768):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffersize = 1024    # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffersize)
        pygame.mixer.music.set_volume(0.5)    
    def CreatePlayerSprite(self):
        self.sprPlayer=Player()
        self.sprPlayer.rect.x=10
        self.sprPlayer.rect.y=self.height/2
 
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.images=load_tile_table('Player.png',48,56)
        self.hitmasks=[]
        for lc in xrange(0,len(self.images)-1):
            self.hitmasks.append(get_colorkey_hitmask(self.images[lc], self.images[lc].get_rect()))
        self.image = self.images[0]
        self.rect=self.image.get_rect()
        self.hitmask=self.hitmasks[0]
        self.Xdirection=1
        self.Ydirection=0
        self.currentFrameIndex=0
        self.currentAnimateFrames=[0,0,0,2,2,2,4,4,4,2,2,2]
        
    def move(self):
        if self.currentFrameIndex<len(self.currentAnimateFrames)-1:
            self.currentFrameIndex=self.currentFrameIndex+1
        else:
            self.currentFrameIndex=0
        currentFrameDirectionModifier =0
        if self.Xdirection==-1:
            currentFrameDirectionModifier =1
        self.image = self.images[self.currentAnimateFrames[self.currentFrameIndex]+currentFrameDirectionModifier]
        if (self.rect.x+self.Xdirection) <5 or (self.rect.x+self.rect.width+self.Xdirection) >1023: 
            self.Xdirection= self.Xdirection * -1
            self.currentFrameIndex=0

        self.hitmask=self.hitmasks[self.currentAnimateFrames[self.currentFrameIndex]+currentFrameDirectionModifier]
        self.rect.move_ip(self.Xdirection*4,0);
             
        
    def setXDirection(self,direction):
        self.Xdirection=direction
        
    def setYDirection(self,direction):
        self.Ydirection=direction   
             
    def setImageFrame(self,frame):
        self.currentFrame=frame 
        self.image = self.images[frame]
        self.hitmask=self.hitmasks[frame]
               
    
if __name__ == "__main__":
    MainWindow = MacMiner()
    MainWindow.MainLoop()