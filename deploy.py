import os
import subprocess
import modal

fooocus_port = 7865
server_timeout = 1200
modal_gpu = "t4"
DIR = "/root/fooocus"

app = modal.App(
    "Fooocus",
    image=modal.Image.debian_slim(python_version="3.11.9")
    .apt_install(
        "wget",
        "git",
        "libgl1",
        "libglib2.0-0",
    )
    .pip_install(
        "torchsde==0.2.6",
        "einops==0.8.0",
        "transformers==4.42.4",
        "safetensors==0.4.3",
        "accelerate==0.32.1",
        "pyyaml==6.0.1",
        "pillow==10.4.0",
        "scipy==1.14.0",
        "tqdm==4.66.4",
        "psutil==6.0.0",
        "pytorch_lightning==2.3.3",
        "omegaconf==2.3.0",
        "gradio==3.41.2",
        "pygit2==1.15.1",
        "opencv-contrib-python-headless==4.10.0.84",
        "httpx==0.27.0",
        "onnxruntime==1.18.1",
        "timm==1.0.7",
        "numpy==1.26.4",
        "tokenizers==0.19.1",
        "packaging==24.1",
        "rembg==2.0.57",
        "groundingdino-py==0.4.0",
        "segment_anything==1.0",
    )
)

volume = modal.Volume.from_name(
    "fooocus", create_if_missing=True
)

@app.function(
        cpu=2,
        gpu=modal_gpu,
        memory=128,
        #keep_warm=1,
        concurrency_limit=1,
        volumes={DIR: volume},
        allow_concurrent_inputs=100,
        timeout=server_timeout,
        container_idle_timeout=300,
)

@modal.web_server(port=fooocus_port, startup_timeout=server_timeout)

def run_fooocus():
    fooocus_folder = os.path.join(DIR, "Fooocus")
    if os.path.exists(fooocus_folder):
        fooocus_process = f"""
            cd {fooocus_folder} && python entry_with_update.py --listen --port {fooocus_port}
        """
    else:
        fooocus_process = f"""
            cd {DIR} && git clone https://github.com/lllyasviel/Fooocus.git && cd Fooocus && pip install -r requirements_versions.txt && python entry_with_update.py --listen --port {fooocus_port}
        """
    subprocess.Popen(fooocus_process, shell=True)
