# ai-code-review-bot

An interactive web application that reviews code in multiple programming languages and provides feedback on bugs, optimizations, style, and best practices using AI.

## Features

- Review Python, Java, JavaScript, and other languages.
- Returns structured feedback as JSON:
  - **Bugs**: potential errors or logical mistakes
  - **Optimizations**: performance improvements
  - **Style**: readability and code formatting tips
  - **Suggestions**: general best practices
- Real-time code review via a clean frontend interface.
- Dynamic placeholder in the textarea depending on the selected language.

## Tech Stack

- **Frontend:** React
- **Backend:** FastAPI
- **AI Model:** GPT-4o-mini via OpenAI API
- **Other:** Axios for frontend API requests, CSS modules for styling


## Setup

### Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create .env file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

5. Start the backend server

```bash
uvicorn main:app --reload
```

### Frontend

1. Navigate to the frontend directory

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React app:

```bash
npm start
```

## Usage
1. Open the frontend in your browser (usually at http://localhost:3000)
2. Paste your code into the textarea
3. Select the language
4. Click Review Code to get structured AI feedback

## Project Structure

```css
ai-code-review-bot/
├── backend/         
│   ├── main.py
│   ├── app/
│   │   └── routes.py
│   └── venv/
├── frontend/        
│   ├── src/
│   └── package.json
└── README.md
```


