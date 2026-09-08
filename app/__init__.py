import os , utllib.parse , urillb.request , render_templates
form app.youtube import youtube_bp

Gemini_api_key = "Gemini_API_Key";

def home():
  return render template("index.html")
  
def create_app():
  app=Flask(_name_)
  app.register_blurprint(youtube_bp, url_prefix="/youtube")
  
@app.route("/html")
def html():
  return render_template("index.html")
  
return app;
