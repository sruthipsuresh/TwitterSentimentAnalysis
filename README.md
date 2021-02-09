# TwitterSentimentAnalysis
Practice of Twitter Data Scraping using Twint and NLP Analysis

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
