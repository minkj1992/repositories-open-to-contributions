import os
from pathlib import Path
import sys
from unittest import mock

SCRIPT_DIR = file = f"{Path(__file__).parents[1]}/custom_python_actions/"
print(SCRIPT_DIR)
sys.path.append(os.path.dirname(SCRIPT_DIR))

from custom_python_actions.check_external_contrib import (
    get_repos_open_to_contributions,
)  # noqa


def test_check_repos_open_to_contributions():
    gh = mock.Mock()
    gh_repo = mock.Mock()
    file_contents = mock.Mock()
    file_contents.decoded.decode.return_value = "one-repo\nanother-repo\n"
    gh_repo.file_contents.return_value = file_contents
    gh.repository.return_value = gh_repo

    repo_list = get_repos_open_to_contributions(gh)

    assert repo_list == ["one-repo", "another-repo"]
