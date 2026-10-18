
import time
import requests
import streamlit as st
from database import setup_database, get_menu

# ---------------- Configuration ----------------
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

st.set_page_config(
    page_title="Bella Italia | AI Assistant",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- Custom styling ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #FFF8F0;
    color: #33251F;
    font-family: 'Inter', sans-serif;
}
header[data-testid="stHeader"] {
    background: transparent;
}
.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
[data-testid="stSidebar"] {
    background: #F5E9DC;
    border-right: 1px solid #E9D7C7;
}
[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}
.hero {
    background: linear-gradient(120deg, #9E3F25, #E47745);
    border-radius: 24px;
    padding: 28px;
    color: white;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 36px;
    font-weight: 800;
    margin: 0;
}
.hero p {
    color: #FFF0E7;
    margin-bottom: 0;
    font-size: 15px;
}
.section-title {
    font-size: 22px;
    font-weight: 750;
    color: #33251F;
    margin: 12px 0 16px 0;
}
.menu-card {
    background: white;
    border: 1px solid #EEDDCF;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
}
.price {
    color: #C6532F;
    font-weight: 750;
    font-size: 18px;
}
.small-muted {
    color: #88756A;
    font-size: 13px;
}
div[data-testid="stChatMessage"] {
    background: white;
    border: 1px solid #F0E0D2;
    border-radius: 16px;
    padding: 14px;
    margin-bottom: 12px;
}
.stChatInput textarea {
    background: white !important;
}
.stButton button {
    border-radius: 12px;
    font-weight: 600;
    min-height: 42px;
}
div[data-testid="stChatInput"] {
    border-color: #E7CBBB;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Database ----------------
setup_database()
menu = get_menu()

# ---------------- Language ----------------
with st.sidebar:
    st.markdown("##  Bella Italia")
    st.caption("Restaurant customer service")

    language = st.selectbox(
        "Language / اللغة / Dil",
        ["English", "العربية", "Türkçe"],
        key="language",
    )

    st.divider()
    st.markdown("### ✨ Quick questions")

    quick_questions = {
        "English": [
            "What pizzas do you have?",
            "What drinks do you have?",
            "What is the price of the Chicken Burger?",
        ],
        "العربية": [
            "ما أنواع البيتزا المتوفرة؟",
            "ما المشروبات المتوفرة؟",
            "كم سعر برغر الدجاج؟",
        ],
        "Türkçe": [
            "Hangi pizzalar var?",
            "Hangi içecekler var?",
            "Tavuk burger ne kadar?",
        ],
    }

    for i, question in enumerate(quick_questions[language]):
        if st.button(question, key=f"quick_{language}_{i}",
                     use_container_width=True):
            st.session_state.pending_question = question

    st.divider()
    st.markdown("### 🧾 About")
    st.caption("AI-powered menu assistance")
    st.caption("Powered by Ollama · Local model")

# ---------------- Main header ----------------
if language == "العربية":
    title = "أهلًا بيك في Bella Italia 🍕"
    subtitle = "شنو نفسك تاكل اليوم؟ اسألني عن المنيو والأسعار والمكونات."
    welcome = "أهلًا بيك! أنا مساعد Bella Italia. أقدر أساعدك بمعلومات المنيو والأسعار والمكونات."
    language_instruction = "Arabic. Reply naturally in Arabic."
elif language == "Türkçe":
    title = "Bella Italia'ya hoş geldiniz 🍕"
    subtitle = "Bugün ne yemek istersiniz? Menü ve fiyatları sorun."
    welcome = "Merhaba! Bella Italia restoran asistanınızım. Menü, fiyatlar ve içerikler hakkında yardımcı olabilirim."
    language_instruction = "Turkish. Reply naturally in Turkish."
else:
    title = "Welcome to Bella Italia 🍕"
    subtitle = "Good food starts with a good question. Explore our menu."
    welcome = "Welcome to Bella Italia! I'm your restaurant assistant. Ask me about menu items, prices, and ingredients."
    language_instruction = "English. Reply naturally in English."

st.markdown(f"""
<div class="hero">
    <h1>{title}</h1>
    <p>{subtitle}</p>
</div>
""", unsafe_allow_html=True)

# ---------------- Menu cards ----------------
st.markdown('<div class="section-title">🍽️ Explore our menu</div>',
            unsafe_allow_html=True)

columns = st.columns(3)
for i, item in enumerate(menu):
    with columns[i % 3]:
        st.markdown(f"""
        <div class="menu-card">
            <div class="small-muted">{item['category']}</div>
            <div style="font-size:17px;font-weight:700;margin:7px 0">
                {item['name']}
            </div>
            <div class="small-muted">{item['description']}</div>
            <div class="price" style="margin-top:12px">
                ${item['price']:.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.markdown('<div class="section-title">💬 Chat with our assistant</div>',
            unsafe_allow_html=True)

# ---------------- Prompt ----------------
menu_text = "\n".join(
    f"- {item['name']} | Category: {item['category']} | "
    f"Price: ${item['price']:.2f} | "
    f"Description: {item['description']}"
    for item in menu
)

system_prompt = f"""
You are the friendly customer service assistant for Bella Italia.
You may ONLY answer questions about menu products, their prices,
categories, ingredients, and availability using the database below.
Do not invent products, prices, ingredients, or restaurant policies.
If the requested information is missing, say you do not have it.
Politely refuse unrelated questions and redirect customers to the menu.
Be concise and helpful.
Always reply in this language: {language_instruction}

DATABASE:
{menu_text}
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": welcome}
    ]

if st.button("🗑️ Clear conversation / مسح المحادثة",
             key="clear_chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": welcome}
    ]
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Support sidebar quick questions
pending = st.session_state.pop("pending_question", None)
user_input = st.chat_input("Ask about our menu...")

if pending:
    user_input = pending

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    api_messages = [{"role": "system", "content": system_prompt}]
    api_messages.extend(
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages[-10:]
        if m["role"] in ("user", "assistant")
    )

    with st.chat_message("assistant"):
        with st.spinner("Preparing your answer..."):
            started = time.perf_counter()
            try:
                response = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": MODEL,
                        "messages": api_messages,
                        "stream": False,
                        "options": {"temperature": 0.2},
                    },
                    timeout=120,
                )
                response.raise_for_status()
                answer = response.json()["message"]["content"]
                elapsed = time.perf_counter() - started
            except requests.exceptions.ConnectionError:
                answer = "Cannot connect to Ollama. Please make sure Ollama is running."
                elapsed = 0
            except requests.exceptions.Timeout:
                answer = "The model took too long to respond. Please try again."
                elapsed = 0
            except (requests.exceptions.RequestException, KeyError, ValueError):
                answer = "Something went wrong. Please try again."
                elapsed = 0

        st.write(answer)
        if elapsed > 0:
            st.caption(f"⏱️ Response time: {elapsed:.2f} seconds")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

st.markdown(
    '<p class="small-muted" style="text-align:center;margin-top:24px">'
    'Bella Italia · Local AI assistant · No online server required'
    '</p>',
    unsafe_allow_html=True,
)