"""Trip Pydantic schemas for request/response validation."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class TripCreate(BaseModel):
    """Schema for creating a new trip."""

    name: str = Field(..., min_length=1, max_length=255, description="Trip name")
    city: str = Field(..., min_length=1, max_length=255, description="Destination city")
    user_id: UUID = Field(..., description="User ID who owns this trip")


class TripResponse(BaseModel):
    """Schema for trip response."""

    id: UUID
    name: str
    city: str
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TripListResponse(BaseModel):
    """Schema for list of trips response."""

    trips: list[TripResponse]

