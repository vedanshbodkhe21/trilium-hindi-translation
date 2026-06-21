import json
import os


def flatten(d, parent_key="", sep="."):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def check_translation_status(folder):
    en_path = f"{folder}/trilium-{folder}-en.json"
    hi_path = f"{folder}/trilium-{folder}-hi.json"

    if not os.path.exists(en_path):
        return None

    with open(en_path, "r", encoding="utf-8") as f:
        en = flatten(json.load(f))

    hi = {}
    if os.path.exists(hi_path):
        with open(hi_path, "r", encoding="utf-8") as f:
            hi = flatten(json.load(f))

    total_keys = len(en)
    translated_keys = 0
    missing_keys = 0

    for k, v in en.items():
        hi_val = hi.get(k, "")
        if hi_val and str(hi_val).strip() != "":
            translated_keys += 1
        else:
            missing_keys += 1

    pct_translated = (translated_keys / total_keys) * 100 if total_keys > 0 else 100.0
    pct_remaining = (missing_keys / total_keys) * 100 if total_keys > 0 else 0.0

    return {
        "total": total_keys,
        "translated": translated_keys,
        "remaining": missing_keys,
        "pct_translated": pct_translated,
        "pct_remaining": pct_remaining,
    }


def main():
    folders = ["client", "server", "website", "readme"]

    print("=" * 72)
    print(
        f"{'Folder':<12} | {'Total Keys':<10} | {'Translated':<10} | {'Remaining':<10} | {'% Remaining':<12}"
    )
    print("-" * 72)

    grand_total = 0
    grand_translated = 0
    grand_remaining = 0

    for folder in folders:
        stats = check_translation_status(folder)
        if stats:
            grand_total += stats["total"]
            grand_translated += stats["translated"]
            grand_remaining += stats["remaining"]

            print(
                f"{folder:<12} | {stats['total']:<10} | {stats['translated']:<10} | {stats['remaining']:<10} | {stats['pct_remaining']:>10.2f}%"
            )
        else:
            print(
                f"{folder:<12} | {'Not found':<10} | {'-':<10} | {'-':<10} | {'-':<12}"
            )

    print("-" * 72)

    if grand_total > 0:
        total_pct_remaining = (grand_remaining / grand_total) * 100
        print(
            f"{'TOTAL':<12} | {grand_total:<10} | {grand_translated:<10} | {grand_remaining:<10} | {total_pct_remaining:>10.2f}%"
        )
    else:
        print(f"{'TOTAL':<12} | {'0':<10} | {'0':<10} | {'0':<10} | {'0.00%':>12}")

    print("=" * 72)


if __name__ == "__main__":
    main()
