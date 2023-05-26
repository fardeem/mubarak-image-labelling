import json
import os

from dotenv import load_dotenv
from google.cloud import vision
from google.oauth2 import service_account

load_dotenv()

service_account_info = json.loads(
    os.environ["GOOGLE_SERVICE_KEY"]
)


def get_ocr_result(image_path):
    credentials = service_account.Credentials.from_service_account_info(
      service_account_info
    )
    client = vision.ImageAnnotatorClient(credentials=credentials)

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return "No text detected"