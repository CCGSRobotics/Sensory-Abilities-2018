from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()

print(execution_path)

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()

prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))

prediction.setModelPath(os.path.join(execution_path, "idenprof_061-0.7933.h5"))

all_images_array = []

prediction.loadModel(num_objects=3)

all_files = os.listdir(os.path.join(execution_path, "Images"))

for each_file in all_files:
    if(each_file.endswith(".jpg") or each_file.endswith(".png")):
        all_images_array.append(os.path.join(os.path.join(execution_path, "Images"), each_file))

print(all_images_array)

results_array = prediction.predictMultipleImages(all_images_array, result_count_per_image=3)

for each_result in results_array:
    predictions, percentage_probabilities = each_result["predictions"], each_result["percentage_probabilities"]
    for index in range(len(predictions)):
        print(predictions[index] , " : " , percentage_probabilities[index])
    print("-----------------------")



#Single Image Prediction
'''
from imageai.Prediction.Custom import CustomImagePrediction
import os
execution_path = os.getcwd()

print(execution_path)

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()

prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))

prediction.setModelPath(os.path.join(execution_path, "idenprof_061-0.7933.h5"))

prediction.loadModel(num_objects=3)

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "RMRC_2019_Rules_V1.jpg"), result_count=4)


for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction + " : " + eachProbability)
'''
