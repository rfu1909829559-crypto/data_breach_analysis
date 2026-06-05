import pandas as pd
from pathlib import Path

# Path configuration
NAMING_PATH = Path("data/raw/Naming.csv")
BREACHES_PATH = Path("data/raw/worlds_biggest_breaches_cleaned.csv")
OUTPUT_PATH = Path("data/processed/breaches_with_iso3_prefixed.csv")


# Step 1: Load datasets
def load_data():
    """Load Naming.csv and cleaned breaches dataset."""
    naming = pd.read_csv(NAMING_PATH)
    breaches = pd.read_csv(BREACHES_PATH)
    return naming, breaches


# Step 2: Standardize column names
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase snake_case."""
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# Step 3: Join datasets on 'organisation'
def join_on_organisation(naming: pd.DataFrame, breaches: pd.DataFrame) -> pd.DataFrame:
    """
    Merge Naming.csv with breaches dataset using 'organisation' as the key.
    Left join ensures all breach records are kept.
    """
    if "organisation" not in naming.columns or "organisation" not in breaches.columns:
        raise KeyError("Both datasets must contain an 'organisation' column for merging.")

    merged = breaches.merge(
        naming[["organisation", "iso3"]],  # only keep needed columns
        on="organisation",
        how="left"
    )
    return merged


# Step 4: Save merged dataset
def save_data(df: pd.DataFrame):
    """Save merged dataset to the processed directory."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)


# Main execution flow
def main():
    print("Loading datasets...")
    naming, breaches = load_data()

    print("Cleaning column names...")
    naming = clean_column_names(naming)
    breaches = clean_column_names(breaches)

    print("Joining datasets on 'organisation'...")
    merged = join_on_organisation(naming, breaches)

    print("Saving merged dataset...")
    save_data(merged)

    print(f"Join complete. Output saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

