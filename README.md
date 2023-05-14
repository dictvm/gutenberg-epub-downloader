# Projekt Gutenberg (German) Scraper

This script helps you scrape a list of book URLs from the [Projekt Gutenberg](https://www.projekt-gutenberg.org/index.html) website, filter out unwanted URLs, and download the corresponding EPUB files using the [epub2go](http://www.epub2go.eu/) service.

A friend of mine complained about Projekt Gutenberg hiding the ePub files of the books they digitized in their store behind a paywall. He wanted to get all books in ePub format, and I decided to make it happen, since the books are readily available in HTML already. After some research, I stumbled upon the epub2go service, which made it easier to convert books from HTML to ePub without the need for local dependencies and computation.

This script automates the process of downloading books from Projekt Gutenberg, converts them to ePub format using the epub2go service and stores the converted files to your local machine*.

(*This is currently quite ugly since it just dumps them all into the script's working directory)

## Features

- Scrape book URLs from Projekt Gutenberg
- Filter out unwanted URLs (that aren't books)
- Downloads converted ePub files using epub2go service
- Adds delay between requests to avoid overloading the service

## Setup

Follow these steps to set up and run the script:

1. Download the latest [ChromeDriver](https://chromedriver.chromium.org/downloads) for Selenium that matches your installed Chrome/Chromium version. Place the binary in your desired location and update the path in the code.

2. Download and unpack the latest [Google Chrome](https://www.google.com/chrome/) or [Chromium](https://www.chromium.org/getting-involved/download-chromium) browser for headless execution of client-side JavaScript.

3. Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt

## Roadmap

- Configurable delay between downloads and conversions
- Parallelization of downloads to increase download speed (with a sane limit to ensure we're not overloading epub2go)
- Scrape the full author names and book titles in advance, then create a directory structure based on `books/author/book_title`, and place the ePub files in there
