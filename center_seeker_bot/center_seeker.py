# This Program will be the first bot that I design for Rocket League!

from tools import *
from objects import *
from routines import *


# This file is for strategy

class Center_Seeker(GoslingAgent):
    def run(self):
        # This bot will be a bully and only try to boom other players
        # when they are on their own half

        # Establishing where the center of the court is
        center = Vector3(0,0,0)
        relative_target = center - self.me.location
        local_target = self.me.local(relative_target)
        if local_target.magnitude() == 0:
            deafaultThrottle(self, 0)
        else:
            defaultPD(self, local_target)
            defaultThrottle(self, 2300)


'''
    def check_foes_in_half(self):
        num_foes = len(self.foes)
        for foe in self.foes:
'''
