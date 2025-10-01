from git import Repo


def main():
    '''Esta funçao vai criar a mensagem para o seu commit'''
    repo = Repo(".")

    # pega as mudanças não commitadas (staged + unstaged)
    diff_text = repo.git.diff()

    # (no futuro aqui entra o LLM que gera a mensagem)
    mensagem = ("chore: add .env and .gitignore, update commit script"
                "- Added .env file for environment configuration (content not exposed))"
                "- Created .gitignore to exclude virtual environment, .env, PyCharm files, and logs"
                "- Updated gitPython.py with diff print and docstring cleanup"
                "- Commented out commit execution for safe testing")

    # faz o commit com tudo
    repo.git.add(A=True)
    repo.index.commit(mensagem)

    print("Commit feito com mensagem:", mensagem)

if __name__ == "__main__":
    main()