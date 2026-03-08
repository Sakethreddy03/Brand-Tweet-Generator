Brand Tweet Generator
Brand Tweet Generator is an AI-powered tool designed to analyze a brand's unique voice and generate 10 perfectly crafted tweets. Whether the objective is engagement, promotion, or brand awareness, this tool uses advanced AI tone-matching to ensure every tweet feels authentic to the brand.


Features
Brand Voice Analysis: Automatically detects the tone, target audience, and key characteristics of any brand (e.g., Nike, Tesla, Duolingo).
Campaign Objectives: Tailor content for Engagement, Sales/Promotion, or Brand Awareness.
AI Tone Matching: Generates content that reflects specific brand personalities (Bold, Witty, Authoritative, etc.).
Smart Formatting: Includes relevant emojis, hashtags, and keeps within the 280-character limit.
Metrics Preview: Shows character counts and estimated engagement scores for every generated tweet.
Export Options: Quickly copy all tweets or export them for social media scheduling.

Tech Stack
Frontend: Streamlit (Python-based web framework)
AI Engine: OpenAI GPT-4 / LangChain
Styling: Custom CSS & HTML Components
Environment: Python 3.9+

 Project Structure

brand-tweet-generator
│
├── app.py                # Main Streamlit application logic and UI
├── prompt.py             # System prompts and AI instruction templates
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── .gitignore            # Files to ignore in Git
├── .env                  # API Keys (OpenAI)
│
├── docs
│   └── approach.md       # Documentation on the prompt engineering approach
│
└── screenshots
    ├── app_ui.png        # UI Screenshot
    └── output_example.png # AI Output Example
    
Getting Started
1. Prerequisites
Python 3.9 or higher installed.
An OpenAI API Key.
2. Installation
Clone the repository to your local machine:
code
Bash
git clone https://github.com/your-username/brand-tweet-generator.git
cd brand-tweet-generator
3. Install Dependencies
code
Bash
pip install -r requirements.txt
4. Configuration
Create a .env file in the root directory and add your OpenAI API key:
code
Env
OPENAI_API_KEY=your_api_key_here
5. Run the App
code
Bash
streamlit run app.py

How to Use
Enter Brand Details: Provide the Brand Name (e.g., Nike) and Industry (e.g., Sportswear).
Set Objective: Choose whether you want to drive sales, boost engagement, or increase awareness.
Describe Product: Give a brief description of what you are tweeting about.
Generate: Click "Generate Tweets" and let the AI analyze the brand voice and produce 10 high-quality tweets.

Author
Name: Sandi Saketh Reddy
Reg No: 2022BCSE07AED635
Organization: Alliance University
Contact: ssandiBTECH22@ced.alliance.edu.in

