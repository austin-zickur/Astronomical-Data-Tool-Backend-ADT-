from SupabaseClient import initialize_supabase

'''
FileName: signup

Developer: Kylee B

Description: functions to query supabase for user authentication

Imported into: 
    * SignUp.py

Functions:
    * signUp():
        input:
            fullName (String)
            email (String)
            password (String)
        output:
            data (JSON)

'''

# initialize supabase for use
supabase = initialize_supabase()

def signUp(fullName, email, password):
    try:
        data = supabase.auth.sign_up({
            'email': f'{email}',
            'password': f'{password}',
            'options': {
                'email_redirect_to': 'http://localhost:5173',
                'data': {
                    'display_name': f"{fullName}"
                }
                },
        })

        if data:
            return data
        else:
            print("Error retrieving data")
            return
        #print(data)
        #return(data)
    except Exception as e:
        print(f"error connecting to DB -- {e}")
        return(f"error connecting to DB -- {e}")
    
def signIn(email, password):
    try:
        data = supabase.auth.sign_in_with_password({
        "email": f"{email}",
        "password": f"{password}"
        })
        if data:
            return data
        else:
            print("Error retrieving data")
            return

    except Exception as e:
            print(f"error connecting to DB -- {e}")
            return(f"error connecting to DB -- {e}")