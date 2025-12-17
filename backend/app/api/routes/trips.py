"""Trip CRUD endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.trip import Trip
from app.models.user import User
from app.schemas.trip import TripCreate, TripListResponse, TripResponse

router = APIRouter()


@router.post(
    "/trips",
    response_model=TripResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_trip(
    trip_data: TripCreate,
    db: Session = Depends(get_db),
):
    """Create a new trip."""
    # Verify user exists
    user = db.query(User).filter(User.id == trip_data.user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {trip_data.user_id} not found",
        )

    # Create trip
    trip = Trip(
        name=trip_data.name,
        city=trip_data.city,
        user_id=trip_data.user_id,
    )
    db.add(trip)
    db.commit()
    db.refresh(trip)

    return trip


@router.get(
    "/trips/{trip_id}",
    response_model=TripResponse,
)
async def get_trip(
    trip_id: UUID,
    db: Session = Depends(get_db),
):
    """Get a trip by ID."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id {trip_id} not found",
        )

    return trip


@router.get(
    "/trips",
    response_model=TripListResponse,
)
async def list_trips(
    user_id: UUID = Query(..., description="User ID to filter trips"),
    db: Session = Depends(get_db),
):
    """List all trips for a specific user."""
    # Verify user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    # Get trips for user
    trips = db.query(Trip).filter(Trip.user_id == user_id).all()

    return TripListResponse(trips=trips)


@router.delete(
    "/trips/{trip_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_trip(
    trip_id: UUID,
    db: Session = Depends(get_db),
):
    """Delete a trip by ID."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id {trip_id} not found",
        )

    db.delete(trip)
    db.commit()

    return None

