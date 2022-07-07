import torch
import torch.nn as nn
from torchvision import datasets, models, transforms
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
model = models.vgg16(pretrained=True)

for param in model.features.parameters():
    param.requires_grad = False

class_names = ['Apple Braeburn', 'Apple Granny Smith', 'Apricot', 'Avocado', 'Banana', 'Blueberry', 'Cactus fruit', 'Cantaloupe', 'Cherry', 'Clementine', 'Corn', 'Cucumber Ripe', 'Grape Blue', 'Kiwi', 'Lemon', 'Limes', 'Mango', 'Onion White', 'Orange', 'Papaya', 'Passion Fruit', 'Peach', 'Pear', 'Pepper Green', 'Pepper Red', 'Pineapple', 'Plum', 'Pomegranate', 'Potato Red', 'Raspberry', 'Strawberry', 'Tomato', 'Watermelon']

num_features = model.classifier[6].in_features
features = list(model.classifier.children())[:-4]
features.extend([nn.Linear(num_features, len(class_names))])
model.classifier = nn.Sequential(*features)

model.load_state_dict(torch.load('/fruit_rec.pt'))

data_dir = "/input_folder"
upload_path = "/input_folder/uploads"
#Applying Transformation
input_transforms = transforms.Compose([
                               transforms.Resize(224),
                               transforms.CenterCrop(224),
                               transforms.ToTensor()])
@app.get("/")
def get_status():
    return {"status": "it works"}

@app.post("/predict_image")
def create_upload_file(uploaded_file: UploadFile):
    file_location = upload_path+'/upload.jpg'
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    input_data = datasets.ImageFolder(data_dir, transform=input_transforms)
    inputloader = torch.utils.data.DataLoader(input_data, batch_size=1, shuffle=True, num_workers=4)

    imgs, classes = next(iter(inputloader))

    prediction = model(imgs)

    _, preds = torch.max(prediction.data, 1)
    class_ind = int(preds[0])
    return {"predicted": class_names[class_ind]}







