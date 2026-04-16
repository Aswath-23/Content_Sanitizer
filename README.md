# Social Media Content Sanitizer

A simple Python script that scans school social media posts, masks banned words with `***`, extracts URLs, and produces a moderator report.

## Requirements satisfied

- List processing using a list of sample posts.
- Word masking with `banned_words = ["bad", "toxic", "hate"]` and `.replace()`.
- Link extraction using `startswith('http')`.
- Summary dictionary that counts moderator flags per user.
- Final report with total posts screened, cleaned posts, and blocked posts.

## Files

- `content_sanitizer.py`: main script
- `sample_posts.txt`: sample posts input
- `links_found.txt`: generated output with found links

## Run

Open a terminal in this folder and run:

```bash
python content_sanitizer.py
```

The script writes links to `links_found.txt` and prints a final report.
