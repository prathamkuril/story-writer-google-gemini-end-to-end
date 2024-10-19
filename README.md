# Story Generator using 'gemini-1.5-pro' and 'gemini-1.5-flash'

The **Story Generator** is a web application that allows users to create unique, AI-generated stories using Google's **Gemini LLMs**. It helps users craft, customize, and continue writing stories by selecting specific genres, tones, and complexities. The app provides an interactive and fun way to guide an AI through the creative writing process, allowing users to input prompts and generate various story elements step-by-step.

## Features

- **LLM Selection**: Choose between **Gemini 1.5 Flash** for fast responses or **Gemini 1.5 Pro** for more detailed, advanced outputs.
- **Generate Story Premise**: Select from genres like Sci-Fi, Horror, or Humor, and the app will generate a unique story premise.
- **Outline Generation**: Based on the generated premise, the app helps build an outline for the story's structure.
- **Story Customization**: Users can customize the tone and complexity of the story, and then generate the first draft.
- **Interactive Continuation**: Guide the AI with custom input to continue the story, allowing creativity and user input to shape the narrative.
- **Save & Load**: Users can save their generated stories locally and load them back for further editing later.
- **Dark-Themed, Aesthetic UI**: The interface is styled with a professional, sleek, dark theme inspired by Apple's design philosophy.

## Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Used to build the front-end of the application.
- **Google Generative AI**: Integrated for AI story generation using **Gemini LLMs**.
- **dotenv**: To load environment variables (for API keys).
- **Logging**: Used for tracking errors and flow within the app.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher.
- [Google Cloud account](https://cloud.google.com/), with **Gemini LLMs** API access.
- API Key for **Google Gemini**.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/<your-username>/story-generator.git
   cd story-generator
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:

   - Create a `.env` file in the root of the project:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key_here
     ```

6. **Run the App**:

   ```bash
   streamlit run StoryGenerator.py
   ```

7. **Access the App**:
   - Once running, open [http://localhost:8501](http://localhost:8501) in your web browser.

## How to Use

### 1. **Select LLM Model**:

- Choose between **Gemini 1.5 Flash** (faster responses) and **Gemini 1.5 Pro** (more advanced responses).

### 2. **Generate Story Premise**:

- Choose a genre like **Sci-Fi**, **Horror**, or **Funny**.
- The app will generate a story premise based on the genre.

### 3. **Generate Story Outline**:

- Once the premise is generated, you can generate an outline that will guide the story's structure.

### 4. **Customize Story**:

- Set the **tone** (e.g., Dark, Inspirational) and **complexity** (on a scale of 1-10) for your story.
- The app will generate the first draft of the story.

### 5. **Continue Writing**:

- Add your own input (optional) to guide the AI in generating the next part of the story.
- The AI will continue based on your input and the previous story.

### 6. **Save and Load**:

- You can save the story to a local file (`saved_story.txt`) and load it back at any time to continue editing.

## Code Structure

```bash
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not included in repo)
├── saved_story.txt     # Placeholder for saved stories (auto-generated)
├── README.md           # Documentation
└── venv/               # Virtual environment folder (not included in repo)
```
