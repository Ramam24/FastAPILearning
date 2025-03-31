import sys
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

# 🔹 Apply fix for Windows event loop
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

DATABASE_URL = "mysql+aiomysql://root:root%40123@localhost/fastapilearning"
engine = create_async_engine(DATABASE_URL, echo=True)
