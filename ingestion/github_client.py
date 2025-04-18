from pathlib import Path
from git import Repo
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader

SUPPORTED_EXTS = {".js", ".ts", ".py", ".vue", ".html", ".css", ".txt"}
EXCLUDED_FILENAMES = {
    ".env", ".gitignore", ".prettierrc", ".eslintrc",
    "package-lock.json", "yarn.lock"
}


from config import settings
import os

def pull_repo():
    repo_path = "repo_cache"

    if not os.path.exists(repo_path):
        Repo.clone_from(settings.REPO_URL, repo_path)
    else:
        Repo(repo_path).remotes.origin.pull()

    print("📂 Filtering files by supported extensions...")

    all_docs = []

    for filepath in Path(repo_path).rglob("*"):
        if (
            filepath.suffix in SUPPORTED_EXTS
            and filepath.name not in EXCLUDED_FILENAMES
            and "node_modules" not in filepath.parts  
        ):
            try:
                loader = TextLoader(str(filepath), encoding="utf-8")
                all_docs.extend(loader.load())
            except Exception as e:
                print(f"⚠️ Skipped {filepath.name}: {e}")

    return all_docs
