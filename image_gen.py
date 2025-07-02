import torch
from diffusers import StableDiffusionPipeline
from huggingface_hub import login
import random

def generate_image(prompt,width=512, height=512):
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16,
    ).to("cuda")
    seed= random.randint(1, 9999999)
    prompt = prompt
    image = pipe(
    prompt,
        negative_prompt="blurry, distorted, low quality, extra limbs, bad anatomy",
        height=height,
        width=width,
        guidance_scale=8.5,
        num_inference_steps=50,
        max_sequence_length=512,
        generator=torch.Generator("cuda").manual_seed(seed)
    ).images[0]
    image.save("assets/temp_img.png")
    return "assets/temp_img.png"