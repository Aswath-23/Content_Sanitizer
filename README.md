# Social Media Content Sanitizer
---

## Objective

* Detects and masks **banned words**
* Extracts **web links** for security checking
* Tracks **user violations**
* Generates a **final moderation report**

---

## Features

### 🔹 Word Filtering

* Replaces banned words like `bad`, `toxic`, `hate` with `***`

### 🔹 Link Extraction

* Detects all URLs (http/https) from posts
* Saves them into a file for review

### 🔹 User Monitoring

* Tracks how many times each user posts flagged content

### 🔹 Report Generation

* Displays:

  * Total posts screened
  * Cleaned posts count
  * Flagged posts count
  * User-wise violations

---

## Technologies Used

* Python 
* Regular Expressions (`re` module)
* File Handling

---

## Output

###  Cleaned Posts

```
User123: I *** this app! Visit http://badsite.com
User123: You are ***! Check https://spamlink.com now
```

###  Extracted Links (`links_found.txt`)

```
http://badsite.com
https://spamlink.com
```

###  Final Report

```
Total Posts Screened: 5
Cleaned Posts: 4
Blocked/Flagged Posts: 4
```
---

## Run the program:

```
python main.py
```
