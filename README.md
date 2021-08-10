# TensorFlow-Lite-Object-Detection-Verdin-IMX8MP
forks from https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi
This demo uses iMX8M Plus NPU to accelerate TensorFLow lite.

How to run:
root@verdin-imx8mp:~# export XDG_RUNTIME_DIR=/run/user/0
root@verdin-imx8mp:~# python3 tf-lite-detection-webcam.py --modeldir /home/root/PyOpenCV --graph lite-model_ssd_mobilenet_v1_1_metadata_2.tflite --labels labelmap.txt --resolution 1280x720
