import requests
from newspaper import Article
from gtts import gTTS
from feedgen.feed import FeedGenerator
import os
import datetime



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
    fe.pubdate(pub_date)

    return fg.rss_str(pretty=True)

def main():
    article_url = "https://example.com/article"
    audio_file = "output.mp3"
    podcast_title = "My Podcast Title"
    podcast_description = "Description of my podcast."
    rss_file = "podcast.rss"

    # Step 1: Extract article content
    article_content = extract_article_content(article_url)

    # Step 2: Convert text to audio
    text_to_audio(article_content, audio_file)

    # Step 3: Generate RSS feed
    current_datetime = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    rss_content = create_rss_feed(podcast_title, article_url, podcast_description, audio_file, current_datetime)

    # Step 4: Save the RSS feed to a file
    with open(rss_file, "w", encoding="utf-8") as f:
        f.write(rss_content)

    print("Podcast generated successfully!")

if __name__ == "__main__":
    main()
