#! python3
import sys, pyperclip

#Creating dictionary of PASSWORDS
PASSWORDS= {
    'email': 'andkjfahufa',
    'fb': 'anjkdhvaidfja' 
}
account = sys.argv[1] # argument passed through command line 
print(account)
'''
    python .\password.py email
Then, sys.argv[1] will store email
'''

#Simple if condition to to get the password if the passed argument is contain in dictionary
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account]) #Copy the password

else:
    print("No such account name")

    
