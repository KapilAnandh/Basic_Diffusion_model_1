import torch
from diffusers import DiffusionPipeline
from PIL import Image
import os
from config import MODEL_ID, DEVICE, GUIDANCE_SCALE, NUM_INFERENCE_STEPS, OUTPUT_DIR
from utils import ensure_dir

class StableDiffusionGenerator:
    def __init__(self, model_id=MODEL_ID, device=DEVICE):
        self.pipe = DiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            use_safetensors=True
        )
        self.pipe.enable_attention_slicing()
        self.pipe = self.pipe.to(device)
        ensure_dir(OUTPUT_DIR)

    def generate(self, prompt: str, steps=NUM_INFERENCE_STEPS, scale=GUIDANCE_SCALE, save=True):
        result = self.pipe(prompt, num_inference_steps=steps, guidance_scale=scale)
        img = result.images[0]
        
        if save:
            filename = os.path.join(OUTPUT_DIR, "output.png")
            img.save(filename)
            print(f"✅ Image saved at: {filename}")
        
        return img
