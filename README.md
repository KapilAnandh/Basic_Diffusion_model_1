## Stable Diffusion Image Generator (Colab + Gradio)

This project is a Stable Diffusion pipeline built with Hugging Face diffusers and gradio.
It runs smoothly on Google Colab GPU and also locally.

## Features

Run Stable Diffusion (v1.5 or SDXL)

Save generated images to examples/

Interactive Gradio Web UI

Easy configuration with config.py

Lightweight, modular, and extensible codebase

Works both in notebooks (Colab) and local environments

## Learning Goals

This project is also designed as a learning resource for anyone new to AI art generation.
By going through the code, you will learn:

How Stable Diffusion works using the Hugging Face diffusers library

How to set up a pipeline for text-to-image generation

How to optimize memory usage with .enable_attention_slicing() (important in Colab GPUs)

How to integrate Gradio to build a simple yet powerful web interface

How to structure a Python ML project with configs, utils, and inference modules

How to save, organize, and share AI-generated outputs

Basics of deploying and sharing AI apps (e.g., via Colab, GitHub, or Hugging Face Spaces)
