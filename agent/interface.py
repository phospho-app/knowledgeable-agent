"""
This will be the file handling the interfacing between the dev user agent repo and the app-template 
"""

# This is the function that will be called when a question is asked to the agent
def ask(query): 
    # Your code here
    response = 'The question was : {}'.format(query) # This is just a dummy response

    return response #str