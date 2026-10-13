from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from collections import Counter
import re


def home(request):
    # 1. Fetch and parse the page
    # url = "https://signaturemedispa.com"  # Change this to your target site
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, "html.parser")
    #
    # # 2. Extract clean, human-readable text from the webpage body
    # # This strips away scripts, CSS styling, and hidden code elements
    # raw_text = soup.get_text().lower()
    #
    # # 3. Clean the text and tokenize it into individual clean words
    # # This regular expression keeps only letters and filters out numbers/punctuation
    # # [a-z](Letters Only)
    # # {3,} (Minimum Word Length) filler words like "on", "in", "at"
    # # \b (Word Boundaries) (like a space, a new line, or a punctuation mark).
    # words = re.findall(r"\b[a-z]{3,}\b", raw_text)
    # print(words)

    # 1. Fetch and parse the page
    url = "https://signaturemedispa.com/"  # Change this to your target site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 2. Extract clean, human-readable text from the webpage body
    # This strips away scripts, CSS styling, and hidden code elements
    raw_text = soup.get_text().lower()

    # 3. Clean the text and tokenize it into individual clean words
    # This regular expression keeps only letters and filters out numbers/punctuation
    words = re.findall(r"\b[a-z]{3,}\b", raw_text)

    # --- THE COMBINATION ENGINE ---

    def get_phrase_combinations(word_list, phrase_length):
        """Slices a list of words into overlapping multi-word phrase combinations."""
        phrases = []
        # Loop through the words to pair up neighboring words
        for i in range(len(word_list) - phrase_length + 1):
            # Join words together based on the desired length (e.g., 2 or 3 words)
            phrase = " ".join(word_list[i: i + phrase_length])
            phrases.append(phrase)
        return phrases

    # 4. Generate 2-word and 3-word phrase combinations
    two_word_phrases = get_phrase_combinations(words, 2)
    three_word_phrases = get_phrase_combinations(words, 3)
    four_word_phrases = get_phrase_combinations(words, 4)

    # 5. Count frequencies using Python's Counter tool
    top_2_word_keywords = Counter(two_word_phrases).most_common(10)
    top_3_word_keywords = Counter(three_word_phrases).most_common(10)
    top_4_word_keywords = Counter(four_word_phrases).most_common(10)

    # --- DISPLAY RESULTS ---
    print("=== TOP 10 TWO-WORD COMBINATIONS ===")
    for phrase, count in top_2_word_keywords:
        print(f"[{count}x] {phrase}")

    print("\n=== TOP 10 THREE-WORD COMBINATIONS ===")
    for phrase, count in top_3_word_keywords:
        print(f"[{count}x] {phrase}")

    print("\n=== TOP 10 FOUR-WORD COMBINATIONS ===")
    for phrase, count in top_4_word_keywords:
        print(f"[{count}x] {phrase}")

    print(f"words len: {len(words)} {len(words) * 0.02}")

    # competitor_url = "https://signaturemedispa.com/"
    # response = requests.get(competitor_url)
    # soup = BeautifulSoup(response.text, "html.parser")
    #
    # page_title = soup.title.string if soup.title else "No Title"
    #
    # # 2. Get the Meta Description (The blurb shown on Google search results)
    # meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    # meta_description = meta_desc_tag.get("content") if meta_desc_tag else "No Description"
    #
    # # 3. Get all H1 Headings (Main topics on the page)
    # h1_headings = [h1.text.strip() for h1 in soup.find_all("h1")]
    #
    # print(f"SEO Title: {page_title}")
    # print(f"SEO Meta Description: {meta_description}")
    # print(f"Primary Headings: {h1_headings}")
    #
    # # Get all the visible human text from the page body
    # raw_text = soup.get_text().lower()
    #
    # # Use a regular expression to extract words, ignoring numbers/punctuation
    # all_words = re.findall(r'\b[a-z]{4,}\b', raw_text)  # filters for words 4+ letters long
    #
    # # Count the most common words used on the page
    # word_counts = Counter(all_words)
    # print("Most frequent words (Potential SEO focus words):")
    # print(word_counts.most_common(10))

    # links = soup.find_all("a")
    # json_array = []
    # for link in links:
    #     url_destination = link.get("href")
    #     link_text = link.text.strip()
    #     json = {
    #         "url_destination": url_destination,
    #         "link_text": link_text,
    #     }
    #     json_array.append(json)
    #
    # print(json_array)

    # For a 4,000-word authority guide, seasoned developers and
    # SEO engineers drop the primary keyword density closer to 0.5% to 1%
    # (about 20 to 40 times total).

    # To fill up the rest of your relevance profile naturally, you use the concept
    # of Semantic Clustering (using variations and synonyms):

    # Primary Phrase (20–40x): "Skin rejuvenation treatment"
    # Secondary Variation A (15x): "Anti-aging procedures"
    # Secondary Variation B (15x): "Collagen stimulation secrets"
    # Secondary Variation C (10x): "Dermal tightening tech"

    return render(request,"main/index.html", {
        "name": "genesis"
    })
