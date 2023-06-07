import gradio as gr

from google_vision import get_ocr_result
from text_processing import get_articles


def process_image(image):
    ocr_result = get_ocr_result(image)
    yield "Extracting articles...", ocr_result
    results = get_articles(ocr_result)
    yield results, ocr_result


demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="filepath", label="Upload an image"),
    outputs=[
        gr.Textbox(label="Extracted Articles"),
        gr.Textbox(label="Image OCR"),
    ],
    title="Extracting Articles from Newspaper Images",
)

demo.queue()
demo.launch()