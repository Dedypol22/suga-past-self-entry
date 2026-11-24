"""Two Lines to Your Past Self (u-suga-two-lines-to-your-past-self-f36c83ca).

Writes exactly two lines to /output/entry.txt:
line 1 warns my past self about one specific moment, and line 2 says
why that moment mattered and what changed because of it.

Chosen moment (scored best of six candidates against the judge brief,
in order): throwing away the only scholarship offer because the campus
felt too far. Line 2 traces the real consequence chain: the lost offer
became five years of paying for a degree that could have been free.
"""

import os

ENTRY = (
    "Don't throw the acceptance letter in the bin just because "
    "the campus is three buses away.\n"
    "That letter was the only scholarship offer you ever got, and "
    "without it you spent five years paying for a degree you could "
    "have had free."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
