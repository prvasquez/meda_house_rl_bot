# This Program will be the first bot that I design for Rocket League!

from tools import *
from objects import *
from routines import *


# This file is for strategy

class Boost_Seeker(GoslingAgent):
    def run(self):
        # this bot grabs boost

        # Checks the list of all boosts if they are active
        # picks the first boost it finds that is active and sets that as its target
        if self.kickoff_flag:
            self.push(kickoff())
        else:
            boost = self.boosts[0]
            self.push(goto_boost(self, boost))

