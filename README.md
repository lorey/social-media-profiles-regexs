# Regular Expressions to Match Social Media Profiles
This repository lists regular expressions to match and extract URLs of social media profiles. For simplicity URLs have to be filtered beforehand, i.e. the regular expression has to be executed on a single URL. To do this, you could use a regular expression matching valid URLs or use a specific library, for example JSOUP for Java. Furthermore, only exact profile urls are matched (for example no profile urls inside a url referencing a post).

Please note: I've also created a [Python library called socials](https://github.com/lorey/socials) that uses these expressions to *automate url detection* and extraction.

## Twitter
    http(s)?:\/\/(.*\.)?twitter\.com\/[A-z0-9_]+\/?
Allowed for usernames are alphanumeric characters and underscores. 

### Verification
Send request to page and check for username in answer (rate limit?)

## Github
    http(s)?:\/\/(www\.)?github\.com\/[A-z0-9_-]+\/?
Exclude subdomains as these redirect to github pages sometimes.

    http(s)?:\/\/([A-z0-9-_]+)\.github\.(com|io)\/?
Regex for pages like someuser.github.io.

### Verification
Use https://api.github.com/users/{user_login} (60 requests/hour unauthenticated)

## Linkedin
    http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/[A-z0-9_-]+\/?
RegEx for public URLs.

    http(s)?:\/\/([\w]+\.)?linkedin\.com\/pub\/[A-z0-9_-]+(\/[A-z0-9]+){3}\/?
Matches public profiles that need three keys(?) after the actual name.

    http(s)?:\/\/([\w]+\.)?linkedin\.com\/recruiter\/[A-z0-9_-]+\/?
RegEx for Linkedin Recruiter URLs.

### Verification
Check page for profile specific html (rate limit?)

## Facebook
    http(s)?:\/\/(www\.)?(facebook|fb)\.com\/[A-z0-9_\\-\\.]+\/?
Matches facebook.com and fb.com (shortlink).

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

#### GET request
A GET request on an existing (but hidden) user with a randomly added point seems to redirect to the real username.
## Instagram
    https?:\/\/(www\.)?instagram\.com\/([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)

The rules:
 * Matches with one . in them disco.dude but not two .. disco..dude
 * Ending period not matched discodude.
 * Match underscores _ _disco__dude_
 * Max characters of 30 1234567890123456789012345678901234567890

## Google Plus
    https?:\/\/plus\.google\.com\/\+[^/]+|\d{21}

Matches username or profile numbers up to 21 digits.

## Skype
    (?:(?:callto|skype):)(?:[a-z][a-z0-9\\.,\\-_]{5,31})(?:\\?(?:add|call|chat|sendfile|userinfo))?

Matches Skype's URLs to add contact, call, chat.
## Telegram
    https?:\/\/(t(elegram)?\.me|telegram\.org)\/([a-z0-9\_]{5,32})\/?
Matches for t.me, telegram.me and telegram.org

## TODO
* Verification checks (ideas first and maybe scripts at a later point)

I plan on adding the following social media profiles at the moment.
* xing
* pinterest
* vimeo
* wordpress
* medium
* youtube
* stackoverflow
* bitbucket
 
Feel free to add any social media site you would like to find here!
