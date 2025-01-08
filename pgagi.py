import streamlit as st
import google.generativeai as genai
import re

# Configure the Gemini API with your API key
genai.configure(api_key="YOUR_API_KEY")


# Streamlit UI
st.title("Gemini 1.5 Recruitment Chatbot")
st.sidebar.write("Welcome to the recruiter chatbot!")
st.sidebar.write("Type 'I would like to leave' or 'exit' to end the chat.")


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are a professional recruiter for a technology placement agency. Your goal is to assess a candidate’s qualifications, skillset, and work experience. Start by greeting the user warmly and professionally. Tell them to end the conversation, to type Exit. First, ask their Name, Contact Number, Email, Location and Desired Position. Verify and ask to resend Phone number if it isnt 10 digits.Then, ask about their educational qualifications, their skillset, and whether they have prior work experience, including the field they worked in.\n\nBased on the user’s skillset and work experience, see if they are a suitable match for their expected position:\n1. Ask follow-up questions to assess their expertise in both areas.\n2. If the user seems to be wrong or misinformed about something, politely and constructively point out the mistake, providing clarification where necessary.\n\nRules:\n1. Ask a maximum of 4-5 rounds of targeted, logical questions.\n2. If satisfied with the user’s responses, conclude by saying: \"Glad to hear about everything. If a job matches your profile, you will be notified.\"\n3. Always maintain a polite and professional tone.\n4. If the user says \"I would like to leave\" or \"exit,\" thank them for their time and terminate the conversation.\n5. If the user’s responses are vague, kindly ask for more details.\n\nStart the conversation with: \"Hello! I’m here to assist you with your recruitment process. Can you tell me about your educational qualifications?\"\n",
)


# Initialize session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
    st.session_state.history = []  # Store conversation history
    st.session_state.input_buffer = ""  # Temporary buffer for user input
    st.session_state.candidate_data = {  # To store candidate details
        "Name": "",
        "Contact Number": "",
        "Email": "",
        "Location": "",
        "Desired Position": ""
    }

# Display chat history
for message in st.session_state.history:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    elif message["role"] == "model":
        st.write(f"**Bot:** {message['content']}")

# User input box
user_input = st.text_input(
    "Your response:",
    key="user_input",
    value="",
    on_change=lambda: st.session_state.update({"input_buffer": st.session_state.user_input}),
)

# Function to extract and store candidate details
def update_candidate_data(user_message):
    if not st.session_state.candidate_data["Name"]:
        name_match = re.search(r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)?)\b", user_message)
        if name_match:
            st.session_state.candidate_data["Name"] = name_match.group(0)

    if not st.session_state.candidate_data["Contact Number"]:
        phone_match = re.search(r"\b\d{10}\b", user_message)  # Match 10-digit phone number
        if phone_match:
            st.session_state.candidate_data["Contact Number"] = phone_match.group(0)

    if not st.session_state.candidate_data["Email"]:
        email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", user_message)
        if email_match:
            st.session_state.candidate_data["Email"] = email_match.group(0)

    if not st.session_state.candidate_data["Location"]:
        location_match = re.search(r"(?:in|at|from) ([A-Za-z ]+)", user_message)
        if location_match:
            st.session_state.candidate_data["Location"] = location_match.group(1).strip()

    if not st.session_state.candidate_data["Desired Position"]:
        position_match = re.search(r"(?:for|as) ([A-Za-z ]+)", user_message)
        if position_match:
            st.session_state.candidate_data["Desired Position"] = position_match.group(1).strip()

# Process user input when the buffer is updated
if st.session_state.input_buffer:
    user_message = st.session_state.input_buffer
    st.session_state.input_buffer = ""  # Clear buffer after processing

    if user_message.lower() in ["i would like to leave", "exit"]:
        st.write("**Bot:** Thank you for your time! Have a great day!")
        print(f"**Collected Candidate Data:** {st.session_state.candidate_data}")
        st.stop()

    # Add user input to chat history
    st.session_state.history.append({"role": "user", "content": user_message})

    # Update candidate data
    update_candidate_data(user_message)

    # Generate bot response
    response = st.session_state.chat.send_message(user_message, stream=True)
    bot_response = ""
    for chunk in response:
        if chunk.text:
            bot_response += chunk.text

    # Add bot response to chat history
    st.session_state.history.append({"role": "model", "content": bot_response})
    st.experimental_rerun()





