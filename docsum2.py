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
import tempfile
from base64 import b64encode

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text, chunk_size=3000, max_chunks=3):
    # Split text into large chunks and limit number of summaries
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
        if len(chunks) >= max_chunks:  # limit to first N chunks
            break

    summaries = []
    for chunk in chunks:
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": f"Summarize this:\n\n{chunk}"}]
        )
        summaries.append(response.choices[0].message.content.strip())

    return "\n\n".join(summaries)

def llm_image(image_data):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{
        "role": "user",
        "content":[
            {"type": "text", "text": "Describe this image."},
            {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + image_data}}
        ]
    }]     
)
    return response.choices[0].message.content.strip()

def extract_text(source, ext, is_raw=False):
    if ext == "txt":
        if is_raw:
            return source
        with open(source, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == "html":
        if is_raw:
            soup = BeautifulSoup(source, "html.parser")
        else:
            with open(source, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
        return soup.get_text()
    elif ext == "pdf":
        if is_raw:
            raise ValueError("PDF content must come from file, not raw bytes.")
        with pdfplumber.open(source) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def summarize_file(path_or_url):
    try:
        if path_or_url.startswith("http"):
            resp = requests.get(path_or_url)
            mime = resp.headers.get("Content-Type", "")
            if "image" in mime:
                b64_img = b64encode(resp.content).decode()
                return llm_image(b64_img)
            else:
                html_text = extract_text(resp.text, "html", is_raw=True)
                return summarize_text(html_text)
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

