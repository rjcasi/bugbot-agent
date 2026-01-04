# src/bugbot_agent/organ_hub.py

from src.bugbot_agent.organs.red_blue_cockpit.controller import RedBlueCockpit

class OrganHub:
    """
    Central registry for all organs attached to the BugBot-Agent.
    """

    def __init__(self, agent):
        self.agent = agent
        self.organs = {}

        # Initialize organs here
        self.register("red_blue_cockpit", RedBlueCockpit(agent))

    def register(self, name, organ):
        self.organs[name] = organ

    def get(self, name):
        return self.organs.get(name)
