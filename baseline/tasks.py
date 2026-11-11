"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""


def count_selected(media_ids: list[str]) -> int:
    return len(media_ids)

def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    result = {}
    for item in media:
        gallery_id = item.get("gallery_id")
        media_id = item.get("id")
        if gallery_id not in result:
            result[gallery_id] = []
        result[gallery_id].append(media_id)
    return result


def total_price(prices_minor: list[int | None]) -> int:
    total = 0
    for price in prices_minor:
        if price is not None:
            total += price
    return total


def first_missing(required: list[str], present: list[str]) -> str | None:
    for i in required:
        if i not in present:
            return i
    return None


import json

def load_events(path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)