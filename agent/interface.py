"""
This will be the file handling the interfacing between the dev user agent repo and the app-template.
If a file is uploaded to the agent, it will be stored in the fodler agent/tmp/{session_id}/
"""

def ask(messages, session_id):

    # This is an exemple

    if len(messages) == 0:
        response = "No message received"
    else:
        # YOUR CODE HERE
        last_message = messages[-1]
        last_message_content = last_message["content"]
        response = f"Your question was {last_message_content} Your session ID is {session_id}"
    # You need to return a string, that will be displayed to the user as a message
    return response #str

# Handle a single file upload
def handle_single_file_upload(session_id, sanitized_filename):
    # YOUR CODE HERE
    # The file is at agent/tmp/{session_id}/{sanitized_filename}
    # You can delete the file with os.remove(path) to free up memory
    pass # no need to return anything

# Handle a single file download request
def handle_single_file_download(session_id):
    # YOUR CODE HERE
    # You need to return the relative path to the file to download (e.g. 'tmp/{session_id}/{filename}')
    # The file will be downloaded in your end user browser
    path_to_file = "path/to/file"
    return path_to_file # type str