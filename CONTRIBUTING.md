# Contributing to social-media-profiles-regexs
To make sure all regexes work as desired, we're using pytest to check them.
Therefore, all regexes can be found inside [a json file](regexes.json)
and the README.md file is generated with the contents of the json file.

So please, do not edit the README.md manually!

## Setting it up
```
# set up a virtual environment
virtualenv -p /use/bin/python3 venv
source venv/bin/activate

# install the dependencies
pip install -r requirements.txt
```

## Making changes
- To add or change a regex, edit [regexes.json](regexes.json). 
  Please use a capture group to extract contained information like usernames.
  Also add tests to make sure everything works as expected.
- To update meta-information edit the template [README.md.template](README.md.template)

After you're done, please run `make`.
It will test your changes and generate the README.md file.
Please open a PR only after you followed these instructions.
