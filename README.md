# Twitter Sentiment Analysis
Created by @sruthipsuresh
Practice of Twitter Data Scraping using Twint and NLP Analysis.
Inspired by this [article](https://towardsdatascience.com/understanding-political-twitter-ce3476a38377), generated individual wordclouds for AOC, Pete Pete Buttigieg, Ted Cruz and Ben Shapiro in images folder. Also made subjectivity/polarity analysis and plotted in seaborn scatterplot.

### Examples of Images Generated
![overall](https://github.com/sruthipsuresh/TwitterSentimentAnalysis/blob/main/images/aoc.png?raw=true)
See the wordcloud generated for AOC from her Tweets so far in 2021!

![overall](https://github.com/sruthipsuresh/TwitterSentimentAnalysis/blob/main/images/buttigieg.png?raw=true)
See the wordcloud generated for Pete Buttigieg from his Tweets so far in 2021!

![overall](https://github.com/sruthipsuresh/TwitterSentimentAnalysis/blob/main/images/polvssub.png?raw=true)
See the polarity vs. subjectivity scatterplot of all the users listed above!


## Documentation:
### Data Collection:
* Install dependencies in script.sh.
* Generate .csv files with tweets from usernames, TODO: configure userlist in modules
* Concatenate all .csv files in one (first strip header with sed 1d, then run cat command)

### Data Cleaning
* Used Google Colab and referenced various articles to clean data.
* Subsetted to username, tweet text.
* Removed all Twitter characters/links from Tweet.
* Data cleaning for NLP analysis.
* Store cleaned data in clean.csv

### Wordcloud Generation
* Followed tutorial on datacamp.
* Generated countplot.
* Generated test wordcloud using only one tweet.
* Combined all tweets in merged dataset for overall wordcloud.
* Combine all tweets by username and generate separate wordclouds.
* Save in images folder.

### Working with Textblob
* Use dataset which is only processed to remove Twitter tags.
* Add polarity and subjectivity columns with Textblob, saved .csv
* Simple plot with username used as hue.

