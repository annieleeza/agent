import os
import json
import re
import time 
import random 
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY" ,"")
MODEL= os.getnev("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing")
  prompt = f"""
you are a professional Gmail email writing assistant.

convert the user"s voice commad into a professional email.

Rules:
-do not copy the command literally 
-do not explain anything 
-do not invent names, dates, prices,companies, attachment, or fact.
-key the email natural and concise
-include an appropriate greeting and closing 

Output exactly:

SUBJECT: <subject>
  
