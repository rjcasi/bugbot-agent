class RedBlueCockpit:
    """
    RB-App integrated as a BugBot-Agent organ.
    This organ acts as the Red/Blue Team cockpit and can call
    the agent's fuzzer, defender, and analyzer.
    """

    def __init__(self, agent):
        self.agent = agent

    def start(self):
        return "Red/Blue Cockpit Organ initialized."

    def run_fuzz(self, target: str):
        return self.agent.fuzzer.fuzz(target)

    def auto_defend(self, event: dict):
        return self.agent.defender.respond(event)

    def explain(self, event: dict):
        return self.agent.analyzer.explain(event)
