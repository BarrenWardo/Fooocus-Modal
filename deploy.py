import os
import subprocess
import modal

fooocus_port = 7860
server_timeout = 600
modal_gpu = "t4"
DIR = "/root/fooocus"

app = modal.App(
    image=modal.Image.debian_slim(python_version="3.11")
    .apt_install(
        "wget",
        "git",
        "libgl1",
        "libglib2.0-0",
    )  
)

volume = modal.Volume.from_name(
    "fooocus", create_if_missing=True
)

@modal.function(
        cpu=2,
        gpu=modal_gpu,
        memory=128,
        keep_warm=1,
        concurrency_limit=1,
        volumes={DIR: volume},
        _allow_background_volume_commits=True,
        allow_concurrent_inputs=10,
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
