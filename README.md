Commit Message Generator - User Guide
=====================================

This service allows you to automatically generate commit messages using AI.  
You only need to use [GitPython](https://gitpython.readthedocs.io/en/stable/) in your project to get your code diff, and then send it to the `/commit` endpoint.

How to Use
----------

1. **Install GitPython in your project:**
   ```
   pip install gitpython
   ```

2. **Generate your git diff using GitPython:**
   ```python
   from git import Repo
   repo = Repo(".")
   diff_text = repo.git.diff()
   ```

3. **Send a POST request to the `/commit` endpoint** with your diff:
   - The endpoint expects a JSON payload like:
     ```json
     {
       "diff_text": "your git diff here"
     }
     ```
   - Example using `curl`:
     ```
     curl -X POST "http://localhost:8000/commit" -H "Content-Type: application/json" -d "{\"diff_text\": \"your git diff here\"}"
     ```

4. **Receive the generated commit message** in the response.

Notes
-----

- You do **not** need to install or use OpenAI or FastAPI in your own project—just GitPython to generate the diff.
- The FastAPI server (provided separately) will handle the AI and return your commit message.
- Make sure to replace `"your git diff here"` with the actual diff string from your repository.

That's it!  
Just generate your diff and send it to `/commit` to get an AI-powered commit message.
