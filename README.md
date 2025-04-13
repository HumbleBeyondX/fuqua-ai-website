# fuqua-ai-website
This is a website designed for posting news and latest research works about AI at the fuqua school of business

# Information
- Name: Boxiao (Daniel) Huang
- Email: boxiao.huang@duke.edu
- github: https://github.com/humblebeyondx
- Date: 2025-04-12


# Project Framework
* Frontend - Vue.js
* Backend - Django
* Database - MySQL


# Run the project

## Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend/Fuquaai-frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Access the application in your browser at:
```
http://localhost:5173/
```

## Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Set up environment variables:
- Make sure your `.env` file is properly configured in the backend directory with:
  ```
  SECRET_KEY=your_secret_key
  DEBUG=True
  DB_NAME=your_db_name
  DB_USER=your_db_user
  DB_PASSWORD=your_db_password
  DB_HOST=localhost
  ```

6. Apply migrations:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```

8. The backend API will be available at:
```
http://localhost:8000/
```


