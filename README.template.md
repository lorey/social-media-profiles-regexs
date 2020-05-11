# Regular Expressions to Match Social Media Profiles
This repository lists regular expressions to match and extract URLs of social media profiles. For simplicity URLs have to be filtered beforehand, i.e. the regular expression has to be executed on a single URL. To do this, you could use a regular expression matching valid URLs or use a specific library, for example JSOUP for Java. Furthermore, only exact profile urls are matched (for example no profile urls inside a url referencing a post).

Please note:
If you want to extract social media links, there are possibly easier ways:

* I've created a [Python library called socials](https://github.com/lorey/socials) that uses these expressions to *automate url detection* and extraction.
You input the urls, it extracts the social media profiles.
* There's also a [Socials API](https://github.com/lorey/socials-api) you can use for free or deploy yourself.
You simply input any URL and it will fetch and return all social media links on this website. Try it [here](http://socials.karllorey.com/try).

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
{% endfor %}
{% endfor -%}

## Monster Regex
If you want to match all social media profiles with one regex, use this monster:

```regex
{{ monster_regex }}

```

