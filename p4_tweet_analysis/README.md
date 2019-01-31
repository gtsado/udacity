## Overview

The dataset that I wrangle in this project (and analyze and visualize) is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. 

WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators, though? Almost always greater than 10. 11/10, 12/10, 13/10, etc. Why? Because "they're good dogs Brent." 

WeRateDogs has over 4 million followers and has received international media coverage.

WeRateDogs downloaded their Twitter archive and sent it to Udacity via email exclusively for you to use in this project. This archive contains basic tweet data (tweet ID, timestamp, text, etc.) for all 5000+ of their tweets as they stood on August 1, 2017.

### Data Used

#### Twitter Archive
  * The WeRateDogs Twitter archive contains basic tweet data for all 5000+ of their tweets, but not everything. 
    One column the archive does contain though: each tweet's text, which was used to extract rating, dog name, and dog "stage" (i.e. doggo, floofer, pupper, and puppo) 
    to make this Twitter archive "enhanced."

#### Additional Data via the Twitter API

  * Back to the basic-ness of Twitter archives: retweet count and favorite count are two of the notable column omissions. 
    This additional data was gathered by querying from Twitter's API using the tweet ids in the twitter archive.

#### Project Parameters
Key points to keep in mind when data wrangling for this project:

1. We only want original ratings (no retweets) that have images. Though there are 5000+ tweets in the dataset, not all are dog ratings and some are retweets.

2. The requirements of this project are only to assess and clean at least 8 quality issues and at least 2 tidiness issues in this dataset.
    * Cleaning includes merging individual pieces of data according to the rules of tidy data.

3. The fact that the rating numerators are greater than the denominators does not need to be cleaned. This unique rating system is a big part of the popularity of WeRateDogs.

4. You do not need to gather the tweets beyond August 1st, 2017. You can, but note that you won't be able to gather the image predictions for these tweets since you don't have access to the algorithm used.


![image](https://user-images.githubusercontent.com/47091273/52027045-ff38ec80-24d7-11e9-95d3-e884b8b20bf4.png)
