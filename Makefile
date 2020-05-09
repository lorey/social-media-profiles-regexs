.RECIPEPREFIX = >

all:
> python src/generate.py
> python -m pytest
