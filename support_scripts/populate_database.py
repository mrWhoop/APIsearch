from app.models.api import Api, EndPoint
from random import randrange

def populate_database():

    # ---------------
    # Cats
    # ---------------

    endpoints = [EndPoint(
        endpoint='/images/search',
        http_method='GET',
        description='Searches or returns Random selection from all approved images.',
        endpoint_keywords=['image', 'random cat image'],
        ),
        EndPoint(
            endpoint='/images/:image_id/analysis',
            http_method='GET',
            description='Get the raw analysis results for any uploaded image',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/images/',
            http_method='GET',
            description="Only returns images from your account, uploaded via 'api/v1/images/upload'",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/images/upload',
            http_method='POST',
            description="Make sure you're using the right field to send the image, and Content-Type header",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/images/:image_id',
            http_method='DEL',
            description=None,
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/images/:image_id/breeds',
            http_method='GET',
            description=None,
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/images/:image_id/breeds/:breed_id',
            http_method='DEL',
            description=None,
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breeds',
            http_method='GET',
            description="Endpoint to get information about different Breeds",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breeds/:breed_id',
            http_method='GET',
            description="Endpoint to get information about different Breeds",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/favourites',
            http_method='GET',
            description="Endpoint to save or get Favourited Images by your Users",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/favourites',
            http_method='POST',
            description="Endpoint to save or get Favourited Images by your Users",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='favourites/:favourite_id',
            http_method='GET',
            description="Endpoint to save or get Favourited Images by your Users",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='favourites/:favourite_id',
            http_method='DEL',
            description="Endpoint to save or get Favourited Images by your Users",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='favourites/:favourite_id',
            http_method='GET',
            description="Endpoints to let your Users Vote on Images",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/votes',
            http_method='GET',
            description="Endpoints to let your Users Vote on Images",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/votes',
            http_method='POST',
            description="Endpoints to let your Users Vote on Images",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/votes/:vote_id',
            http_method='GET',
            description="Endpoints to let your Users Vote on Images",
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/votes/:vote_id',
            http_method='DEL',
            description="Endpoints to let your Users Vote on Images",
            endpoint_keywords=[],
        )
    ]

    api = Api(
        name='The Cat API',
        description="An open, free, read & write API all about Cats. The Cat API gives you access to 10000's of Cat images, and breeds. Upload your own Images. Get detailed info on all Cat Breeds. Allow your Users to Favourite or Vote on Images. Save a custom value with each request so you can match data to your Users.",
        base_url='https://api.thecatapi.com/v1/',
        api_keywords=['CatAPI', 'Cats', 'Cat Pictures'],
        popularity=randrange(0,10),
        service_level=randrange(0,10),
        latency=randrange(0,1000),
        reliability=randrange(0,10),
        endpoints=endpoints,
        https=True,
        authenticaton='apiKey',
        cors=None,
        docs='https://developers.thecatapi.com/',
        category='Animals'
    )

    api.save()

    # ---------------
    # Cataas
    # ---------------

    endpoints = [
        EndPoint(
        endpoint='/cat',
        http_method='GET',
        description='Get a random cat',
        endpoint_keywords=['Random', 'cat'],
        ),
        EndPoint(
            endpoint='/cat/says/{text}',
            http_method='GET',
            description='Get random cat saying text',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/cat/{id}',
            http_method='GET',
            description='Get cat by id',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/cat/{id}/says/{text}',
            http_method='GET',
            description='Get cat by id saying text',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/cat/{tag}',
            http_method='GET',
            description='Get random cat by tag',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/cat/{tag}/says/{text}',
            http_method='GET',
            description='Get random cat by tag saying text',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/api/cats',
            http_method='GET',
            description='Count how many cat',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/api/tags',
            http_method='GET',
            description='Will return all tags',
            endpoint_keywords=[],
        )
    ]

    api = Api(
        name='CATAAS',
        description='Cat as a service. Is a REST API to spread peace and love (or not) thanks to cats. Have 1987 cats for now.',
        base_url='https://cataas.com/',
        api_key=['Cat', 'Cats', 'Cat Pictures', 'CATASS'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        https=True,
        authenticaton=None,
        cors=True,
        docs='https://cataas.com/',
        category='Animals'
    )

    api.save()

    # ----------------
    # Dog API
    # ----------------

    endpoints = [
        EndPoint(
            endpoint='/facts',
            http_method='GET',
            description='list facts',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/groups',
            http_method='GET',
            description='list groups',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/groups/{id}',
            http_method='GET',
            description='get group',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/groups/{id}',
            http_method='GET',
            description='get group',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/breeds',
            http_method='GET',
            description='list breeds',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/breeds/{id}',
            http_method='GET',
            description='get breed',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Dog API',
        description='The Dog API provides information on over 340 dog breeds, 20 breed groups, and fun facts. Our data is accurate and constantly updated. Easily integrate this information into your own website or application with our user-friendly API. Get started today and discover more about the world of dogs.',
        base_url='https://dogapi.dog/api/v2',
        api_key=['Dog', 'DogAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        https=False,
        authenticaton=None,
        cors=None,
        docs='https://dogapi.dog/',
        category='Animals'
    )

    api.save()

    # ----------------
    # Dogs
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/breeds/list/all',
            http_method='GET',
            description='List all breeds',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breeds/image/random',
            http_method='GET',
            description='Display single random image from all dogs collection',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/images',
            http_method='GET',
            description='Returns an array of all the images from a breed, e.g. hound',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/images',
            http_method='GET',
            description='Returns an array of all the images from a breed, e.g. hound',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breeds/image/random/{number}',
            http_method='GET',
            description='Display multiple random images from all dogs collection',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/images/random',
            http_method='GET',
            description='Random image from a breed collection',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/images/random/{number}',
            http_method='GET',
            description='Multiple images from a breed collection',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/list',
            http_method='GET',
            description='Returns an array of all the sub-breeds from a breed',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/{sub-breed}/images',
            http_method='GET',
            description='Returns an array of all the images from the sub-breed',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/{sub-breed}/list',
            http_method='GET',
            description='Returns an array of all the sub-breeds from a breed',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/{sub-breed}/images/random',
            http_method='GET',
            description='Single random image from a sub breed collection',
            endpoint_keywords=[],
        ),
        EndPoint(
            endpoint='/breed/{breed}/{sub-breed}/images/random/{number}',
            http_method='GET',
            description='Multiple images from a sub-breed collection',
            endpoint_keywords=[],
        )
    ]

    api = Api(
        name='Dog API',
        description="The internet's biggest collection of open source dog pictures.",
        base_url='https://dog.ceo/api',
        api_keywords=['Dog', 'dogAPI', 'animals'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        https=True,
        authenticaton=None,
        cors=True,
        docs='https://dog.ceo/dog-api/',
        category='Animals'
    )

    api.save()

    # ----------------
    # Foxes
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/{status_code}',
            http_method='GET',
            description='GET method',
            endpoint_keywords=['cat', 'status code'],
        )
    ]

    api = Api(
        name='HTTP Cats',
        description='Cat for every HTTP Status',
        base_url='https://http.cat',
        api_keywords=['cat', 'status code', 'http'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        https=True,
        authenticaton=None,
        cors=None,
        docs='https://http.cat/',
        category='Animals'
    )

    api.save()

    # ----------------
    # HTTP Dogs
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/{status_code}',
            http_method='GET',
            description='GET method',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='HTTP Status Dogs',
        description='Dogs for every HyperText Transfer Protocol response status code.',
        base_url='https://http.dog/',
        api_keywords=['Dog', 'DogAPI', 'animals'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        https=True,
        authenticaton=None,
        cors=None,
        docs='https://http.dog/',
        category='Animals'
    )

    api.save()

    # ----------------
    # Meow Facts
    # ---------------

    api = Api(
        name='Meow Facts',
        description='🐈 a simple api which returns a catfact',
        base_url='https://meowfacts.herokuapp.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=[],
        https=True,
        authenticaton=None,
        cors=False,
        docs=None,
        category='Animals'
    )

    api.save()

    # ----------------
    # Open Dog Registry
    # ---------------

    api = Api(
        name='Open Dog Registry',
        description='A free and open-source API for dog breeds',
        base_url='https://registry.dog/api/v1',
        api_keywords=['Dog', 'adoption', 'animal'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=[],
        https=True,
        authenticaton='OAuth',
        cors=True,
        docs='https://registry.dog/',
        category='Animals'
    )

    api.save()

    # ----------------
    # Petfinder
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/animals',
            http_method='GET',
            description='Returns one "page" of details (defaulting to the first 20 results) on a group of animals based on criteria given in the parameters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/animals/{id}',
            http_method='GET',
            description='Returns details on the specified animal based on ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/types',
            http_method='GET',
            description='Returns an array of animal types. This provides the possible values for the "type" parameter, covering species, color, coat, and gender.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/types/{type}',
            http_method='GET',
            description='Returns information on a single animal type.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/types/{type}/breeds',
            http_method='GET',
            description='Returns possible breed values for a given animal type',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/organizations',
            http_method='GET',
            description='Returns details on a group of organizations based on criteria given in parameters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/organizations/{id}',
            http_method='GET',
            description='Returns details on a single organization based on ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
    ]

    api = Api(
        name='Petfinder',
        description='The Petfinder API (Application Programming Interface) allows you to access the Petfinder database of hundreds of thousands of pets ready for adoption and over ten thousand animal welfare organizations. You can use the API to build your own dynamic websites or applications backed by the same data used on Petfinder.com.',
        base_url='https://api.petfinder.com/v2/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://www.petfinder.com/developers/v2/docs/',
        category='Animals'
    )

    api.save()

    # ----------------
    # RandomDog
    # ---------------

    api = Api(
        name='RandomDog',
        description='Random pictures of dogs',
        base_url='https://random.dog/woof.json',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs=None,
        category='Animals'
    )

    api.save()

    # ----------------
    # RandomFox
    # ---------------

    api = Api(
        name='RandomFox',
        description='Random pictures of foxes',
        base_url='https://randomfox.ca/floof/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=False,
        https=True,
        cors=False,
        docs=None,
        category='Animals'
    )

    api.save()

    # ----------------
    # AniList
    # ---------------

    api = Api(
        name='AniList',
        description='The AniList GraphQL API provides quick and powerful access to over 500k anime and manga entries, including character, staff, and live airing data. The AniList & AniChart websites themselves run on the API, so almost everything you can do on the sites, you can do via the API.',
        base_url='https://graphql.anilist.co',
        api_keywords=[],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=[],
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://docs.anilist.co/',
        category='Anime',
        type='GraphQL'
    )

    api.save()

    # ----------------
    # AnimeNewsNetwork
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/reports.xml',
            http_method='GET',
            description="On the reports page you'll find a list of various dynamically-generated reports.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/api.xml',
            http_method='GET',
            description="If you need more information than the basic details provided in the reports, use this API to fetch detailled information for each title.",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='AnimeNewsNetwork',
        description='Anime industry news',
        base_url='https://cdn.animenewsnetwork.com/encyclopedia',
        api_keywords=['Anime', 'News'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://www.animenewsnetwork.com/encyclopedia/api.php',
        category='Anime',
        type='XML'
    )

    api.save()

    # ----------------
    # AOT quotes
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/quote',
            http_method='GET',
            description="Simply make a GET request to the endpoint and retrieve the quote along with the author's name for use in your application.",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Attack on Titan Quotes API',
        description='The AOT Quotes API provides random quotes from the Attack on Titan series, perfect for adding a touch of anime flavor to your project.n',
        base_url='https://aot-api.vercel.app',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://attackontitanquotes.vercel.app/',
        category='Anime'
    )

    api.save()

    # ----------------
    # Jikan
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v4/anime/{id}/full',
            http_method='GET',
            description='Full anime Resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}',
            http_method='GET',
            description='Anime Resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/characters',
            http_method='GET',
            description='Returns anime characters Resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/staff',
            http_method='GET',
            description='Returns anime staff Resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/episodes',
            http_method='GET',
            description='Returns list of anime episodes',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/episodes/{episode}',
            http_method='GET',
            description='Returns a single anime episode resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/news',
            http_method='GET',
            description='Returns list of news articles related to the entry',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/forum',
            http_method='GET',
            description='Returns a list of forum topics related to the entry',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/videos',
            http_method='GET',
            description='Returns videos related to the entry',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/videos/episodes',
            http_method='GET',
            description='Returns episode videos related to the entry',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/pictures',
            http_method='GET',
            description='Returns pictures related to the entry',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/statistics',
            http_method='GET',
            description='Returns anime statistics',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/moreinfo',
            http_method='GET',
            description='Returns additional anime info',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/recommendations',
            http_method='GET',
            description='Returns anime recommendations',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/userupdates',
            http_method='GET',
            description='Returns a list of users who have added/updated/removed the entry on their list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/reviews',
            http_method='GET',
            description='Returns anime reviews',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/reviews',
            http_method='GET',
            description='Returns anime reviews',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/relations',
            http_method='GET',
            description='Returns anime relations',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/themes',
            http_method='GET',
            description='Returns anime themes',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/external',
            http_method='GET',
            description='Returns anime external links',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime/{id}/streaming',
            http_method='GET',
            description='Returns anime streaming links',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/anime',
            http_method='GET',
            description='Returns search results for anime',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}/full',
            http_method='GET',
            description='Returns complete character resource data',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}',
            http_method='GET',
            description='Returns character resource',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}/anime',
            http_method='GET',
            description='Returns anime that character is in',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}/manga',
            http_method='GET',
            description='Returns manga that character is in',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}/voices',
            http_method='GET',
            description="Returns the character's voice actors",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters/{id}/pictures',
            http_method='GET',
            description="Returns pictures related to the entry",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/characters',
            http_method='GET',
            description="Returns search results for characters",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/clubs/{id}',
            http_method='GET',
            description="Returns Club Resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/clubs/{id}/members',
            http_method='GET',
            description="Returns Club Members Resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/clubs/{id}/staff',
            http_method='GET',
            description="Returns Club Staff",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/clubs/{id}/relations',
            http_method='GET',
            description="Returns Club Relations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/clubs',
            http_method='GET',
            description="Returns search results for clubs",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/genres/anime',
            http_method='GET',
            description="Returns entry genres, explicit_genres, themes and demographics",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/genres/manga',
            http_method='GET',
            description="Returns entry genres, explicit_genres, themes and demographics",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/magazines',
            http_method='GET',
            description="Returns magazines collection",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/full',
            http_method='GET',
            description="Returns complete manga resource data",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}',
            http_method='GET',
            description="Returns pictures related to the entry",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/characters',
            http_method='GET',
            description="Returns manga characters resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/news',
            http_method='GET',
            description="Returns manga characters resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/forum',
            http_method='GET',
            description="Returns a list of manga forum topics",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/pictures',
            http_method='GET',
            description="Returns a list of manga pictures",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/statistics',
            http_method='GET',
            description="Returns anime statistics",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/moreinfo',
            http_method='GET',
            description="Returns manga moreinfo",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/recommendations',
            http_method='GET',
            description="Returns manga recommendations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/userupdates',
            http_method='GET',
            description="Returns manga user updates",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/reviews',
            http_method='GET',
            description="Returns manga reviews",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/relations',
            http_method='GET',
            description="Returns manga relations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga/{id}/external',
            http_method='GET',
            description="Returns manga external links",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/manga',
            http_method='GET',
            description="Returns search results for manga",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}/full',
            http_method='GET',
            description="Returns complete character resource data",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}',
            http_method='GET',
            description="Returns pictures related to the entry",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}/anime',
            http_method='GET',
            description="Returns person's anime staff positions",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}/voices',
            http_method='GET',
            description="Returns person's voice acting roles",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}/manga',
            http_method='GET',
            description="Returns person's published manga works",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people/{id}/pictures',
            http_method='GET',
            description="Returns a list of pictures of the person",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/people',
            http_method='GET',
            description="Returns search results for people",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/producers/{id}',
            http_method='GET',
            description="Returns producer resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/producers/{id}/full',
            http_method='GET',
            description="Returns producer resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/producers/{id}/external',
            http_method='GET',
            description="Returns producer's external links",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/producers',
            http_method='GET',
            description="Returns producers collection",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/random/anime',
            http_method='GET',
            description="Returns a random anime resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/random/manga',
            http_method='GET',
            description="Returns a random manga resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/random/characters',
            http_method='GET',
            description="Returns a random character resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/random/people',
            http_method='GET',
            description="Returns a random character resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/random/users',
            http_method='GET',
            description="Returns a random user profile resource",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/recommendations/anime',
            http_method='GET',
            description="Returns recent anime recommendations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/recommendations/manga',
            http_method='GET',
            description="Returns recent manga recommendations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/reviews/anime',
            http_method='GET',
            description="Returns recent anime reviews",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/reviews/manga',
            http_method='GET',
            description="Returns recent manga reviews",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/schedules',
            http_method='GET',
            description="Returns weekly schedule",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users',
            http_method='GET',
            description="Returns search results for users",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/userbyid/{id}',
            http_method='GET',
            description="Returns username by ID search",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/full',
            http_method='GET',
            description="Returns complete user resource data",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}',
            http_method='GET',
            description="Returns user profile",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/statistics',
            http_method='GET',
            description="Returns user statistics",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/favorites',
            http_method='GET',
            description="Returns user favorites",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/userupdates',
            http_method='GET',
            description="Returns user updates",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/about',
            http_method='GET',
            description="Returns user about in raw HTML",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/history',
            http_method='GET',
            description="Returns user history (past 30 days)",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/friends',
            http_method='GET',
            description="Returns user friends",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/reviews',
            http_method='GET',
            description="Returns user reviews",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/recommendations',
            http_method='GET',
            description="Returns Recent Anime Recommendations",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/clubs',
            http_method='GET',
            description="Returns user clubs",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{username}/external',
            http_method='GET',
            description="Returns user's external links",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/seasons/now',
            http_method='GET',
            description="Returns current seasonal anime",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/seasons/{year}/{season}',
            http_method='GET',
            description="Returns seasonal anime",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/seasons',
            http_method='GET',
            description="Returns available list of seasons",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/seasons/upcoming',
            http_method='GET',
            description="Returns upcoming season's anime",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/top/anime',
            http_method='GET',
            description="Returns top anime",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/top/manga',
            http_method='GET',
            description="Returns top manga",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/top/people',
            http_method='GET',
            description="Returns top people",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/top/characters',
            http_method='GET',
            description="Returns top characters",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/top/reviews',
            http_method='GET',
            description="Returns top reviews",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/watch/episodes',
            http_method='GET',
            description="Returns Recently Added Episodes",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/watch/episodes/popular',
            http_method='GET',
            description="Returns Popular Episodes",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/watch/promos',
            http_method='GET',
            description="Returns Recently Added Promotional Videos",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/watch/promos/popular',
            http_method='GET',
            description="Returns Popular Promotional Videos",
            endpoint_keywords=['GET', 'testGET'],
        ),
    ]

    api = Api(
        name='Jikan API',
        description='Jikan is an Unofficial MyAnimeList API. It scrapes the website to satisfy the need for a complete API - which MyAnimeList lacks.',
        base_url='https://api.jikan.moe',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://docs.api.jikan.moe/#section/Information',
        category='Anime'
    )

    api.save()

    # ----------------
    # What Anime
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/search',
            http_method='GET',
            description='This method is the easiest if your image is already hosted somewhere in public. Otherwise, you must upload the image.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/search',
            http_method='POST',
            description='Search by image upload. Supported Content-Types are image/*, video/*, application/octet-stream and application/x-www-form-urlencoded',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/me',
            http_method='GET',
            description='Get info about your account',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='test_api',
        description='Test API description',
        base_url='http://localhost:8000',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://soruly.github.io/trace.moe-api/#/docs',
        category='Anime'
    )

    api.save()

    # ----------------
    # Mangadex
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/client',
            http_method='GET',
            description='List own Api Clients',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client',
            http_method='POST',
            description='Create ApiClient',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}',
            http_method='GET',
            description='Get Api Client by ID',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}',
            http_method='POST',
            description='Edit ApiClient',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}',
            http_method='DELETE',
            description='Delete Api Client',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}/secret',
            http_method='GET',
            description='Delete Api Client',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}/secret',
            http_method='POST',
            description='Regenerate Client Secret',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/client/{id}/secret',
            http_method='POST',
            description='Regenerate Client Secret',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/author',
            http_method='GET',
            description='Author list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/author',
            http_method='POST',
            description='Create author',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/author/{id}',
            http_method='GET',
            description='Get author',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/author/{id}',
            http_method='PUT',
            description='Update author',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/author/{id}',
            http_method='DELETE',
            description='Delete author',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/captcha/solve',
            http_method='POST',
            description='Solve captcha',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/chapter',
            http_method='GET',
            description='Get chapter list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/chapter/{id}',
            http_method='GET',
            description='Get chapter',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/chapter/{id}',
            http_method='PUT',
            description='Update chapter',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/chapter/{id}',
            http_method='DELETE',
            description='Delete chapter',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/cover',
            http_method='GET',
            description='CoverArt list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/cover/{mangaOrCoverId}',
            http_method='POST',
            description='Upload cover',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/cover/{mangaOrCoverId}',
            http_method='GET',
            description='Get cover',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/cover/{mangaOrCoverId}',
            http_method='PUT',
            description='Update cover',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/cover/{mangaOrCoverId}',
            http_method='DELETE',
            description='Delete cover',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list',
            http_method='POST',
            description='Create CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list/{id}',
            http_method='GET',
            description='Get CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list/{id}',
            http_method='PUT',
            description='Update CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list/{id}',
            http_method='DELETE',
            description='Delete CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list/{id}/follow',
            http_method='POST',
            description='Follow CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/list/{id}/follow',
            http_method='DELETE',
            description='Unfollow CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/list/{listId}',
            http_method='POST',
            description='Add Manga in CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/list/{listId}',
            http_method='DELETE',
            description='Remove Manga in CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/list/{listId}',
            http_method='DELETE',
            description='Remove Manga in CustomList',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/ping',
            http_method='GET',
            description='Ping healthcheck',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga',
            http_method='GET',
            description='Manga list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga',
            http_method='POST',
            description='Create manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/aggregate',
            http_method='GET',
            description='Get Manga volumes & chapters',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}',
            http_method='GET',
            description='Get Manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}',
            http_method='PUT',
            description='Update Manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}',
            http_method='PUT',
            description='Update manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}',
            http_method='DELETE',
            description='Delete manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/follow',
            http_method='POST',
            description='Follow manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/follow',
            http_method='DELETE',
            description='Unfollow manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/feed',
            http_method='GET',
            description='Manga feed',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/random',
            http_method='GET',
            description='Get a random manga',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/tag',
            http_method='GET',
            description='Tag list',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/status',
            http_method='GET',
            description='Get all Manga reading status for logged User',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/status',
            http_method='GET',
            description='Get a manga reading status',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/status',
            http_method='POST',
            description='Update manga reading status',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/draft/{id}',
            http_method='GET',
            description='Get specific manga draft',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/draft/{id}/commit',
            http_method='POST',
            description='Submit a manga draft',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/draft',
            http_method='GET',
            description='Get a list of manga drafts',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/rating',
            http_method='GET',
            description='Get your ratings',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/rating/{mangaId}',
            http_method='GET',
            description='Create or update manga rating',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/rating/{mangaId}',
            http_method='DELETE',
            description='Delete manga rating',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/read',
            http_method='GET',
            description='Manga read markers',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/{id}/read',
            http_method='POST',
            description='Manga read markers batch',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/manga/read',
            http_method='GET',
            description='Manga read markers',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/user/history',
            http_method='GET',
            description='Get user read history',
            endpoint_keywords=['GET', 'testGET'],
        ),
    ]

    api = Api(
        name='MangaDex',
        description='MangaDex is an ad-free manga reader offering high-quality images. Some of the API is open, while more advanced functionalities require authentication.',
        base_url='http://api.mangadex.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.mangadex.org/docs/',
        category='Anime'
    )

    api.save()

    # ----------------
    # Nekosia API
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v1/images/:category',
            http_method='GET',
            description='This endpoint allows you to fetch random images from a selected category.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/getImageById/:id',
            http_method='GET',
            description='Retrieve details about a specific image.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/tags',
            http_method='GET',
            description='Retrieve a full list of all tags, anime titles, and characters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
    ]

    api = Api(
        name='Nekosia',
        description='The Best Anime and Nekos API for Your Projects Infuse your projects with anime magic and a dash of feline charm! Explore a diverse range of endpoints designed to meet all your anime-related needs. Scroll down and discover the purr-fect solutions that will bring your projects to life! Meow~~ 🐾',
        base_url='http://api.nekosia.cat/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://nekosia.cat/documentation?page=introduction',
        category='Anime'
    )

    api.save()

    # ----------------
    # Cats
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v2/check',
            http_method='GET',
            description='The check endpoint accepts a single IP address (v4 or v6). Optionally you may set the maxAgeInDays parameter to only return reports within the last x amount of days.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/reports',
            http_method='GET',
            description='The reports endpoint accepts a single IP address (v4 or v6). Optionally you may set the maxAgeInDays parameter to only return reports within the last x amount of days. You can also adjust the pagination with the perPage parameter, and navigate the pagination via the page parameter.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/blacklist',
            http_method='GET',
            description="The blacklist is the culmination of all of the valiant reporting by AbuseIPDB users. It's a list of the most reported IP addresses.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/blacklist',
            http_method='GET',
            description="The blacklist is the culmination of all of the valiant reporting by AbuseIPDB users. It's a list of the most reported IP addresses.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/report',
            http_method='POST',
            description="The blacklist is the culmination of all of the valiant reporting by AbuseIPDB users. It's a list of the most reported IP addresses.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/check-block',
            http_method='GET',
            description="The check-block endpoint accepts a subnet (v4 or v6) denoted with CIDR notation.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/bulk-report',
            http_method='POST',
            description="If reporting IP addresses one by one may not seem efficient to you, we offer an endpoint that allows a CSV file of IPs to be reported in one shot. Such a list can be extracted from your secure log file or similar.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/clear-address',
            http_method='DELETE',
            description="The clear-address endpoint accepts a single IP address (v4 or v6). The only property it returns is the number of reports deleted from your account.",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='AbuseIPDB',
        description='The AbuseIPDB API allows you to utilize our database programmatically. This is most commonly done through Fail2Ban, which comes prepackaged with an AbuseIPDB configuration.',
        base_url='https://api.abuseipdb.com/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.abuseipdb.com/',
        category='Anti-Malware'
    )

    api.save()

    # ----------------
    # FishFish
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v1/domains/:domain',
            http_method='GET',
            description='The domain name to get.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/domains',
            http_method='GET',
            description='Get domains via filters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/domains/:domain',
            http_method='POST',
            description='The domain name to create.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/domains/:domain',
            http_method='PATCH',
            description='The domain name to update.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/domains/:domain',
            http_method='DELETE',
            description='The domain name to delete.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/:url',
            http_method='GET',
            description='The URL to get.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/',
            http_method='GET',
            description='The URL to get via filters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/:url',
            http_method='GET',
            description='The URL to get via filters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/:url',
            http_method='POST',
            description='The URL to create, URL-encoded.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/:url',
            http_method='PATCH',
            description='The URL to update.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/urls/:url',
            http_method='DELETE',
            description='The URL to delete.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users/:id',
            http_method='GET',
            description='The user ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users',
            http_method='POST',
            description='The new user.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users/:id',
            http_method='PATCH',
            description='Update user.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users/:id',
            http_method='DELETE',
            description='Delete user.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/users/@me/tokens',
            http_method='POST',
            description='Create Session Token',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/users/:uid/tokens/:tid',
            http_method='GET',
            description='Get main token',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/users/:uid/tokens',
            http_method='POST',
            description='Create main token',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/users/:uid/tokens/:tid',
            http_method='DELETE',
            description='Delete main token',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='FishFish',
        description="An anti-phishing service that focuses on quick, automated detection of threat resources before they're used for evil.",
        base_url='https://api.fishfish.gg',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.fishfish.gg/docs/',
        category='Anti-Malware'
    )

    api.save()

    # ----------------
    # Google Safe Browsing
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v5alpha1/hashList/{name}',
            http_method='GET',
            description='Get the latest contents of a hash list.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v5alpha1/hashLists:batchGet',
            http_method='GET',
            description='Get multiple hash lists at once.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v5alpha1/hashLists',
            http_method='GET',
            description='List hash lists.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v5alpha1/hashes:search',
            http_method='GET',
            description='Search for full hashes matching the specified prefixes.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v5/hashes:search',
            http_method='GET',
            description='Search for full hashes matching the specified prefixes.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/fullHashes:find',
            http_method='POST',
            description='Finds the full hashes that match the requested hash prefixes.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/threatListUpdates:fetch',
            http_method='POST',
            description='Fetches the most recent threat list updates.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/threatLists',
            http_method='GET',
            description='Lists the Safe Browsing threat lists available for download.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/threatMatches:find',
            http_method='POST',
            description='Finds the threat entries that match the Safe Browsing lists.',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Google Safe Browsing',
        description='Enables client applications to check web resources (most commonly URLs) against Google-generated lists of unsafe web resources. The Safe Browsing APIs are for non-commercial use only. If you need to use APIs to detect malicious URLs for commercial purposes – meaning “for sale or revenue-generating purposes” – please refer to the Web Risk API.',
        base_url='https://safebrowsing.googleapis.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developers.google.com/safe-browsing/reference/rest',
        category='Anti-Malware'
    )

    api.save()
    # ----------------
    # Metacert
    # ---------------

    api = Api(
        name='MetaCert',
        description='MetaCert tells you which links are safe and which websites you can trust.',
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://metacert.com/about.html',
        category='Anti-Malware'
    )

    api.save()

    # ----------------
    # phish.directory
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/adblock/adgaurd',
            http_method='GET',
            description='AdGuard adblocker adlist',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/adblock/ublock',
            http_method='GET',
            description='uBlock Origin adblocker adlist',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/adblock/pihole',
            http_method='GET',
            description='Pi-hole adblocker adlist',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/domain',
            http_method='GET',
            description='Returns a list of all domains.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/domain/:id',
            http_method='GET',
            description='Returns a domain by its ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/domain/check',
            http_method='GET',
            description='Checks if a domain is phishing/malicious.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/email/check',
            http_method='GET',
            description='Check email address reputation and validity.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/metrics',
            http_method='GET',
            description='Get comprehensive system metrics',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/',
            http_method='GET',
            description='Redirect to docs',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/up',
            http_method='GET',
            description='Check if the API is up.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/version',
            http_method='GET',
            description='Get the API version',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/health',
            http_method='GET',
            description='Check the health of the API',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/docs',
            http_method='GET',
            description='API documentation',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/docs',
            http_method='GET',
            description='Admin API documentation',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/user/signup',
            http_method='POST',
            description='Create new user account',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/user/login',
            http_method='POST',
            description='Authenticate user and get JWT token',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/user/me',
            http_method='GET',
            description='Get authenticated user profile and metrics',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user',
            http_method='GET',
            description='Return a list of all users.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/:id',
            http_method='GET',
            description='Returns a user by their ID',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/:id',
            http_method='PATCH',
            description='Updates a user by their ID',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/:id',
            http_method='DELETE',
            description='Deletes a user by their ID',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/new',
            http_method='POST',
            description='Creates a new user.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/:id/:role',
            http_method='PATCH',
            description="Updates a user's role by their ID",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/admin/user/:id/:useExtended',
            http_method='PATCH',
            description="Updates a user's useExteded data enum",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Phish Directory',
        description='Phish Directory is a community-driven database of phishing URLs. Our goal is to help you stay safe from phishing attacks by providing you with the latest information on phishing URLs.',
        base_url='https://api.phish.directory',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://api.phish.directory/docs/',
        category='Anti-Malware'
    )

    # ----------------
    # VirusTotal
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v2/file/report',
            http_method='GET',
            description='Retrieve file scan reports',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/scan',
            http_method='POST',
            description='Upload and scan a file',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/scan/upload_url',
            http_method='GET',
            description='Get a URL for uploading files larger than 32MB',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/rescan',
            http_method='POST',
            description='Re-scan a file',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/download',
            http_method='GET',
            description='Download a file',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/network-traffic',
            http_method='GET',
            description='Retrieve network traffic report',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/feed',
            http_method='GET',
            description='Retrieve live feed of all files submitted to VirusTotal',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/clusters',
            http_method='GET',
            description='Retrieve file clusters',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/file/search',
            http_method='GET',
            description='Search for files',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/url/report',
            http_method='GET',
            description='Retrieve URL scan reports',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/url/feed',
            http_method='GET',
            description='Retrieve live feed of all URLs submitted to VirusTotal',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/url/scan',
            http_method='GET',
            description=None,
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/url/scan',
            http_method='POST',
            description=None,
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/domain/report',
            http_method='GET',
            description='Retrieves a domain report',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/ip-address/report',
            http_method='GET',
            description='Retrieve an IP address report',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/comments/get',
            http_method='GET',
            description='Get comments for a file or URL',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/comments/put',
            http_method='GET',
            description='Post comment for a file or URL',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='VirusTotal',
        description='The VirusTotal API lets you upload and scan files or URLs, access finished scan reports and make automatic comments without the need of using the website interface. In other words, it allows you to build simple scripts to access the information generated by VirusTotal.',
        base_url='https://www.virustotal.com/vtapi',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.virustotal.com/v2.0/reference/getting-started',
        category='Anti-Malware'
    )

    api.save()

    # ----------------
    # Cats
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling-pro',
            http_method='POST',
            description='Generate a video from an image using the Kling 1.6 Pro model.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling-pro',
            http_method='GET',
            description='Get the list of the kling-pro tasks.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling/{task-id}',
            http_method='GET',
            description='Get the status of the kling task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling-std',
            http_method='POST',
            description='Generate a video from an image using the Kling 1.6 Std model.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling-std',
            http_method='GET',
            description='Get the list of the kling-pro tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-to-video/kling/{task-id}',
            http_method='GET',
            description='Get the status of the kling task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/mystic',
            http_method='POST',
            description='Convert descriptive text input into images using AI. This endpoint accepts a variety of parameters to customize the generated images.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/mystic/{task-id}',
            http_method='GET',
            description='Get the status of the Mystic task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/mystic',
            http_method='GET',
            description='Get the status of all Mystic tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/loras',
            http_method='GET',
            description=None,
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image',
            http_method='POST',
            description='Convert descriptive text input into images using AI. This endpoint accepts a variety of parameters to customize the generated images.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/imagen3',
            http_method='POST',
            description='Convert descriptive text input into images using AI. This endpoint accepts a variety of parameters to customize the generated images.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/imagen3/{task-id}',
            http_method='GET',
            description='Get the status of the Imagen3 task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/imagen3',
            http_method='GET',
            description='Get the status of all Imagen3 tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/flux-dev',
            http_method='POST',
            description='Convert descriptive text input into images using AI. This endpoint accepts a variety of parameters to customize the generated images.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/flux-dev/{task-id}',
            http_method='GET',
            description='Get the status of the flux-dev task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/text-to-image/flux-dev',
            http_method='GET',
            description='Get the status of the flux-dev tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/beta/text-to-image/reimagine-flux',
            http_method='POST',
            description='(Beta, synchronous) Reimagine Flux is a new AI model that allows you to generate images from text prompts.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-upscaler',
            http_method='POST',
            description='This asynchronous endpoint enables image upscaling using advanced AI algorithms. Upon submission, it returns a unique task_id which can be used to track the progress of the upscaling process. For real-time production use, include the optional webhook_url parameter to receive an automated notification once the task has been completed. This allows for seamless integration and efficient task management without the need for continuous polling.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-upscaler/{task-id}',
            http_method='GET',
            description='Get the status of the upscaling task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-upscaler',
            http_method='GET',
            description='Get the status of the upscaling tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-relight',
            http_method='POST',
            description='Relight an image using AI. This endpoint accepts a variety of parameters to customize the generated images.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-relight/{task-id}',
            http_method='GET',
            description='Get the status of the relight task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-relight',
            http_method='GET',
            description='Get the status of the relight tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-style-transfer',
            http_method='POST',
            description=None,
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-style-transfer',
            http_method='GET',
            description='Get the status of all Style Transfer tasks',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/image-style-transfer/{task-id}',
            http_method='GET',
            description='Get the status of all Style Transfer task',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/beta/remove-background',
            http_method='POST',
            description='This endpoint removes the background from an image provided via a URL. The URLs in the response are temporary and valid for 5 minutes only.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/ai/classifier/image',
            http_method='POST',
            description='Accepts an image file as input and analyzes it to determine the probability that the image was generated by artificial intelligence, providing a confidence score.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/resources',
            http_method='GET',
            description='Retrieve a list of resources based on various filter criteria such as orientation, content type, license, and more.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/resources/{resource-id}',
            http_method='GET',
            description='Retrieve the detailed information of a specific resource by its ID. This endpoint supports multiple resource types including PSD, vector, photo, and AI-generated content.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/icons',
            http_method='GET',
            description='Get a list of icons based on the provided parameters and ordering criteria.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/icons/{id}',
            http_method='GET',
            description='Get detailed information about a specific icon identified by its unique ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/icons/{id}/download',
            http_method='GET',
            description='Download the specified icon by its unique ID in the requested format and size.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/resources/{resource-id}/download',
            http_method='GET',
            description='Download a specific resource by providing the resource ID. This endpoint supports downloading various types of resources including vectors, PSDs, photos, and AI-generated content.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/resources/{resource-id}/download/{resource-format}',
            http_method='GET',
            description='Retrieve a resource by specifying both the resource ID and the format. This endpoint allows for precise downloading of resources in the desired format.',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='FREEP!K',
        description='The most advanced AI features, the largest content library, and everything the future holds—all in one powerful API that you can set up instantly.',
        base_url='https://api.freepik.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.freepik.com/introduction',
        category='Art and Design'
    )

    api.save()

    # ----------------
    # Cats
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v4/icons/search',
            http_method='GET',
            description='Search for icons by query string and filter parameters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/icons/{icon_id}',
            http_method='GET',
            description='Get details about a specific icon.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/iconsets/{iconset_id}/icons',
            http_method='GET',
            description='Provides a list of all icons in an icon set sorted descendingly by the popularity of the icons.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/iconsets',
            http_method='GET',
            description='List all public icon sets in descending order of when they were published.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/iconsets/{iconset_id}',
            http_method='GET',
            description='Get details about a specific icon set.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/categories/{category_identifier}/iconsets',
            http_method='GET',
            description='List public icon sets in a category in descending order of when they were published.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{user_id}/iconsets',
            http_method='GET',
            description='List all public icon sets owned by a specific user in descending order of when they were published.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/authors/{author_id}/iconsets',
            http_method='GET',
            description='List all public icon sets owned by a specific author in descending order of when they were published.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/styles/{style_identifier}/iconsets',
            http_method='GET',
            description='List public icon sets of a specific style in descending order of when they were published.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/authors/{author_id}',
            http_method='GET',
            description='Get details about a specific author identified by a unique ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/categories',
            http_method='GET',
            description='List all categories sorted ascendingly by their identifier.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/categories/{category_identifier}',
            http_method='GET',
            description='Get details about a specific category identified by its identifier.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/licenses/{license_id}',
            http_method='GET',
            description='Get details about a specific license by its unique ID.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/styles',
            http_method='GET',
            description='List all styles sorted ascendingly by their identifier.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v4/users/{user_id}',
            http_method='GET',
            description='Get details about a specific user.',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='ICONFINDER',
        description='Millions of graphics for your design projects. Created by independent designers.',
        base_url='https://api.iconfinder.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.iconfinder.com/reference/search',
        category='Art and Design'
    )

    api.save()

    # ----------------
    # Noun Project
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v2/client/blacklist/id',
            http_method='POST',
            description='Add id to blacklist.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/client/blacklist/term',
            http_method='POST',
            description='Add term to os blacklist',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/client/blacklist',
            http_method='GET',
            description='View os blacklist',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/icon/{icon_id}',
            http_method='GET',
            description='Public os get icon by id',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/icon/{icon_id}/download',
            http_method='GET',
            description='Public download edited icon',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/icon',
            http_method='GET',
            description='Public os icon search',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/icon/autocomplete',
            http_method='GET',
            description='Public os icon autocomplete',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/client/usage',
            http_method='GET',
            description='Get client usage',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/client/report',
            http_method='POST',
            description='Report icon usage',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/collection',
            http_method='GET',
            description='Public os collection search',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/collection/{collection_id}',
            http_method='GET',
            description='Public os get collection by id',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Noun Project',
        description='Grab a hold of the World’s Visual Language! Use it in your service or application.',
        base_url='https://api.thenounproject.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://api.thenounproject.com/index.html',
        category='Art and Design'
    )

    api.save()

    return


#----------------
# Cats
# ---------------

    endpoints = [
        EndPoint(
        endpoint='/testGET',
        http_method='GET',
        description='GET method',
        endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='test_api',
        description='Test API description',
        base_url='http://localhost:8000',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=,
        https=,
        cors=,
        docs=,
        category=
    )