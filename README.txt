# Projekt Gutenberg Scraper

This script helps you scrape a list of book URLs from the [Projekt Gutenberg](https://www.projekt-gutenberg.org/index.html) website, filter out unwanted URLs, and download the corresponding EPUB files using the [epub2go](http://www.epub2go.eu/) service.

## Features

- Scrapes book URLs from Projekt Gutenberg
- Filters out unwanted URLs
- Downloads EPUB files using epub2go service
- Adds delay between requests to avoid overloading the service
- Compatible with Python 3.x and Linux environments

## Setup

Follow these steps to set up and run the script:

1. Download the latest [ChromeDriver](https://chromedriver.chromium.org/downloads) that matches your installed Chrome/Chromium version. Place the binary in your desired location and update the path in the code.

2. Download and unpack the latest [Google Chrome](https://www.google.com/chrome/) or [Chromium](https://www.chromium.org/getting-involved/download-chromium) browser for headless execution of client-side JavaScript.

3. Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt

## Roadmap

- Configurable delay between downloads and conversions
- Parallelization of downloads to increase download speed (with a sane limit to ensure we're not overloading epub2go)
- Scrape the full author names and book titles in advance, then create a directory structure based on `books/author/book_title`, and place the EPUB files in there
