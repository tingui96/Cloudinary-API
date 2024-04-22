import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def initial():
    return { 'hello wold' }

@app.get("/api/cloudinary")
def read_root(url,name):
    response = up_image(url,name)
    return response
