import json
import os
from datetime import datetime
from utils import compute_hash

CHAIN_FILE = "chain.json"

class Blockchain:
    def __init__(self):
        self.chain = []
        self.load_chain()

    def create_genesis_block(self):
        """Creates the first block of the blockchain."""
        genesis_block = {
            "index": 0,
            "timestamp": str(datetime.utcnow()),
            "content_hash": "0",
            "previous_hash": "0",
        }
        genesis_block["hash"] = compute_hash(genesis_block)
        self.chain.append(genesis_block)
        self.save_chain()

    def load_chain(self):
        if os.path.exists(CHAIN_FILE):
            with open(CHAIN_FILE, "r") as f:
                self.chain = json.load(f)
        if not self.chain:
            self.create_genesis_block()

    def save_chain(self):
        with open(CHAIN_FILE, "w") as f:
            json.dump(self.chain, f, indent=4)

    def add_block(self, content_hash: str):
        last_block = self.chain[-1]
        block = {
            "index": len(self.chain),
            "timestamp": str(datetime.utcnow()),
            "content_hash": content_hash,
            "previous_hash": last_block["hash"],
        }
        block["hash"] = compute_hash(block)
        self.chain.append(block)
        self.save_chain()
        return block

    def verify_content(self, content_hash: str):
        """Check if a given content hash exists in the chain."""
        for block in self.chain:
            if block["content_hash"] == content_hash:
                return True, block
        return False, None

    def is_chain_valid(self):
        """Check integrity of the chain."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            if current["previous_hash"] != prev["hash"]:
                return False

            if compute_hash({k: v for k, v in current.items() if k != "hash"}) != current["hash"]:
                return False
        return True
