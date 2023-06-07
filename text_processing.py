import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = """
You will be given OCR transcript of an image of a newspaper. Extract the articles. There will be multiple.

For each article, retrieve the Article title, author, date, concise and short summary. 

You must return all the articles you find. There will be multiple articles! Do not number the articles and just separate them using an empty line.
"""

def run_through_gpt(text: str) -> str:
  results = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
          { "role": "system", "content": SYSTEM_PROMPT },
          { "role": "user", "content": text },
      ]
  )

  return results.choices[0].message.content

def get_articles(ocr_output: str) -> str: 
  midpoint = len(ocr_output) // 2
  part1 = ocr_output[:midpoint]
  part2 = ocr_output[midpoint:]

  part1_results = run_through_gpt(part1)
  part2_results = run_through_gpt(part2)

  results = f"{part1_results}\n\n{part2_results}"

  return results