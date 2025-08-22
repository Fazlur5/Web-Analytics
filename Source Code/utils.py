import hashlib
import json

def normalize_text(text: str) -> str:
    """Normalize text by stripping and lowercasing for consistent hashing."""
    return text.strip().lower()

def compute_hash(data: dict) -> str:
    """Compute SHA256 hash of a dictionary."""
    data_string = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(data_string).hexdigest()
