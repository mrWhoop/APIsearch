def evaluateExecutionTime(model:str, start, end, query:str, implementation:str, mongo):
    deltaTime = end - start
    data = {
        "query": query,
        "model": model,
        "implementation": implementation,
        "start": start,
        "end": end,
        "deltaTime": deltaTime
    }

    mongo['api']['time'].insert_one(data)

def evaluateTokenUsage(model:str, inputTokens:int, thinkingTokens:int, outputTokens:int, totalTokens:int, query:str, implementation:str, mongo):

    data = {
        "query": query,
        "model": model,
        "implementation": implementation,
        "inputTokens": inputTokens,
        "thinkingTokens": thinkingTokens,
        "outputTokens": outputTokens,
        "totalTokens": totalTokens
    }

    mongo['api']['token'].insert_one(data)