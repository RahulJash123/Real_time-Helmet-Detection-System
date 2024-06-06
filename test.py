from roboflow import Roboflow
import os

os.environ["DATASET_DIRECTORY"] = "dataset"

rf = Roboflow(api_key="9dUUp5PTKNPuhONxd3B7")
project = rf.workspace("coders-ks").project("helmet-detection-534zu")
version = project.version(1)
dataset = version.download("yolov5")