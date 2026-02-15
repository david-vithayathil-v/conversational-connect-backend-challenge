from fastapi import APIRouter
from app.api.v1.services.main import BackendService

router = APIRouter()
backend_service = BackendService()


@router.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint
    
    Returns:
        dict[str, str]: Health status
    """
    return {"status": "ok"}

@router.get("/settings")
def settings() -> dict[str, str]:
    """Settings endpoint
    
    Returns:
        dict[str, str]: Settings information
    """
    backend_service = BackendService()
    return backend_service.get_settings()
