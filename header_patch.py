        with gr.Box(visible=os.environ.get("SPACE_ID")):
            if os.environ.get("SPACE_ID") and str(os.environ.get("IS_SHARED_UI", "") or "") not in ("", "0"):
                gr.HTML(f"""
                <div class="gr-prose" style="max-width: 80%; font-size: 12px; line-height: 20px; font-family: monospace;">
                    <p>▲ Automatic1111's Stable Diffusion WebUI + Mikubill's ControlNet WebUI extension | Running on Hugging Face | Loaded checkpoint: <a href="https://civitai.com/models/10752/the-allys-mix-iii-revolutions" style="target=" _blank"="">theAllysMixIII_v10</a></p>
                    <p>▲ Docker build from <a href="https://github.com/kalaspuff/stable-diffusion-webui-docker" style="target=" _blank"="">🐙 GitHub ➔ kalaspuff/stable-diffusion-webui-docker</a> / <a href="https://huggingface.co/spaces/carloscar/stable-diffusion-webui-docker" style="target=" _blank"="">🤗 Hugging Face ➔ carloscar/stable-diffusion-webui-docker</a></p>
                    <p>▲ Duplicate this Space to run it privately without a queue + load additional checkpoints, VAE, LoRA models, etc.&nbsp;&nbsp;<a style="display:inline-block; position: absolute;" target="_blank" href="https://huggingface.co/spaces/{os.environ["SPACE_ID"]}?duplicate=true"><img style="margin: 0; height: 16px; position: relative; top: 2px;" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Duplicate%20Space-blue" alt="Duplicate Space"></a></p>
                </div>
                """)
            elif os.environ.get("SPACE_ID"):
                import torch
                if not torch.cuda.is_available():
                    gr.HTML(f"""
                    <div class="gr-prose" style="max-width: 80%; font-size: 12px; line-height: 20px; font-family: monospace;">
                        <p>▲ Docker setup: <a href="https://huggingface.co/spaces/carloscar/stable-diffusion-webui-docker" style="target=" _blank"="">🤗 Hugging Face ➔ carloscar/stable-diffusion-webui-docker</a> | <a href="https://github.com/kalaspuff/stable-diffusion-webui-docker" style="target=" _blank"="">🐙 GitHub ➔ kalaspuff/stable-diffusion-webui-docker</a></p>
                        <p>▲ Load additional checkpoints, VAE, LoRA models, etc. Read more on the README at the GitHub link above.</p>
                        <p>▲ This Space is currently running on CPU, which may yield very slow results - you can upgrade for a GPU <a href="https://huggingface.co/spaces/{os.environ["SPACE_ID"]}/settings" style="text-decoration: underline" target="_blank">in the Settings tab</a></p>
                    </div>
                    """)
                else:
                    gr.HTML(f"""
                    <div class="gr-prose" style="max-width: 80%; font-size: 12px; line-height: 20px; font-family: monospace;">
                        <p>▲ Docker setup: <a href="https://huggingface.co/spaces/carloscar/stable-diffusion-webui-docker" style="target=" _blank"="">🤗 Hugging Face ➔ carloscar/stable-diffusion-webui-docker</a> | <a href="https://github.com/kalaspuff/stable-diffusion-webui-docker" style="target=" _blank"="">🐙 GitHub ➔ kalaspuff/stable-diffusion-webui-docker</a></p>
                        <p>▲ Load additional checkpoints, VAE, LoRA models, etc. Read more on the README at the GitHub link above.</p>
                        <p>▲ This Space has GPU enabled - remember to remove the GPU from the space <a href="https://huggingface.co/spaces/{os.environ["SPACE_ID"]}/settings" style="text-decoration: underline" target="_blank">in the Settings tab</a> when you're done.</p>
                    </div>
                    """)
