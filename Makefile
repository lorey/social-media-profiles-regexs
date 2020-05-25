.RECIPEPREFIX = >

all:
> python src/generate.py
> python -m pytest
> python src/reformat_json.py
