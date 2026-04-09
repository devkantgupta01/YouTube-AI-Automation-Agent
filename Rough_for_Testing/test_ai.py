from tools.generate_content import generate_video_content

# but your script name haere-------------------------------------------------------------------
with open("downloads/Testing Video for Youtube-Ai-Agent.txt", "r", encoding="utf-8") as f: 
    script = f.read()

result = generate_video_content(script)

print("\nGenerated Metadata:\n")

print("Title:", result["title"])
# print("\nDescription:", result["description"])
print("Hashtags:", result["hashtags"])
print("Tags:", result["tags"])
print("Category:", result["category"])