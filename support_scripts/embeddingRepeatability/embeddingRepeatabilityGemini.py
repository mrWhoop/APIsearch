import os
import json
from google import genai
from google.genai import types
from google.genai.errors import APIError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from dotenv import load_dotenv

queries = [
"animals",
"books",
"storage",
"crypto",
"currency exchange",
"malware",
"education",
"jobs",
"music",
"security",
"weather",
"car rent",
"fitness",
"streaming",
"random pictures",
"animal shelter",
"holidays",
"productivity",
"fraud prevention",
"stocks",
"jokes",
"joke generator",
"data analysis",
"calendar",
"religion",
"data storage",
"translator",
"profanity filter",
"dictionary",
"climate",
"ticket purchase",
"recipes",
"drugs",
"federal jobs",
"song lyrics",
"podcasts",
"news",
"advice",
"space",
"URL shortener",
"Dropbox",
"PASTEBIN",
"FINCEPT",
"kanye.rest",
"flickr",
"Imgur",
"THE WORLD BANK",
"eBay",
"National Weather Service API",
"MEGA",
"Google Books",
"CATAAS",
"FREEP!K",
"Lingua Robot",
"1Forge",
"Bitquery",
"Trestle",
"Oxford Dictionaries",
"Vector Express",
"Todoist",
"Advice Slip",
"Gmail",
"Mailgun",
"Tomba",
"languagelayer",
"veriphone",
"file.io",
"Ticketmaster",
"FMP",
"PunkAPI",
"TheCocktailDB",
"FraudLabs PRO",
"Lexigram",
"Nutritionix",
"JOBICY",
"Juju",
"ambee",
"last.fm",
"Spotify",
"chucnorris.io",
"stock prices in real-time",
"PDF generation from HTML",
"convert text to speech",
"GraphQL API for address autocomplete",
"real-time stock market API free",
"cryptocurrency price API with WebSocket",
"currency exchange rate API JSON",
"financial news API with sentiment analysis",
"language detection API multilingual",
"email validation API free",
"product search API for e-commerce",
"inventory management REST API",
"current weather data API JSON",
"air quality API Europe",
"climate data API for research",
"UV index API free tier",
"API to fetch tax rates by country",
"expense tracking API for small business",
"API to validate health insurance numbers",
"API for package tracking real-time",
"random joke or insult generator",
"funny inspirational quotes or riddles generator",
"stock picture provider or picture generator",
"free simple fitness and meal tracking API",
"natural disaster alerts in real-time",
"crime data and police district information",
"free, unlimited link shortener service",
"ticket purchase, event promotion and venue reservation",
"real time and historical weather data",
"spam and profanity filter free API",
"virus scanning or unsafe website list provider",
"VAT information on European countries",
"simple to use animal facts and pictures API",
"real-time news across the globe",
"beer and brewery information",
"B2B information sharing and digital identity providing",
"job search in government sector",
"free tokenizer for language research",
"secure cloud storage and file sharing",
"free open API for song lyrics and trivia",
"currency exchange REST API with https support and apiKey authentication",
"GraphQL API with OAuth and https support",
"cloud storage API with apiKey authentication and CORS enabled",
"music streaming REST API with OAuth method of authentication",
"document conversion API with cors and https support",
"secret generator API with https support and basic authentication",
"music lyrics REST OAuth https enabled",
"email delivery service REST API with apiKey authentication",
"package tracking API with apiKey authentication and no https support",
"REST cat fact API with https",
"GraphQL Job search API with Oauth authentication",
"air quality REST API with apiKey and https support",
"latest google news retrieval API",
"music mastering REST API with https support and apiKey authentication",
"REST todo app with https and Oauth authentication",
"financial news API with cors and https support",
"RESTful API for picture retrieval",
"anti-phishing API with https support",
"news API with apiKey authentication and https support",
"open REST pet adoption API",
"apiKey authentication website preview API with https support",
"fast anti-phishing REST API with https support",
"websocket cryptocurrency API with https",
"graphql blockchain data API with apiKey auth",
"secure RESTful trademark search open API",
"global holiday API with https and cors support",
"open currency exchange rate data API with cors and https support",
"RESTful API for phone number validation with apiKey auth method",
"secure restful profanity filter with no authentication requirement",
"specialised dictionary API with https and apiKey",
"secure latex to PDF compilation API",
"secure temporary file sharing REST api with https support",
"open brewery information API with https and cors support",
"secure transaction screening API with apiKey authentication",
"REST university information API with https support",
"free URL shortener service with apiKey authentication https and cors support",
"secure real-time UV index API with apiKey method of authentication",
"API for spam detection with https and cors support and apiKey authentication",
"charity list and vetting API with apiKey authentication and no https support",
"open but secure REST API for website icon fetching"
]

OUTPUT_Gemini = "embedding_Gemini_determinism.jsonl"

load_dotenv()

# gemini_client = genai.Client(api_key=os.environ['GEMINI_API_KEY'])

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(APIError)
)
def embed_single_query(query: str):
    return gemini_client.models.embed_content(
        model='models/gemini-embedding-001',
        contents=query,
        config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
    )

if len(queries) != 160:
    print("Wrong number of queries!")
    exit()

with open(OUTPUT_Gemini, "w", encoding="utf-8") as file:
    for i, query in enumerate(queries):
        print(i, query)
        for j in range(1, 10 + 1):
            response = embed_single_query(query)
            count = gemini_client.models.count_tokens(
                model='models/gemini-embedding-001',
                contents=query
            )

            embedding = response.embeddings[0].values

            record = {
                "query_id": i,
                "query": query,
                "repeated": j,
                "model": 'gemini-embedding-001',
                "dimensions": len(embedding),
                "embedding": embedding,
                "input_tokens": count.total_tokens,
            }

            file.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

print('Gemini done.')
