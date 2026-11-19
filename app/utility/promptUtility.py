def generatePrompt(query):
    system_prompt = """
You are an expert MongoDB query generator. Your sole task is to generate a `query` that would be passed directly into a `db.collection.find(query)` method in MongoDB.

**Output Format:**
* Always return a JSON object.
* Do NOT include the `db.collection.find()` call itself.
* Do NOT include any explanatory text, comments, or extra newlines outside the JSON structure.
* Do NOT use $regex operator in combination with $in and $all operators

---

**MongoDB `API` Collection Schema:**

```json
{
  "name": { "type": "string",
            "description": "API name"
            },
  "description": { "type": "string",
                   "description": "API description"
                },
  "api_keywords": { "type": ["string"] },
  "https": { "type": "boolean",
             "description": "Field indicating if API is using https"},
  "authentication": { "type": "string",
            "description": "Field indicating API authentication method, possible options are null, OAuth, Basic, apiKey"},
  "cors": { "type": "boolean",
            "description": "Field indicating if API is using CORS"},
  "type": { "type": "string",
            "description": "Field indicating API style, possible options are SOAP, WebSocket, REST, GraphQL"},
  "category": { "type": "string",
                "description": "Field indicating API category, possible options are: Text Analysis, Weather, Tracking, Business, Music, Books, Calendar, Personality, Machine Learning, Health, Sports & Fitness, Test Data, Animals, Patent, Currency Exchange, Fraud Prevention, Dictionaries, Photography, Continuous Integration, Shopping, Art and Design, Education, Disasters, Security, Documents & Productivity, Environment, URL Shorteners, Science & Math, Data Validation, Anti-Malware, Open Source Projects, Open Data, Cryptocurrency, Anime, Food & Drink, Events, Finance, Jobs, Vehicle, Cloud storage and File Sharing, News"},          
}
``` 
            """
    user_prompt = "**USER QUERY:** " + query + "\n"

    return system_prompt, user_prompt

def buildDocument(metadata):
    try:
        authentication = metadata['authentication']
    except KeyError:
        authentication = None

    try:
        https = metadata['https']  # True --> uses https; False --> uses http; null --> skip
    except KeyError:
        https = None
    try:
        cors = metadata['cors']  # True --> uses cors; False --> does not use cors; null skip
    except KeyError:
        cors = None

    category = metadata['category']  # Falls into category
    type = metadata['type']  # Is 'type' API

    document = metadata['name'] + " is " + type + " API.\n"
    document = document + metadata['description'] + "\n"
    document = document + "It belongs to " + '"' + category + '"' + " category.\n"

    if authentication is None:
        pass
    else:
        document = document + "It uses " + authentication + " method of authentication.\n"

    if https is None:
        pass
    elif https:
        document = document + "It supports HTTPS.\n"
    else:
        document = document + "It does not support HTTPS.\n"

    if cors is None:
        pass
    elif cors:
        document = document + "It supports CORS.\n"
    else:
        document = document + "It does not support CORS.\n"

    return document

def generateComparisonPrompt(docs, query):

    system_prompt = """
                    You are an expert document analyst. Your task is to compare provided documents and produce a **concise** comparative analysis. Do NOT include <script> tags or inline event handlers. Use semantic HTML (sections, headings, lists). Keep style minimal - no external CSS links.
        
                    ### INSTRUCTIONS:
                    1. **Analyze and Compare:** Review the text from all documents to identify the key **similarities, differences, and unique points** 
                    2. **Strict Grounding:** Base your entire response *only* on the content provided in the [DOCUMENT] section. Do not use outside knowledge or make assumptions.
                    3. **User query:** Based on provided user query recommend one of the documents.
                    4. **Output Format:** **Use semantic HTML (sections, headings, lists)** Provide 4 sections in HTML: 1) Recommendation, 2) Similarities, 3) differences, 4) Unique points per document. Keep each section concise. Return only HTML. Keep style minimal - no external CSS links.
                    """

    user_prompt = "### USER QUERY:" + query + "\n"

    document = docs['documents']
    metadata = docs['metadatas']

    user_prompt = user_prompt + "### DOCUMENTS:\n"
    for i in range(len(document)):
        user_prompt = user_prompt + "####[" + metadata[i]['name'] + "]\n"  + buildDocument(metadata[i]) + "\n\n"

    print(user_prompt)

    return (system_prompt, user_prompt)