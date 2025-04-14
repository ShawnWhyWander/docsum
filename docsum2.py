import argparse
import os
import requests
from groq import Groq
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import mimetypes
from bs4 import BeautifulSoup
import pdfplumber

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=[{"role":"user", "content": f"Summarize this:{text}"}]
    )
    return response.choices[0].message.content.strip()

def llm_image(image_data):
    response = client.chat.completions.create(
        model="llava-llama3-8b",
        messages=[{
        "role": "user",
        "content":[
            {"type": "text", "text": "Describe this image."},
            {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + image_data}}
        ]
    }]     
)
    return response.choices[0].message.content.strip()

def extract_text(path,ext):
    if ext == "txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == "html":
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            return soup.get_text()
    elif ext == "pdf":
        with pdfplumber.open(path) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    else: raise ValueError(f"Unsupported file type:{ext}")

def summarize_file(path_or_url):
    try:
        if path_or_url.startswith("http"):
            resp = requests.get(path_or_url)
            mime = resp.headers.get("Content-Type", "")
            if "image" in mime:
                b64_img = b64encode(resp.content).decode()
                return llm_image(b64_img)
            else:
                temp_file = BytesIO(resp.content)
                temp_file.name = "temp.html"
                return summarize_text(extract_text(temp_file.name, "html"))
        else:
            mime = mimetypes.guess_type(path_or_url)[0]
            if mime and "image" in mime:
                with open(path_or_url, "rb") as f:
                    b64_img = b64encode(f.read()).decode()
                    return llm_image(b64_img)
            else:
                ext = os.path.splitext(path_or_url)[-1].lower().strip(".")
                return summarize_text(extract_text(path_or_url, ext))
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize documents or images.")
    parser.add_argument("input", help="File path or URL to summarize")
    args = parser.parse_args()

    summary = summarize_file(args.input)

    print (summary)

