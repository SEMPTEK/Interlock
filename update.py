"""
This script is used to update the rest of the software. This script is meant to be stand-alone and cannot be run
by any other script.
"""

from git import Repo
import os


def updater():
    path = os.path.dirname(os.path.realpath(__file__))
    Repo.clone_from("https://github.com/JohnMcLaughlin-SnS/Companion", path)


if __name__ == "__main__":
    updater()
