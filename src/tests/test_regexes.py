import re

import pytest

from src.generate import read_regex_data, generate_monster_regex


def make_testdata():
    """
    Load the test data.
    """
    data = read_regex_data()
    for platform, types in data.items():
        for type, type_def in types.items():
            if "tests" in type_def:
                for url, matches in type_def["tests"].items():
                    yield type_def["regex"], url, matches
            else:
                raise RuntimeError("%s:%s has no tests!" % (platform, type))


@pytest.mark.parametrize("regex,url,matches", make_testdata())
def test_regex(regex, url, matches):
    """
    Test a single regex.
    :param regex: regex to test.
    :param url: url applied as test case.
    :param matches: expected matches as a dict<name:value> or None if invalid url
    """
    fullmatch = re.fullmatch(regex, url)
    if matches:
        # there's an expected results, i.e. the dict is not None
        assert fullmatch is not None, "Regex did not match at all"
        # removed because we might have queries with optional groups, e.g. medium posts with users or publications
        # assert len(fullmatch.groups()) == len(matches), "Regex has more than expected capturing groups"
        for name, match in matches.items():
            assert fullmatch.group(name) == match, "Group %s invalid" % name
    else:
        # no dict, assert no match
        assert fullmatch is None


@pytest.mark.parametrize("regex,url,matches", make_testdata())
def test_regex_without_protocol(regex, url, matches):
    # take the url and remove protocol
    url_without_protocol = url.replace("http:", "").replace("https:", "")
    test_regex(regex, url_without_protocol, matches)


def test_monster_regex():
    """
    Make sure monster regex matches all tests of all regexes.
    """
    data = read_regex_data()
    regex = re.compile(generate_monster_regex())
    for platform, types in data.items():
        for type, type_def in types.items():
            for url, matches in type_def["tests"].items():
                if matches:
                    assert regex.match(url), "url %s does not match" % url
