"""
This will be the file handling the interfacing between the dev user agent repo and the app-template 
"""

# This is the function that will be called when a question is asked to the agent
def ask(messages): 
    # Your code here

    # This is an example of how to get the last message received by the agent
    if len(messages) == 0:
        response = "No message received"
    else:
        last_message = messages[-1]
        response = "Your question was : " + last_message["content"]

    return response #str