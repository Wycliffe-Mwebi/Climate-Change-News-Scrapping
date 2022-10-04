# Scraping IMDB Top rated Movies
IMDb (an acronym for Internet Movie Database) is an online database of information related to films, television programs, home videos, video games, and streaming content online — including cast, production crew, and personal biographies, plot summaries, trivia, ratings, and fan, and critical reviews.


1. Download the webpage using requests
2. Parse the HTML source code using beautiful Soup
3. Extract topic names, descriptions, and URLs from page
4. Compile the data and create a CSV file using Pandas

Site: https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=1&ref_=adv_prv
</Br>
Here we will scrap all the top 1000 top rated movies resides across multiple pages.
