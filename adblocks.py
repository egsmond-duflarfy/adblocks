import requests


def get_urls():
    """Pull urls"""
    path = "https://raw.githubusercontent.com/egsmond-duflarfy/ad_blocks/refs/heads/main/master.txt"
    response = requests.get(path, timeout=30)

    if response.status_code != 200:
        print("Failed to fetch URLs")
        return []

    urls = list(set(response.text.splitlines()))
    print(f"urls: {len(urls):,}")
    return urls


def add_urls(urls, urls_to_add="add.txt"):
    """Add urls and write updated master.txt"""

    def ad_syntax(s):
        return f"||{s}^"

    with open(urls_to_add, "r", encoding="utf-8") as f:
        raw = {line.strip() for line in f if line.strip()}

    formatted = {ad_syntax(url) for url in raw}
    new_urls = formatted - set(urls)

    if not new_urls:
        print("No new urls to add")
        return

    updated_urls = urls + list(new_urls)

    print(f"Total urls: {len(updated_urls):,}\n")
    print("Adding:")
    for url in new_urls:
        print(url)

    with open("master.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(updated_urls))
