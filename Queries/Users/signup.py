from supabase import initialize_supabase

'''
FileName: signup

Developer: Kylee B

Description: functions to query supabase for user authentication

Imported into: 
    * SignUp.py

Functions:
    * signUp():
        input:
            email (String)
            password (String)
        output:
            data (JSON)

'''

# initialize supabase for use
supabase = initialize_supabase()

def signUp(email, password):
    try:
        data = supabase.auth.sign_up({
            'email': f'{email}',
            'password': f'{password}',
            'options': {
                'email_redirect_to': 'https://example.com/welcome',
                },
        })
        print(data)
        return(data)
    except Exception as e:
        print(f"error connecting to DB -- {e}")
        return(f"error connecting to DB -- {e}")