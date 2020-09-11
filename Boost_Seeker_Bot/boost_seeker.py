# This Program will be the first bot that I design for Rocket League!

from tools import *
from objects import *
from routines import *


# This file is for strategy

class Boost_Seeker(GoslingAgent):
    def run(agent):
        # this bot grabs boost

        # Checks the list of all boosts if they are active
        # picks the first boost it finds that is active and sets that as its target
        if agent.kickoff_flag:
            agent.push(kickoff())
        else:
            boost = agent.boosts[0]
            agent.push(goto_boost(agent, boost))

