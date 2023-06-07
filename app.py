import gradio as gr

from google_vision import get_ocr_result
from text_processing import get_articles


def process_image(image):
    ocr_result = get_ocr_result(image)
    results = get_articles(ocr_result)
    return f"{results}\n\n\nOCR Result:\n{ocr_result}"


demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="filepath", label="Upload an image"),
    outputs="text",
    title="OCR using Google Vision API",
)

demo.launch()