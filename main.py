import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Giza Explorer", page_icon="🏜️")

# --- 2. DATA ---
knowledge_base = {
    "who built": "The Great Pyramid was built by Pharaoh Khufu.",
    "when": "It was built around 2580–2560 BC.",
    "height": "It is about 138.5 meters (454 ft) tall.",
    "location": "Located on the Giza Plateau, Egypt.",
    "blocks": "It has about 2.3 million stone blocks.",
    "slaves": "It was built by paid laborers, not slaves.",
    "sphinx": "The Sphinx stands nearby, likely representing Khafre."
}

def get_answer(query):
    for key in knowledge_base:
        if key in query.lower():
            return knowledge_base[key]
    return "I don't have that record."

# --- 3. CHAT INTERFACE ---
st.title("🏜️ Pyramids of Giza Guide")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask about the pyramids..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = get_answer(prompt)
    time.sleep(0.5)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
