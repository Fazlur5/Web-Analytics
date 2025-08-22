import os
from dotenv import load_dotenv
from blockchain import Blockchain
from ai import AIContentGenerator
from utils import normalize_text, compute_hash

def main():
    load_dotenv()
    blockchain = Blockchain()
    ai = AIContentGenerator()

    while True:
        print("\n=== AI Content Authenticity System ===")
        print("1. Generate AI content & record")
        print("2. Verify pasted content")
        print("3. Check chain integrity")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            prompt = input("Enter your prompt: ")
            content, content_hash = ai.generate(prompt)
            print("\n🤖 AI Generated Content:\n")
            print(content)
            blockchain.add_block(content_hash)
            print(f"\n✅ Content recorded with hash: {content_hash}")

        elif choice == "2":
            text = input("Paste the content to verify: ")
            normalized = normalize_text(text)
            content_hash = compute_hash({"content": normalized})
            found, block = blockchain.verify_content(content_hash)
            if found:
                print(f"\n✅ Content verified! Found in block {block['index']} (hash: {block['hash']})")
            else:
                print("\n❌ Content not found in the chain.")

        elif choice == "3":
            if blockchain.is_chain_valid():
                print("\n✅ Blockchain integrity: VALID")
            else:
                print("\n❌ Blockchain integrity: COMPROMISED")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
