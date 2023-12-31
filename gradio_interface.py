import gradio as gr

def demo_function(text: str) -> str:
    return text

demo = gr.Interface(
    fn=demo_function,
    inputs=gr.components.Textbox(label='Input'),
    outputs=gr.components.Textbox(label='Output'),
    allow_flagging='never'
)

if __name__ == '__main__':
    demo.launch()
