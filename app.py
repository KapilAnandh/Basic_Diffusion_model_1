import gradio as gr
from inference import StableDiffusionGenerator
from config import NUM_INFERENCE_STEPS, GUIDANCE_SCALE

generator = StableDiffusionGenerator()

def generate_image(prompt, steps, scale):
    return generator.generate(prompt, steps, scale, save=False)

demo = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your creative prompt here..."),
        gr.Slider(1, 50, value=NUM_INFERENCE_STEPS, label="Steps"),
        gr.Slider(1, 20, value=GUIDANCE_SCALE, label="Guidance scale")
    ],
    outputs="image",
    title="Stable Diffusion Image Generator",
    description="Generate AI images using Hugging Face Diffusers and Gradio."
)

if __name__ == "__main__":
    demo.launch(share=True)
