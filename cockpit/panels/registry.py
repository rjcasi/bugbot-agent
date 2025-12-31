class OrganRegistry:
    def __init__(self):
        self._organs = {}

    def register(self, name, factory):
        self._organs[name] = factory

    def create(self, name, *args, **kwargs):
        return self._organs[name](*args, **kwargs)


def default_registry():
    from bugbot_agent.cockpit.panels.topology_panel import TopologyPanel
    from bugbot_agent.geometry.metric_panel import MetricPanel
    from bugbot_agent.geometry.curvature_panel import CurvaturePanel

    reg = OrganRegistry()
    reg.register("topology", lambda space: TopologyPanel(space))
    reg.register("metric", lambda structure: MetricPanel(structure))
    reg.register("curvature", lambda structure: CurvaturePanel(structure))
    return reg