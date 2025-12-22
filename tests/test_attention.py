def test_attention_runs():
    from symbolic_attention.tensor import SymbolicAttentionTensor
    att = SymbolicAttentionTensor(dim=32)
    out = att.encode("hello world")
    assert "tokens" in out
    assert "vector" in out