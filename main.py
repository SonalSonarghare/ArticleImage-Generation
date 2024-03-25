from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

api_key = os.environ['OPENAI_KEY']
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/generateimg.html')
def generate_img():
  return render_template('generateimg.html')


@app.route('/generate', methods=['POST'])
def generate():
  if request.method == 'POST':
    title = request.json.get('title')
    headings = request.json.get('headings')
    language = request.json.get('language')
    style = request.json.get('style')
    tone = request.json.get('tone')

    # Construct the prompt as a ChatPromptTemplate object
    prompt = ChatPromptTemplate.from_template(
        f"Generate an article on title {title} with {headings} headings in {language} language of 2000 word limit , using a {style} style and {tone} tone."
    )

    # Pass the prompt object to the LLMChain constructor
    llm = ChatOpenAI(temperature=0.5)
    chain = LLMChain(llm=llm, prompt=prompt)

    # Invoke the model chain with the constructed prompt
    output = chain.run(prompt=prompt)

    # Replace each Heading 1 and Heading 2 with bold formatting
    output = output.replace("Title:", "<strong>Title:</strong>")
    output = output.replace("Introduction", "<strong>Introduction:</strong>")
    output = output.replace("Heading 1:", "<strong>Heading 1:</strong>")
    output = output.replace("Heading 2:", "<strong>Heading 2:</strong>")
    output = output.replace("Conclusion", "<strong>Conclusion:</strong>")

    # Format output with HTML tags for headings
    output = "<div>" + output.replace("\n", "</div><div>") + "</div>"

    return output


@app.route('/generateimages/<prompt>')
def generateimg(prompt):
  print("prompt:", prompt)
  client = OpenAI(api_key=api_key)

  # Generate an image using DALL·E 2 model
  response = client.images.generate(
      model="dall-e-2",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=3,  # Generate 3 images
  )

  # Extract necessary information from the ImagesResponse object
  image_urls = [image.url for image in response.data]

  # Return the image URLs as JSON
  return jsonify(image_urls)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
