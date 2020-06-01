# Regular Expressions to Match Social Media Profiles
This repository lists regular expressions to match and extract information from URLs of social media profiles.
So if you find a hyperlink to this repo somewhere on the web, i.e. https://github.com/lorey/social-media-profiles-regexs/, 
the regular expressions in this repo allow you find out it's a Github link pointing to a repo
as well as extract the username `lorey` and the repo name `social-media-profiles-regexs` from this URL.

Please note:
If you want to extract social media links, depending on your case, there are possibly easier ways:

* I've created a [Python library called socials](https://github.com/lorey/socials) that uses these expressions to *automate url detection* and data extraction.
You input the urls, it extracts the type of platform as well as the contained information, e.g. the linked social media profiles.
* There's also a [Socials API](https://github.com/lorey/socials-api) which makes the socials python package available via REST and JSON. 
You can use it for free at [socials.karllorey.com](http://socials.karllorey.com/) or deploy it yourself.
You simply input any URL you want to extract profiles from. It will then fetch and return all social media links from the given website. 
Try it [here](http://socials.karllorey.com/try).

If you're missing a particular platform, please feel free to add it.
Also feel free to add a test that does not work.
An explanation of how this repo works can be found in [CONTRIBUTING.md](CONTRIBUTING.md).
You might also open an issue, of course, I'm happy to help!

## Table of Contents
{% for platform in data -%}
- [{{ platform }}](#{{ platform|replace(" ", "-") }})
{% endfor -%}
- [Monster Regex](#monster-regex)


{% for platform, types in data.items() %}
## {{ platform }}
{% for type in types %}
### {{ type }}
```regex
{{ data[platform][type].regex }}
```
{{ data[platform][type].note }}

Examples: 
{% for url in data[platform][type]["tests"] %}
{%- if data[platform][type]["tests"][url] %}
- {{ url }}
{%- endif -%}
{%- endfor %}
{% endfor %}
{% endfor -%}

## Monster Regex
If you want to match all social media profiles with one regex, use this monster:

```regex
{{ monster_regex }}

```

