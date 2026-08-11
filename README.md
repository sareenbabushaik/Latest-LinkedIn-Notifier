LinkedIn Notifier 🤖

A small Python project that monitors selected LinkedIn profiles, detects their latest posts, uses a local Ollama LLM to generate a relevant comment, and opens the post in the browser for manual review and posting.

🚀 What It Does

The project follows this workflow:

LinkedIn Profile URLs
        ↓
CSV Data Extraction
        ↓
LinkedIn API
        ↓
Check Latest Post
        ↓
Post Found?
    ↙        ↘
  No          Yes
  ↓            ↓
Skip       Extract Caption
               ↓
          Ollama / phi3:mini
               ↓
        Generate Comment
               ↓
        Open LinkedIn Post
               ↓
       Review & Post Manually

Main Features

Reads multiple LinkedIn profile URLs from a CSV file.

Checks profiles for their latest posts through the LinkedIn API.

Skips profiles when no post is available.

Sends the post caption to a locally running Ollama model.

Generates a short, professional and relevant LinkedIn comment.

Opens the corresponding LinkedIn post in the browser.

Keeps the final decision to post the comment with the user.

⚠️ Important API Limitation

This project requires special LinkedIn API permissions/approved access to read other members' profiles/posts.

A basic LinkedIn API access token is not sufficient for this functionality.

Without the required LinkedIn permissions, the post-retrieval portion of the project will not work.

🛠️ Tech Stack

Python

Pandas — CSV/data extraction

Requests — LinkedIn API requests

Ollama — local AI inference

Phi-3 Mini — local LLM used for comment generation

Webbrowser — opens LinkedIn posts

PyWhatKit — optional WhatsApp notification functionality

📁 Project Structure

LinkedIn-Notifier/
│
├── app.py
├── data_extractor.py
├── llm.py
├── caption_generator.py
├── whatsapp_messenger.py
├── account.csv
└── README.md

📄 account.csv

Add the LinkedIn profiles you want to monitor
Use normal URLs in the CSV. Do not use Markdown link syntax.

⚙️ Installation

1. Clone the repository

git clone <your-github-repository-url>
cd LinkedIn-Notifier

2. Install Python dependencies

pip install pandas requests ollama pywhatkit

3. Install Ollama

Install Ollama for your operating system and make sure it is running.

Then download the model:

ollama pull phi3:mini

You can verify it with:

ollama list

4. Configure LinkedIn API access

Add your LinkedIn access token in llm.py:

ACCESS_TOKEN = "YOUR_LINKEDIN_ACCESS_TOKEN"

Do not upload your real access token to GitHub.

For a public repository, use an environment variable instead.

▶️ Running the Project

Run:

python app.py

The program will:

Read the profiles from account.csv.

Check each profile through the LinkedIn API.

Skip the profile if no post is returned.

Extract the latest post caption when a post is found.

Send the caption to Ollama.

Generate an AI comment.

Print the generated comment.

Open the LinkedIn post in your browser.

Let you manually review and post the comment.

Example terminal output:

New post found from Bhadraksh Bhargava

Generated comment:
Great work! This is a practical example of applying AI to solve a real-world problem.

🧠 AI Comment Generation

The project uses Ollama locally instead of a cloud-based LLM API.

The model receives the LinkedIn post caption and is instructed to generate a comment that is:

Short

Professional

Relevant

Natural

Not overly promotional

Free of hashtags and emojis

The generated comment is not automatically posted. The LinkedIn post is opened in the browser so the user can review it and decide whether to post it.

🔐 Security

Never commit sensitive credentials to GitHub.

Do not publish:

LinkedIn access tokens

API keys

Phone numbers

Other private credentials

For example, add sensitive files to .gitignore:

.env
*.env

For production/public use, store credentials in environment variables.

🎯 Who Is This Useful For?

This can be useful for:

Highly engaged LinkedIn users

Students building their professional network

Professionals who actively engage with their network

Creators who follow specific accounts

Users who regularly monitor posts from selected people

The purpose is to reduce repetitive profile-checking while keeping the user in control of the final interaction.

🚧 Current Limitations

Requires appropriate LinkedIn API access.

LinkedIn API permissions may restrict access to other members' profiles/posts.

The project currently checks the latest available post; persistent duplicate-post tracking is not yet implemented.

AI-generated comments should be reviewed before posting.

LinkedIn API availability and permissions can change.

The project does not automatically publish comments.

🔮 Future Improvements

Possible improvements include:

Store previously processed post IDs.

Detect only genuinely new posts.

Add scheduled/background monitoring.

Improve comment generation based on post type.

Add a GUI/dashboard.

Add notifications when a new post is detected.

Support multiple Ollama models.

Add better error handling and logging.

⚖️ Responsible Use

This project is designed as a personal productivity and learning tool.

The generated comments should be reviewed before posting. Use LinkedIn's APIs and automation capabilities according to LinkedIn's applicable policies, permissions, and terms.

📌 Project Goal

The main goal of this project is to learn how to combine:

API Integration
      +
Data Extraction
      +
Conditional Logic
      +
Local LLM
      +
Browser Interaction

into a practical AI-powered Python application.

Built as a learning project using Python and Ollama.
