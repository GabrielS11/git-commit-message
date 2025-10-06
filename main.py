from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gitPython import generate_commit_message
import re

app = FastAPI()

class DiffRequest(BaseModel):
    diff_text: str

def is_valid_diff(diff_text: str) -> bool:
    """
    Basic validation to check if the input is a git diff.
    Looks for typical diff headers and patterns.
    """
    # Check for unified diff header and at least one diff hunk
    if not diff_text:
        return False
    # Must start with 'diff --git' or '---' and '+++'
    if not (diff_text.startswith('diff --git') or diff_text.startswith('---')):
        return False
    # Must contain at least one hunk header
    if re.search(r'^@@ .+ @@', diff_text, re.MULTILINE):
        return True
    return False

@app.post("/commit")
async def create_commit_message(request: DiffRequest):
    '''
    Endpoint to generate a commit message from a git diff.
    Validates the input and returns the generated commit message.
    '''
    if not is_valid_diff(request.diff_text):
        raise HTTPException(status_code=400, detail="Invalid diff format. Please provide a valid git diff.")
    try:
        message = generate_commit_message(request.diff_text)
        return {"commit_message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))