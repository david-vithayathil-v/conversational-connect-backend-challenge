from app.core.config import get_settings


class BackendService:
    """Service for managing application settings."""
    
    def get_settings(self) -> dict[str, str]:
        """Fetch settings from env and return as dict
        Returns:
            dict[str, str]: Current settings
        """
        
        settings = get_settings()
        return {
            "service_name": settings.service_name,
            "environment": settings.environment,
            "log_level": settings.log_level,
            "log_format": settings.log_format,
            "api_v1_prefix": settings.api_v1_prefix,
        }