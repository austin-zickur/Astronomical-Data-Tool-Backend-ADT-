from supabase import create_client, Client

# Replace these with your project details
SUPABASE_URL = "https://your-supabase-project-url.supabase.co"
SUPABASE_KEY = "your-supabase-api-key"

def initialize_supabase():
    # Create a Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase

# Example usage
if __name__ == "__main__":
    supabase = initialize_supabase()
    print("Supabase client initialized successfully!")
