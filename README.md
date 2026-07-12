# URL-Detector

Local dev and Docker instructions for the project.

## Local development

1. Backend

- Create a virtualenv and install requirements:

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Backend will start at `http://127.0.0.1:8000`.

2. Frontend

- Install and start React dev server:

```powershell
cd frontend
npm install
npm start
```

Frontend dev server runs at `http://localhost:3000` and talks to the backend configured by `REACT_APP_API_URL`.

## Environment variables

- Frontend: `REACT_APP_API_URL` (default: `http://127.0.0.1:8000`). Put in `frontend/.env` or export before starting.
- Backend: no required env vars for this prototype.

## Docker (recommended)

Use docker-compose to build and run both services together:

```powershell
docker compose up --build
```

- Backend exposed on `http://localhost:8000`
- Frontend served on `http://localhost:3000`

## Notes

- The backend currently uses a simple string-checker in `backend/main.py`. Replace with a trained model (see `train_model.py`) before production use.
- Do not commit model binaries or large datasets. They are ignored by `.gitignore`.
