from tools import *
from objects import *
from routines import *


# This file is for strategy

class Bully(GoslingAgent):
    def run(self):
        # This bot will be a bully and only try to boom other players
        # when they are on their own half

        relative_target = self.ball.location - self.me.location
        local_target = self.me.local(relative_target)
        defaultPD(self, local_target)
        defaultThrottle(self, 2300)

