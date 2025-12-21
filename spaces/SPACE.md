# 🐞 BugBot Cyber Arena — Hugging Face Space

This Space is the **public cockpit** for the BugBotAgent organism.

It exposes:

- **Symbolic Attention Tensor** — compresses input into a symbolic vector space  
- **STDP Spiking Layer** — adapts synaptic weights over time  
- **Cyber Fuzz Engine** — generates and detects fuzz/anomaly patterns  
- **Robotics Embodiment** — simulates motor-like state updates  
- **LLM Cortex Adapter** — lets you swap the “brain organ” live (Transformers / ChatGPT / Grok)  

The Space UI lets you:

1. Enter natural language, commands, or fuzz patterns (e.g., `<script>`, `AAAAA`, `../`).  
2. Choose which LLM backend powers the **cortex organ**.  
3. Inspect the full internal state of the organism after one cycle:
   - perception → adaptation → defense → embodiment → reflection.

---

## 🔧 Technical Details

- Frontend: **Gradio**  
- Backend: `BugBotAgent` (Python)  
- LLM integration: `src/llm_adapter/`  
- Organs:
  - `src/symbolic_attention/`
  - `src/spiking_stdp/`
  - `src/cyber_arena/`
  - `src/robotics/`
  - `src/llm_adapter/`

Entry point for the Space:

```bash
spaces/cyber_arena_app/app.py