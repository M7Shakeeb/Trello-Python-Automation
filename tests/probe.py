import os
import sys

# Read variables directly from the OS (Docker Environment)
key = os.environ.get("TRELLO_KEY")
token = os.environ.get("TRELLO_TOKEN")

print("-" * 30)
print("🔍 DIAGNOSTIC PROBE STARTED")

if not key:
    print("❌ TRELLO_KEY is Missing/None")
    sys.exit(1) # Fail the pipeline
elif key == "$TRELLO_KEY":
    print("❌ TRELLO_KEY is literal string '$TRELLO_KEY' (Injection Failed)")
    sys.exit(1)
else:
    # Print only first 4 chars to prove we have the real value securely
    print(f"✅ TRELLO_KEY found! Starts with: {key[:4]}...")

if not token:
    print("❌ TRELLO_TOKEN is Missing/None")
    sys.exit(1)
else:
    print(f"✅ TRELLO_TOKEN found! Starts with: {token[:4]}...")

print("-" * 30)