from dotenv import load_dotenv
from supabase import create_client,Client
import os

load_dotenv()

def supabase() -> Client:
    return create_client(
        os.getenv("SUPABASE_URL"),
        os.getenv("SUPABASE_KEY")
    )

