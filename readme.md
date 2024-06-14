# 2023/24 T3 Eric FP Prototype

## 1. Getting Started

1. Install Python 3.10.11 (3.8 <= version <= 3.11)
   - [Download](https://www.python.org/downloads/release/python-31011/)
   - Required for TensorFlow and Keras 2.12.0

2. Create and activate a virtual environment (Windows)

   ```bash
   python -m venv myvenv && source myvenv/Scripts/activate
   ```

3. Install required packages

    ```bash
    pip install tensorflow==2.12.0 keras==2.12.0 numpy pillow flet
    ```

4. Replace your models (**keras_model.h5** and **labels.txt**) in the **models/** folder.
   > The default model is for dogs and cats classification.
   > You can replace the model with your own trained model on Teachable Machine.
   > To train your model, see

5. Run the script

    ```bash
    python main.py
    ```

6. Click the Floating Action Button (FAB) to select images.

7. Should see the results on screen.

## 2. Train & Obtain a Classification Model

1. Go to [Teachable Machine](https://teachablemachine.withgoogle.com/).
2. Click on **Get Started**.
3. Click on **Image Project**.
4. Train your model.
5. Click on "Export Model" and select **TensorFlow** tab.
6. Make sure "Model convertsion type" is selected "Keras", then click "Download my model".
7. Replace the model in the **models/** folder with the downloaded model.
