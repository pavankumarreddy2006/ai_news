# Render Deployment Checklist

- Set backend root directory to `backend`
- Set frontend root directory to `frontend`
- Configure backend env vars from `.env.example`
- Configure frontend `VITE_API_BASE_URL` and `VITE_WS_URL`
- Verify backend start command: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
- Verify frontend build command: `npm install && npm run build`

