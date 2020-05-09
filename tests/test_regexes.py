import json
import logging
import re

import pytest


def make_testdata():
    with open("regexes.json") as regexes_file:
        data = json.load(regexes_file)
    for platform, types in data.items():
        for type, type_def in types.items():
            if "tests" in type_def:
                for url, matches in type_def["tests"].items():
                    yield type_def["regex"], url, matches
            else:
                raise RuntimeError("%s:%s has no tests!" % (platform, type))


@pytest.mark.parametrize("regex,url,matches", make_testdata())
def test_regex(regex, url, matches):
    fullmatch = re.fullmatch(regex, url)
    if matches:
        # there's an expected results, i.e. the dict is not None
        assert fullmatch is not None, "Regex did not match at all"
        assert len(fullmatch.groups()) == len(matches), "Regex has more than expected capturing groups"
        for name, match in matches.items():
            assert fullmatch.group(name) == match, "Group %s invalid" % name
    else:
        # no dict, assert no match
        assert fullmatch is None
