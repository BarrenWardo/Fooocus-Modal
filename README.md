# 🚀 Fooocus-Modal

Deploy the Fooocus App using Modal with persistent volume.

## 📖 Tutorial

Follow this guide, and you can deploy the [Fooocus](https://github.com/lllyasviel/Fooocus.git) web app on modal in just a few minutes.

### 🛠️ Setting up Modal

1. Start by registering on [Modal](https://modal.com). 💰 (Bonus - You'll get $30 free every month.)

![Register on Modal](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/fa2ad8d8-506d-4d92-936a-1eeac9ea9ed5)

2. Once registered, click on your profile & then settings (top right corner).

![Profile Settings](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/fccc64bc-7ed5-4da4-9c4a-1093f69187b9)

3. Now click on "API Tokens".

![API Tokens](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/582c8c2b-47d5-4a9d-8efe-7a0734374d35)

4. Click on "New Token".

![New Token](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/7f3eb080-3803-4973-8a08-96a59f6ddc7f)

5. You'll get this window. Now copy the command mentioned here.

![Copy Command](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/de7f6126-4060-406e-bfe1-4475732399c9)

### 🖥️ Getting System Ready

6. Open Terminal.
7. Install modal:
   ```bash
   pip install modal
   ```
8. Check if modal is installed using this command:
   ```bash
   modal --version
   ```
   It should look something like this:

![Modal Version](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/98666410-c729-4bbb-89eb-5b21890c96da)

9. Now paste the command copied at step 5 & run it.
10. Then run:
    ```bash
    modal config show
    ```
    You should be able to see Token ID & Token Secret already set up here.

![Modal Config](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/3eb50d28-eace-4cba-af73-33569341d206)

11. Now go to any folder you want to run the setup from & git clone this repo & go into the cloned folder.
    ```bash
    git clone https://github.com/BarrenWardo/Fooocus-Modal.git && cd Fooocus-Modal
    ```

### 🚀 Deploy Fooocus

12. You can deploy it now by running:
    ```bash
    modal deploy deploy.py
    ```

13. You'll get a URL which should be something like this. Open it. Enjoy!
    ```
    xxyyzz-fooocus.modal.run
    ```

It'll take a few minutes for the web app to start. You can check logs on the modal dashboard.

Now Enjoy!

### 📝 Additional Notes

- You can stop the app by going to your Modal Dashboard > Deployed Apps > Fooocus > Stop (Top right)

![Stop App - Step 1](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/31ed3a76-b1b0-49e0-b30d-96c18f577b9c)
![Stop App - Step 2](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/8fde8481-843a-493e-ad47-0338d5e13932)

- You can also temporarily deploy using `modal serve`. Documentation [here](https://modal.com/docs/reference/cli/serve). You need to keep the terminal running. If the terminal is stopped, then the app gets stopped.
  - Go into Fooocus-Modal folder using terminal & run any command below:
    - `modal serve deploy.py` (runs until the terminal is closed)
    - `modal serve deploy.py --timeout 3600` (runs for 3600 seconds = 1 hour; you can change this number. Also, the terminal needs to be open or the app gets stopped)
   
- The deployment is currently set to run on a Tesla T4 GPU and 1 container which will cost approximately $1 per hour. You can change it in the deploy.py file at [line 7](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/365e72d0-5011-4c3a-a1ed-3ee65bd37d78). The GPU list is available [here](https://modal.com/docs/reference/modal.gpu).
   - “t4”
   - “l4”
   - “a100”
   - “h100”
   - “a10g”
   - “any”

- Modal Pricing :

![Modal Pricing](https://github.com/BarrenWardo/Fooocus-Modal/assets/86141456/ca311751-ab76-4fcb-8a70-dee269eb986f)


### 📓 Dev Notes

I know this might not be the best or most optimal way to deploy the app, but I tried my level best.
If you liked this, consider giving a star on this repo & supporting me here:

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H8OQTUC)
