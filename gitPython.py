from git import Repo


def main():
    '''Esta funçao vai criar a mensagem para o seu commit'''''
    repo = Repo(".")

    # pega as mudanças não commitadas (staged + unstaged)
    diff_text = repo.git.diff()

    # (no futuro aqui entra o LLM que gera a mensagem)
    mensagem = "fix: commit automático de teste"

    # faz o commit com tudo
    repo.git.add(A=True)
    repo.index.commit(mensagem)

    print("Commit feito com mensagem:", mensagem)

if __name__ == "__main__":
    main()