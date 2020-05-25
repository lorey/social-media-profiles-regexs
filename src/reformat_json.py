import json
import os


REGEXES_FILE = "regexes.json"
REGEXES_FILE_TMP = "regexes-formatted.json"

if __name__ == "__main__":
    # will format the file

    # open input file
    with open(REGEXES_FILE) as f:
        regex_file_content = json.load(f)

    # create temp file with formatted output
    with open(REGEXES_FILE_TMP, "w") as f:
        json.dump(regex_file_content, f, sort_keys=True, indent=2)

    # replace input file if everything went right
    os.rename(REGEXES_FILE_TMP, REGEXES_FILE)
