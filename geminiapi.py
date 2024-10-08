#!pip install  google-generativeai
#!export GOOGLE_API_KEY="AIzaSyDe2mNWz_K3aPQXqdjp6vSaRCprDL70I0s"
import google.generativeai as genai
import os

# Configuration
#genai.configure(api_key=os.getenv("AIzaSyDe2mNWz_K3aPQXqdjp6vSaRCprDL70I0s"))
genai.configure(api_key="<ap-_key>")
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 4096}

#initialize
model = genai.GenerativeModel("gemini-pro", generation_config=generation_config)

#generate conetct
response =model.generate_content(["What is the meaning of life?"])
print(response)

