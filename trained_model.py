import subprocess

# Properly format the command string
command = (
    "python C:\\ML_projects\\helmet_detection2\\yolov5\\train.py "
    "--img 640 --batch 16 --epochs 20 "
    "--data C:\\ML_projects\\helmet_detection2\\dataset\\HELMET-DETECTION-1\\data.yaml "
    "--weights yolov5s.pt --cache"
)

# Run the command
subprocess.run(command, shell=True, check=True)


python C:\ML_projects\helmet_detection2\yolov5\detect.py --weights C:\ML_projects\helmet_detection2\yolov5\runs\train\exp\weights\best.pt --img 640 --conf 0.1 --source C:\ML_projects\helmet_detection2\img4.jpeg