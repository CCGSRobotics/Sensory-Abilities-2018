from imageai.Prediction.Custom import ModelTraining
model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("Hazmat Training")
model_trainer.trainModel(num_objects=61, num_experiments=100, enhance_data=True, batch_size=32, show_network_summary=True)

#Algorithms for image prediction include SqueezeNet, ResNet, InceptionV3, DenseNet
