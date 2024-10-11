import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from google.api_core import retry

# Load environment variables
load_dotenv()

# Fetch Gemini API key from environment variables
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to retry the story generation
def generate_with_retry(model, prompt):
    return model.generate_content(prompt, request_options={"retry": retry.Retry()})

# Define the persona early on before referencing it
persona = '''\
You are an award-winning science fiction author with a penchant for expansive,
intricately woven stories. Your ultimate goal is to write the next award-winning
sci-fi novel.'''

# Streamlit front-end
st.set_page_config(page_title="Story Generator", layout="centered")

# Set background gradient and custom styles
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap');

    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #333333 100%);
        color: white;
        font-family: 'Plus Jakarta Sans', sans-serif;
        text-align: center;
    }
    h1, h2, h3 {
        color: #f0f0f0;
        font-weight: 700;
        text-align: center;
    }
    .stButton button {
        background-color: #4CAF50; /* Softer green color */
        border-radius: 12px;
        color: white;
        padding: 10px 20px;
        font-size: 1.1em;
        box-shadow: 0 4px 12px rgba(0, 255, 0, 0.2);
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton button:hover {
        background-color: #388E3C;
        transform: translateY(-3px);
    }
    .stButtonSmall button {
        background-color: #4CAF50;
        border-radius: 8px;
        color: white;
        padding: 8px 16px;
        font-size: 0.9em;
        transition: background-color 0.3s ease;
    }
    .step-description {
        font-size: 1.2em;
        color: #dcdcdc;
        margin-bottom: 20px;
        text-align: center;
    }
    .generated-text {
        text-align: justify;
        max-width: 600px;
        margin: 0 auto;
    }
    .contact-card {
        background-color: #293241;
        padding: 15px;
        border-radius: 12px;
        color: white;
        margin-top: 30px;
        text-align: center;
    }
    .contact-card a {
        color: #4CAF50;
        text-decoration: none;
        margin-right: 10px;
    }
    .copyright {
        margin-top: 30px;
        font-size: 0.9em;
        color: #dcdcdc;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# Landing Area with Title and Introduction
st.title("🌟 Gemini Story Generator")
st.markdown("""
Welcome to the **Gemini Story Generator**! This tool allows you to create unique, AI-powered stories. Here's what you can do at each step:
1. **Generate a Premise**: Choose between Sci-Fi, Horror, or Funny genres to start.
2. **Build an Outline**: Develop an outline based on your premise.
3. **Customize Your Story**: Set the tone and complexity.
4. **Continue Writing**: Add your inputs to guide the AI's narrative.
5. **Save/Load**: Save your progress and come back later to finish your story.

Let's get started! 🚀
""")
st.markdown("---")

# Progress bar to track writing steps
progress = st.progress(0)

# Initialize session state for premise, outline, and story
if 'premise' not in st.session_state:
    st.session_state['premise'] = ''
if 'outline' not in st.session_state:
    st.session_state['outline'] = ''
if 'story' not in st.session_state:
    st.session_state['story'] = ''

# Step 1: Generate Premise with Genre Options
st.subheader("🎬 Step 1: Craft Your Premise")
st.markdown('<p class="step-description">Select a genre and generate a unique story premise.</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🛸 Generate Sci-Fi Premise"):
        premise_prompt = f"{persona}\nWrite a single sentence premise for a sci-fi story featuring cats."
        st.session_state['premise'] = generate_with_retry(model, premise_prompt).text
        st.success("Sci-Fi Premise Generated!")
        st.markdown(f'<p class="generated-text">{st.session_state["premise"]}</p>', unsafe_allow_html=True)
        progress.progress(25)

with col2:
    if st.button("👻 Generate Horror Premise"):
        premise_prompt = '''You are an acclaimed horror writer with a talent for chilling stories. Write a premise for a horror story involving an abandoned house.'''
        st.session_state['premise'] = generate_with_retry(model, premise_prompt).text
        st.success("Horror Premise Generated!")
        st.markdown(f'<p class="generated-text">{st.session_state["premise"]}</p>', unsafe_allow_html=True)
        progress.progress(25)

with col3:
    if st.button("😂 Generate Funny Premise"):
        premise_prompt = '''You are a humorist known for hilarious and light-hearted tales. Write a premise for a funny story about a talking dog.'''
        st.session_state['premise'] = generate_with_retry(model, premise_prompt).text
        st.success("Funny Premise Generated!")
        st.markdown(f'<p class="generated-text">{st.session_state["premise"]}</p>', unsafe_allow_html=True)
        progress.progress(25)

# Step 2: Generate Outline
if st.session_state['premise']:
    st.subheader("📜 Step 2: Build Your Outline")
    st.markdown('<p class="step-description">Generate a structured outline for your story based on the premise.</p>', unsafe_allow_html=True)
    if st.button("📝 Generate Outline"):
        outline_prompt = f"{persona}\nYou have a gripping premise in mind:\n{st.session_state['premise']}\nWrite an outline for the plot of your story."
        st.session_state['outline'] = generate_with_retry(model, outline_prompt).text
        st.success("Outline Generated!")
        st.markdown(f'<p class="generated-text">{st.session_state["outline"]}</p>', unsafe_allow_html=True)
        progress.progress(50)

# Step 3: Customize Story
if st.session_state['outline']:
    st.subheader("🎨 Step 3: Customize Your Story")
    st.markdown('<p class="step-description">Set the tone and complexity of your story before starting the first draft.</p>', unsafe_allow_html=True)
    
    tone = st.selectbox("🔮 Choose the tone of the story", ['Serious', 'Humorous', 'Dark', 'Inspirational'])
    complexity = st.slider("🧠 Plot Complexity", 1, 10)

    persona_custom = f"{persona}\nYou prefer to write in a {tone.lower()} tone with a plot complexity level of {complexity}."

    if st.button("💡 Generate First Draft"):
        starting_prompt = f"{persona_custom}\nYou have a gripping premise:\n{st.session_state['premise']}\nYour rich outline is:\n{st.session_state['outline']}\nBegin the story."
        st.session_state['story'] = generate_with_retry(model, starting_prompt).text
        st.success("Story Draft Generated!")
        st.markdown(f'<p class="generated-text">{st.session_state["story"]}</p>', unsafe_allow_html=True)
        progress.progress(75)

# Step 4: Continue Writing with Input
if st.session_state['story']:
    st.subheader("📖 Step 4: Continue Writing Your Story")
    st.markdown('<p class="step-description">Add suggestions or inputs to guide the next part of your story.</p>', unsafe_allow_html=True)

    user_input = st.text_input("💬 Add a suggestion or input (optional)")
    if st.button("🔄 Continue Writing"):
        continuation_prompt = f"{persona_custom}\nPremise: {st.session_state['premise']}\nOutline: {st.session_state['outline']}\nWhat you've written so far:\n{st.session_state['story']}\n\nUser Input: {user_input}\nContinue writing."
        st.session_state['story'] += generate_with_retry(model, continuation_prompt).text
        st.success("Story Continued!")
        st.markdown(f'<p class="generated-text">{st.session_state["story"]}</p>', unsafe_allow_html=True)
        progress.progress(100)

# Fun Feature: Subplot Generator
if st.session_state['story']:
    st.subheader("🎭 Add a Twist! (Optional)")
    st.markdown('<p class="step-description">Add an exciting subplot to your story.</p>', unsafe_allow_html=True)
    if st.button("🎬 Generate Subplot"):
        subplot_prompt = f"{persona_custom}\nAdd an exciting subplot to this story."
        subplot = generate_with_retry(model, subplot_prompt).text
        st.session_state['story'] += f"\n\n**Subplot**: {subplot}"
        st.success("Subplot Added!")
        st.markdown(f'<p class="generated-text">{st.session_state["story"]}</p>', unsafe_allow_html=True)

# Save and Load Functionality - Adjusted Button Placement
st.subheader("💾 Save/Load Your Progress")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="stButtonSmall">', unsafe_allow_html=True)
    if st.button("💾 Save Story"):
        with open('saved_story.txt', 'w') as f:
            f.write(st.session_state['story'])
        st.success("Story Saved!")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stButtonSmall">', unsafe_allow_html=True)
    if st.button("📂 Load Story"):
        try:
            with open('saved_story.txt', 'r') as f:
                st.session_state['story'] = f.read()
            st.success("Story Loaded!")
            st.markdown(f'<p class="generated-text">{st.session_state["story"]}</p>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("No saved story found!")
    st.markdown('</div>', unsafe_allow_html=True)

# Final Story Display
st.subheader("📜 Your Final Story")
st.markdown(f'<p class="generated-text">{st.session_state["story"]}</p>', unsafe_allow_html=True)

# Footer Section with Contact Info and Copyright
st.markdown("---")
st.markdown(
    """
    <div class="contact-card">
        <h3>Contact</h3>
        <p>👨‍💻 Created by Pratham Kuril</p>
        <p><a href="https://github.com/prathamkuril" target="_blank">GitHub</a> | <a href="https://www.linkedin.com/in/prathamkuril" target="_blank">LinkedIn</a></p>
    </div>
    <p class="copyright">© 2024 Pratham Kuril. All rights reserved.</p>
    """, unsafe_allow_html=True
)

