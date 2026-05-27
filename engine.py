import os
import time
from google import genai

client = genai.Client()

# Core content to ensure the site stays up
PAGES = {
    "index.html": "The evolution of digital business and why all-in-one platforms are replacing fragmented tool stacks.",
    "automation.html": "A guide on building a stress-free automated sales funnel for beginners.",
    "courses.html": "How to structure and launch your first online course for maximum student success."
}

if __name__ == "__main__":
    with open("template.html", "r") as f:
        template = f.read()

    for filename, topic in PAGES.items():
        # ONLY build if file doesn't exist or is tiny (avoids quota issues)
        if os.path.exists(filename) and os.path.getsize(filename) > 500:
            print(f"Skipping {filename}, already exists.")
            continue
            
        try:
            print(f"Generating {filename}...")
            time.sleep(90) # Keep delay to avoid 429 errors
            response = client.models.generate_content(
                model="gemini-2.0-flash", 
                contents=f"Write a 600-word educational guide about {topic}. Use HTML tags."
            )
            
            final_html = template.replace("{CONTENT}", response.text)
            with open(filename, "w") as f:
                f.write(final_html)
            print(f"Successfully created {filename}.")
            
        except Exception as e:
            print(f"FAILED {filename}: {e}")
