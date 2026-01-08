import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Giza Explorer Pro",
    page_icon="🏜️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. THE EXPANDED KNOWLEDGE BASE ---
# Format: "Button Label": ("Keywords to search", "The Answer")
# We use this structure so the button looks nice, but the search logic is smart.
faq_data = {
    # --- GREETINGS & SOCIAL ---
    "👋 Say Hello": (["hello", "hi", "hey", "greetings"], 
        "Greetings, traveler! I am the Guardian of the Plateau. Ask me anything about the Great Pyramids."),
    "🙏 Thank You": (["thank", "thanks", "cool"], 
        "You are most welcome. May your journey be full of discovery!"),
    "👋 Goodbye": (["bye", "goodbye", "exit"], 
        "Farewell! May Ra guide your path."),
    "🤖 Who are you?": (["who are you", "what are you", "bot"], 
        "I am an AI guide programmed to share the secrets of the Giza Plateau."),

    # --- THE BASICS ---
    "🏗️ Who built them?": (["who built", "builder", "khufu", "pharaoh"], 
        "The Great Pyramid was built by Pharaoh Khufu. The other two were built by his son Khafre and grandson Menkaure."),
    "📅 When was it built?": (["when", "year", "date", "old", "time"], 
        "The Great Pyramid was built during the Fourth Dynasty, around 2580–2560 BC."),
    "📏 How tall is it?": (["tall", "height", "high"], 
        "It was originally 146.6 meters (481 ft) tall. Today, due to erosion and the loss of its capstone, it stands at about 138.5 meters (454 ft)."),
    "📍 Where is it?": (["where", "location", "city", "map"], 
        "The pyramids are located on the Giza Plateau, on the west bank of the Nile, near modern-day Cairo, Egypt."),

    # --- CONSTRUCTION FACTS ---
    "🧱 How many blocks?": (["blocks", "how many stones", "count"], 
        "The Great Pyramid consists of approximately 2.3 million stone blocks."),
    "⚖️ How heavy is it?": (["weight", "heavy", "mass", "tons"], 
        "The total mass is estimated at 5.9 million tons. A single block weighs between 2.5 and 15 tons!"),
    "⛰️ What material?": (["material", "stone", "limestone", "granite"], 
        "The core is local limestone. The inner chambers are pink granite from Aswan (800km away). The original outer casing was polished white Tura limestone."),
    "⛓️ Built by slaves?": (["slave", "labor", "workers"], 
        "Common myth! Archaeologists have found worker villages proving it was built by 20,000–30,000 skilled, paid laborers who ate meat and bread."),
    "🧪 The 'Super' Mortar": (["mortar", "cement", "glue"], 
        "The blocks are held together by a gypsum-based mortar. It is incredibly strong—stronger than the stones themselves—and its exact chemical composition remains a mystery."),

    # --- MYSTERIES & FEATURES ---
    "🦁 The Sphinx": (["sphinx", "cat", "lion"], 
        "The Great Sphinx stands guard nearby. It has the body of a lion and the head of a Pharaoh (likely Khafre). It is the oldest known monumental sculpture in Egypt."),
    "🚪 What's Inside?": (["inside", "interior", "chamber", "room"], 
        "Inside are three main chambers: the King's Chamber, the Queen's Chamber, and the unfinished Subterranean Chamber."),
    "❄️ Air Conditioning?": (["temperature", "heat", "cool", "air"], 
        "Despite the scorching desert heat, the temperature inside the inner chambers stays a constant 20°C (68°F)—the same as the average temperature of the earth."),
    "🌌 Star Alignment": (["align", "star", "orion", "north"], 
        "The pyramids are aligned to True North with accuracy within 3/60th of a degree. The three pyramids also align almost perfectly with the belt stars of the Orion constellation."),
    "🕳️ The Big Void": (["void", "scan", "hidden", "secret"], 
        "In 2017, scientists using muon scanning discovered a massive 'Big Void' above the Grand Gallery. Its purpose is completely unknown."),
    "🛑 8 Sides?": (["sides", "concave", "eight", "shape"], 
        "The Great Pyramid is not actually 4-sided. It is 8-sided! The faces are slightly concave (indented), a feature only visible from the air under specific lighting."),
    
    # --- TOURISM ---
    "🎟️ Ticket Cost": (["ticket", "cost", "price", "entry"], 
        "As of 2025, a general entry ticket to the Giza Plateau is roughly 540 EGP for tourists, but entering the Great Pyramid itself requires an extra, more expensive ticket."),
    "🐪 Camel Rides": (["camel", "horse", "ride"], 
        "You can ride camels or horses at Giza, but be careful! Agree on a price *before* you get on, or you might get scammed."),
}

# --- 3. HELPER FUNCTIONS ---
def get_answer(user_query):
    user_query = user_query.lower()
    
    # 1. Search our detailed FAQ data
    for label, (keywords, answer) in faq_data.items():
        for keyword in keywords:
            if keyword in user_query:
                return answer
    
    # 2. Fallback for unknown questions
    return "I do not have that record in my hieroglyphs. Try using the buttons in the sidebar!"

def handle_click(question_text):
    """When a sidebar button is clicked, add the question and answer to chat history."""
    st.session_state.messages.append({"role": "user", "content": question_text})
    response = get_answer(question_text)
    st.session_state.messages.append({"role": "assistant", "content": response})

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🎒 Explorer's Toolkit")
    st.markdown("Select a topic to ask:")
    
    # DYNAMIC BUTTON LOOP
    # This automatically creates a button for every item in our dictionary
    for button_label, (keywords, answer) in faq_data.items():
        # We use the first keyword as the 'question' sent to the chat
        question_to_ask = keywords[0].capitalize() + "?" 
        
        if st.button(button_label, use_container_width=True):
            handle_click(question_to_ask)

    st.markdown("---")
    if st.button("🗑️ Clear History", type="primary", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- 5. MAIN CHAT INTERFACE ---
st.title("🏜️ Giza Explorer Pro")
st.markdown("Welcome to the **Giza Plateau**. I can answer questions about history, construction, mysteries, and tourism.")
st.divider()

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add an initial greeting from the bot
    st.session_state.messages.append({"role": "assistant", "content": "Greetings! I am the Guardian of the Plateau. How may I assist you?"})

# Display History
for msg in st.session_state.messages:
    icon = "🗿" if msg["role"] == "assistant" else "🤠"
    with st.chat_message(msg["role"], avatar=icon):
        st.markdown(msg["content"])

# User Input
if prompt := st.chat_input("Ask a question (e.g., 'How tall is it?')..."):
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🤠"):
        st.markdown(prompt)

    # 2. Bot Response
    response = get_answer(prompt)
    with st.chat_message("assistant", avatar="🗿"):
        time.sleep(0.4)  # Thinking delay
        st.markdown(response)
    
    # 3. Save Bot Message
    st.session_state.messages.append({"role": "assistant", "content": response})
