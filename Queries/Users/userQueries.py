from SupabaseClient import initialize_supabase, initialize_supabase_admin

'''
FileName: signup

Developer: Kylee B

Description: functions to query supabase for user authentication

Imported into: 
    * SignUp.py

Functions:
    * signUp():
        input:
            params:
                fullName (String)
                email (String)
                password (String)
        output:
            data (Array)
    * getEmails():
        input:
        output:
            emails (Array)

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
    
# for checking if a userExists
def getEmails():
    supabase_admin = initialize_supabase_admin()
    data = supabase_admin.auth.admin.list_users()
    emails = []
    for user in data:
        email = user.user_metadata['email']
        print(user.user_metadata['email'])
        emails.append(email)
    #print(emails)
    return emails
    #print(data[0].user_metadata['email']) 

# delete user account
def deleteUserAccount(userId):
    supabase_admin = initialize_supabase_admin()
    response = supabase_admin.auth.admin.delete_user(userId)
    print(response)
    return response

def getPatchNotes():
      response = supabase.table('patch_notes').select('*').order('created_at', desc=True).execute()
      return response
''' -- UNUSED --
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

#Austin's testing of getting user id
def userId(user):
    session = supabase.auth.get_user()
    if session['user']:
        print(f"User ID: {session['user']['id']}")
    else:
        print("No user logged in")
''' 

#DEBUG BELOW:
'''
if __name__ == "__main__":
    getEmails()
'''