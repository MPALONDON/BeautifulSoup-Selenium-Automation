# BeautifulSoup & Selenium Book Automation

This Python project scrapes book data from [Books to Scrape](https://books.toscrape.com/) and automatically submits it into a Google Form. It also includes optional data analytics for visualizing the scraped data.

---

## Features

- Scrapes book information from multiple pages:
  - Title
  - URL
  - Price
  - Rating
  - Stock availability
- Automatically submits the data to a Google Form
- Optional analytics using **Matplotlib** to visualize average price by rating
- Users can use **their own Google Form** with 5 text input fields:
  1. Book Title
  2. Book URL
  3. Book Price
  4. Book Rating
  5. Book Stock

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MPALONDON/BeautifulSoup-Selenium-Automation.git
```

### 2. Navigate to your project folder

```bash
cd <your-project-folder>
```

### 3. Install dependencies

It’s recommended to use a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux
pip install -r requirements.txt
```

---

### 4. Set up your Google Form (Optional)

If you want to use your own Google Form:

1. Create a Google Form with **5 text inputs** in this order:
   - Book Title
   - Book URL
   - Book Price
   - Book Rating
   - Book Stock
2. Copy the form URL.
3. Create a `.env` file in the project root with:

```
GOOGLE_FORM_URL="YOUR_GOOGLE_FORM_URL_HERE"
```

If `.env` is not provided, the program will use the default form URL.

---

### 5. Run the program

```bash
python main.py
```

- The program will ask how many pages to scrape.
- It will scrape the data from the specified number of pages and submit it to your Google Form.
- Optional analytics will be displayed automatically before submission.

---

## Analytics

The program creates a simple bar chart showing **average book price by rating** using Matplotlib. This allows you to quickly visualize trends in the scraped data.

---

## Notes

- Currently uses `time.sleep()` to wait for pages to load; WebDriverWait is not implemented.
- Make sure your Google Form is open to accept responses.
- Only works for **Books to Scrape** structure.

---


