import git

repo = git.Repo(".")  # Inicializa el repositorio actual
commits = repo.git.log("HEAD@{1}..HEAD", "--oneline")
print(commits)
