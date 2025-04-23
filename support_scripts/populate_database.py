from app.models.api import Api, EndPoint
from random import randrange

def populate_database():

    # ANIMALS

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
        api_keywords=['Cat', 'Cats', 'Cat Pictures', 'CATASS'],
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
        api_keywords=['Dog', 'DogAPI'],
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

    # ANIME

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

    # ANTI-MALWARE

    # ----------------
    # AbuseIPDB
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

    api.save()

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

    # ART & DESIGN

    # ----------------
    # FREEP!K
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
    # ICONFINDER
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

    # BOOKS

    # ----------------
    # Bhagavad Gita
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v2/chapters/',
            http_method='GET',
            description='Get all chapters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v2/chapters/{ID}/',
            http_method='GET',
            description='Get particular chapter based on ID',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Bhagavad Gita',
        description='Bhagavad Gita API is an open-source REST API that lets anyone use the text from Srimad Bhagavad Gita in their own web or mobile application(s).',
        base_url='https://bhagavad-gita3.p.rapidapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=True,
        docs='https://rapidapi.com/bhagavad-gita-bhagavad-gita-default/api/bhagavad-gita3',
        category='Books'
    )

    api.save()

    # ----------------
    # Google Books
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v1/volumes',
            http_method='GET',
            description='Get volume.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users/{userId}/bookshelves',
            http_method='GET',
            description="Retrieving a list of a user's public bookshelves.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/users/{userId}/bookshelves/{shelf}',
            http_method='GET',
            description="Retrieving a specific public bookshelf.",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='test_api',
        description='Test API description',
        base_url='https://www.googleapis.com/books',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.google.com/books/docs/v1/using',
        category='Books'
    )

    api.save()

    # ----------------
    # Harry Potter API
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/books',
            http_method='GET',
            description='Return all Harry Potter books.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/books/random',
            http_method='GET',
            description='A single random book.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/characters',
            http_method='GET',
            description='Returns all Harry Potter characters.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/characters/random',
            http_method='GET',
            description='Returns a random Harry Potter character.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/houses',
            http_method='GET',
            description='Returns the four Hogwarts Houses with some extra data.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/houses/random',
            http_method='GET',
            description='Returns a random Hogwarts House with some extra data.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/spells',
            http_method='GET',
            description='Returns all the spells mentioned in the saga with a description.',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/spells/random',
            http_method='GET',
            description='Returns a random spell mentioned in the saga with a description.',
            endpoint_keywords=['GET', 'testGET'],
        ),
    ]

    api = Api(
        name='Harry Potter API',
        description='Test API description',
        base_url='https://potterapi-fedeperin.vercel.app/en',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=False,
        https=True,
        cors=True,
        docs='https://vlaurencena.github.io/harry-potter-openapi-swagger-ui/',
        category='Books'
    )

    api.save()

    # ----------------
    # OPEN Library
    # ---------------

    api = Api(
        name='test_api',
        description="Open Library offers a suite of APIs to help developers get up and running with our data. This includes RESTful APIs, which make Open Library data availabile in JSON, YAML and RDF/XML formats. There's also an earlier, now deprecated JSON API which is preserved for backward compatibility.",
        base_url='https://openlibrary.org/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=None,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://openlibrary.org/developers/api',
        category='Books'
    )

    api.save()

    # ----------------
    # Penguin Publishing
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/resources/authors',
            http_method='GET',
            description='search for authors',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/authors/AUTHORID',
            http_method='GET',
            description='details for a specific author',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/works',
            http_method='GET',
            description='search for works',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/works/WORKID',
            http_method='GET',
            description='details for a specific work',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/titles',
            http_method='GET',
            description='search for titles',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/title/ISBN',
            http_method='GET',
            description='details for a specific title',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/authorevents',
            http_method='GET',
            description='search for author events',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/resources/authorevents/EVENTID',
            http_method='GET',
            description='details for a specific author event',
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='Penguin Publishing',
        description="The Penguin Random House Rest Services can be used to get data about books, authors and events.",
        base_url='https://reststop.randomhouse.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.penguinrandomhouse.biz/webservices/rest/',
        category='Books'
    )

    api.save()

    # ----------------
    # Charity Search
    # ---------------

    endpoints = [
        EndPoint(
            endpoint='/v1/charitysearch',
            http_method='GET',
            description='This method enables you to search the entire database of IRS registered nonprofits. Use this API to return multiple charities based on user inputs such as an EIN, charity name, category, city, state, and ZIP Code. You can control the number of records that are returned and page position to implement Pagination. To filter out ineligible organizations simply pass the value eligible=1',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/categories',
            http_method='GET',
            description='This method enables you to provide a list of categories to your end-users allowing them to focus their search on a specific category. OrgHunter uses the NTEE Classification System developed by the National Center for Charitable Statistics as part of its keyword searching criteria. The National Taxonomy of Exempt Entities (NTEE) system is used by the IRS and NCCS to classify nonprofit organizations. It is also used by the Foundation Center to classify both grants and grant recipients (typically nonprofits or governments).',
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/charitybasic',
            http_method='GET',
            description="This method enables you to generate detailed information on a specific charity. This method accepts two parameters, your API key and the charity's EIN. The charity basic API provides detailed information on the charity including its current status with the IRS. In most cases, the charity basic API provide sufficient information to the end-user related a specific charity.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/charitygeolocation',
            http_method='GET',
            description="This method enables you to generate detailed information on a specific charity. This method accepts two parameters, your API key and the charity's EIN. The charity GeoLocation API provides detailed information on the charity including its current status with the IRS. This is an excellent option if you intend to include a Google maps widget within your application or website.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/charityfinancial',
            http_method='GET',
            description="This method enables you to generate detailed information on a specific charity. This method accepts two parameters, your API key and the charity's EIN. The charity Financial API provides detailed information on the charity including its current status with the IRS. This API is designed to provide detailed financial information from the charity's latest form 990 and is an excellent option if you intend to integrate financial charts and graphs into your project.",
            endpoint_keywords=['GET', 'testGET'],
        ),
        EndPoint(
            endpoint='/v1/charitypremium',
            http_method='GET',
            description="This method enables you to generate detailed information on a specific charity. This method accepts two parameters, your API key and the charity's EIN. The charity Premium API is our most comprehensive and provides detailed information on the charity including its current status with the IRS. This API is an excellent option if you intend to include detailed financial information, financial charts and graphs along with detailed mapping information.",
            endpoint_keywords=['GET', 'testGET'],
        )
    ]

    api = Api(
        name='The OrgHunter Charity',
        description="The OrgHunter Charity API provides developers access to over 2.5M charities. Our Charity API goes well beyond the IRS pub78 data source and enables your organization to perform accurate real-time charity vetting. Over 1,500 websites and mobile applications depend on our Charity API daily, making us the largest charity data provider on the market today!",
        base_url='http://data.orghunter.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://charityapi.com/charity-api-summary-search',
        category='Business'
    )

    api.save()

    # BUSINESS

    # ----------------
    # Domainsdb.info
    # ---------------

    endpoints = None

    api = Api(
        name='Domains-Index API',
        description="Registered domains search checks the lists of registered domains for names containing particular words/phrases/numbers or symbols. Technically it's just a GUI interface for domains-index.com database containing more than 260M of registered domains and 1000+ TLDS including newGTLDs. It's free to use and could be helpful domains/marketing research tool.",
        base_url='https://api.domainsdb.info',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.domainsdb.info/v1/',
        category='Business'
    )

    api.save()

    # ----------------
    # Favicon.im
    # ---------------

    endpoints = None

    api = Api(
        name='Favicon.im/{domain}',
        description="Instantly fetch and display the favicon for any website.",
        base_url='https://favicon.im',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://favicon.im/',
        category='Business'
    )

    api.save()

    # ----------------
    # Freelancer
    # ---------------

    endpoints = None

    api = Api(
        name='freelancer developers',
        description="Use the Freelancer API to access a cloud workforce of skilled freelancers from your website, app or software. Why hire people when you can just make an API call to the cloud?",
        base_url='https://developers.freelancer.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.freelancer.com/docs',
        category='Business'
    )

    # ----------------
    # Gmail
    # ---------------

    endpoints = None

    api = Api(
        name='Gmail',
        description="The Gmail API is a RESTful API that can be used to access Gmail mailboxes and send mail. For most web applications the Gmail API is the best choice for authorized access to a user's Gmail data and is suitable for various applications, such as: Read-only mail extraction, indexing, and backup; Automated or programmatic message sending; Email account migration; Email organization including filtering and sorting of messages; Standardization of email signatures across an organization",
        base_url='https://www.googleapis.com/gmail',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.google.com/workspace/gmail/api/guides',
        category='Business'
    )

    api.save()

    # ----------------
    # Google Analytics
    # ---------------

    endpoints = None

    api = Api(
        name='Google Analytics',
        description="Google Analytics is the go-to platform for millions of website and app owners seeking to gain a deeper understanding of their website and app performance. With Google Analytics, you can fine-tune your digital strategy, optimize your campaigns, and take your online presence to new heights.",
        base_url='https://analyticsdata.googleapis.com/v1beta/properties/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.google.com/analytics/devguides/reporting/data/v1',
        category='Business'
    )

    api.save()

    # ----------------
    # MailboxValidator
    # ---------------

    endpoints = None

    api = Api(
        name='MailboxValidator',
        description="Email Validation Services. Secure and reliable email validation service to check for invalid email addresses. It connects to the mail server and checks whether the mailbox exists or not. It reduces email bounce rate & costs. It increases conversion rate & sender reputation.",
        base_url='https://api.mailboxvalidator.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.mailboxvalidator.com/api-single-validation',
        category='Business'
    )

    api.save()

    # ----------------
    # mailgun
    # ---------------

    endpoints = None

    api = Api(
        name='Mailgun',
        description="Transactional Email Delivery Service & API for Developers. Try our email API and top-notch email sending service designed for developers. Enhance your transactional email capabilities seamlessly.  ",
        base_url='https://api.mailgun.net',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://documentation.mailgun.com/docs/mailgun/quickstart-guide/quickstart',
        category='Business'
    )

    api.save()

    # ----------------
    # Mailjet
    # ---------------

    endpoints = None

    api = Api(
        name='Mailjet',
        description="Connect with your ideal customer, anywhere. All the email tools you need to hit the inbox. Discover our easy-to-use platform for designing and sending your email marketing campaigns, newsletters, and automated emails.",
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
        docs='https://www.mailjet.com/',
        category='Business'
    )

    api.save()

    # ----------------
    # markerapi
    # ---------------

    endpoints = None

    api = Api(
        name='MARKER',
        description="Use our trademark search API to search the US trademarks database (USPTO) based on a search string. Our API allows search by serial number, trademark, owner, upcoming expiration date, and product/service description. Sign up to integrate trademark data into your application.",
        base_url='https://markerapi.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=False,
        https=True,
        cors=None,
        docs='https://markerapi.com/',
        category='Business'
    )

    api.save()

    # ----------------
    # Trello
    # ---------------

    endpoints = None

    api = Api(
        name='Trello',
        description="The best way to build on top of Trello is to create a Power-Up! With Power-Ups you can add buttons to cards and boards, show previews of attachments on Trello cards, and much more - all inside of Trello! Power-Ups add extra functionality inside of Trello and let you and your team work with more perspective. Some Power-Ups help you automate your workflows, others give you a new view into the data you have stored in cards.",
        base_url='https://api.trello.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/',
        category='Business'
    )

    api.save()

    # ----------------
    # Tomba Email finder
    # ---------------

    endpoints = None

    api = Api(
        name='Tomba',
        description="Tomba, your unique B2B email finder and verifier, provides a distinctive lead database for effortless and effective outreach scaling.",
        base_url='https://api.tomba.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://tomba.io/api',
        category='Business'
    )

    api.save()

    # ----------------
    # Valid Email
    # ---------------

    endpoints = None

    api = Api(
        name='Clientsbee',
        description="With Clientsbee Embark on a journey of technological discovery with our advanced technographics data, designed to unveil the intricate layers of digital ecosystems and empower businesses with actionable insights.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=False,
        docs='https://clientsbee.com/',
        category='Business'
    )

    api.save()

    # CALENDAR

    # ----------------
    # Abstract’s Holiday API
    # ---------------

    endpoints = None

    api = Api(
        name='Holidays API',
        description="Retrieve religious, non-public and public holidays for 200+ countries worldwide and for any specific year",
        base_url='https://holidays.abstractapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://docs.abstractapi.com/holidays',
        category='Calendar'
    )

    api.save()

    # ----------------
    # Byabbe
    # ---------------

    endpoints = None

    api = Api(
        name='Wikipedia, On this Day',
        description="This API can be used to retrieve birth, deaths, and events for any given day of the year. The data is all harvested from Wikipedia and therefore licensed under Creative Commons Attribution-ShareAlike 3.0 Unported License. The API itself is available as-is. Just keep calm and query on.",
        base_url='https://byabbe.se/on-this-day',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://byabbe.se/on-this-day/#/',
        category='Calendar'
    )

    api.save()

    # ----------------
    # Calendar Index
    # ---------------

    endpoints = None

    api = Api(
        name='CALENDARIFIC',
        description="Welcome to the Calendarific Global Holidays API. We cover over 230 countries and 3000 states around the world. We are constantly adding new countries and states. Feel free to send us an email if your country is not included in the list. This document covers how to use our API. Let us know if you have any questions. The Calendarific API is built on REST principles. Authenticated users can interact with any of our URIs by using the specified HTTP request method. We enforce using SSL encryption by issuing requests through HTTPS.",
        base_url='https://calendarific.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://calendarific.com/api-documentation',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Church Calendar
    # ---------------

    endpoints = None

    api = Api(
        name='Liturgical Calendar API',
        description="The API provides access to Roman Catholic liturgical calendar according to the norms set forth by the liturgical reform after the II Vatican Council. Several Sanctorale calendars are available and others can be added easily.",
        base_url='http://calapi.inadiutorium.cz',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='http://calapi.inadiutorium.cz/api-doc',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Czech Namedays Calendar
    # ---------------

    endpoints = None

    api = Api(
        name='Svátky API',
        description="Lookup for a name and returns nameday date",
        base_url='https://svatky.adresa.info/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://svatky.adresa.info/',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Google Calendar
    # ---------------

    endpoints = None

    api = Api(
        name='Google Calendar',
        description="Enhance the Google Calendar experience. Insert interactive content, powered by your account data or an external service, with add-ons.",
        base_url='https://www.googleapis.com/calendar/v3/calendars',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.google.com/workspace/calendar/api/guides/overview',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Hebrew Calendar
    # ---------------

    endpoints = None

    api = Api(
        name='Hebrew Calendar',
        description="Our mission at Hebcal.com is to increase awareness of Jewish holidays and to help Jews to be observant of the mitzvot. You can embed Hebcal.com content directly onto your synagogue website with our JavaScript, JSON and RSS APIs.",
        base_url='https://www.hebcal.com/hebcal',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.hebcal.com/home/195/jewish-calendar-rest-api',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Holidays
    # ---------------

    endpoints = None

    api = Api(
        name='Holiday API',
        description="Stop maintaining holiday data. Start building what matters. Fresh, accurate holiday data—just an API call away. Skip the scraping. Ditch the spreadsheets.",
        base_url='https://holidayapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://holidayapi.com/docs',
        category='Calendar'
    )

    api.save()

    # ---------------
    # Nager.Date
    # ---------------

    endpoints = None

    api = Api(
        name='Public Holiday Api',
        description="The api provides a simple way to query the holidays of over 100 countries, also it is possible to query long weekends. For IoT devices there is an endpoint to check if today is a holiday",
        base_url='https://date.nager.at/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://date.nager.at/Api',
        category='Calendar'
    )

    api.save()

    # ---------------
    # TimeZones iCal Library
    # ---------------

    endpoints = None

    api = Api(
        name='TimeZones iCal Library',
        description="The convenient way to directly access the most recent official time zone information for iCalendar files with JavaScript.",
        base_url='https://tz.add-to-calendar-technology.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://tz.add-to-calendar-technology.com/',
        category='Calendar'
    )

    api.save()

    # Cloud storage and File Sharing

    # ----------------
    # Box
    # ---------------

    endpoints = None

    api = Api(
        name='Box',
        description="All the developer resources to help you get the most from Box products",
        base_url='https://api.box.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.box.com/reference/',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # ----------------
    # Dropbox
    # ---------------

    endpoints = None

    api = Api(
        name='Dropbox',
        description="Dropbox delivers tools that help you move your work forward faster, keep it safe, and let you collaborate with ease.",
        base_url='https://www.dropbox.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.dropbox.com/developers/documentation',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # ----------------
    # Google Drive
    # ---------------

    endpoints = None

    api = Api(
        name='Google Drive',
        description="Enhance the Google Drive experience. Insert interactive content, powered by your account data or an external service, with add-ons. Show a custom interface for uploading files from Drive into your third-party service. Enable users to quickly create files from custom templates.",
        base_url='https://www.googleapis.com/drive/v3/files',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.google.com/workspace/drive',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # ----------------
    # OneDrive
    # ---------------

    endpoints = None

    api = Api(
        name='OneDrive',
        description="The OneDrive & SharePoint developer platform provides the APIs, components, and tools to access files and content across Microsoft 365, including: OneDrive personal, OneDrive for Business, SharePoint Online",
        base_url='https://graph.microsoft.com/v1.0',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://learn.microsoft.com/en-us/onedrive/developer/?view=odsp-graph-online',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # ----------------
    # Pastebin
    # ---------------

    endpoints = None

    api = Api(
        name='PASTEBIN',
        description="Pastebin is a website where you can store any text online for easy sharing. The website is mainly used by programmers to store pieces of sources code or configuration information, but anyone is more than welcome to paste any type of text. The idea behind the site is to make it more convenient for people to share large amounts of text online.",
        base_url='https://pastebin.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://pastebin.com/doc_api',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # ----------------
    # Mega.nz
    # ---------------

    endpoints = None

    api = Api(
        name='MEGA',
        description="Securely store files of any size. Backup important folders, sync items across multiple devices, and share files with total control and privacy.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://mega.io/developers',
        category='Cloud storage and File Sharing'
    )

    api.save()

    # Continuous Integration

    # ----------------
    # CircleCI
    # ---------------

    endpoints = None

    api = Api(
        name='CircleCI',
        description="We build CI/CD tooling to keep the world’s best engineers shipping great code. Engineering teams of all sizes use CircleCI to easily build, test, and deploy production-ready code. Focus on your code, and beyond. Trigger automatic tests whenever anything in your ecosystem changes: libraries, images, even LLMs.",
        base_url='https://circleci.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://circleci.com/docs/api/v2/index.html',
        category='Continuous Integration'
    )

    api.save()

    # ----------------
    # CloudBees Codeship
    # ---------------

    endpoints = None

    api = Api(
        name='CloudBees',
        description="CloudBees CI is a fully-featured, cloud native capability that can be hosted on-premise or in the public cloud used to deliver CI at scale. It provides a shared, centrally managed, self-service experience for all your development teams running Jenkins. CloudBees CI on modern cloud platforms is designed to run on Kubernetes. CloudBees CI on traditional platforms has been developed for on-premise installations.",
        base_url='https://api.codeship.com/v2',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.cloudbees.com/docs/cloudbees-codeship/latest/api-overview/',
        category='Continuous Integration'
    )

    api.save()

    # ----------------
    # Travis CI
    # ---------------

    endpoints = None

    api = Api(
        name='Travis CI',
        description="Sync your GitHub projects with Travis CI to test your code in minutes.",
        base_url='https://api.travis-ci.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.travis-ci.com/api',
        category='Continuous Integration'
    )

    api.save()

    # Cryptocurrency

    # ----------------
    # Bitquery
    # ---------------

    endpoints = None

    api = Api(
        name='Bitquery',
        description="Bitquery provides historical and real-time indexed data for 40+ blockchains through Graphql APIs, Websockets, SQL, and Cloud providers such as AWS, Snowflake, Google, Azure, Kafka etc. Get APIs for token trades, transfers, holders, transactions, address balances, Smart contract events, calls, NFT trades, transfers, etc.",
        base_url='https://streaming.bitquery.io/graphql',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://bitquery.io/',
        category='Cryptocurrency'
    )

    api.save()

    # ----------------
    # BitcoinAverage
    # ---------------

    endpoints = None

    api = Api(
        name='BitcoinAverage',
        description="Welcome to the BitcoinAverage API! The world's best and longest running Cryptocurrency price API provider. These APIs can be used to gather real-time, OHLC, volume and historical price data for the following Cryptocurrencies: Bitcoin (BTC), Bitcoin Cash (BCH), Litecoin (LTC), Ethereum (ETH), Dash (DASH), Ripple (XRP), Monero (XMR) plus many more.",
        base_url='https://apiv2.bitcoinaverage.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://apiv2.bitcoinaverage.com/',
        category='Cryptocurrency'
    )

    api.save()

    # ----------------
    # Bitmex
    # ---------------

    endpoints = None

    api = Api(
        name='Bitmex',
        description="BitMEX offers a fully featured REST API and a powerful streaming WebSocket API. All market and user data is available and updates in real-time. The BitMEX APIs are open and complete. Every function used by the BitMEX website is exposed via the API, allowing developers full control to build any kind of application on top of BitMEX.",
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
        docs='https://www.bitmex.com/app/apiOverview',
        category='Cryptocurrency'
    )

    api.save()

    # ----------------
    # Blockchain
    # ---------------

    endpoints = None

    api = Api(
        name='Blockchain.com',
        description="Bitcoin Payment, Wallet & Transaction Data",
        base_url='https://api.blockchain.com/exchange',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.blockchain.com/explorer/api',
        category='Cryptocurrency'
    )

    api.save()

    # Currency Exchange

    # ----------------
    # 1Forge
    # ---------------

    endpoints = None

    api = Api(
        name='1Forge',
        description="1Forge provides real-time quote data (bid & ask) for 700+ pairs. To see a full list of supported currency pairs, please see the full currency pair list. At this time, we do not offer historical data, however, clients are more than welcome to archive our quotes locally for internal use. By connecting directly to brokers and liquidity providers, we are able to provide data as fast as any ECN or brokerage. Depending on how active the market is, you can see price updates over 200 times per second for a single currency pair. No other quote provider in the world can match our accuracy, speed or level of service.",
        base_url='https://api.1forge.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://1forge.com/api',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # Currencylayer
    # ---------------

    endpoints = None

    api = Api(
        name='currencylayer',
        description="Currencylayer provides a simple REST API with real-time and historical exchange rates for 168 world currencies, delivering currency pairs in universally usable JSON format - compatible with any of your applications. Spot exchange rate data is retrieved from several major forex data providers in real-time, validated, processed and delivered hourly, every 10 minutes, or even within the 60-second market window. Providing the most representative forex market value available ('midpoint' value) for every API request, the currencylayer API powers currency converters, mobile applications, financial software components and back-office systems all around the world.",
        base_url='https://api.currencylayer.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://currencylayer.com/documentation',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # ExchangeRate-API
    # ---------------

    endpoints = None

    api = Api(
        name='',
        description="The Accurate & Reliable Exchange Rate API 🌍 Currency conversion rates for 161 currencies. 🏆 Over 14 years of exceptional uptime & support. ✅ Perfect for SaaS, Dashboards & E-Commerce. Hundreds of thousands of developers relax while our exchange rate API delivers forex rates, day-in, day-out!",
        base_url='https://v6.exchangerate-api.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.exchangerate-api.com/docs/overview',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # Exchangeratesapi.io
    # ---------------

    endpoints = None

    api = Api(
        name='exchangerates',
        description="With over 15 exchange rate data sources, the Exchangerates API is delivering exchanging rates data for more than 170 world currencies. This API has several endpoints, where each of them serves a different purpose, use case. The endpoints include functionalities like receiving the latest exchange rates information for a specific set, or for all currencies; conversion from one to another currency; receiving data Time-series for multiple or for one currency, and preserving the API daily for the fluctuation data.",
        base_url='https://api.exchangeratesapi.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://exchangeratesapi.io/documentation/',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # Fixer.io
    # ---------------

    endpoints = None

    api = Api(
        name='fixer',
        description="Powered by 15+ exchange rate data sources, the Fixer API is capable of delivering real-time exchange rate data for 170 world currencies. The API comes with multiple endpoints, each serving a different use case. Endpoint functionalities include getting the latest exchange rate data for all or a specific set of currencies, converting amounts from one currency to another, retrieving Time-Series data for one or multiple currencies and querying the API for daily fluctuation data.",
        base_url='https://data.fixer.io/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://fixer.io/documentation',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # Frankfurter
    # ---------------

    endpoints = None

    api = Api(
        name='Frankfurter',
        description="Frankfurter is a free, open-source currency data API that tracks reference exchange rates published by institutional and non-commercial sources like the European Central Bank. No usage caps or API keys. Works great client-side in the browser or mobile apps. The public API is available at api.frankfurter.dev. If preferred, you can self-host.",
        base_url='https://api.frankfurter.dev/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://frankfurter.dev/',
        category='Currency Exchange'
    )

    api.save()

    # ----------------
    # FxRatesAPI
    # ---------------

    endpoints = None

    api = Api(
        name='FxRatesAPI',
        description="Our API supports over 185 currencies and provides mid-market rates that are aggregated from more than 20 sources. Whether you're building a finance app, e-commerce platform, or simply need to convert currencies for your business, our API is designed to make the process quick and easy. This documentation will guide you through the steps of getting started with our API, including authentication, available endpoints, and response formats.",
        base_url='https://api.fxratesapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=False,
        docs='https://fxratesapi.com/docs',
        category='Currency Exchange'
    )

    api.save()

    # Data Validation

    # ----------------
    # Cloudmersive Validate
    # ---------------

    endpoints = None

    api = Api(
        name='Cloudmersive',
        description="Data Validation APIs. Validate key business data thoroughly.Email Address Validation. Validate whether an email is real when you accept it. Phone Number Validation. Validate and retrieve information for any phone number. Street Address Validation. Validate a street address, with full support for international addresses. VAT Number Validation. Validate and retrieve information for a VAT number or code. Domain Name Validation. Validate and retrieve WHOIS information for a domain name. Name Validation. Validate and extract information from names or code identifiers. IP Address Validation. Validate and retrieve key details about IP addresses, including geolocation.",
        base_url='https://api.cloudmersive.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://api.cloudmersive.com/',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # languagelayer
    # ---------------

    endpoints = None

    api = Api(
        name='languagelayer',
        description="Languagelayer is a simple and powerful REST API built to efficiently match text of any length to its corresponding language, cross-referencing single words, expressions and grammatical constructions, as well as taking into account any existing accents, dialects and other linguistic deviations. The languagelayer API relies on an ever-advancing, powerful and AI-based (Artificial Intelligence) detection algorithm, which increases in complexity and performance with each language detection API request performed. Only this way the languagelayer service can be capable of processing over 170 different languages & accents worldwide. In spite of its complexity behind the curtains, our language detection API continuously manages to stand out due to its easy-to-use REST interface, simple JSON response format, quick response time and low bandwidth consumption.",
        base_url='http://api.languagelayer.com/detect',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://languagelayer.com/documentation',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # Lob.com
    # ---------------

    endpoints = None

    api = Api(
        name='Lob',
        description="Your customer aren’t ignoring you. They just never saw your email. Or ad. Or social post. Digital overload is real. Lob is the antidote, powering personalized, automated, and trackable direct mail that outperforms digital (and other direct mail providers) at any scale.",
        base_url='https://api.lob.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.lob.com/',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # mailboxlayer
    # ---------------

    endpoints = None

    api = Api(
        name='mailboxlayer',
        description="Mailboxlayer offers a simple REST-based JSON API enabling you to thoroughly check and verify email addresses right at the point of entry into your system. In addition to checking the syntax, the actual existence of an email address using MX-Records and the Simple Mail Transfer Protocol (SMTP), and detecting whether or not the requested mailbox is configured to catch all incoming mail traffic, the mailboxlayer API is linked to a number of regularly updated databases containing all available email providers, which simplifies the separation of disposable (e.g. mailinator) and free email addresses (e.g. gmail, yahoo) from individual domains. Combined with typo checks, did-you-mean suggestions and a numeric score reflecting the quality of each email address, these structures will make it simple to automatically filter 'real' customers from abusers and increase response and success rates of your email campaigns.",
        base_url='http://apilayer.net/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://mailboxlayer.com/documentation',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # NumValidate
    # ---------------

    endpoints = None

    api = Api(
        name='NumValidate',
        description="NumValidate is an open source REST API powered by Google LibPhoneNumber that provides a simple yet effective way to validate and format a phone number. We have language bindings in Shell, Javascript (JQuery), Ruby and Java! You can view code examples in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.",
        base_url='https://numvalidate.com/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://numvalidate.com/numvalidate-docs/index.html',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # numverify
    # ---------------

    endpoints = None

    api = Api(
        name='numverify',
        description="NumVerify offers a full-featured yet simple RESTful JSON API for national and international phone number validation and information lookup for a total of 232 countries around the world. Requested numbers are processed in real-time, cross-checked with the latest international numbering plan databases and returned in handy JSON format enriched with useful carrier, geographical location and line type data. Integrating the numverify API into your application will enable you to verify the validity of phone numbers at the point of entry, protecting you from fraud and increasing good leads.",
        base_url='http://apilayer.net/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://numverify.com/documentation',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # Phone Validation
    # ---------------

    endpoints = None

    api = Api(
        name='Trestle',
        description="Trestle provides identity data for businesses. This identity data is key for building and maintaining great customer relationships.",
        base_url='https://api.trestleiq.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://trestle-api.redoc.ly/',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # PurgoMalum
    # ---------------

    endpoints = None

    api = Api(
        name='PurgoMalum',
        description="PurgoMalum is a simple, free, RESTful web service for filtering and removing content of profanity, obscenity and other unwanted text. PurgoMalum's interface accepts several parameters for customization and can return results in plain text, XML and JSON. PurgoMalum is designed to remove words from input text, based on an internal profanity list (you may optionally add your own words to the profanity list through a request parameter (see Request Parameters below). It is designed to recognize character alternates often used in place of standard alphabetic characters, e.g. @ will be recognized as an a, $ will be recognized as an s, and so forth. PurgoMalum also utilizes a list of safe words, i.e. innocuous words which contain words from the profanity list (class for example). These safe words are excluded from the filter. If you discover any bugs or have any concerns, please contact me, and I will do my best to address them.",
        base_url='https://www.purgomalum.com/service',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.purgomalum.com/',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # US Autocomplete
    # ---------------

    endpoints = None

    api = Api(
        name='US Autocomplete',
        description="nter address data quickly with real-time address suggestions.",
        base_url='https://us-autocomplete-pro.api.smarty.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.smarty.com/docs/cloud',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # US Extract
    # ---------------

    endpoints = None

    api = Api(
        name='US Extract',
        description="Extract postal addresses from any text including emails.",
        base_url='https://us-extract.api.smarty.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.smarty.com/products/apis/us-extract-api',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # US Street Address
    # ---------------

    endpoints = None

    api = Api(
        name='US Street Address',
        description="Extract postal addresses from any text including emails",
        base_url='https://us-street.api.smarty.com/street-address',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.smarty.com/docs/cloud/us-street-api',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # vatlayer
    # ---------------

    endpoints = None

    api = Api(
        name='vatlayer',
        description="Vatlayer is a simple JSON-based REST API enabling you to validate VAT numbers, retrieve all or single EU VAT rates based on IP address or country code, convert prices in compliance with EU VAT rates and types, and more. API results are requested using a transparent and easy-to-understand URL structure and delivered in handy JSON format, making for the highest possible level of compatibility with any of your applications, systems, programming languages and frameworks. The following API documentation explains in detail API properties, parameters and features, provides integration guides and code examples for PHP and jQuery.ajax.",
        base_url='http://apilayer.net/api/validate',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://vatlayer.com/documentation',
        category='Data Validation'
    )

    api.save()

    # ----------------
    # Veriphone
    # ---------------

    endpoints = None

    api = Api(
        name='veriphone',
        description="Clean your contact list and prevent fraud by validating phone numbers. Veriphone will validate, format, lookup the carrier and line type of any phone number.",
        base_url='https://api.veriphone.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://veriphone.io/docs/v2',
        category='Data Validation'
    )

    api.save()

    # Development TODO

    # Dictionaries

    # ----------------
    # Lingua Robot
    # ---------------

    endpoints = None

    api = Api(
        name='Lingua Robot',
        description="English dictionary API providing an access to data of over 800 000 English lexical entries, such as words, phrasal verbs, multi-word expressions.",
        base_url='https://lingua-robot.p.rapidapi.com/language/v1/entries/en',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://linguarobot.docs.apiary.io/',
        category='Dictionaries'
    )

    api.save()

    # ----------------
    # Merriam-Webster
    # ---------------

    endpoints = None

    api = Api(
        name='Merriam-Webster',
        description="The Merriam-Webster Dictionary API gives developers access to a comprehensive resource of dictionary and thesaurus content as well as specialized medical, Spanish, ESL, and student-friendly vocabulary. Make your applications better by integrating our authoritative definitions, etymologies, audio pronunciations, synonyms and antonyms, and more. Our robust API empowers developers to enhance word games and create educational, language learning, and other word-related applications for the digital environment. We look forward to seeing all of the new, innovative products powered by Merriam-Webster's trusted references.",
        base_url='https://www.dictionaryapi.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://dictionaryapi.com/',
        category='Dictionaries'
    )

    api.save()

    # ----------------
    # Oxford
    # ---------------

    endpoints = None

    api = Api(
        name='Oxford Dictionaries',
        description="Oxford Dictionaries is at the forefront of lexical research and our products will help you succeed whether you are building a game, learning application, or next-generation speech and text technology",
        base_url='https://od-api-sandbox.oxforddictionaries.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=False,
        docs='https://developer.oxforddictionaries.com/documentation',
        category='Dictionaries'
    )

    api.save()

    # ----------------
    # Wordnik
    # ---------------

    endpoints = None

    api = Api(
        name='Wordnik',
        description="Request definitions, example sentences, spelling suggestions, synonyms and antonyms (and other related words), word phrases, pronunciations, random words, words of the day, and much more.",
        base_url='http://api.wordnik.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://developer.wordnik.com/docs',
        category='Dictionaries'
    )

    api.save()

    # ----------------
    # Words
    # ---------------

    endpoints = None

    api = Api(
        name='WORDSAPI',
        description="Use it to find definitions for more than 150,000 words. You can find synonyms, antonyms, or similar words. Words API includes hierarchical information.",
        base_url='https://wordsapiv1.p.mashape.com/words/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.wordsapi.com/docs/',
        category='Dictionaries'
    )

    api.save()

    # Disasters

    # ----------------
    # USGS
    # ---------------

    endpoints = None

    api = Api(
        name='USGS',
        description="This is an implementation of the FDSN Event Web Service Specification, and allows custom searches for earthquake information using a variety of parameters. Please note that automated applications should use Real-time GeoJSON Feeds for displaying earthquake information whenever possible, as they will have the best performance and availability for that type of information.",
        base_url='https://earthquake.usgs.gov/fdsnws/event/1/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://earthquake.usgs.gov/fdsnws/event/1/',
        category='Disasters'
    )

    api.save()

    # ----------------
    # RWLabs
    # ---------------

    endpoints = None

    api = Api(
        name='ReliefWeb API',
        description="The ReliefWeb API was originally built to power a mobile/ low-bandwidth version of the ReliefWeb website. Enhancements and a public release provided access to ReliefWeb's curated and continuously updated data archive. It's now used to serve much of the main site, content on other OCHA sites, and third party apps. All the content of ReliefWeb is available through its API. The API aligns with current API best-practices, and is intended to be friendly to developers, as well as machines. It is publicly accessible using HTTP requests and returns JSON data.",
        base_url='https://api.reliefweb.int/v1/reports',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://apidoc.reliefweb.int/',
        category='Disasters'
    )

    api.save()

    # ----------------
    # PredictHQ
    # ---------------

    endpoints = None

    api = Api(
        name='PredictHQ',
        description="Get up and running with the PredictHQ APIs. Explore our API Endpoints, API Guides, Data Science Guides and more.",
        base_url='https://api.predicthq.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://api.predicthq.com/docs/',
        category='Disasters'
    )

    api.save()

    # ----------------
    # Ambee
    # ---------------

    endpoints = None

    api = Api(
        name='ambee',
        description="Safeguard your business against disasters with natural disasters API. Ambee’s natural disasters API offers real-time data on disasters such as earthquakes, cyclones, floods, volcanoes, droughts, and forest fires. Fortify your business outcomes from their impact by integrating this API today.",
        base_url='https://api.ambeedata.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.ambeedata.com/',
        category='Disasters'
    )

    api.save()

    # Documents & Productivity TODO

    # Education

    # ----------------
    # Current Affairs
    # ---------------

    endpoints = None

    api = Api(
        name='Current Affairs Of India',
        description="This API will provides you with educational information and to help you compete in competative exams.",
        base_url='https://current-affairs-of-india.p.rapidapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://rapidapi.com/malaithiru370/api/current-affairs-of-india',
        category='Education'
    )

    api.save()

    # ----------------
    # NationNode
    # ---------------

    endpoints = None

    api = Api(
        name='NationNode',
        description="Empowering Your Apps with Global Knowledge. Effortlessly access accurate, country-specific data to power your apps. From population stats to currency details, our free API delivers it all—fast, reliable, and always up-to-date.",
        base_url='https://countries-api-abhishek.vercel.app',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://github.com/Abhishekkjainn/countriesAPI/blob/main/README.md',
        category='Education'
    )

    api.save()

    # ----------------
    # Secrets-APi
    # ---------------

    endpoints = None

    api = Api(
        name='Secrets API',
        description="Welcome to the Secrets API. This API allows you to manage and retrieve secrets anonymously.",
        base_url='https://secrets-api.appbrewery.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='Basic',
        https=True,
        cors=None,
        docs='https://secrets-api.appbrewery.com/',
        category='Education'
    )

    api.save()

    # Environment

    # ----------------
    # AirVisual
    # ---------------

    endpoints = None

    api = Api(
        name='IQAir',
        description="AirVisual platform API. Unlock the power of real-time air quality data with IQAir's AirVisual platform API. Seamlessly integrate global air pollution insights into your apps, websites, or IoT platforms to deliver the most accurate information.",
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
        docs=None,
        category='Environment'
    )

    api.save()

    # ----------------
    # OpenAQ
    # ---------------

    endpoints = None

    api = Api(
        name='OpenAQ',
        description="The OpenAQ API provides open access to global air quality data, following REST principles with resource-oriented URLs, standard HTTP response codes, and JSON-formatted responses. OpenAQ focuses on criteria air pollutants, primarily aggregating PM2.5, PM10, SO2, NO2, CO, O3, BC, relative humidity and temperature measurement data. For a limited set of locations, we have data for PM1, PM4, CO2, NO, NOx, CH4 & UFP.",
        base_url='https://api.openaq.org/v3/locations',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.openaq.org/using-the-api/quick-start',
        category='Environment'
    )

    api.save()

    # ----------------
    # AQICN
    # ---------------

    endpoints = None

    api = Api(
        name='Air Quality Programmatic APIs',
        description="The JSON API can be used for advanced programmatic integration: Access to more than 11000 station-level and 1000 city-level data, Geo-location query (based on latitude/longitude or IP address), Individual AQI for all pollutants (PM2.5, PM10, NO2, CO, SO2, Ozone), Station name and coordinates, Originating EPA name and link, Current weather conditions, Stations within a map lat/lng bounds, Search stations by name, Air Quality forecast (for 3~8 days)",
        base_url='http://api.waqi.info',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://aqicn.org/json-api/doc/',
        category='Environment'
    )

    api.save()

    # ----------------
    # PVWatts
    # ---------------

    endpoints = None

    api = Api(
        name='PVWatts',
        description="PVWatts® Version 8 is is the current version of the PVWatts API. Updates from Version 6 include a bifacial module option, a new input for monthly irradiance losses, new inputs for specifying albedo, and updates to the photovoltaic module, inverter, and thermal effects models to use more detailed and industry-accepted algorithms. PVWatts V8 also updates the weather data to 2020 TMY data from the NREL National Solar Radiation Database (NSRDB) for locations covered by the database. (The NSRDB weather data used in PVWatts V6 is from around 2015.) This update provides production estimates based on the latest, state-of-the art models from NREL that may differ from the V6 estimates, depending on the location and inputs. From a coding perspective, PVWatts V8 replaces the pvwattsv5 compute module with pvwattsv8 so that the PVWatts Calculator, web API, and implementation of PVWatts in the System Advisor Model (SAM) all use the same underlying model.",
        base_url='https://developer.nrel.gov/api/pvwatts',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developer.nrel.gov/docs/solar/pvwatts/v8/',
        category='Environment'
    )

    api.save()

    # ----------------
    # UK Carbon Intensity
    # ---------------

    endpoints = None

    api = Api(
        name='Carbon Intensity API',
        description="National Energy System Operator’s Carbon Intensity API provides an indicative trend of regional carbon intensity of the electricity system in Great Britain (GB) up to 2 days ahead of real-time. It provides programmatic and timely access to both forecast and estimated carbon intensity data. The Carbon Intensity forecast includes CO2 emissions related to electricity generation only. The includes emissions from all large metered power stations, interconnector imports, transmission and distribution losses, and accounts for national electricity demand, embedded wind and solar generation.",
        base_url='https://api.carbonintensity.org.uk',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://carbon-intensity.github.io/api-definitions/#carbon-intensity-api-v2-0-0',
        category='Environment'
    )

    api.save()

    # ----------------
    # NOAA Climate Data
    # ---------------

    endpoints = None

    api = Api(
        name='NOAA Climate Data',
        description="NCDC's Climate Data Online (CDO) offers web services that provide access to current data. This API is for developers looking to create their own scripts or programs that use the CDO database of weather and climate data. An access token is required to use the API, and each token will be limited to five requests per second and 10,000 requests per day.",
        base_url='https://www.ncei.noaa.gov/cdo-web/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.ncdc.noaa.gov/cdo-web/webservices/v2',
        category='Environment'
    )

    api.save()

    # ----------------
    # WeatherStack
    # ---------------

    endpoints = None

    api = Api(
        name='Weatherstack',
        description="The weatherstack API was built to deliver accurate weather data for any application and use case, from real-time and historical weather information all the way to 14-day weather forecasts, supporting all major programming languages. Our straightforward API design will make it easy to use the API — continue reading below to get started.",
        base_url='https://api.weatherstack.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://weatherstack.com/documentation',
        category='Environment'
    )

    api.save()

    # Events

    # ----------------
    # Ticketmaster
    # ---------------

    endpoints = None

    api = Api(
        name='Ticketmaster',
        description="The Real Backstage Pass to Live Event Tap into the Ticketmaster open developer network which gives you the flexibility and scale to bring unforgettable live events to fans. It's our technology - your way.",
        base_url='https://app.ticketmaster.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developer.ticketmaster.com/products-and-docs/apis/getting-started/',
        category='Events'
    )

    api.save()

    # ----------------
    # Songkick
    # ---------------

    endpoints = None

    api = Api(
        name='Songkick',
        description="The Songkick API gives you easy access to the biggest live music database in the world: over 6 million upcoming and past concerts... and growing every day! Easily add concerts to your website or application. Use of the Songkick API will be subject to the standard terms of our partnership agreement and a license fee.",
        base_url='https://api.songkick.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.songkick.com/developer/getting-started',
        category='Events'
    )

    api.save()

    # Finance TODO

    # Food & Drink TODO

    # Fraud Prevention

    # ----------------
    # FraudLabs Pro
    # ---------------

    endpoints = None

    api = Api(
        name='FraudLabs Pro',
        description="Screen an order transaction for payment fraud. This REST API will detect all possibles fraud traits based on the input parameters supplied. The more input parameter supplied, the higher accuracy of fraud detection. Protect your online business by signing up for a FREE license.",
        base_url='https://api.fraudlabspro.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.fraudlabspro.com/developer/api/screen-order',
        category='Fraud Prevention'
    )

    api.save()

    # ----------------
    # Jumio
    # ---------------

    endpoints = None

    api = Api(
        name='Jumio',
        description="Jumio provides a variety of services for verifying the identities of your online users, as well as the Jumio Portal where you can configure and manage your transactions with Jumio. To get started:",
        base_url='https://account.amer-1.jumio.ai',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.jumio.com/production/Content/Resources/SwaggerUI/dist/indexAccount.html',
        category='Fraud Prevention'
    )

    api.save()

    # ----------------
    # Onfido
    # ---------------

    endpoints = None

    api = Api(
        name='onfido',
        description="Our mission is to make digital identity simple for everyone. We power open, secure, and inclusive relationships between businesses and their customers around the world. ",
        base_url='https://api.eu.onfido.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://documentation.onfido.com/api/latest/',
        category='Fraud Prevention'
    )

    api.save()

    # Games & Comics

    # Geocoding

    # Government

    # Health

    # Jobs

    # Machine Learning

    # Music

    # News

    # Open Data

    # Open Source Projects

    # Patent

    # Personality

    # Photography

    # Science & Math

    # Security

    # Shopping

    # Social

    # Sports & Fitness

    # Test Data

    # Text Analysis

    # Tracking

    # Transportation

    # URL Shorteners

    # Vehicle

    # Video

    # Weather

    return


    #----------------
    # Cats
    # ---------------

    endpoints = None

    api = Api(
        name='',
        description="",
        base_url='',
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