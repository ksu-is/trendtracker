# TrendTracker Project

# Step 1: Welcome message
print("Welcome to TrendTracker")

# Step 2: Ask user what they want to search
user_input = input("What trends are you looking for? (example: Eurotrip outfits) ")

# Step 3: Simulated trending topics
trending_topics = ["summer outfits", "streetwear", "minimal style", "travel looks"]

# Step 4: Show results
print("\nSearching trends for:", user_input)
print("Here are some trending ideas:")

for topic in trending_topics:
    print("-", topic)

# Step 5: Show total
print("\nTotal trends found:", len(trending_topics))
