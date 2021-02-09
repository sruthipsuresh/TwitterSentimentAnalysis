# Twitter Sentiment Analysis
Practice of Twitter Data Scraping using Twint and NLP Analysis.
Inspired by https://towardsdatascience.com/understanding-political-twitter-ce3476a38377, generated individual wordclouds for AOC, Pete Pete Buttigieg, Ted Cruz and Ben Shapiro in images folder.

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
