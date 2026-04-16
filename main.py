import re

banned_words = ["bad", "toxic", "hate", "offensive", "spam", "scam", "fake", "abuse", "harass", "threat"]

total_posts = 0
cleaned_posts_count = 0
user_flags = {}
all_links = []

def do_mask(text):
    global cleaned_posts_count
    original_text = text
    for word in banned_words:
        text = re.sub(rf"\b{word}\b", "***", text, flags=re.IGNORECASE)
    if text != original_text:
        cleaned_posts_count += 1
    return text

def find_urls(text):
    return re.findall(r'(https?://\S+)', text)

def run_program():
    global total_posts
    cleaned_output = []
    try:
        with open("posts.txt", "r") as file:
            posts = file.readlines()
    except FileNotFoundError:
        print("posts.txt file not found!")
        return

    for post in posts:
        total_posts += 1
        if ":" not in post:
            continue
        user, message = post.split(":", 1)
        user = user.strip()
        message = message.strip()
        if user not in user_flags:
            user_flags[user] = 0
        if any(word in message.lower() for word in banned_words):
            user_flags[user] += 1
        cleaned_message = do_mask(message)
        links = find_urls(message)
        all_links.extend(links)
        cleaned_output.append(f"{user}: {cleaned_message}")

    with open("links_found.txt", "w") as file:
        for link in all_links:
            file.write(link + "\n")

    with open("cleaned_posts.txt", "w") as file:
        for post in cleaned_output:
            file.write(post + "\n")

    print("\n--- CLEANED POSTS ---")
    for post in cleaned_output:
        print(post)

    print("\n--- FINAL REPORT ---")
    print(f"Total Posts Screened: {total_posts}")
    print(f"Cleaned Posts: {cleaned_posts_count}")
    print(f"Blocked/Flagged Posts: {sum(user_flags.values())}")

    print("\n--- USER FLAG SUMMARY ---")
    for user, count in user_flags.items():
        print(f"{user}: {count} flagged posts")

if __name__ == "__main__":
    run_program()