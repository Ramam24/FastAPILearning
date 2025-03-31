import asyncio
import nest_asyncio
import sys
from config import engine
from models import Base

# 🔹 Fix for event loop issue
nest_asyncio.apply()

# 🔹 Windows-specific event loop fix
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
