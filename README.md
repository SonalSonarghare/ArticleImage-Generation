# AI Article Generator with DALL-E Image Integration

## Overview
This project is a web application that generates tailored articles using Flask, OpenAI's Langchain, and DALL-E image generation capabilities. It allows users to specify various parameters such as article title, number of headings, language, writing style, and tone to create custom articles. Additionally, DALL-E is utilized to generate visually stunning images corresponding to the article content.

## Features
- **Tailored Article Generation:** Users can input parameters such as title, headings, language, style, and tone to generate custom articles tailored to their preferences.
- **DALL-E Image Integration:** The application integrates with OpenAI's DALL-E to generate images corresponding to the article content, enhancing the visual appeal of the articles.
- **Sleek User Interface:** The web interface is designed with a sleek and responsive layout using Tailwind CSS, providing an optimal user experience.

## Technologies Used
- **Flask:** Python web framework used for building the backend server and routing.
- **OpenAI:** API used for language generation (Langchain) and image generation (DALL-E).
- **Tailwind CSS:** Utility-first CSS framework used for styling the web interface.
- **HTML/CSS/JavaScript:** Frontend languages used for building the user interface and handling user interactions.

## Setup Instructions
1. **Clone the Repository**: Clone this repository to your local machine using `git clone https://github.com/your-username/your-repo.git`.
2. **Install Dependencies**: Install the required dependencies using `pip install -r requirements.txt`.
3. **Set Environment Variables**: Set up your OpenAI API key as an environment variable named `OPENAI_KEY` (for image generation) and `OPENAI_API_KEY` (Article generation) . Link to create Open API key: https://platform.openai.com/api-keys
4. **Watch the source.css**: Run the CLI tool to scan your template files for classes and build your CSS ie- to watch the source.css file run in shell : `npm run tw`
5.  **Run the Application**: Run the Flask application using `python main.py`.
6.  **Access the Application**: Access the application in your web browser at [http://localhost:5000] or (for replit) Once the Flask application is running in Replit, you can access it by clicking on the "Open in New Tab" option provided by Replit.

## Usage
1. Navigate to the home page of the web application.
2. Enter the desired parameters for article generation, including title, headings, language, style, and tone.
3. Click the "Submit" button to generate the article.
4. Optionally, click the "Generate Images" button to generate images corresponding to the article content using DALL-E.
5. View the generated article and images on the web page.

## Useful Sources
1. Signup on Replit: http://join.replit.com/CWH-AI
2. Link to the Repl: https://replit.com/@21107033sonalso/ArticleImage-Generation?v=1
3. Tailwindcss Installation:https://tailwindcss.com/docs/installation
4. Langchain Documentation: https://python.langchain.com/docs/get_started/quickstart
5. Openapi Documentation:https://platform.openai.com/docs/overview
6. Link to create open API key: https://platform.openai.com/api-keys



## License
This project is licensed under the MIT License.
