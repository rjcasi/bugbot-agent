def test_agent_cycle():
    from bugbot_agent import BugBotAgent
    from bugbot_agent.organ_hub import (
        SymbolicAttentionTensor, STDPSpikingLayer,
        CyberFuzzEngine, RoboticsEmbodiment
    )

    agent = BugBotAgent(
        attention_module=SymbolicAttentionTensor(dim=32),
        spiking_module=STDPSpikingLayer(dim=32),
        cyber_defense_module=CyberFuzzEngine(),
        robotics_module=RoboticsEmbodiment(),
        llm_module=None,
    )

    out = agent.step("hello")
    assert "perceived" in out
    assert "adapted" in out