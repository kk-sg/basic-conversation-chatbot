# OpenAI-Powered Streamlit Chatbot

This repository contains a simple yet powerful AI chatbot application built with Streamlit and powered by OpenAI's GPT-3.5-turbo model. The application demonstrates how to create an interactive chat interface that leverages advanced language models to provide intelligent responses to user queries.

## Features

- Interactive chat interface
- Integration with OpenAI's GPT-3.5-turbo model
- Persistent chat history
- User-friendly design
- Secure API key handling

## Repository Contents

- `basic.py`: The basic version of the chatbot application
- `better_layout.py`: An improved version with enhanced UI and user experience
- `requirements.txt`: List of Python dependencies

## Versions

### Basic Version (`basic.py`)

The basic version provides core functionality:
- Simple Streamlit interface
- Integration with OpenAI's API
- Basic chat history display

**Note:** For the basic version, users need to input their OpenAI API key in a `.env` file in the project root directory.

### Improved Version (`better_layout.py`)

The improved version enhances the user experience with:
- Advanced layout using Streamlit's column feature
- Visually appealing chat bubbles with avatars
- Improved error handling
- Secure user input for OpenAI API key
- Enhanced code organization and modularity

**Live Demo:** You can try the improved version online at [https://basic-conversation-chatbot.streamlit.app](https://basic-conversation-chatbot.streamlit.app)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/openai-streamlit-chatbot.git
cd openai-streamlit-chatbot
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Version

1. Create a `.env` file in the project root and add your OpenAI API key:
```text
OPENAI_API_KEY=your_api_key_here
```

2. Run the basic version:
```
streamlit run basic.py
```

### Improved Version

1. Run the improved version:
```
streamlit run better_layout.py
```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter your OpenAI API key when prompted in the web interface.

4. Start chatting with the AI!

Alternatively, you can use the live demo of the improved version at [https://openai-chatbot-demo.streamlit.app](https://openai-chatbot-demo.streamlit.app)

## Security Note

- For the basic version, ensure your `.env` file is added to `.gitignore` to prevent accidentally sharing your API key.
- The improved version (`better_layout.py`) requires users to input their own OpenAI API key in the web interface. This key is used only for the current session and is not stored by the application, ensuring the security of your API credentials.

## Contributing

Contributions to improve the chatbot or extend its functionality are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## Acknowledgments

- OpenAI for providing the GPT-3.5-turbo model
- Streamlit for their excellent web application framework



