import os
import google.generativeai as genai

# 1. Pull your secret key from GitHub's vault securely
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is missing. Check your repository secrets!")
    exit(1)

# 2. Wake up the Gemini Engine
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Ask it a question (We can change this prompt to whatever you want automated later!)
prompt = "Give me one interesting, highly creative daily tip for digital automation or building autonomous projects."

print(f"Sending request to Gemini... Prompt: '{prompt}'")

try:
    response = model.generate_content(prompt)
    output_text = response.text
    
    print("\n--- Success! Gemini Response ---")
    print(output_text)
    print("--------------------------------")
    
    # 4. Save the response into a local text file inside your repository
    with open("daily_output.txt", "w", encoding="utf-8") as file:
        file.write(output_text)
    print("Saved response to daily_output.txt successfully!")

except Exception as e:
    print(f"An error occurred while connecting to the AI: {e}")
