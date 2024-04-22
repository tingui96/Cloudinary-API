import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()


cloudinary.config(
cloud_name = "dwxlnnou1",
api_key = "978228329273535",
api_secret = os.getenv('API_SECRET'),
)


def up_image(url,name):
    try:
        response = cloudinary.uploader.upload(url, public_id=name, overwrite=True, ocr = "adv_ocr")
        return response["info"]["ocr"]["adv_ocr"]["data"][0]["fullTextAnnotation"]["text"]
    except Exception as error:
        print("Error",error)
    


app = FastAPI()

@app.get("/")
def initial():
    return { 'hello wold' }

@app.get("/api/cloudinary")
def read_root(url,name):
    response = up_image(url,name)
    return response
