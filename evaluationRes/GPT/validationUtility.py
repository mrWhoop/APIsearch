
ALLOWED_ATTRIBUTES = {
    "name",
    "description",
    "base_url",
    "api_keywords",
    "https",
    "authentication",
    "cors",
    "docs",
    "category",
    "type"
}

LOGICAL_OPERATORS = {
    "$and",
    "$or",
    "$nor"
}

FIELD_OPERATORS = {
    "$eq",
    "$ne",
    "$gt",
    "$gte",
    "$lt",
    "$lte",
    "$in",
    "$all",
    "$elemMatch",
    "$size",
    "$not",
    "$regex",
    "$options"
}

# IMPLEMENTIRANO Z UPRABO UMETNE INTELIGENCE

def validateMongoQuery(query):

    if not isinstance(query, dict) or not query:
        return False

    for key, value in query.items():

        # Logical operators
        if key in LOGICAL_OPERATORS:

            if not isinstance(value, list) or not value:
                return False

            if not all(validateMongoQuery(item) for item in value):
                return False

        # Field-level operators
        elif key.startswith("$"):

            if key not in FIELD_OPERATORS:
                return False

            if key == "$not":
                if not isinstance(value, dict):
                    return False

                if not validateFieldOperators(value):
                    return False

            elif key in {"$in", "$all"}:
                if not isinstance(value, list):
                    return False

            elif key == "$elemMatch":
                if not validateMongoQuery(value):
                    return False

            elif key == "$size":
                if not isinstance(value, int) or value < 0:
                    return False

            elif key == "$regex":
                if not isinstance(value, str):
                    return False

            elif key == "$options":
                if not isinstance(value, str):
                    return False

        # Field names
        else:

            if key not in ALLOWED_ATTRIBUTES:
                return False

            if isinstance(value, dict):
                if not validateFieldOperators(value):
                    return False

    return True


def validateFieldOperators(operators):

    if not isinstance(operators, dict) or not operators:
        return False

    for key, value in operators.items():

        if key not in FIELD_OPERATORS:
            return False

        if key == "$not":
            if not isinstance(value, dict):
                return False

            if not validateFieldOperators(value):
                return False

        elif key in {"$in", "$all"}:
            if not isinstance(value, list):
                return False

        elif key == "$elemMatch":
            if not validateMongoQuery(value):
                return False

        elif key == "$size":
            if not isinstance(value, int) or value < 0:
                return False

        elif key == "$regex":
            if not isinstance(value, str):
                return False

        elif key == "$options":
            if not isinstance(value, str):
                return False

    # $options must accompany $regex
    if "$options" in operators and "$regex" not in operators:
        return False

    return True
