Initially  **download model fruit_rec.pt** from the link below (due to file size) and include it in root folder:  
https://drive.google.com/drive/folders/1aco2IKkyzprG1OhSOaRFdeig-cLlWhCz?usp=sharing  
  
COMMANDS: 
- build the docker image :  
`docker build -t K2_DSCM034`
- run the image :  
`docker run -d -p 0.0.0.0:8000:8000/tcp --name K2_DSCM034_container K2_DSCM034`
  
API CALLS:  
- GET / -> returns just a simple message to test that the server is running  
- POST /predict_image -> requires image file to be uploaded and returns as response predicted class (fruit/vegetable name)  

##### example output :  
`{  
    "predicted": "Watermelon"  
}`

POST example: 
<img width="866" alt="example" src="https://user-images.githubusercontent.com/64424805/177720829-6276dca2-a1a1-4a71-a18c-ad6de994a00a.png">
