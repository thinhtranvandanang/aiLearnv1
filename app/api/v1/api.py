from fastapi import APIRouter
from app.api.v1.endpoints import auth, tests, submit, results, history

api_router = APIRouter()

@api_router.get("/")
def api_root():
    return {
        "message": "EduNexia API v1",
        "version": "1.0.0",
        "endpoints": {
            "auth": "/auth",
            "google_oauth": "/auth/google",
            "practice_tests": "/practice-tests", 
            "submissions": "/submissions",
            "learning_history": "/students"
        }
    }

# Đăng nhập truyền thống: /api/v1/auth/student/login
api_router.include_router(auth.router, prefix="/auth/student", tags=["Authentication"])

# Google OAuth: /api/v1/auth/google/login và /api/v1/auth/google/callback
api_router.include_router(auth.google_router, prefix="/auth", tags=["Google OAuth"])

api_router.include_router(tests.router, prefix="/practice-tests", tags=["Practice Tests"])
api_router.include_router(submit.router, prefix="/practice-tests", tags=["Submission"])
api_router.include_router(results.router, prefix="/submissions", tags=["Results & Suggestions"])
api_router.include_router(history.router, prefix="/students", tags=["Learning History"])