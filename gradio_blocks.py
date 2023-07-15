import gradio as gr

def demo_function(text: str) -> str:
    return text

def clear_function() -> tuple:
    return '', ''

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_text = gr.components.Textbox(label='Input')
            with gr.Row():
                clear = gr.components.Button(value='Clear', variant='stop')
                submit = gr.components.Button(value='Submit', variant='primary')
        output_text = gr.components.Textbox(label='Output')

    submit.click(demo_function, [input_text], [output_text])
    clear.click(clear_function, [], [input_text, output_text])

if __name__ == '__main__':
    demo.launch()
