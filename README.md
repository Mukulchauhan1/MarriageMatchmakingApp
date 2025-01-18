# Marriage Matchmaking App

## Description
A backend application to manage user profiles and matchmaking using FastAPI and SQLite.

## Features
- Create, read, update, and delete user profiles.
- Find potential matches based on user information.

## Setup and Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MarriageMatchmakingApp.git
   cd MarriageMatchmakingApp
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
