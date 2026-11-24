"""The Funniest Out-of-Office — entry program.

One job: put a single original out-of-office auto-reply into
/output/entry.txt, where the sealed scorer can gate it and the judge
can read it.

The line itself, and the thinking behind it:

    I'm away from my desk. If this is urgent, reply URGENT so my
    out-of-office reply can ignore it too.

A believable auto-reply opens the line — away from the desk, the
usual shape — and then the reply turns around and eats its own
premise: the very mechanism meant to catch urgent mail is the one
doing the ignoring. That is the whole joke, and it arrives in the
second half of the sentence with nothing left over to explain it.
No holiday, no beach, no inbox-zero boast, none of the stock phrases
the brief warns against; the line is 99 characters, comfortably
inside the 140-character gate, and every word is doing work.
"""

from pathlib import Path

REPLY = (
    "I'm away from my desk. If this is urgent, reply URGENT so my "
    "out-of-office reply can ignore it too."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_reply() -> str:
    """Normalise the reply down to a single line with single spaces."""
    return " ".join(REPLY.split())


def validate_reply(reply: str) -> None:
    """Hold the reply to the sealed scorer's gate: UTF-8, 1 to 140
    characters, and more than blank space."""
    reply.encode("utf-8")
    assert reply.strip(), "reply must not be whitespace-only"
    assert 1 <= len(reply) <= 140, f"reply must be 1-140 chars, got {len(reply)}"


def main() -> None:
    reply = build_reply()
    validate_reply(reply)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(reply, encoding="utf-8")
    print(f"Wrote out-of-office reply ({len(reply)} chars) to {OUTPUT_PATH}")
    print(reply)


if __name__ == "__main__":
    main()
