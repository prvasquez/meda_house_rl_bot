# This Program will be the first bot that I design for Rocket League!

from tools import *
from objects import *
from routines import *


# This file is for strategy

class Boost_Seeker(GoslingAgent):
    def run(self):
        # this bot grabs boost
        target = self.boost.location - self.me.location
        local_target = self.me.local(target)

        defaultPD(self, local_target)
        defaultThrottle(self, 2300)



