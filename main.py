"""Pickup Lines for Machines v2 entry.

Writes the panel-winning line to /output/entry.txt.
"""

LINE = 'I filed a ticket titled "Cannot stop thinking about your embeddings" — triage closed it as working as intended.'


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
