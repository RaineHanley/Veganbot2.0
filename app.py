import openai
import gradio as gr

openai.api_key = "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"




messages = [
    # {"role": "system", "content": "You are a helpful AI assistant that only provides vegan recipies using only ingredients in the input.You add a vegan fact after every recipe"}
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Enter the ingredients you would like to use")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Vegan Recipe AI",
             description="Ask me to create a recipe for you using the ingredients you have at home",
             theme="compact").launch(share=True)