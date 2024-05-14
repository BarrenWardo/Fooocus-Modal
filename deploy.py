import os
import subprocess
import modal

fooocus_port = 7865
server_timeout = 1200
modal_gpu = "t4"
DIR = "/root/fooocus"

app = modal.App(
    "Fooocus",
    image=modal.Image.debian_slim(python_version="3.11")
    .apt_install(
        "wget",
        "git",
        "libgl1",
        "libglib2.0-0",
    )
    .pip_install(
        "torchsde==0.2.5",
        "einops==0.4.1",
        "transformers==4.30.2",
        "safetensors==0.3.1",
        "accelerate==0.21.0",
        "pyyaml==6.0",
        "Pillow==9.2.0",
        "scipy==1.9.3",
        "tqdm==4.64.1",
        "psutil==5.9.5",
        "pytorch_lightning==1.9.4",
        "omegaconf==2.2.3",
        "gradio==3.41.2",
        "pygit2==1.12.2",
        "opencv-contrib-python==4.8.0.74",
        "httpx==0.24.1",
        "onnxruntime==1.16.3",
        "timm==0.9.2",
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
        _allow_background_volume_commits=True,
        allow_concurrent_inputs=100,
        timeout=server_timeout,
        container_idle_timeout=120,
)

@modal.web_server(port=fooocus_port, startup_timeout=server_timeout)

def run_fooocus():
    fooocus_folder = os.path.join(DIR, "Fooocus")
    if os.path.exists(fooocus_folder):
        fooocus_process = f"""
            cd {fooocus_folder} && git pull && pip install -r requirements_versions.txt && python entry_with_update.py --listen --port {fooocus_port}
        """
    else:
        fooocus_process = f"""
            cd {DIR} && git clone https://github.com/lllyasviel/Fooocus.git && cd Fooocus && pip install -r requirements_versions.txt && python entry_with_update.py --listen --port {fooocus_port}
        """
    subprocess.Popen(fooocus_process, shell=True)
