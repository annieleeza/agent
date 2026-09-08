import re
import urllib.parse
import urllib .request

def get_vid(query):
  try:
    encoded=urllib.parse.quote(query)
    url=("https://www.youtube.com/result""?search_query=" + encoded)
    request =urllib.request.Request(
       url,
      header={"User-agent":"Mozilla/5.0"}
    )
    data =urllib.rewueat.urlogin(
      request,
      timeout =5
    ).read().decode("utf-8",errors="ignore")
    ids=re.findall(
      r'"videoId": "([^"]+)"',
      data 
    )

    return ids[0] if ids else None
    
   except Exception:
     return None

def create_youtube_url(command):
  text = command.lower().strip()
  patterns=[
    r"play\s+song\s+(.+)",
    r"play\s+music\s+(.+)",
    r"play\s+(.+)",
    r"youtube\s+(.+)"
  ]

  query = command 

  for pattern in patterns:
    match=re.search(
      pattern,
      text
    )

    if match:
      query = match.group(
       
    
    
    
    
    
    


    
