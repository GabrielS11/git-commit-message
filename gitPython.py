from git import Repo


def main():
    repo = Repo(".")
    print(repo.git_dir)

    print("\n\n\n")


    last_commit = repo.head.commit

    print("Ultimo commit hash: ", last_commit.hexsha)
    print("Autor: ", last_commit.author)
    print("Mensagem: ", last_commit.message)
    print("Data: ", last_commit.committed_datetime)


if __name__ == "__main__":
    main()