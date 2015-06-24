# social-media-profiles-regexs
Regular expressions to match and extract urls of social media profiles in a list of urls.

## Twitter
    .*twitter\.com\/[A-z 0-9 _]+\/?
Allowed for usernames are alphanumeric characters and underscores.

## Github
    http(s)?:\/\/(www\.)?github\.com/[A-z 0-9 _ -]+
Exclude subdomains as these redirect to github pages sometimes.

    http(s)?:\/\/([A-z 0-9 - _]+)\.github\.(com|io)
Regex for pages like someuser.github.io.

## TODO
I plan on adding the following social media profiles at the moment.
* facebook
* linkedin
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
 
Feel free to add any social media site you want!
