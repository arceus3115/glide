"""User Pydantic schemas for request/response validation."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserResponse(BaseModel):
    """Schema for user response."""

    id: UUID
    external_id: str | None
    email: str | None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

