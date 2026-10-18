#  Bella Italia — AI Restaurant Chatbot

A local AI-powered restaurant customer service chatbot built with Python, Streamlit, SQLite, and Ollama.

Bella Italia helps customers explore the restaurant menu, check prices and descriptions, and ask questions in English, Arabic, or Turkish.

## Features

- **AI-powered customer service:** Uses the locally running `llama3.2:3b` language model through Ollama.
- **Interactive web interface:** Built with Streamlit.
- **SQLite database:** Stores restaurant menu items, categories, descriptions, prices, and availability.
- **Multilingual support:** English, Arabic, and Turkish interface and responses.
- **Quick questions:** Provides suggested questions based on the selected language.
- **Menu display:** Shows menu items, descriptions, categories, and prices.
- **Conversation controls:** Supports temporary conversation history and clearing the chat.
- **Local execution:** Runs on your computer without requiring a hosted AI server.

##  Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web user interface |
| Ollama | Runs the local language model |
| Llama 3.2 (3B) | Generates chatbot responses |
| SQLite | Stores restaurant menu information |
| Requests | Communicates with the Ollama API |

## Project Structure

```text
restaurant-chatbot/
├── app.py
├── database.py
├── restaurant.db
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python installed on your computer.
- Ollama installed and running.
- The `llama3.2:3b` model downloaded through Ollama.

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Marwamursi/restaurant-chatbot.git
cd restaurant-chatbot
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Install and start the Ollama model

Install Ollama from its official website if it is not already installed.

Pull the model:

```powershell
ollama pull llama3.2:3b
```

Make sure Ollama is running before starting the chatbot. You can check the installed models with:

```powershell
ollama list
```

### 5. Run the application

```powershell
python -m streamlit run app.py
```

Open the local URL printed in the terminal, usually:

`http://localhost:8501`

Streamlit may select another port if the default port is already in use.

## Database

The application uses SQLite to store restaurant menu information, including:

- Product name
- Category
- Description
- Price
- Availability

The database is initialized by `database.py`. If the menu table is empty, the application inserts the sample menu items defined in the code.

The menu data is sample data created for this educational project.

## Testing

The following chatbot scenarios were tested successfully:

| Test | Expected behavior | Result |
|---|---|---|
| Ask which pizzas are available | Lists available pizzas and prices | Passed |
| Ask for the Chicken Burger price | Returns the database price of $9.00 | Passed |
| Ask an unrelated question | Politely redirects the user to restaurant topics | Passed |
| Ask about the Chicken Burger in Arabic | Responds in Arabic with the correct price | Passed |
| Ask about the Chicken Burger in Turkish | Responds in Turkish with the correct price | Passed |

These results reflect the scenarios tested during development and do not guarantee that every possible input will be handled correctly.

## Privacy and Limitations

- The language model runs locally through Ollama.
- The application requires Ollama and the selected model to be available on the computer.
- The chatbot is designed to answer questions about the restaurant menu, not to provide general-purpose assistance.
- Menu information is limited to the data available in the database.
- This project is an educational prototype and is not a hosted public chatbot.

##  Author

**Marwa Mursi**

GitHub: [@Marwamursi](https://github.com/Marwamursi)

##  License

This project was created for educational purposes. Add a formal open-source license if you intend to distribute the project under specific reuse terms.
