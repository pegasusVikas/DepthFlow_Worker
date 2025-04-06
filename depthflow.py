import os
from DepthFlow.Scene import DepthScene
from retrieveAssets import download_files_from_gcp

GCP_IMG_PATH = "images/"
IMAGES_LOCAL_PATH = "images"
VIDEOS_LOCAL_PATH = "videos"

def generate_depthflow_video(imagePath, outputPath ,animation="zoom",speed=1.0, time=3):
    # Create a DepthScene object
    scene = DepthScene()

    # Load the input image
    scene.input(image=imagePath)

    match animation:
        case "zoom":
            scene.zoom()
        case "dolly":
            scene.dolly()
        case "vertical":
            scene.vertical()
        case "horizontal":
            scene.horizontal()
        case "circle":
            scene.circle()
        case "orbital":
            scene.orbital()

    # Add main animation with specified output format and speed
    scene.main(output=outputPath, time=time)



if __name__ == "__main__": 
    img_paths = download_files_from_gcp(GCP_IMG_PATH, IMAGES_LOCAL_PATH)
    my_list: list[dict[str, int]] = [
    {"animation": "zoom"},
    {"animation": "circle"},
    {"animation": "dolly"},
    {"animation": "horizontal"},
    {"animation": "orbital"},
    ]

    os.makedirs(VIDEOS_LOCAL_PATH, exist_ok=True)

    for i in range(len(img_paths)):
        imagePath = img_paths[i]
        outputPath = f"{VIDEOS_LOCAL_PATH}/video{i}"
        animation = my_list[i]["animation"]
        generate_depthflow_video(imagePath, outputPath, animation=animation)

    
    


#depthflow input -i C:\Users\Vikas\Pictures\Screenshots\trident.png  main --format mp4 --output output1 --speed 1.2
#python ./DepthFlow1/Examples/Basic.py input -i hammer.png zoom  main --format mp4 --output output1 