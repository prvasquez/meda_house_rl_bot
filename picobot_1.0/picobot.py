from tools import *
from objects import *
from routines import *


# This file is for strategy

class ExampleBot(GoslingAgent):
    def run(agent):
        # An example of using raw utilities:
        relative_target = agent.ball.location - agent.me.location
        local_target = agent.me.local(relative_target)
        defaultPD(agent, local_target)
        defaultThrottle(agent, 2300)
        default
