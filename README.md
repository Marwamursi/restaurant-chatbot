
# Bella Italia — AI Restaurant Chatbot

A local AI-powered restaurant customer service chatbot built with Python, Streamlit, SQLite, and Ollama.

## Features

- Chat interface built with Streamlit.
- Local language model powered by Ollama.
- Restaurant menu stored in an SQLite database.
- Answers questions about menu items, categories, prices, and descriptions.
- Supports multiple response languages through a language selector.
- Temporary conversation history during the Streamlit session.
- Response-time display.
- Runs locally without requiring a hosted web server.

## Technology Stack

- Python
- Streamlit
- SQLite
- Ollama
- Llama 3.2 (3B)

## Project Structure

    restaurant-chatbot/
    ├── app.py
    ├── database.py
    ├── restaurant.db
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Prerequisites

Install the following before running the application:

- Python 3.10 or a compatible Python version.
- Ollama for Windows.
- The Llama 3.2 3B model.

## Installation

1. Clone or download this repository.

2. Open a terminal in the project directory.

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate it on Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Install and start Ollama, then download the model:

   ```bash
   ollama pull llama3.2:3b
   ```

7. Run the application:

   ```bash
   streamlit run app.py
   ```

8. Open the local URL shown in the terminal, usually:

   http://localhost:8501

## Database

The application uses SQLite to store restaurant menu information,
including product names, categories, descriptions, prices, and availability.

The database setup function creates the menu table and inserts sample
menu items when the table is empty.

## How It Works

1. The customer submits a question through the Streamlit interface.
2. The application retrieves menu information from SQLite.
3. The menu information is included in the system prompt.
4. Ollama generates a response using the local language model.
5. The response is displayed in the chat interface.

## Limitations

- Ollama must be installed and running locally.
- The required model must be downloaded before use.
- Responses depend on the information available in the restaurant database.
- Response speed depends on the computer's hardware and model performance.

## Disclaimer

This is an educational project demonstrating local language models,
database integration, and AI-powered customer service.

Restaurant menu information is sample data and should be verified
before use in a real restaurant.
