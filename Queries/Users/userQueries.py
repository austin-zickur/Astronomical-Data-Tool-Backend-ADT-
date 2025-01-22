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
#supabase = initialize_supabase()

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
    
def getEmails():
    data = supabase.auth.admin.list_users()
    emails = []
    for user in data:
        email = user.user_metadata['email']
        print(user.user_metadata['email'])
        emails.append(email)
    #print(emails)
    return emails
    #print(data[0].user_metadata['email']) 

    #Austin's testing of getting user id
def userId(user):
    session = supabase.auth.get_user()
    if session['user']:
        print(f"User ID: {session['user']['id']}")
    else:
        print("No user logged in")

if __name__ == "__main__":
    getEmails()