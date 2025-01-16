from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
# Replace these with your project details
SUPABASE_URL = os.getenv("API_URL")
SUPABASE_KEY = os.getenv("API_KEY")

def initialize_supabase():
    # Create a Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase

# Example usage
if __name__ == "__main__":
    supabase = initialize_supabase()
    print("Supabase client initialized successfully!")
