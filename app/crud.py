from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import StoreStatus, BusinessHours, StoreTimeZone

async def get_store_status(db: AsyncSession, store_id: str):
    result = await db.execute(select(StoreStatus).filter(StoreStatus.store_id == store_id))
    return result.scalars().all()

async def get_business_hours(db: AsyncSession, store_id: str):
    result = await db.execute(select(BusinessHours).filter(BusinessHours.store_id == store_id))
    return result.scalars().all()

async def get_store_timezone(db: AsyncSession, store_id: str):
    result = await db.execute(select(StoreTimeZone).filter(StoreTimeZone.store_id == store_id))
    return result.scalars().first()
