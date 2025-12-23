import gradio as gr
from src.robotics.arena import RoboticsArena

arena = RoboticsArena()

def step():
    return arena.step()

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Robotics Arena")
    out = gr.JSON()
    btn = gr.Button("Step")
    btn.click(step, outputs=out)

demo.launch()