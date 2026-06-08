import pandas as pd
from pathlib import Path
import unicodedata
import re

INPUT_PATH = Path("data/raw/worlds_biggest_breaches_cleaned.csv")
OUTPUT_PATH = Path("data/processed/worlds_biggest_breaches_fixed.csv")
REPORT_PATH = Path("data/processed/mojibake_report.txt")

# ---------------------------------------------------------
# Common mojibake patterns (UTF-8 mis-decoded as Latin-1)
# ---------------------------------------------------------
MOJIBAKE_PATTERNS = [
    "Ã©", "Ã¨", "Ãª", "Ã«",
    "Ã¡", "Ã ", "Ã¢", "Ã£",
    "Ã³", "Ã²", "Ã´", "Ãµ",
    "Ãº", "Ã¹", "Ã»",
    "Ã§", "Ã±",
    "â€“", "â€”", "â€", "â€™", "â€œ", "â€"
]

def looks_mojibake(s: str) -> bool:
    if pd.isna(s):
        return False
    return any(p in s for p in MOJIBAKE_PATTERNS)

# ---------------------------------------------------------
# Try multiple decoding strategies
# ---------------------------------------------------------
def try_fix(s: str) -> str:
    if pd.isna(s):
        return s

    original = s

    # Strategy 1: latin1 → utf8
    try:
        s1 = s.encode("latin1").decode("utf8")
        if not looks_mojibake(s1):
            return s1
    except:
        pass

    # Strategy 2: cp1252 → utf8
    try:
        s2 = s.encode("cp1252").decode("utf8")
        if not looks_mojibake(s2):
            return s2
    except:
        pass

    # Strategy 3: utf8 → latin1 (rare but possible)
    try:
        s3 = s.encode("utf8").decode("latin1")
        if not looks_mojibake(s3):
            return s3
    except:
        pass

    # Strategy 4: unicode normalize
    s4 = unicodedata.normalize("NFKC", s)
    if not looks_mojibake(s4):
        return s4

    # If all fail, return original
    return original

# ---------------------------------------------------------
# Main scanning + fixing
# ---------------------------------------------------------
def main():
    df = pd.read_csv(INPUT_PATH)

    if "organisation" not in df.columns:
        raise KeyError("Dataset must contain 'organisation' column.")

    fixed = []
    report_lines = []

    for idx, s in df["organisation"].items():
        if looks_mojibake(s):
            fixed_s = try_fix(s)
            fixed.append(fixed_s)

            if fixed_s != s:
                report_lines.append(f"[FIXED] {s}  →  {fixed_s}")
            else:
                report_lines.append(f"[UNRESOLVED] {s}")
        else:
            fixed.append(s)

    df["organisation_fixed"] = fixed

    # Save fixed CSV
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    # Save report
    with open(REPORT_PATH, "w", encoding="utf8") as f:
        f.write("\n".join(report_lines))

    print(f"Scan complete.")
    print(f"Fixed file saved to: {OUTPUT_PATH}")
    print(f"Report saved to: {REPORT_PATH}")

if __name__ == "__main__":
    main()
