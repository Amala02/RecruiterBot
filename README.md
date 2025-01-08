# RecruiterBot

## Project Description
This is a Recruiting Bot that was made with the help of Gemini+Streamlit. Gemini 1.5 Pro is the exact model used for making this chatbot. 

It can: 
- Collect candidate information such as Name, Contact number, emailID, desired position etc.
- Ensure Number provided is valid and collect Educational qualification details along with Skill set. 
- Ask candidate questions based on the qualification provided to assess their expertise.
- If satisfactory, bot informs candidates that if match is found, it will be informed. 


## Installation

Follow these steps to set up and run the recruitment chatbot locally:

Prerequisites
Ensure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- Virtual Environment (recommended)

### Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/Amala02/RecruiterBot.git
cd <repository_folder>
```
### Step 2: Install requirements

```bash
pip install streamlit google-generativeai
```
### Step 3: Set up Google API key

Visit https://ai.google.dev/aistudio and obtain API key. Replace YOUR_API_KEY in pgagi.py with your key.

### Step 4: Run App

```bash
cd <your project folder>
streamlit run pgagi.py
```    

## Technical Details:
- Google AI Studio for APIs
- Backed by Gemini 1.5 Pro
- Prompt Engineered to assess candidates carefully
- Stores candidate data for further processing/use

## Prompt Design
The system instruction defines the core behavior and personality of the chatbot. It sets the context, rules, and expectations for how the chatbot interacts with the user.

- Role: The system instruction acts as the persona or guide for the chatbot. It directs the model on how to behave, what questions to ask, and what actions to take at specific moments.
- Tone and Professionalism: The tone is explicitly instructed to be polite and professional throughout the conversation.
- Clarifications: It emphasizes that if a user makes a mistake or provides incorrect information, the chatbot should correct them gently.
- Conversation Flow: The instructions are structured to start with a greeting, collect candidate details, assess their qualifications, and offer follow-up questions. The chatbot will conclude by notifying the candidate of a potential match if applicable.
- Exit Strategy: The chatbot is instructed to gracefully handle user requests to exit the conversation by thanking them for their time.

## Challenges
There were some issues faced during course of the development. There were some version clashes initially. Secondly, getting the bot to coherently respond and prompt engineer was a hard task. Third problem was to sustain a chat flow and store history of the user conversation with the bot. 

