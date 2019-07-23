# Regular Expressions to Match Social Media Profiles

This repository lists regular expressions to match and extract URLs of social media profiles. For simplicity URLs have to be filtered beforehand, i.e. the regular expression has to be executed on a single URL. To do this, you could use a regular expression matching valid URLs or use a specific library, for example JSOUP for Java. Furthermore, only exact profile urls are matched (for example no profile urls inside a url referencing a post).

Please note: I've also created a [Python library called socials](https://github.com/lorey/socials) that uses these expressions to _automate url detection_ and extraction.

## Twitter

    ^(?:http(?:s)?:\/\/)?(?:www\.)?twitter\.com\/(?:#!\/)?(?:\@)?(?:pages\/)?(?:[\w\-]*\/)*(\w{1,15})$

Allowed for usernames are alphanumeric characters and underscores.

### Verification

Send request to page and check for username in answer (rate limit?)

## Github

    ^(?:(?:http|https):\/\/)?(?:www.)?(?:github\.(?:com|io))\/([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38})(?:\/)?$|(?:(?:http|https):\/\/)?([a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38})(?:\.github\.(?:com|io))(?:\/)?([a-zA-Z0-9_-]+)?(?:\/)?$

Regex to get username from urls and from subdomain of github urls

### Verification

Use https://api.github.com/users/{user_login} (60 requests/hour unauthenticated)

## Linkedin

    ^(?:http(?:s)?:\/\/)?(?:www\.|\w\w\.)?linkedin\.com\/((?:in)\/(?:[a-zA-Z0-9-]{5,30}(?:\/)?)|(?:profile\/)(?:view\?id=[0-9]+))$

RegEx for public URLs.

    http(s)?:\/\/([\w]+\.)?linkedin\.com\/pub\/[A-z0-9_-]+(\/[A-z0-9]+){3}\/?

Matches public profiles that need three keys(?) after the actual name.

### Verification

Check page for profile specific html (rate limit?)

## Facebook

    ^(?:(?:http|https):\/\/)?(?:www.|m.)?(?:facebook\.com|fb\.me|fb\.com)\/(?!home.php)(?:(?:\w)*#!\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\.-]+)$

Matches facebook.com fb.me and fb.com (shortlink). Excludes home.php or root page

### Verification

Since Facebook redirects these URLs to all kinds of objects (user, pages, events, and so on), you have to verifiy that it's actually a user. See https://developers.facebook.com/docs/graph-api/reference/profile

#### API

http://graph.facebook.com/v2.3/{{username}} gives the following result, if the user exists:

    {
        "error": {
        "message": "(#803) Cannot query users by their username ({{specified username}})",
        "type": "OAuthException",
        "code": 803
        }
    }

Online test: https://regex101.com/r/koN8C2/3

#### GET request

A GET request on an existing (but hidden) user with a randomly added point seems to redirect to the real username.

## Instagram

    ^(?:(?:http|https):\/\/)?(?:www.)?(?:instagram.com|instagr.am)\/([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)$

The rules:

- Matches with one . in them disco.dude but not two .. disco..dude
- Ending period not matched discodude.
- Match underscores \_ _disco\_\_dude_
- Max characters of 30 1234567890123456789012345678901234567890
  Online test: https://regex101.com/r/DBVLCq/1

## Google Plus

    https?:\/\/plus\.google\.com\/\+[^/]+|\d{21}

Matches username or profile numbers up to 21 digits.

## Skype

    ^(?:(?:callto|skype):)(?:[a-z][a-z0-9\\.,\\-_]{5,31})(?:\\?(?:add|call|chat|sendfile|userinfo))?$

Matches Skype's URLs to add contact, call, chat.

## Telegram

    https?:\/\/(t(elegram)?\.me|telegram\.org)\/([a-z0-9\_]{5,32})\/?

Matches for t.me, telegram.me and telegram.org

## Stack Overflow

    /^http(s)?:\/\/(www\.)?stackoverflow\.com\/users\/[0-9]+\/[A-z0-9_-]+\/?$/

Matches for Stack Overflow profile pages (e.g. https://stackoverflow.com/users/2544348/marnix-harderwijk)

## Reddit

    ^(?:(?:http|https):\/\/)?(?:www.)?(?:reddit\.(?:com))\/(?:u\/|user\/)([a-zA-Z0-9-_]{3,20})\/?$

Matches usernames
Online test: https://regex101.com/r/G46SgM/3/

## Youtube

    ^(?:(?:http|https):\/\/)?(?:www.)?(?:youtube\.(?:com|co\.uk|net|de)|youtu\.be)\/(?:c\/|channel\/|user\/)?([a-zA-Z0-9-.'_]{6,20})$

Matches usernames and channels
Online test: https://regex101.com/r/ysB9CX/2

## TODO

- Verification checks (ideas first and maybe scripts at a later point)

I plan on adding the following social media profiles at the moment.

- xing
- pinterest
- vimeo
- wordpress
- medium
- bitbucket

Feel free to add any social media site you would like to find here!
