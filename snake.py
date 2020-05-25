# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:14:20 2020

@author: User
"""


class snake:
    def __init__(self, Lenght=4):    
        self.lenght=Lenght
        self.position=[[10,10]]
        for i in range(0,Lenght-1):
            self.position.append([9-i,10])
   
    def move_down(self):
        
        prev_position=(self.position[0]).copy()
        
        i=0
        for x in self.position:
            if i==0:
                self.position[i][0]+=1
            else:
                buff=self.position[i]
                self.position[i]=prev_position
                prev_position=buff
            i+=1
            
            
    def move_up(self):
        
        prev_position=(self.position[0]).copy()
        
        i=0
        for x in self.position:
            if i==0:
                self.position[i][0]-=1
            else:
                buff=self.position[i]
                self.position[i]=prev_position
                prev_position=buff
            i+=1
   

    def move_right(self):
        
        prev_position=(self.position[0]).copy()
        
        i=0
        for x in self.position:
            if i==0:
                self.position[i][1]+=1
            else:
                buff=self.position[i]
                self.position[i]=prev_position
                prev_position=buff
            i+=1
    
    def move_left(self):
        
        prev_position=(self.position[0]).copy()
        
        i=0
        for x in self.position:
            if i==0:
                self.position[i][1]-=1
            else:
                buff=self.position[i]
                self.position[i]=prev_position
                prev_position=buff
            i+=1