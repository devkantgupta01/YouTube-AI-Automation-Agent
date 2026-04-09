from openai import OpenAI
import json
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_video_content(script_text):

    prompt = f"""
You are a YouTube SEO expert.

Based on the following video script, generate optimized YouTube metadata.

Return ONLY valid JSON.

Required format:



{{
"title": "...",

"hashtags": ["#tag1","#tag2","#tag3"],
"tags": ["keyword1","keyword2","keyword3"],
"category": "Education / Entertainment / Technology / etc",
}}

Rules:
- Title must be catchy and SEO optimized

- Include trending hashtags
- Tags must maximize discoverability
- Category must be appropriate
- No extra explanation
- Only JSON

SCRIPT:
{script_text}
"""
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    result = response.choices[0].message.content

    # print("\nRAW AI RESPONSE:\n", result)

    result = result.strip()

    # remove markdown formatting if present
    if "```" in result:
        result = result.split("```")[1]

    # find first and last JSON brackets
    start = result.find("{")
    end = result.rfind("}") + 1

    clean_json = result[start:end]

    return json.loads(clean_json)

# "thumbnail_prompt": "Detailed visual description for YouTube thumbnail"
#  - Thumbnail prompt must be visually descriptive
# "description": "...",      --> line 22
# - Description must be engaging and natural --> line 30
