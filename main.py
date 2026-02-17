from adblocks import get_urls, add_urls


def main():
    print("Hello from adblocks!\n")

    urls = get_urls()
    add_urls(urls, urls_to_add="add.txt")


if __name__ == "__main__":
    main()
