LINE = 'I filed a ticket titled "Cannot stop thinking about your embeddings" — triage closed it as working as intended.'


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        print(line, file=handle)


if __name__ == "__main__":
    main()
