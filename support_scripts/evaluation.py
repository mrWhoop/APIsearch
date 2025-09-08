import os
import time
import json

import google.generativeai as genai

def databaseQuerySearchGemini(userQuery):
    # Choose a Gemini model. 'gemini-pro' is a good general-purpose model.
    # You might also consider 'gemini-1.5-flash' or 'gemini-1.5-pro' for specific needs.

    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    modelGemini = genai.GenerativeModel('gemini-1.5-pro')

    prompt = """
        You are an expert MongoDB query generator. Your sole task is to generate the `query` document (and optionally the `projection` document) that would be passed directly into a `db.collection.find(query, projection)` method in MongoDB.

        **Output Format:**
        * Always return a JSON object.
        * The JSON object MUST have a key `query` whose value is the MongoDB query document.
        * If a projection is requested, the JSON object MUST also have a key `projection` whose value is the MongoDB projection document. If no projection is needed, omit the `projection` key.
        * Do NOT include the `db.collection.find()` call itself.
        * Do NOT include any explanatory text, comments, or extra newlines outside the JSON structure.
        * For dates, use the format `{"$date": "YYYY-MM-DDTHH:MM:SSZ"}` to represent `ISODate()`. This is a common way to represent dates for JSON parsing.

        ---

        **MongoDB `API` Collection Schema:**

        ```json
        {
          "_id": { "type": "ObjectId" },
          "name": { "type": "string",
                    "description": "API name"
                    },
          "description": { "type": "string",
                            "description": "API description"
                        },
          "api_keywords": { "type": ["string"] },
          "popularity": {"type": "number",
                         "description": "A calculated popularity score for the product, ranging from 0 to 10, where 0 is least popular and 10 is most popular."
                         },
          "service_level": {"type": "number",
                         "description": "A calculated service level score for the product, ranging from 0 to 10, where 0 is least reliable and 10 is most reliable."
                         },
          "latency": {"type": "number",
                         "description": "A latency measure for the product, ranging from 0 to 1000, measured in milliseconds where 0 is most responsive and 1000 is least responsive."
                         },
          "reliability": {"type": "number",
                         "description": "A reliability measure for the product, ranging from 0 to 10, ranging from 0 to 10, where 0 is least reliable and 10 is most reliable."
                         },
          "https": { "type": "boolean",
                    "description": "Field indicating if API is using https or not."},
          "category": { "type": "string",
                    "description": "Field indicating API category, possible options are: Animals, Anime, Anti-Malware, Art and Design, Books, Business, Calendar, Cloud storage and File Sharing, Continuous Integration, Cryptocurrency, Currency Exchange, Data Validation, Dictionaries, Disasters, Documents & Productivity, Education, Enviroment, Events, Finance, Food & Drink, Fraud Prevention, Health, Jobs, Machine Learning, Music, News, Open Data, Open Source Projects, Patent, Personality, Photography, Science & Math, Security, Sports & Fitness, Test Data, Text Analysis, Tracking, URL Shorteners, Vehicle, Weather"},          
        }
        ```
        Request: 
    """ + userQuery

    response = modelGemini.generate_content(prompt)
    response = response.candidates[0].content.parts[0].text

    return response

def repeatabilityTestGemini(query, repetitions):

    results = dict()
    results['query'] = query

    responses = list()
    responsesSet = set()

    for i in range(repetitions):

        time.sleep(5)

        res = databaseQuerySearchGemini(query)
        responses.append(res)
        responsesSet.add(res)


    results['responseCount'] = len(responsesSet)
    results['responses'] = responses

    fileName = "evaluationRes/gemini/" + query.replace(' ', '_') +".json"

    with open(fileName, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)