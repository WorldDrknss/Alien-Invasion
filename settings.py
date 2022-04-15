# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:31:46 2021

@author: I am The God Father
"""

class Settings:
    
    def __init__(self):
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = (60, 60, 60)
        self.bullet_allow = 10

        self.alien_speed = 0.75
        self.fleet_drop_speed = 2
        #fleet_direction of 1 represents right, -1 respresents left
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inisialize settings that change during gameplay"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.75
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        """increase speeds"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)