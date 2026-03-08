Brand Tweet Generator
Brand Tweet Generator is an AI-powered tool designed to analyze a brand's unique voice and generate 10 perfectly crafted tweets. Whether the objective is engagement, promotion, or brand awareness, this tool uses advanced AI tone-matching to ensure every tweet feels authentic to the brand.
<img width="520" height="341" alt="s0" src="https://github.com/user-attachments/assets/eece0d19-533d-4348-9d42-173137009733" />

<img width="628" height="460" alt="s1" src="https://github.com/user-attachments/assets/bf183c50-cecd-413d-8e47-69dbab255133" />

<img width="511" height="263" alt="s2" src="https://github.com/user-attachments/assets/56948b6f-88ad-43fc-8aff-054e4c7a8c6d" />

<img width="605" height="389" alt="s3" src="https://github.com/user-attachments/assets/0b503fa9-9b03-4af0-be7e-4c3deb5cc4c3" />

<img width="602" height="451" alt="s4" src="https://github.com/user-attachments/assets/66c30616-ae12-4b5a-8470-bd79d6a7d5e7" />

<img width="575" height="479" alt="s5" src="https://github.com/user-attachments/assets/03d8eb90-00b4-427f-b567-81acabd73bea" />

<img width="554" height="367" alt="s6" src="https://github.com/user-attachments/assets/36a57802-5724-46fe-92e7-92da705013e9" />

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
git clone https://github.com/Sakethreddy03/brand-tweet-generator.git
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




