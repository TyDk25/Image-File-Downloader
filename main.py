import requests 

url ="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/2005_Volkswagen_Golf_GTi_2.0_Front.jpg/200px-2005_Volkswagen_Golf_GTi_2.0_Front.jpg"
response = requests.get(url)



with open("image.jpg", "wb") as file:
    (file.write(response.content))
    


