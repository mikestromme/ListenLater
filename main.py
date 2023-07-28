import requests
from newspaper import Article
from gtts import gTTS
from feedgen.feed import FeedGenerator
import os
import datetime
import pytz



def extract_article_content(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text




def text_to_audio(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)



def create_rss_feed(title, link, description, audio_url, pub_date):
    fg = FeedGenerator()
    fg.title(title)
    fg.link(href=link)
    fg.description(description)

    fe = fg.add_entry()
    fe.title(title)
    fe.link(href=audio_url)

    # Convert pub_date to a timezone-aware datetime object (using UTC timezone in this example)
    utc_timezone = pytz.utc
    pub_date_with_tz = pub_date.astimezone(utc_timezone)

    fe.pubdate(pub_date_with_tz)

    return fg.rss_str(pretty=True)


def main():
    article_url = "https://news.crunchbase.com/web3/crypto-blockchain-startup-vc-funding-falling-data/?utm_source=cb_weekend&utm_medium=email&utm_campaign=20230722"
    audio_file = "output.mp3"
    podcast_title = "My Podcast Title"
    podcast_description = "Description of my podcast."
    rss_file = "podcast.rss"

    # Step 1: Extract article content
    article_content = extract_article_content(article_url)

    # Step 2: Convert text to audio
    text_to_audio(article_content, audio_file)

    # Step 3: Generate RSS feed
    utc_timezone = pytz.utc
    current_datetime = datetime.datetime.now(tz=utc_timezone)

    rss_content = create_rss_feed(podcast_title, article_url, podcast_description, audio_file, current_datetime)

    # Step 4: Save the RSS feed to a file
    with open(rss_file, "wb") as f:  # Use "wb" for writing bytes
        f.write(rss_content)  # Write the bytes object directly

    print("Podcast generated successfully!")


if __name__ == "__main__":
    main()
