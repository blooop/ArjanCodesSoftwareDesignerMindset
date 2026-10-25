FROM ghcr.io/blooop/python_template/devcontainer:latest

# This repo keeps its PDFs in Git LFS (.gitattributes). The shared image has
# no git-lfs, and without it `git status` and `git commit` fail in the
# container on the LFS clean filter. Drop this file and go back to "image":
# once the shared image ships git-lfs.
USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends git-lfs \
    && rm -rf /var/lib/apt/lists/*
USER vscode
