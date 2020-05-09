from generate import render_readme

README_RENDERING_ERR = "README not rendered, please run generate.py and commit"


def test_generation():
    with open("README.md") as file:
        assert render_readme() == file.read(), README_RENDERING_ERR
