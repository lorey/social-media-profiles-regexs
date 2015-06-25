# social-media-profiles-regexs
Regular expressions to match and extract urls of social media profiles in a list of url.s

## Twitter
    .*twitter\.com\/[A-z 0-9 _]+\/?
Allowed for usernames are alphanumeric characters and underscores. 
Verification: Send request to page and check for username in answer.

## Github
    http(s)?:\/\/(www\.)?github\.com/[A-z 0-9 _ -]+
Exclude subdomains as these redirect to github pages sometimes.

    http(s)?:\/\/([A-z 0-9 - _]+)\.github\.(com|io)
Regex for pages like someuser.github.io.

Verification: Use https://api.github.com/users/{user_login}

## Linkedin
    http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/(A-z 0-9 _ -)\/?
Public URLs. (TODO: there are also linkedin.com/userxy profiles.

    http(s)?:\/\/([\w]+\.)?linkedin\.com\/pub\/[A-z 0-9 _ -]+(\/[A-z 0-9]+){3}\/?
public profiles that need the three keys after the actual name.


## TODO
* Verification checks (ideas first and maybe scripts at a later point)

I plan on adding the following social media profiles at the moment.
* facebook
* xing
* instagram
* google plus
* pinterest
* vimeo
* skype
* wordpress
* medium
* youtube
* stackoverflow
* bitbucket
 
Feel free to add any social media site you would like to find here!
