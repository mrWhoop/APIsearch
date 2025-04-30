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

    # Documents & Productivity

    # ---------------
    # Cloudmersive Document and Data Conversion
    # ---------------

    endpoints = None

    api = Api(
        name='Cloudmersive',
        description="Document and Data Conversion APIs. Convert files and content between file formats. Convert data between file formats. Instantly.",
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
        docs='https://cloudmersive.com/convert-api#documentation',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # DynamicDocs
    # ---------------

    endpoints = None

    api = Api(
        name='ADVICEment',
        description="Generate dynamic PDFs with JSON to PDF API based on LaTeX.",
        base_url='https://api.advicement.io/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://advicement.io/dynamic-documents-api/documentation/getting-started',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # File.io
    # ---------------

    endpoints = None

    api = Api(
        name='file.io',
        description="Simply upload a file, share the link, and after it is downloaded, the file is completely deleted. For added security, set an expiration on the file and it is deleted within a certain amount of time, even if it was never downloaded. All files are encrypted when stored on our servers.",
        base_url='https://www.file.io/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.file.io/developers',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # pdfEndpoint
    # ---------------

    endpoints = None

    api = Api(
        name='pdfEndpoint',
        description="Effortlessly Convert HTML and URLs to PDF. High-quality output, easy integration, and full control over formatting for all your HTML to PDF needs. All it takes is just a few lines of code and you can customize your output with a variety of options. Check our Documentation to learn how do that.",
        base_url='https://api.pdfendpoint.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://pdfendpoint.com/docs',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # pdflayer
    # ---------------

    endpoints = None

    api = Api(
        name='pdflayer',
        description="The pdflayer API was built to provide a quick and seamless way to automate HTML to PDF conversion in any application. Its lightweight RESTful infrastructure is based on an efficient combination of the most powerful PDF rendering engines available, making it the most cost-effective and reliable option for anyone looking to process small or large numbers of documents within short time windows. The pdflayer API comes with a full set of customization functionalities, including document configuration, a series of layout adjustment options, authentication and security, design and branding tweaks, and much more.",
        base_url='http://api.pdflayer.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://pdflayer.com/documentation',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # PrexView
    # ---------------

    endpoints = None

    api = Api(
        name='PrexView',
        description="Create documents programmatically. Transform your data from XML or JSON to high quality, beautiful and readable documents in PDF, HTML, PNG or JPG.",
        base_url='https://api.prexview.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://prexview.com/docs/',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # RenderPDF.io
    # ---------------

    endpoints = None

    api = Api(
        name='RenderPDF.io',
        description="Cheapest & easiest API to convert HTML to PDF. RenderPDF.io provides developer-friendly APIs to convert HTML to modern PDF 🥰. Leave the boring, hard & tedious tasks to RenderPDF.io. We'll give you the rendered PDF files in no time 😎.",
        base_url='https://renderpdf.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://docs.renderpdf.io/',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # Restpack
    # ---------------

    endpoints = None

    api = Api(
        name='restpack',
        description="HTML to PDF API: Simple PDF Conversion API you are looking for. Generate fully structured PDFs with few lines of code.",
        base_url='https://restpack.io/api/html2pdf',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://restpack.io/html2pdf',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # Todoist
    # ---------------

    endpoints = None

    api = Api(
        name='Todoist',
        description="Clarity, finally. Join 50+ million professionals who simplify work and life with the world’s #1 to-do list app. Capture tasks at the speed of thought. Achieve mental clarity by sorting tasks into Today, Upcoming, or using custom filters. See only what you need, when you need it. Make the most of your time. Schedule due dates, visualize your week in calendar view, and set recurring tasks with ease. Give your team a shared space to collaborate and stay on top of it all – alongside but separate from your personal tasks and projects.",
        base_url='https://api.todoist.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://todoist.com/api/v1/docs',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # Vector Express
    # ---------------

    endpoints = None

    api = Api(
        name='Vector Express',
        description="Free Vector Conversion Convert your vector files for free. We also offer an API!",
        base_url='https://vector.express/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/vector-express/vectorexpress-api',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # Vertopal
    # ---------------

    endpoints = None

    api = Api(
        name='Vertopal',
        description="Reliable & High-Performance File Conversion API. Create reliable desktop, mobile, and web applications using our powerful file conversion API.",
        base_url='https://api.vertopal.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=False,
        docs='https://www.vertopal.com/en/developer/api/introduction',
        category='Documents & Productivity'
    )

    api.save()

    # ---------------
    # WakaTime
    # ---------------

    endpoints = None

    api = Api(
        name='WakaTime',
        description="Dashboards for developers. Code stats, straight from your IDE. Automated time tracking leaderboards for programmers.",
        base_url='https://api.wakatime.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://wakatime.com/developers',
        category='Documents & Productivity'
    )

    api.save()

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

    # Finance

    # ---------------
    # Alpha Vantage
    # ---------------

    endpoints = None

    api = Api(
        name='Alpha Vantage',
        description="Stock Market Data API for Software Applications.  Realtime & historical stock market data APIs. Options, forex, crypto & other asset classes. 60+ technical & economic indicators. Market news API & sentiments. Global coverage",
        base_url='https://www.alphavantage.co',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.alphavantage.co/documentation/',
        category='Finance'
    )

    api.save()

    # ---------------
    # Barchart OnDemand
    # ---------------

    endpoints = None

    api = Api(
        name='barchart',
        description="Barchart features a diverse set of market data APIs that can be easily integrated into your website. Whether you're looking for a small, medium, large or enterprise solution, we'll create a custom package for you that exceeds your expectations. Explore our Market Data APIs below.",
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
        docs='https://www.barchart.com/ondemand/api',
        category='Finance'
    )

    api.save()

    # ---------------
    # Financial Data
    # ---------------

    endpoints = None

    api = Api(
        name='Financial Data',
        description="An Outstanding Collection Of Financial Data. Our API provides access to a variety of financial information. You can get end-of-day or intraday market data, examine company financial statements and ratios, access insider trading, institutional trading, or earnings release data. Additionally, you can explore alternative data to uncover unique investment opportunities.",
        base_url='https://financialdata.net/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://financialdata.net/documentation',
        category='Finance'
    )

    api.save()

    # ---------------
    # Financial Modeling Prep
    # ---------------

    endpoints = None

    api = Api(
        name='FMP',
        description="Financial data for every need. We provide one of the most accurate financial data available on the market. You can get historical prices, fundamental data, insider transactions, and much more that goes back 30 years in history.",
        base_url='https://financialmodelingprep.com/stable',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://site.financialmodelingprep.com/developer/docs/stable',
        category='Finance'
    )

    api.save()

    # ---------------
    # Fincept Insights
    # ---------------

    endpoints = None

    api = Api(
        name='FINCEPT',
        description="Welcome! TLK Industries Insights. Explore Financial Economic Market Trends Worldwide. Unlock Global Financial Insights with TLK Industries. Insight delivers data-driven solutions, helping businesses and individuals make smarter decisions and achieve sustained growth globally.",
        base_url='',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://insights.fincept.in/',
        category='Finance'
    )

    api.save()

    # ---------------
    # Plaid
    # ---------------

    endpoints = None

    api = Api(
        name='Plaid',
        description="Built to power the world of digital finance. Join the thousands of companies that use Plaid to increase conversion, lower fraud, and grow revenue.",
        base_url='https://production.plaid.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://plaid.com/docs/',
        category='Finance'
    )

    api.save()

    # ---------------
    # Razorpay IFSC
    # ---------------

    endpoints = None

    api = Api(
        name='Razorpay',
        description="Razorpay IFSC Toolkit. Process IFSC codes via our toolkit. Fire up your tools and query our API for the IFSC codes. An API to query IFSC codes. IFSC dataset available for download. Code to generate the dataset. A blog post on the 'why'.",
        base_url='https://ifsc.razorpay.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/razorpay/ifsc/wiki/API',
        category='Finance'
    )

    api.save()

    # ---------------
    # Tradier
    # ---------------

    endpoints = None

    api = Api(
        name='tradier',
        description="Send trades for US-based equities and options easily using the language of your choice. Real-time, delayed, and historical market data available through request/response and streaming interfaces. Easy APIs for registered entities to open an account, get it funded, and start trading. HTTP streaming APIs for streaming market data and limit charting data for Tradier Brokerage account holders.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=True,
        docs='https://documentation.tradier.com/',
        category='Finance'
    )

    api.save()

    # ---------------
    # World Trading Data
    # ---------------

    endpoints = None

    api = Api(
        name='marketstack',
        description="Obtain real-time stock data for more than 30,000 tickers down to the minute, request intraday quotes for tickers from IEX, or search 15+ years of accurate EOD historical market data. Easily integrate the API and make use of 30,000+ worldwide stock tickers with our Stock Price endpoint or integrate more than 500,000 tickers with our EOD endpoint collected from more global exchanges, including Nasdaq, NYSE, and more. We have built a simple, powerful and scalable REST API with an uptime of close to 100%. It will take you less than 5 minutes to get started. Get up and running quickly using the Free Plan, allowing for 100 data requests per month. Instant access, no contract or payment required.",
        base_url='https://api.marketstack.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://marketstack.com/documentation_v2',
        category='Finance'
    )

    api.save()

    # ---------------
    # YNAB
    # ---------------

    endpoints = None

    api = Api(
        name='YANB.API',
        description="A better outcome for your income. A tool to help you find yourself financially. Simplify spending and clarify priorities with the YNAB Method for maximizing money.",
        base_url='https://api.ynab.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=True,
        docs='https://api.ynab.com/',
        category='Finance'
    )

    api.save()

    # Food & Drink

    # ---------------
    # Edamam
    # ---------------

    endpoints = None

    api = Api(
        name='Edamam',
        description="Leading provider of nutrition data and analytics. Get free access to a database with close to 900,000 foods and over 680,000 unique UPC codes. License over 180,000 full recipes and nutrition for over 2.3 million web recipes. Search over 2.3 million recipes by diets, calories and nutrient ranges. Personalized meal recommendations using 28 nutrients and 40 diets/allergies. We track several hundred thousand recipes from over 500 sources to build live trends of what is being cooked, what is popular and what is new.",
        base_url='https://api.edamam.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developer.edamam.com/edamam-docs-nutrition-api',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # Open Brewery DB
    # ---------------

    endpoints = None

    api = Api(
        name='Open Brewery DB',
        description="Open Brewery DB is a free dataset and API with public information on breweries, cideries, brewpubs, and bottleshops. The goal of Open Brewery DB is to maintain an open-source, community-driven dataset and provide a public API for brewery-related data.",
        base_url='https://api.openbrewerydb.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://www.openbrewerydb.org/documentation',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # PunkAPI
    # ---------------

    endpoints = None

    api = Api(
        name='PunkAPI',
        description="A FastAPI-based project that serves as a digital archive of BrewDog's DIY Dog beers. It provides an API to access detailed information about each beer, including its recipe and associated image. The catalog data was initially extracted from a PDF document and transformed into JSON and PNG files. These files are placed in data and img folders according to their sequential number within the catalog. So, PunkAPI offers an interface to interact with this data.",
        base_url='https://punkapi.online',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://github.com/alxiw/punkapi',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # Spoonacular
    # ---------------

    endpoints = None

    api = Api(
        name='spoonacular',
        description="Our knowledge engineers spent years crafting our complex food ontology, which allows us to understand the relationships between ingredients, recipes, nutrition, allergens, and more.",
        base_url='https://api.spoonacular.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://spoonacular.com/food-api/docs',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # The Report of the Week
    # ---------------

    endpoints = None

    api = Api(
        name='The Report of the Week',
        description="This API returns all reviews done on The Report of the Week youtube channel",
        base_url='https://www.thereportoftheweek.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/andyklimczak/TheReportOfTheWeek-API',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # TheCocktailDB
    # ---------------

    endpoints = None

    api = Api(
        name='TheCocktailDB',
        description="An open, crowd-sourced database of drinks and cocktails from around the world. We also offer a free cocktail API for anyone wanting to use it.",
        base_url='www.thecocktaildb.com/api/json',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.thecocktaildb.com/api.php',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # TheMealDB
    # ---------------

    endpoints = None

    api = Api(
        name='TheMealDB',
        description="Welcome to TheMealDB: An open, crowd-sourced database of recipes from around the world. We offer a free recipe API for anyone wanting to use it, with additional premium features if required.",
        base_url='www.themealdb.com/api/json',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.themealdb.com/api.php',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # What’s on the menu?
    # ---------------

    endpoints = None

    api = Api(
        name='What’s on the menu?',
        description="There's a lot of data behind The New York Public Library's What's On The Menu?, and here's your chance to explore it. This is built for programmers and power-users, so if you're looking for an easier way to explore the dataset you may want to take a look at our Biweekly data exports, which are in CSV format. However if you're looking to do powerful analysis of historical menu data, this is the tool for you.",
        base_url='http://api.menus.nypl.org/menus',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://nypl.github.io/menus-api/',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # WhiskyHunter
    # ---------------

    endpoints = None

    api = Api(
        name='WhiskyHunter',
        description="Tools For Collectors, Traders & Whisky Lovers! We monitor data from 29 whisky auctions. Our database contains 4488618 past & 19003 records from live auctions. We also keep an eye on major online retailers.",
        base_url='https://whiskyhunter.net/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://whiskyhunter.net/api/',
        category='Food & Drink'
    )

    api.save()

    # ---------------
    # Zestful
    # ---------------

    endpoints = None

    api = Api(
        name='Zestful',
        description="Zestful's ingredient parser API turns plain recipe strings into beautiful, structured JSON data. Zestful makes recipe apps smarter about managing ingredients. Zestful transforms ingredients from opaque strings to meaningful data in easy-to-consume JSON format.",
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
        docs='https://zestfuldata.com/docs',
        category='Food & Drink'
    )

    api.save()

    # Fraud Prevention

    # ---------------
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

    # Games & Comics TODO

    # Geocoding TODO

    # Government TODO

    # Health

    # ---------------
    # Healthcare.gov
    # ---------------

    endpoints = None

    api = Api(
        name='Healthcare.gov',
        description="Educational content about the US Health Insurance Marketplace",
        base_url='https://www.healthcare.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.healthcare.gov/developers/',
        category='Health'
    )

    api.save()

    # ---------------
    # ICD-10 Codes
    # ---------------

    endpoints = None

    api = Api(
        name='ICD-10-CM',
        description="ICD-10-CM (International Classification of Diseases, 10th Revision, Clinical Modification) is a medical coding system for classifying diagnoses and reasons for visits in U.S. health care settings.",
        base_url='https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://clinicaltables.nlm.nih.gov/apidoc/icd10cm/v3/doc.html',
        category='Health'
    )

    api.save()

    # ---------------
    # Lexigram
    # ---------------

    endpoints = None

    api = Api(
        name='Lexigram',
        description="Lexigram provides users with a simple, easy-to-use interface for extracting targeted information from the patient record while preserving the rich contextual data that doctors work so hard to capture.",
        base_url='https://app.lexigram.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.lexigram.io/',
        category='Health'
    )

    api.save()

    # ---------------
    # Makeup
    # ---------------

    endpoints = None

    api = Api(
        name='Makeup API',
        description="Makeup Information",
        base_url='http://makeup-api.herokuapp.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='http://makeup-api.herokuapp.com/',
        category='Health'
    )

    # ---------------
    # Medicare
    # ---------------

    endpoints = None

    api = Api(
        name='CMS.gov',
        description="CMS is the federal agency that provides health coverage to more than 160 million through Medicare, Medicaid, the Children's Health Insurance Program, and the Health Insurance Marketplace. CMS works in partnership with the entire health care community to improve quality, equity and outcomes in the health care system.",
        base_url='https://data.cms.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://data.cms.gov/provider-data/docs',
        category='Health'
    )

    api.save()

    # ---------------
    # NPPES
    # ---------------

    endpoints = None

    api = Api(
        name='NPPES NPI Registry',
        description="National Plan & Provider Enumeration System, info on healthcare providers registered in US. NPI Registry Public Search is a free directory of all active National Provider Identifier (NPI) records. Healthcare providers acquire their unique 10-digit NPIs to identify themselves in a standard way throughout their industry.",
        base_url='https://npiregistry.cms.hhs.gov/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://npiregistry.cms.hhs.gov/api-page',
        category='Health'
    )

    api.save()

    # ---------------
    # Nutritionix
    # ---------------

    endpoints = None

    api = Api(
        name='Nutritionix',
        description="Our goal is to make it easier to understand what you eat. Through our interactive nutrition tools and world-renowned nutrition database, we help millions of consumers understand nutrition every single day.",
        base_url='https://api.uat.syndigo.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docx.syndigo.com/developers/docs/nutritionix-api-guide',
        category='Health'
    )

    api.save()

    # ---------------
    # openFDA
    # ---------------

    endpoints = None

    api = Api(
        name='openFDA',
        description="openFDA is an Elasticsearch-based API that serves public FDA data about nouns like drugs, devices, and foods. Not all data in openFDA has been validated for clinical or production use. And because openFDA only serves publicly available data, it does not contain data with Personally Identifiable Information about patients or other sensitive information.",
        base_url='https://api.fda.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://open.fda.gov/apis/',
        category='Health'
    )

    api.save()

    # Jobs

    # ---------------
    # Adzuna
    # ---------------

    endpoints = None

    api = Api(
        name='adzuna',
        description="Get the very latest ads and data with Adzuna's API. Get job ads to display on your own website. Use Adzuna's up-to-the-minute employment data to power your own website, reporting and data visualisations.",
        base_url='https://api.adzuna.com/v1/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developer.adzuna.com/overview',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Careerjet
    # ---------------

    endpoints = None

    api = Api(
        name='careerjet',
        description="Careerjet is a job search engine designed to make the process of finding a job on the internet easier for the user. It maps the huge selection of job offerings available on the internet in one extensive database by referencing job listings originating from job boards, recruitment agency websites and large specialist recruitment sites. Using a fast and straightforward interface, users can query this database and save themselves the trouble of visiting each site individually. The job offerings themselves are not hosted by Careerjet and users are always redirected to the original job listing. Essentially, Careerjet acts as traffic driver to those sites. Careerjet's job search engine network encompasses over 90 countries, featuring separate interfaces that are translated into 28 languages.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://www.careerjet.com/partners/api/',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Jobicy
    # ---------------

    endpoints = None

    api = Api(
        name='JOBICY',
        description="Seeking to enhance your remote job feed with top-tier opportunities? Discover the power of Jobicy’s public API, RSS and XML feeds! Effortlessly integrate our expansive selection of remote job listings into your platform. Transform your job feed into a gateway of career possibilities!",
        base_url='https://jobicy.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://jobicy.com/jobs-rss-feed',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Jobs2Careers
    # ---------------

    endpoints = None

    api = Api(
        name='Jobs2Careers',
        description=" By becoming a Jobs2Careers Publisher, you are able to add rich job content to your website and monetize your current traffic. You'll be providing a great jobseeker experience, and partnering with one of the largest job aggregators in the world.  There are 3 ways to access our jobs: 1. Job Search API 2. XML Feed 3. Widget ",
        base_url='http://api.jobs2careers.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='http://api.jobs2careers.com/api/spec.pdf',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Juju
    # ---------------

    endpoints = None

    api = Api(
        name='Juju',
        description="Juju smarter job search. Search jobs from sites all over the web!",
        base_url='http://www.juju.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://www.juju.com/publisher/spec/',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Reed
    # ---------------

    endpoints = None

    api = Api(
        name='reed.co.uk',
        description="Founded in 1995, Reed.co.uk was the first recruitment website offered by a recruitment agency in the UK. Since then, Reed.co.uk has grown to become one of the UK's leading jobs and careers site.",
        base_url='https://www.reed.co.uk/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.reed.co.uk/developers',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Search.gov Jobs
    # ---------------

    endpoints = None

    api = Api(
        name='USAJOBS',
        description="Find your federal government job.",
        base_url='https://data.usajobs.gov/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://developer.usajobs.gov/api-reference/',
        category='Jobs'
    )

    api.save()

    # ---------------
    # The Muse
    # ---------------

    endpoints = None

    api = Api(
        name='The Muse',
        description="The Muse is the go-to destination for the next-generation workforce to research companies and careers. More than 70 million visitors each year trust our two platforms, The Muse and Fairygodboss, to help them win at work, from professional advancement and skills-building techniques to finding a new job. We believe great ideas can come from anywhere, and support a collaborative environment with open participation from people who have different ideas, experiences, and perspectives. It’s our diverse team that makes The Muse an interesting and innovative place to work.",
        base_url='https://www.themuse.com/api/public',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.themuse.com/developers/api/v2',
        category='Jobs'
    )

    api.save()

    # ---------------
    # Upwork
    # ---------------

    endpoints = None

    api = Api(
        name='Upwork',
        description="Connecting clients in need to freelancers who deliver. Integrate Upwork functionalities to your web-based or mobile apps. Upwork Developers Site offers you access to our web services to build your own applications and to integrate our features and workflow to your dashboards, websites and management systems.",
        base_url='https://api.upwork.com/graphql',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.upwork.com/developer/documentation/graphql/api/docs/index.html',
        category='Jobs',
        type='GraphQL'
    )

    api.save()

    # Machine Learning

    # ---------------
    # Cloudmersive
    # ---------------

    endpoints = None

    api = Api(
        name='Cloudmersive',
        description="Powerful Deep Learning Image Recognition and Processing APIs. Advanced Machine Learning APIs for recognizing and processing images.",
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
        docs='https://api.cloudmersive.com/docs/convert.asp',
        category='Machine Learning'
    )

    api.save()

    # ---------------
    # Keen IO
    # ---------------

    endpoints = None

    api = Api(
        name='Keen',
        description="The Fully Managed Event Streaming Platform. Event Streaming API for developers, built on Apache Kafka®, Storm®, and Cassandra®. Flexible Event Streaming that Scales with Your Application.",
        base_url='https://api.keen.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://keen.io/docs/api/',
        category='Machine Learning'
    )

    api.save()

    # ---------------
    # Unplugg
    # ---------------

    endpoints = None

    api = Api(
        name='Unplugg API',
        description="This API currently provides forecasting for timeseries data that you can test below. You can use it to forecast energy comsuption, temperature, or any other timeseries data which has some seasonality effect.",
        base_url='https://api.unplu.gg',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://unplu.gg/test_api.html',
        category='Machine Learning'
    )

    api.save()

    # ---------------
    # Wit.ai
    # ---------------

    endpoints = None

    api = Api(
        name='wit.ai',
        description="Build Natural Language Experiences. Enable people to interact with your products using voice and text. Easily create bots that people can chat on their preferred messaging platform. Make multimodal interaction available to anyone, anywhere through the apps you create. Enable people to use their voices to control smart speakers, appliances, lighting and more. Create customizable expiriences for people, whethr they're at home or on the go.",
        base_url='https://api.wit.ai',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://wit.ai/docs',
        category='Machine Learning'
    )

    api.save()

    # Music

    # ---------------
    # AI Mastering
    # ---------------

    endpoints = None

    api = Api(
        name='AI Mastering',
        description="Automated Music Mastering",
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
        docs='https://app.swaggerhub.com/apis/aimastering/aimastering/1.0.0',
        category='Music'
    )

    api.save()

    # ---------------
    # Bandsintown
    # ---------------

    endpoints = None

    api = Api(
        name='Bandsintown',
        description="The Bandsintown API is designed for artists and enterprises representing artists. It offers read-only access to artist info and artist events: artist info: returns the link to the Bandsintown artist page, the link to the artist photo, the current number of trackers and more artist events: returns the list of events including their date and time, venue name and location, ticket links, lineup, description, title, and the link to the Bandsintown event page",
        base_url='https://rest.bandsintown.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://app.swaggerhub.com/apis/Bandsintown/PublicAPI/3.0.1',
        category='Music'
    )

    api.save()

    # ---------------
    # Discogs
    # ---------------

    endpoints = None

    api = Api(
        name='Discogs',
        description="Unlock the Ultimate Record Collecting Experience. Discover essential tools for your record collecting journey with Discogs. Experience unparalleled music discovery, comprehensive collection management, and a vibrant community revolutionizing record collecting.",
        base_url='https://api.discogs.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.discogs.com/developers/',
        category='Music'
    )

    api.save()

    # ---------------
    # Freesound
    # ---------------

    endpoints = None

    api = Api(
        name='Freesound',
        description="With the Freesound API you can browse, search, and retrieve information about Freesound users, packs, and the sounds themselves of course. You can find similar sounds to a given target (based on content analysis) and retrieve automatically extracted features from audio files, as well as perform advanced queries combining content analysis features and other metadata (tags, etc…). With the Freesound API, you can also upload, comment, rate and bookmark sounds!",
        base_url='https://freesound.org/apiv2',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://freesound.org/docs/api/overview.html',
        category='Music'
    )

    api.save()

    # ---------------
    # Genius
    # ---------------

    endpoints = None

    api = Api(
        name='Genius',
        description="Genius is the world’s biggest collection of song lyrics and musical knowledge.",
        base_url='https://api.genius.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://docs.genius.com/#/getting-started-h1',
        category='Music'
    )

    api.save()

    # ---------------
    # Genrenator
    # ---------------

    endpoints = None

    api = Api(
        name='Binary Jazz',
        description="Much like Binary Jazz itself, the genrenator is the product of a bunch of us chatting and tossing ideas around and something sticks. In this case, it came from a discussion about obscure genres we didn't know existed, veered to the Every Noise At Once database that Spotify uses to inform their genres and playlists, and ended with the question what if we could create an API that served random genres? The Genrenator Twitter bot is also a product of this.",
        base_url='https://binaryjazz.us/wp-json/genrenator',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://binaryjazz.us/genrenator-api/',
        category='Music'
    )

    api.save()

    # ---------------
    # Jamendo
    # ---------------

    endpoints = None

    api = Api(
        name='Jamendo',
        description="Please use our Api to build awesome music applications, support independent artists and express your creativity through mash-ups and innovative products! We provide more than 20 different read methods to access a catalog of half-a-million tracks, some powerful features for music discovery like search and radios, OAuth2 based authentication, 5 write methods to manage user library, and a website to monitor your app statistics.",
        base_url='https://api.jamendo.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.jamendo.com/v3.0/docs',
        category='Music'
    )

    api.save()

    # ---------------
    # KKBOX
    # ---------------

    endpoints = None

    api = Api(
        name='KKBOX',
        description="Get music libraries, playlists, charts, and perform out of KKBOX's platform",
        base_url='https://api.kkbox.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://docs-en.kkbox.codes/',
        category='Music'
    )

    api.save()

    # ---------------
    # LastFm
    # ---------------

    endpoints = None

    api = Api(
        name='last.fm',
        description="Explore Top Music Powered by your Scrobbles. We bring together your favourite music services and join up listening, watching and sharing to connect your musical world. Below you can visualise, in real-time, the listening habits & trends of Last.fm's global community. Go Explore.",
        base_url='http://ws.audioscrobbler.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.last.fm/api/intro',
        category='Music'
    )

    api.save()

    # ---------------
    # Lyrics.ovh
    # ---------------

    endpoints = None

    api = Api(
        name='Lyrics.ovh',
        description="Simple API to retrieve the lyrics of a song.",
        base_url='https://api.lyrics.ovh',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://lyricsovh.docs.apiary.io/#reference/0/lyrics-of-a-song/search',
        category='Music'
    )

    api.save()

    # ---------------
    # Mixcloud
    # ---------------

    endpoints = None

    api = Api(
        name='Mixcloud',
        description="Play, share and make money from music. Use Mixcloud to play any music you like, build communities and get paid directly. We take care of the music copyright for you.",
        base_url='https://api.mixcloud.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.mixcloud.com/developers/',
        category='Music'
    )

    api.save()

    # ---------------
    # MusicBrainz
    # ---------------

    endpoints = None

    api = Api(
        name='MusicBrainz',
        description="MusicBrainz is a community-maintained open source encyclopedia of music information. This means that anyone — including you — can help contribute to the project by adding information about your favorite artists and their works. In 2000, Gracenote took over the free CDDB project and commercialized it, essentially charging users for accessing the very data they themselves contributed. In response, Robert Kaye founded MusicBrainz. The project has since grown rapidly from a one-man operation to an international community of enthusiasts that appreciates both music and music metadata. Along the way, the scope of the project has expanded from its origins as a mere CDDB replacement to the true music encyclopedia MusicBrainz is today. As an encyclopedia and as a community, MusicBrainz exists only to collect as much information about music as we can. We do not discriminate or prefer one type of music over another, and we try to collect information about as many different types of music as possible. Whether it is published or unpublished, popular or fringe, western or non-western, human or non-human — we want it all in MusicBrainz.",
        base_url='https://musicbrainz.org/ws/2',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://musicbrainz.org/doc/MusicBrainz_API',
        category='Music'
    )

    api.save()

    # ---------------
    # Musixmatch
    # ---------------

    endpoints = None

    api = Api(
        name='musixmatch',
        description="Lyrics API. The Musixmatch Lyrics API allows you to get access to Musixmatch metadata about song and lyrics.",
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
        docs='https://docs.musixmatch.com/lyrics-api/introduction',
        category='Music'
    )

    api.save()

    # ---------------
    # Openwhyd
    # ---------------

    endpoints = None

    api = Api(
        name='openwhyd',
        description="Openwhyd is a free and open-source music curation service that allows users to create playlists of music tracks from various streaming platforms (YouTube, SoundCloud, Vimeo, Deezer…) and to discover the music posted by other users.",
        base_url='https://openwhyd.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://openwhyd.github.io/openwhyd/API',
        category='Music'
    )

    api.save()

    # ---------------
    # Songkick
    # ---------------

    endpoints = None

    api = Api(
        name='Songkick',
        description="The best api for live music. The Songkick API gives you easy access to the biggest live music database in the world: over 6 million upcoming and past concerts... and growing every day! Easily add concerts to your website or application.",
        base_url='https://api.songkick.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.songkick.com/developer/getting-started',
        category='Music'
    )

    api.save()

    # ---------------
    # SoundCloud
    # ---------------

    endpoints = None

    api = Api(
        name='SoundCloud',
        description="Discover. Get Discovered. Discover your next obsession, or become someone else’s. SoundCloud is the only community where fans and artists come together to discover and connect through music.",
        base_url='https://developers.soundcloud.com/docs/api/explorer/open-api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.soundcloud.com/docs/api/explorer/open-api',
        category='Music'
    )

    api.save()

    # ---------------
    # Spotify
    # ---------------

    endpoints = None

    api = Api(
        name='Spotify',
        description="etrieve metadata from Spotify content or control playback. Spotify Web API enables the creation of applications that can interact with Spotify's streaming service, such as retrieving content metadata, creating and managing playlists, or controlling playback.",
        base_url='https://api.spotify.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.spotify.com/documentation/web-api',
        category='Music'
    )

    api.save()

    # ---------------
    # TasteDive
    # ---------------

    endpoints = None

    api = Api(
        name='test_dive',
        description="TasteDive (formerly TasteKid) helps you discover new music, movies, TV shows, books, authors, games, podcasts, and people with shared interests. As a visitor, you can get instant suggestions using our recommendation engine. You can also hang around a bit longer, create a taste profile, discover interesting people, and learn about cool bands, movies, books or games from their profiles.",
        base_url='https://tastedive.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://tastedive.com/read/api',
        category='Music'
    )

    api.save()

    # ---------------
    # TheAudioDB
    # ---------------

    endpoints = None

    api = Api(
        name='TheAudioDB',
        description="https://theaudiodb.com/api",
        base_url='TheAudioDB is a community Database of audio artwork and metadata with a free music API. The content here is only possible thanks to the hard work of our editors.',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.theaudiodb.com/api_guide.php',
        category='Music'
    )

    api.save()

    # News

    # ---------------
    # Associated Press
    # ---------------

    endpoints = None

    api = Api(
        name='Associated Press',
        description="Build powerful integrations with our APIs and Metadata Services. Looking for seamless access to AP news content, metadata or elections data? AP has the right API for you.",
        base_url='https://api.ap.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://api.ap.org/media/v/docs/',
        category='News'
    )

    api.save()

    # ---------------
    # Chronicling America
    # ---------------

    endpoints = None

    api = Api(
        name='Chronicling America',
        description="Chronicling America provides access to information about historic newspapers and select digitized newspaper pages. To encourage a wide range of potential uses, we designed several different views of the data we provide, all of which are publicly visible. Each uses common Web protocols, and access is not restricted in any way. You do not need to apply for a special key to use them. Together they make up an extensive application programming interface (API) which you can use to explore all of our data in many ways.",
        base_url='https://chroniclingamerica.loc.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://chroniclingamerica.loc.gov/about/api/',
        category='News'
    )

    api.save()

    # ---------------
    # Currents
    # ---------------

    endpoints = None

    api = Api(
        name='Currents',
        description="Curate and Analyze Online News Effortlessly with Currents News API. Currents News API provides a comprehensive solution for curating global news and delivering it in a parsable format.",
        base_url='https://api.currentsapi.services',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://currentsapi.services/en/docs/',
        category='News'
    )

    api.save()

    # ---------------
    # Feedbin
    # ---------------

    endpoints = None

    api = Api(
        name='Feedbin',
        description="RSS reader",
        base_url='https://api.feedbin.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://github.com/feedbin/feedbin-api',
        category='News'
    )

    api.save()

    # ---------------
    # Finlight
    # ---------------

    endpoints = None

    api = Api(
        name='finlight.me',
        description="Get Real-Time News and Deep Insights with our Financial News API",
        base_url='https://api.finlight.me',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://docs.finlight.me/',
        category='News'
    )

    api.save()

    # ---------------
    # New York Times
    # ---------------

    endpoints = None

    api = Api(
        name='New York Times',
        description="Provides news from New York Times.",
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
        docs='https://developer.nytimes.com/apis',
        category='News'
    )

    api.save()

    # ---------------
    # News
    # ---------------

    endpoints = None

    api = Api(
        name='NewsAPI',
        description="The main use of News API is to search through every article published by over 150,000 news sources and blogs in the last 5 years. Think of us as Google News that you can interact with programmatically!",
        base_url='https://newsapi.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://newsapi.org/docs',
        category='News'
    )

    api.save()

    # ---------------
    # OkSurf
    # ---------------

    endpoints = None

    api = Api(
        name='OkSurf!',
        description="The OkSurf News API provides a simple, free REST API for developers to retrieve the latest Google news in a familiar JSON format. This news service is absolutely free. No account or signup is required.Retrieve all Google News headlines.",
        base_url='https://ok.surf/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://ok.surf/swagger',
        category='News'
    )

    api.save()

    # ---------------
    # The Guardian
    # ---------------

    endpoints = None

    api = Api(
        name='The Guardian',
        description="The OkSurf News API provides a simple, free REST API for developers to retrieve the latest Google news in a familiar JSON format. This news service is absolutely free. No account or signup is required.Retrieve all Google News headlines.",
        base_url='https://content.guardianapis.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://open-platform.theguardian.com/documentation/',
        category='News'
    )

    api.save()

    # Open Data

    # ---------------
    # Archive.org
    # ---------------

    endpoints = None

    api = Api(
        name='Archive.org',
        description="The Internet Archive (the “Archive”) is a 501(c)(3) nonprofit organization committed to Universal Access of Knowledge. The Archive runs several services including the Archive.org search engine, OpenLibrary, and the Wayback Machine. In alignment with its mission, the Archive encourages developers to add media to archive.org, as well as to consume and re-purpose media and its metadata, for the great good of our community and beyond.",
        base_url='https://archive.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://archive.readme.io/reference/getting-started',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Callook.info
    # ---------------

    endpoints = None

    api = Api(
        name='CALLLOOK',
        description="United States ham radio callsigns. NO-NONSENSE AMATEUR RADIO U.S.A. CALLSIGN LOOKUPS.",
        base_url='	https://callook.info',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://callook.info/api_reference.php',
        category='Open Data'
    )

    api.save()

    # ---------------
    # CARTO
    # ---------------

    endpoints = None

    api = Api(
        name='CARTO',
        description="CARTO is the only cloud-first spatial platform built for accelerated, modern GIS. It runs natively on top of your cloud data warehouse platform (e.g. Google BigQuery, Snowflake, AWS Redshift, etc.), providing easy access to highly scalable spatial analysis and visualization capabilities in the cloud — be it for analytics, app development, data engineering, and more.",
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
        docs='https://docs.carto.com/carto-user-manual/workflows/executing-workflows-via-api',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Enigma Public
    # ---------------

    endpoints = None

    api = Api(
        name='enigma',
        description="Enigma is building the single most reliable source of data on U.S. businesses. Our goal is to deliver the most actionable intelligence on the health and identity of every U.S. business.",
        base_url='https://api.enigma.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://developers.enigma.com/docs/api',
        category='Open Data'
    )

    api.save()

    # ---------------
    # LinkPreview
    # ---------------

    endpoints = None

    api = Api(
        name='LinkPreview',
        description="Link preview is a feature that provides users with a glimpse of a web page’s content before actually clicking on the link. It typically includes a preview of the page’s title, a brief description, an image, and the URL. Link previews are commonly used in messaging apps, social media platforms, and email clients to give users an idea of what to expect when they click on a shared link. With the LinkPreview API, you can programmatically obtain detailed website information, including the title, preview image, and brief description, for any given URL.",
        base_url='https://api.linkpreview.net',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://docs.linkpreview.net/',
        category='Open Data'
    )
    
    api.save()

    # ---------------
    # Microlink.io
    # ---------------

    endpoints = None

    api = Api(
        name='Microlink.io',
        description="Browser as API. Microlink is a fast, scalable, and reliable high-level API to control a headless browser built for businesses and developers. Proudly open source.",
        base_url='https://api.microlink.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://microlink.io/',
        category='Open Data'
    )

    api.save()

    # ---------------
    # OpenCorporates
    # ---------------

    endpoints = None

    api = Api(
        name='opencorporates',
        description="This documentation covers the main API (the so-called REST API). The API provides all the information available on the OpenCorporates website as data. By default it returns data as JSON, but XML is also available. Access to all the data is free for open data projects under the same open licence conditions as the rest of OpenCorporates. An API key is required in order to use the OpenCorporates API, and usage limits depend on your account type and plan. If you are matching company names to legal entities from an existing dataset, you should investigate using Open Refine, software which allows data to be filtered and cleansed more easily and more quickly than any other tool we know of. OpenCorporates provides a highly popular reconciliation API for Open Refine, which allows matching company names to legal entities.",
        base_url='https://api.opencorporates.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.opencorporates.com/documentation/API-Reference',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Recreation Information Database
    # ---------------

    endpoints = None

    api = Api(
        name='The Recreation Information Database',
        description="Recreation Information Database - RIDB. RIDB is a part of the Recreation One Stop (R1S) program, which oversees the operation of Recreation.gov -- a user-friendly, web-based resource to citizens, offering a single point of access to information about recreational opportunities nationwide. The website represents an authoritative source of information and services for millions of visitors to federal lands, historic sites, museums, waterways and other destinations and activities.",
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
        docs='https://ridb.recreation.gov/docs',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Scoop.it
    # ---------------

    endpoints = None

    api = Api(
        name='Scoop.it!',
        description="Research and publish the best content. Publish your topic page with curated content in minutes. Distribute it automatically with your network to build your professional brand. Curate, share, and read content on private hubs. Publish on your websites and blogs, newsletters and social media. Aggregate curated content across multiple WordPress blogs.",
        base_url='https://www.scoop.it',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=False,
        cors=None,
        docs='https://www.scoop.it/dev/api/1/intro',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Universities List
    # ---------------

    endpoints = None

    api = Api(
        name='university-domains-list',
        description="Do you need a list of universities and their domain names? You found it! This package includes a JSON file that contains domains, names and countries of most of the universities of the world. Example usecases: You can create a validation script that checks the email domain, You can automatically generate a user's country and university by looking at their emails. You can use this data source in three ways: Use the JSON file as your data source and do whatever you like with your favourite programming language, Use free hosted-API, Use the tiny Python app to serve a fast API that you can query data.",
        base_url='http://universities.hipolabs.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/Hipo/university-domains-list',
        category='Open Data'
    )

    api.save()

    # ---------------
    # UPC database
    # ---------------

    endpoints = None

    api = Api(
        name='UPC database',
        description="The UPCDatabase API allows you to access our database in a simple, programmatic way using conventional HTTP requests with any programming language. The API documentation will start with a general overview about the design and technology that has been implemented, followed by reference information about specific endpoints.",
        base_url='https://api.upcdatabase.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://upcdatabase.org/api',
        category='Open Data'
    )

    api.save()

    # ---------------
    # Wikidata
    # ---------------

    endpoints = None

    api = Api(
        name='MediaWiki',
        description="The MediaWiki software is used by tens of thousands of websites and thousands of companies and organisations. It powers Wikipedia and also this website. MediaWiki helps you collect and organise knowledge and make it available to people. It's powerful, multilingual, free and open, extensible, customisable, reliable, and free of charge. Find out more and if MediaWiki is right for you.",
        base_url='https://www.example.org/w/api.php',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.mediawiki.org/wiki/API:Main_page',
        category='Open Data'
    )

    api.save()

    # Open Source Projects

    # ---------------
    # Drupal.org
    # ---------------

    endpoints = None

    api = Api(
        name='Drupal.org',
        description="Create Ambitious Digital Experiences. Drupal is a fully composable CMS that allows you to design a digital experience to your vision.",
        base_url='https://www.drupal.org/api-d7',
        api_keywords=['Drupal', 'CMS'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.drupal.org/drupalorg/docs/apis/rest-and-other-apis',
        category='Open Source Projects'
    )

    api.save()

    # ---------------
    # Evil Insult Generator
    # ---------------

    endpoints = None

    api = Api(
        name='Evil Insult Generator',
        description="Evil Insults",
        base_url='https://evilinsult.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://evilinsult.com/api',
        category='Open Source Projects'
    )

    api.save()

    # ---------------
    # Libraries.io
    # ---------------

    endpoints = None

    api = Api(
        name='Libraries.io',
        description="Libraries.io is a free service that collects publicly available open source package information scraped from the internet. With it you can search 9.96M packages by license, language, or explore new, trending, or popular packages.",
        base_url='https://libraries.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://libraries.io/api',
        category='Open Source Projects'
    )

    api.save()

    # Patent

    # ----------------
    # EPO
    # ---------------

    endpoints = None

    api = Api(
        name='European Patent Offce',
        description="Open Patent Services (OPS) is a web service which provides access to the EPO's raw data via a standardised XML interface. It does this using RESTful architecture. OPS data is extracted from the EPO's bibliographic, worldwide legal status, full-text and image databases. It is therefore from the same sources as the Espacenet and European Patent Register data.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.epo.org/',
        category='Patent'
    )

    api.save()

    # ----------------
    # USPTO
    # ---------------

    endpoints = None

    api = Api(
        name='United States Patent and Trademark Office',
        description="The United States Patent and Trademark Office (USPTO) is the federal agency under the Department of Commerce and is responsible for granting U.S. patents and registering trademarks. Our mission is to drive U.S. innovation and global competitiveness for the benefit of all Americans.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.uspto.gov/learning-and-resources/data-and-statistics',
        category='Patent'
    )

    api.save()

    # Personality

    # ---------------
    # Advice Slip
    # ---------------

    endpoints = None

    api = Api(
        name='Advice Slip',
        description="The Advice Slip JSON API is provided for free. 😎 It currently gives out over 10 million pieces of advice every year.",
        base_url='https://api.adviceslip.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.adviceslip.com/',
        category='Personality'
    )

    api.save()

    # ---------------
    # chucknorris.io
    # ---------------

    endpoints = None

    api = Api(
        name='chucknorris.io',
        description="chucknorris.io is a free JSON API for hand curated Chuck Norris facts.",
        base_url='https://api.chucknorris.io/jokes',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.chucknorris.io/',
        category='Personality'
    )
    
    api.save()

    # ---------------
    # FavQs.com
    # ---------------

    endpoints = None

    api = Api(
        name='FavQs',
        description="",
        base_url='https://favqs.com/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://favqs.com/api',
        category='Personality'
    )

    api.save()

    # ---------------
    # Forismatic
    # ---------------

    endpoints = None

    api = Api(
        name='',
        description="Here we collect the most inspiring expressions of mankind. There are not any catalogues of phrases or lists of authors on the site, full of sages and philosophers’ thoughts, writers and outstanding people’s aphorisms. We don’t believe in a random choice. Only you can guide your destiny. Just listen to yourself and one of the most inspiring expressions of mankind will be the sign for you.",
        base_url='http://api.forismatic.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://forismatic.com/en/api/',
        category='Personality'
    )

    api.save()

    # ---------------
    # Hindi Quotes
    # ---------------

    endpoints = None

    api = Api(
        name='हिन्दी Quotes',
        description="Get random Hindi quotes of different categories.",
        base_url='https://hindi-quotes.vercel.app',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://hindi-quotes.vercel.app/',
        category='Personality'
    )

    api.save()

    # ---------------
    # Hindi Quotes and Shayari
    # ---------------

    endpoints = None

    api = Api(
        name='Pure विचार',
        description="This API is completely free to use and provides a collection of quotes and shayari in Hindi and English. As we continue to grow, we will keep updating our database with more content to ensure a rich and diverse collection. I created this API because I noticed that there were no proper resources available for quotes and shayaris in Hindi audio format. This API is an attempt to bridge that gap and provide users with meaningful and inspiring content.",
        base_url='https://www.purevichar.in/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://www.purevichar.in/tool/apitool/',
        category='Personality'
    )

    api.save()

    # ---------------
    # icanhazdadjoke
    # ---------------

    endpoints = None

    api = Api(
        name='icanhazdadjoke',
        description="icanhazdadjoke.com can be used as an API for fetching a random joke, a specific joke, or searching for jokes in a variety of formats.",
        base_url='https://icanhazdadjoke.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://icanhazdadjoke.com/api',
        category='Personality'
    )

    api.save()

    # ---------------
    # kanye.rest
    # ---------------

    endpoints = None

    api = Api(
        name='kanye.rest',
        description="A free REST API for random Kanye West quotes (Kanye as a Service)",
        base_url='https://api.kanye.rest',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://kanye.rest/',
        category='Personality'
    )

    api.save()

    # ---------------
    # Medium
    # ---------------

    endpoints = None

    api = Api(
        name='Medium',
        description="Community of readers and writers offering unique perspectives on ideas",
        base_url='https://api.medium.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://github.com/Medium/medium-api-docs',
        category='Personality'
    )

    api.save()

    # ---------------
    # Meme
    # ---------------

    endpoints = None

    api = Api(
        name='Meme API',
        description="JSON API for a random meme scraped from reddit",
        base_url='https://meme-api.com/gimme',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/D3vd/Meme_Api',
        category='Personality'
    )

    api.save()

    # ---------------
    # Programming Quotes
    # ---------------

    endpoints = None

    api = Api(
        name='Programming Quotes',
        description="A free restful API serving quality programming quotes by programmers",
        base_url='https://programming-quotesapi.vercel.app/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://programming-quotesapi.vercel.app/docs',
        category='Personality'
    )

    api.save()

    # ---------------
    # Quoterism
    # ---------------

    endpoints = None

    api = Api(
        name='Quoterism',
        description="Collection of the most inspiring expressions of mankind",
        base_url='https://www.quoterism.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.quoterism.com/developer',
        category='Personality'
    )

    api.save()

    # ---------------
    # Riddles API
    # ---------------

    endpoints = None

    api = Api(
        name='Riddles API',
        description="Get random riddles on every API call.",
        base_url='https://riddles-api.vercel.app',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://riddles-api.vercel.app/',
        category='Personality'
    )

    api.save()

    # ---------------
    # Traitify
    # ---------------

    endpoints = None

    api = Api(
        name='traitify',
        description="Welcome to Traitify's Personality API! We understand that behind every user is a human being with a personality waiting to be discovered. With that in mind, we've created a diverse set of fun visual assessments used to uncover personality types and traits. Your users simply select 'Me' or 'Not Me' to a brief series of images and voila! Instant, actionable data. With this psychology-backed data in hand, the possibilities are endless - any way that personalization can help you is now within reach.",
        base_url='https://api.traitify.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://app.traitify.com/developer/documentation',
        category='Personality'
    )

    # Photography

    # ---------------
    # Flickr
    # ---------------

    endpoints = None

    api = Api(
        name='flickr',
        description="The best place to be a photographer online. Flickr is a community in the truest sense: we’re here for each other, full stop. Get inspired. Get feedback. Get lost in a weird new photo style! We’ve got your back. There’s a home for every photo on Flickr. Store, organize, curate, and show off your creativity, all in one place. Not-so-humble-brag: Flickr is the largest collection of Creative Commons-licensed imagery on earth. Come get inspired and join the fun.",
        base_url='https://live.staticflickr.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://www.flickr.com/services/api/',
        category='Photography'
    )

    api.save()

    # ---------------
    # Getty Images
    # ---------------

    endpoints = None

    api = Api(
        name='gettyimages',
        description="Unlock the power of world‑class visual content with the Getty Images API. Easy to implement, our flexible API brings the best visual content straight to you and your customers, letting you integrate outstanding images, videos, and illustrations from Getty Images and iStock directly into your platform.",
        base_url='https://api.gettyimages.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.gettyimages.com/docs/',
        category='Photography'
    )

    api.save()

    # ---------------
    # Giphy
    # ---------------

    endpoints = None

    api = Api(
        name='Giphy',
        description="GIPHY is the best way to search, share, discover and create GIFs on the Internet. The content on GIPHY's website, app, and API is all of the best and most popular GIFs on the web, along with content created by talented GIF artists and world-class brands. Our goal is to help make finding and sharing the good GIFs easier.",
        base_url='https://api.giphy.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developers.giphy.com/docs/',
        category='Photography'
    )

    api.save()

    # ---------------
    # Gyazo
    # ---------------

    endpoints = None

    api = Api(
        name='Gyazo',
        description="The Gyazo API can be used in a wide array of apps to upload new images, show a Gyazo user’s images, and more. It provides a RESTful API for HTTP requests and returns a response in JSON. This should be familiar to anyone who has used major APIs before such as Amazon S3 and Twitter.",
        base_url='https://upload.gyazo.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://gyazo.com/api/docs',
        category='Photography'
    )

    api.save()

    # ---------------
    # Imgur
    # ---------------

    endpoints = None

    api = Api(
        name='Imgur',
        description="Imgur's API exposes the entire Imgur infrastructure via a standardized programmatic interface. Using Imgur's API, you can do just about anything you can do on imgur.com, while using your programming language of choice. The Imgur API is a RESTful API based on HTTP requests and JSON responses.",
        base_url='https://api.imgur.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://apidocs.imgur.com/',
        category='Photography'
    )

    api.save()

    # ---------------
    # Lorem Picsum
    # ---------------

    endpoints = None

    api = Api(
        name='Lorem Picsum.',
        description="Lorem Picsum. The Lorem Ipsum for photos.",
        base_url='https://picsum.photos',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://picsum.photos/',
        category='Photography'
    )

    api.save()

    # ---------------
    # ObjectCut
    # ---------------

    endpoints = None

    api = Api(
        name='',
        description="This is the RESTful API for our AI Solution for Background or Foreground Removal. This solution allows clients to remove background or foreground from images without need to resize it, keeping or removing then just the main object visible.",
        base_url='https://background-removal.p.rapidapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://objectcut.com/',
        category='Photography'
    )

    api.save()

    # ---------------
    # Pexels
    # ---------------

    endpoints = None

    api = Api(
        name='pexels',
        description="Start building with the power of Pexels. Give your users access to our entire photo and video library without leaving your app or website. It’s free and seamlessly integrates with just a few lines of code. Get started and immediately receive your unique API key.",
        base_url='https://api.pexels.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.pexels.com/api/documentation/',
        category='Photography'
    )

    api.save()

    # ---------------
    # ScreenShotLayer
    # ---------------

    endpoints = None

    api = Api(
        name='ScreenShotLayer',
        description="Capture highly customizable snapshots of any website.Powerful Screenshot API for any application",
        base_url='http://api.screenshotlayer.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://screenshotlayer.com/documentation',
        category='Photography'
    )

    api.save()

    # ---------------
    # Unsplash
    # ---------------

    endpoints = None

    api = Api(
        name='Unsplash',
        description="The most powerful photo engine in the world. Welcome to the Official Unsplash API. Create with the largest open collection of high-quality photos.",
        base_url='https://api.unsplash.com/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://unsplash.com/documentation',
        category='Photography'
    )

    api.save()

    # ---------------
    # Wallhaven
    # ---------------

    endpoints = None

    api = Api(
        name='wallhaven',
        description="wallhaven. The best wallpapers on the Net!",
        base_url='',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://wallhaven.cc/help/api',
        category='Photography'
    )

    api.save()

    # Science & Math

    # ---------------
    # CORE
    # ---------------

    endpoints = None

    api = Api(
        name='CORE',
        description="We deliver services for a wide range of audiences, including researchers, libraries, universities, innovative companies and funders. Process and analyse the largest structured collection of open research with their full texts, manage your research papers, make them more discoverable, and comply with funder mandates. All this you can do with CORE Services.",
        base_url='https://api.core.ac.uk',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://api.core.ac.uk/docs/v3',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # GBIF
    # ---------------

    endpoints = None

    api = Api(
        name='GBIF',
        description="Free and open access to biodiversity data. GBIF—the Global Biodiversity Information Facility—is an international network and data infrastructure funded by the world's governments and aimed at providing anyone, anywhere, open access to data about all types of life on Earth.",
        base_url='https://api.gbif.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://techdocs.gbif.org/en/openapi/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # iDigBio
    # ---------------

    endpoints = None

    api = Api(
        name='iDigBio',
        description="Integrated Digitized Biocollections (iDigBio) is the National Resource for Advancing Digitization of Biodiversity Collections (ADBC) funded by the National Science Foundation. Through ADBC, data and images for millions of biological specimens are being made available in electronic format for the research community, government agencies, students, educators, and the general public. iDigBio is a data aggregator. This means that data is provided to iDigBio through various publishing mechanisms.",
        base_url='https://search.idigbio.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/idigbio/idigbio-search-api/wiki',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # ITIS
    # ---------------

    endpoints = None

    api = Api(
        name='ITIS',
        description="Integrated Taxonomic Information System. Welcome to ITIS, the Integrated Taxonomic Information System. Here you will find authoritative taxonomic information on plants, animals, fungi, and microbes of North America and the world. Our mission is to communicate a comprehensive taxonomy of global species that enables biodiversity information to be discovered, indexed, and connected across all human endeavors. The ITIS program partners with specialists from around the world to assemble scientific names and their taxonomic relationships. ITIS is an Associate Participant of the Global Biodiversity Information Facility (GBIF) and a partner and contributor to the Catalogue of Life (COL) and ChecklistBank which are the basis of the GBIF Backbone Taxonomy.",
        base_url='https://www.itis.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.itis.gov/ws_description.html',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Launch Library
    # ---------------

    endpoints = None

    api = Api(
        name='Launch Library 2',
        description="The Launch Library 2 API is the official successor of the popular Launch Library API. It keeps its core features whilst also including everything the broader Space Launch Now API had to offer. The result is a large database delivering a more complete experience for each rocket launch and space event. The philosophy behind the API also remains unchanged : the entire database is accessible to everyone, for free.",
        base_url='https://ll.thespacedevs.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://thespacedevs.com/llapi',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Minor Planet Center
    # ---------------

    endpoints = None

    api = Api(
        name='Asterank',
        description="Asterank offers a database API for the Minor Planet Center's MPCORB.DAT data files. This API is a simple way to quickly apply constraints to a set of over 600,000 asteroids. Users can construct queries with specific constraints across all data attributes recorded by the MPC. Information is updated nightly from the MPC's MPCORB.dat dataset. The database queries are based on mongodb's json-formatted 'find' operation. See below for an example of a complex query.",
        base_url='http://asterank.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://www.asterank.com/mpc',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # NASA
    # ---------------

    endpoints = None

    api = Api(
        name='{ NASA APIs }',
        description="Welcome to the NASA API portal. The objective of this site is to make NASA data, including imagery, eminently accessible to application developers. This catalog focuses on broadly useful and user friendly APIs and does not hold every NASA API.",
        base_url='https://api.nasa.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.nasa.gov/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Newton
    # ---------------

    endpoints = None

    api = Api(
        name='newton',
        description="A really micro micro-service for advanced math.",
        base_url='https://newton.now.sh/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/aunyks/newton-api',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Numbers
    # ---------------

    endpoints = None

    api = Api(
        name='MathTOOLS Numbers',
        description="Number of the day, random number generation , number facts and anything else you want to do with numbers.",
        base_url='https://api.math.tools',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://math.tools/api/numbers/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Numbers
    # ---------------

    endpoints = None

    api = Api(
        name='NUMBERSAPI',
        description="Bring meaning to your metrics and stories to your dates with our API of interesting number facts.",
        base_url='http://numbersapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='http://numbersapi.com',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Open Notify
    # ---------------

    endpoints = None

    api = Api(
        name='Open Notify',
        description="Open APIs From Space Open Notify is an open source project to provide a simple programming interface for some of NASA’s awesome data. I do some of the work to take raw data and turn them into APIs related to space and spacecraft.",
        base_url='http://api.open-notify.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='http://open-notify.org/Open-Notify-API/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Open Science Framework
    # ---------------

    endpoints = None

    api = Api(
        name='Open Science Framework ',
        description="Welcome to the Open Science Framework API. With this API you can access users, projects, components, logs, and files from the Open Science Framework. The Open Science Framework (OSF) is a free, open-source service maintained by the Center for Open Science. The OSF serves as a repository and archive for study designs, materials, data, manuscripts, or anything else associated with your research during the research process. Every project and file on the OSF has a permanent unique identifier, and every registration (a permanent, time-stamped version of your projects and files) can be assigned a DOI. You can use the OSF to measure your impact by monitoring the traffic to projects and files you make public. With the OSF you have full control of what parts of your research are public and what remains private.",
        base_url='https://api.osf.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://developer.osf.io',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # SHARE
    # ---------------

    endpoints = None

    api = Api(
        name='SHARE',
        description="A free, open, dataset about research and scholarly activities",
        base_url='https://share.osf.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://share.osf.io/api/v2/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # SpaceX
    # ---------------

    endpoints = None

    api = Api(
        name='SpaceX-API',
        description="Open Source REST API for launch, rocket, core, capsule, starlink, launchpad, and landing pad data. ",
        base_url='https://api.spacexdata.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/r-spacex/SpaceX-API/blob/master/docs/README.md',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # Sunrise and Sunset
    # ---------------

    endpoints = None

    api = Api(
        name='Sunrise Sunset',
        description="Sunrise-Sunset is a free online tool that provides information about day length, twilight, sunrise and sunset times for any location of the world. Our purpose is to make it easy to everybody to access Sun related information through simple tools that offers accurate information.",
        base_url='https://api.sunrise-sunset.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://sunrise-sunset.org/api',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # USGS Earthquake Hazards Program
    # ---------------

    endpoints = None

    api = Api(
        name='USGS Earthquake Hazards Program',
        description="Earthquake Hazards Program. The USGS monitors and reports on earthquakes, assesses earthquake impacts and hazards, and conducts targeted research on the causes and effects of earthquakes. We undertake these activities as part of the larger National Earthquake Hazards Reduction Program (NEHRP), a four-agency partnership established by Congress.",
        base_url='https://earthquake.usgs.gov/fdsnws',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://earthquake.usgs.gov/fdsnws',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # USGS Water Services
    # ---------------

    endpoints = None

    api = Api(
        name='USGS Water Services',
        description="USGS Water Services. This site provides USGS water data in machine-readable formats via REST APIs, a common framework programs use to search and download data. The services below each provide a different type of data, ranging from instantaneous measurements of streamflow to information about individual USGS sites and more. The links below lead to documentation for how to use each service, and web forms to build queries for each endpoint.",
        base_url='https://waterservices.usgs.gov/nwis/iv',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://waterservices.usgs.gov/docs/',
        category='Science & Math'
    )

    api.save()

    # ---------------
    # World Bank
    # ---------------

    endpoints = None

    api = Api(
        name='THE WORLD BANK',
        description="The World Bank Group works in every major area of development. We provide a wide array of financial products and technical assistance and help countries share and apply innovative knowledge and solutions to tackle today’s intertwined development challenges. World Bank APIs provide access to various types of data and databases: The Indicators API provides programmatic access to time series development data and metadata. Most of the articles in this section are devoted to the Indicators API, The Data Catalog API provides information about the thousands of development-relevant datasets available through the World Bank Data Catalog, The Projects API provides access to World Bank operations data, i.e., active, pipeline and closed projects implemented in countries and around the world, The Finances API provides programmatic access to World Bank financial data (loans, credits, financial statements, etc) delivered on the World Bank Finances platform, The Climate Data API provides access to historical and modelled climate data from the Climate Knowledge Portal",
        base_url='https://api.worldbank.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information',
        category='Science & Math'
    )

    api.save()

    # Security

    # ---------------
    # Censys.io
    # ---------------

    endpoints = None

    api = Api(
        name='censys',
        description="Censys provides the most complete view of the entire public-facing internet. Censys continually scans the entire public IPv4 address space using automatic protocol detection, examining all possible IP and port combinations. The results accurately represent the Internet’s current state. Censys also leverages redirects and the Domain Name System to discover and scan in-use IPv6 addresses.",
        base_url='https://search.censys.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=False,
        docs='https://search.censys.io/api',
        category='Security'
    )

    api.save()

    # ---------------
    # CRXcavator
    # ---------------

    endpoints = None

    api = Api(
        name='CRXcavator',
        description="CRXcavator automatically scans the entire Chrome, Firefox, and Edge Web Stores every 3 hours and produces a quantified risk score for each browser extension based on several factors. These factors include permissions, inclusion of vulnerable third party javascript libraries, weak content security policies, missing details from the associated web store description, and more. Organizations can use this tool to assess the browser extensions they have installed and to move towards implementing explicit allow (allowlisting) for their organization.",
        base_url='https://api.crxcavator.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://crxcavator.io/apidocs',
        category='Security'
    )

    api.save()

    # ---------------
    # FishFish
    # ---------------

    endpoints = None

    api = Api(
        name='FishFish',
        description="An anti-phishing service that focuses on quick, automated detection of threat resources before they're used for evil. We provide live updates to our database via a WebSocket feed. ",
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
        category='Security'
    )

    api.save()

    # ---------------
    # HaveIBeenPwned
    # ---------------

    endpoints = None

    api = Api(
        name='HaveIBeenPwned',
        description="Check if your email address is in a data breach. This site came about after what was, at the time, the largest ever single breach of customer accounts — Adobe. I often did post-breach analysis of user credentials and kept finding the same accounts exposed over and over again, often with the same passwords which then put the victims at further risk of their other accounts being compromised.",
        base_url='https://haveibeenpwned.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://haveibeenpwned.com/API/v3',
        category='Security'
    )

    api.save()

    # ---------------
    # phish.directory
    # ---------------

    endpoints = None

    api = Api(
        name='Phish Directory',
        description="Keeping you safe from phishing attacks. Phish Directory is a community-driven database of phishing URLs. Our goal is to help you stay safe from phishing attacks by providing you with the latest information on phishing URLs.",
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
        category='Security'
    )

    api.save()

    # ---------------
    # Secrets-APi
    # ---------------

    endpoints = None

    api = Api(
        name='Secrets API',
        description="Welcome to the Secrets API. This API allows you to manage and retrieve secrets anonymously. Please refer to the documentation below for details on how to interact with the API. The API is rate limited to 100 requests every 15 minutes. All user submitted data (including registration, tokens, usernames, passwords, secrets) are erased on a regular basis. This API is just for education purposes, please don't rely on it for production.",
        base_url='https://secrets-api.appbrewery.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='Basic',
        https='apiKey',
        cors=None,
        docs='https://secrets-api.appbrewery.com/',
        category='Security'
    )

    api.save()

    # ---------------
    # SecurityTrails
    # ---------------

    endpoints = None

    api = Api(
        name='SecurityTrails',
        description="Data for Security companies, researchers and teams. Fast, always up cyber security API that allows you to access current and historical data. The API is paid via a simple pricing structure that allows you to embed our data into your applications.",
        base_url='https://api.securitytrails.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://securitytrails.com/corp/api',
        category='Security'
    )

    api.save()

    # ---------------
    # Shodan
    # ---------------

    endpoints = None

    api = Api(
        name='Shodan',
        description="See which ports an IP has open, what SSL/ TLS versions it supports, which country it's located in, what web technologies the website uses and much more. Shodan has a curated DNS database that contains information about hostnames likely to run a service. Use it to help map out your organization's attack surface. Subscribe to real-time data feeds to get notified when new ports are detected, vulnerabilities are discovered or network configurations change.",
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
        docs='https://developer.shodan.io/api/clients',
        category='Security'
    )

    api.save()

    # ---------------
    # UK Police
    # ---------------

    endpoints = None

    api = Api(
        name='DATA.POLICE.UK',
        description="This is the site for open data about crime and policing in England, Wales and Northern Ireland. You can download street-level crime, outcome, and stop and search data in clear and simple CSV format and explore the API containing detailed crime data and information about individual police forces and neighbourhood teams. You can also download data on police activity, and a range of data collected under the police annual data requirement (ADR) including arrests and 101 call handling. All the data on this site is made available under the Open Government Licence v3.0.",
        base_url='https://data.police.uk/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://data.police.uk/docs/',
        category='Security'
    )

    api.save()

    # ---------------
    # Whoisfreaks
    # ---------------

    endpoints = None

    api = Api(
        name='WhoisFreaks',
        description="Unleash the Power of Data with Our Domain and IP Intelligence. Elevate your cyber-security strategy with our domain and IP intelligence services. Designed for analysts, researchers, and brand owners. Our platform provides unparalleled insights and monitoring capabilities to protect your digital assets. Stay ahead of threats, ensure brand integrity, and make informed decisions with real-time data you can trust. Our platform seamlessly integrates with existing systems, enhancing workflow efficiency and effectiveness. We are committed to quality, up-to-date information, and unparalleled support, continuously evolving to stay ahead of industry trends.",
        base_url='https://api.whoisfreaks.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://whoisfreaks.com/products/whois-api',
        category='Security'
    )

    api.save()

    # ---------------
    # WhoisJSONApi
    # ---------------

    endpoints = None

    api = Api(
        name='',
        description="Whois API for looking up accurate domain data. Bulk WHOIS Lookups & URL Availability Checks Made Easy. Effortlessly retrieve accurate WHOIS details for any domain with our REST API. Perform bulk WHOIS queries and check URL availability in real time, all in a structured JSON format for seamless integration into your applications.",
        base_url='https://whoisjsonapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://whoisjsonapi.com/page/documentation',
        category='Security'
    )

    api.save()

    # Shopping

    # ---------------
    # Best Buy
    # ---------------

    endpoints = None

    api = Api(
        name='Best Buy',
        description="Welcome to the Best Buy Developer API site! Whether you’re an API pro, a beginning developer or a Best Buy partner, our extensive API catalog is waiting for your imagination. Our API suite allows you to query Products, Stores and much more. Come on in to explore our data, browse descriptions of the available attributes and see examples of working requests and responses.",
        base_url='https://api.bestbuy.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://bestbuyapis.github.io/api-documentation/',
        category='Shopping'
    )

    api.save()

    # ---------------
    # eBay
    # ---------------

    endpoints = None

    api = Api(
        name='eBay',
        description="We connect people and build communities to create economic opportunity for all. At eBay, we create pathways to connect millions of sellers and buyers in more than 190 markets around the world. Our technology empowers our customers, providing everyone the opportunity to grow and thrive — no matter who they are or where they are in the world. And the ripple effect of our work creates waves of change for our customers, our company, our communities and our planet.",
        base_url='https://api.ebay.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developer.ebay.com/',
        category='Shopping'
    )

    api.save()

    # Social TODO

    # Sports & Fitness

    # ---------------
    # balldontlie
    # ---------------

    endpoints = None

    api = Api(
        name='BALLDONTLIE',
        description="The #1 API for Live Sports Data and Analytics. Real-time stats, player insights, and game analytics for developers, analysts, and sports enthusiasts. Access the most affordable and comprehensive sports API on the market.",
        base_url='https://api.balldontlie.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://www.balldontlie.io/',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # City Bikes
    # ---------------

    endpoints = None

    api = Api(
        name='CityBikes',
        description="City Bikes around the world",
        base_url='http://api.citybik.es',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://api.citybik.es/v2/',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # F1 API
    # ---------------

    endpoints = None

    api = Api(
        name='F1 API',
        description="F1 Connect Api. Your free API, ready for development. This API provides access to a wealth of data related to Formula 1 races, drivers, teams, circuits, and more. All the data its provided in JSON format and its ready to use. Simply fetch https://f1api.dev with the endpoint that you like. You can also use our new SDK tool to fetch the data, with our methods and types.",
        base_url='https://f1api.dev',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://f1api.dev/docs',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # F1 Data API
    # ---------------

    endpoints = None

    api = Api(
        name='F1 Data API',
        description="An API that serves the F1 Archive. Formula 1 data API that delivers data from the F1 Archive dating back to 1950",
        base_url='https://api.bthree.uk/f1',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://github.com/jacobbrewer1/f1-data-docs',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Football (Soccer) Videos
    # ---------------

    endpoints = None

    api = Api(
        name='ScoreBat',
        description="We decided to make all our video data accessible to developers! You can now build your own football website or app using our Video API and give your users the ability to watch video highlights of the matches of their favorite football leauges. Our Video API allows you to embed all official video highlights of the Premier League, Champions League, La Liga, Serie A, Europa League and many more into your website or app.",
        base_url='https://www.scorebat.com/video-api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://www.scorebat.com/video-api/',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Football Prediction
    # ---------------

    endpoints = None

    api = Api(
        name='The Football Prediction API',
        description="The Football Prediction API is a REST API that offers prediction data (JSON) for upcoming football (soccer) matches.",
        base_url='https://football-prediction-api.p.rapidapi.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='X-Mashape-Key',
        https=True,
        cors=None,
        docs='https://developer.boggio-analytics.com/',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Football-Data.org
    # ---------------

    endpoints = None

    api = Api(
        name='Football-Data.org',
        description="Football-data.org provides football data and statistics (live scores, fixtures, tables, squads, lineups/subs, etc.) in a machine-readable way. I won't announce how awesome football-data is, you're welcome to find out by yourself (or not). Access to the top competitions is and will be free forever as this was the initial purpose to setup the project. However if you need more competitions, in-depth data there are several paid plans available to serve your needs. If you need historical data, more requests or something out of the box just drop me a line, I'm glad to help.",
        base_url='https://api.football-data.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://docs.football-data.org/general/v4/index.html',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Golf-Data
    # ---------------

    endpoints = None

    api = Api(
        name='Golf Data API',
        description="Golf data API with golf course, club and hole information",
        base_url=' https://api.bthree.uk/golf',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://github.com/Jacobbrewer1/golf-data-docs',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # JCDecaux Bike
    # ---------------

    endpoints = None

    api = Api(
        name='JCDecaux',
        description="Enjoy our open data to create innovative services. We believe in shared innovation and the creative potential of communities to make cities ever more inventive and accessible. With JCDecaux developer, create new applications and services through an easy-to-access distibution of data under Open License. From the location of the bike stations to the availability of bikes and parking spaces in real time, use our data to experiment new representations or to provide innovative and useful services to users. You can access this data through a simple download or an advanced web API.",
        base_url='https://api.jcdecaux.com/vls',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developer.jcdecaux.com/#/opendata/vls?page=getstarted',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # NHL Records and Stats
    # ---------------

    endpoints = None

    api = Api(
        name='nhlapi',
        description="NHL historical data and statistics.",
        base_url='https://api-web.nhle.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://gitlab.com/dword4/nhlapi/-/blob/master/swagger/openapi.yaml?ref_type=heads',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Strava
    # ---------------

    endpoints = None

    api = Api(
        name='STRAVA',
        description="Track your progress and cheer each other on. Strava athletes upload millions of activities every day. Our open API and this rich data set yield diverse opportunities for developers, from creating new hardware to augmenting the Strava experience. The Strava V3 API is a publicly available interface that allows developers to access Strava data. The interface is stable and used by the Strava mobile apps. However, we occasionally make major changes to improve performance and enhance our features",
        base_url='https://www.strava.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://developers.strava.com/docs/reference/',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # SuredBits
    # ---------------

    endpoints = None

    api = Api(
        name='SUREDBITS',
        description="Thank you and welcome to Suredbits' Lightning App API documentation. This API allows you to query our NFL, NBA and Crypto Exchange data. Our NFL and NBA APIs offer multiple channels including teams, players, games, scores, and statistics. Our Crypto Exchange API allows you to stream data on Trades, Tickers and Order Books.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=False,
        docs='https://suredbits.com/api/#lightning-api-v0-beta-documentation',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # TheSportsDB
    # ---------------

    endpoints = None

    api = Api(
        name='TheSportsDB',
        description="An open, crowd-sourced sports database of artwork and metadata with a free sports API.",
        base_url='https://www.thesportsdb.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://www.thesportsdb.com/docs_api_examples',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # Wger
    # ---------------

    endpoints = None

    api = Api(
        name='WGER',
        description="Workout manager data as exercises, muscles or equipment. Can be self hosted FLOSS workout and fitness tracker. ",
        base_url='https://wger.de',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://wger.de/api/v2/schema/ui',
        category='Sports & Fitness'
    )

    api.save()

    # ---------------
    # CricData
    # ---------------

    endpoints = None

    api = Api(
        name='CricetData',
        description="Free to use, super-high bandwidth, high performance Cricket API. CricAPI was the first to provide free high quality Cricket API since September 2015 under the brand “CricAPI.com”. The organization has since changed hands, and “Cricket Data” – the new avatar – promises to continue supporting cricket enthusiasts all over the globe with rich and reliable cricket data in API format. Cricket score api was never this easy to use. We are ISO 9001:2015 Certified. The only exclusive provider of free to use, high bandwidth, high performance Cricket API. If you’re looking for CricAPI, Cricket API, Cricket Live Score API, Cricket Scorecard API or Cricket Ball by Ball API you’ve come to the right place. The source for Ultimate Cricket API – right here, right now.",
        base_url='https://api.cricapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://cricketdata.org/',
        category='Sports & Fitness'
    )

    api.save()

    # Test Data

    # ---------------
    # Bacon Ipsum
    # ---------------

    endpoints = None

    api = Api(
        name='Bacon Ipsum',
        description="The Bacon Ipsum JSON API is a REST interface for generating meaty lorem ipsum text and can be used by any application. Pass in the following parameters using an HTTPS GET and we’ll return a JSON string array of paragraphs.",
        base_url='https://baconipsum.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://baconipsum.com/json-api/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # Beeceptor's CRUD APIs
    # ---------------

    endpoints = None

    api = Api(
        name='Beeceptor',
        description="Welcome to the Beeceptor API reference! If you're new to Beeceptor, be sure to create an account and explore all the features. Please note that Beeceptor APIs are available for users with Team plans and above. Throughout this documentation, a mention of Beeceptor endpoint refers to the sub-domain name you have created.",
        base_url='https://api.beeceptor.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://beeceptor.com/docs/api-overview/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # Dicebear Avatars
    # ---------------

    endpoints = None

    api = Api(
        name='DiceBear',
        description="With DiceBear you can create awesome avatars for your project in no time. Whether you are looking for abstract shapes or lovingly designed characters, you will find something suitable among our avatar styles. And no matter how and for what you want to use the avatars, DiceBear offers the right solution! In addition to purely random avatars, you can also create deterministic avatars for user identities. With the built-in PRNG you create the same avatar over and over again based on a seed. But also individual avatars are possible! Just use the countless options that each avatar style provides. And thanks to the JavaScript library, HTTP API, CLI, Figma plugin, Editor and Playground, your next avatar is always just a stone's throw away!",
        base_url='https://api.dicebear.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://www.dicebear.com/how-to-use/http-api/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # JSONing
    # ---------------

    endpoints = None

    api = Api(
        name='JSONing',
        description="Mock API. Free and open source fake API for testing and prototyping. Instantly generate a custom API from a JSON object. Create rules to handle error cases and customize HTTP codes, headers, and bodies. Use this tool for free; you can also retrieve the source code and set up a local installation.",
        base_url='https://api.jsoning.com/mock/public',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKEy',
        https=True,
        cors=True,
        docs='https://jsoning.com/api/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # JSONPlaceholder
    # ---------------

    endpoints = None

    api = Api(
        name='{JSON} Placeholder',
        description="Free fake and reliable API for testing and prototyping.",
        base_url='https://jsonplaceholder.typicode.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://jsonplaceholder.typicode.com/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # Micro-Jaymock
    # ---------------

    endpoints = None

    api = Api(
        name='micro-jaymock',
        description="Tiny API mocking microservice for generating fake JSON data.",
        base_url='https://jaymock.now.sh',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://micro-jaymock.vercel.app/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # RandomUser
    # ---------------

    endpoints = None

    api = Api(
        name='Random User Generator',
        description="A free, open-source API for generating random user data. Like Lorem Ipsum, but for people.",
        base_url='https://randomuser.me/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://randomuser.me/documentation',
        category='Test Data'
    )

    api.save()

    # ---------------
    # RoboHash
    # ---------------

    endpoints = None

    api = Api(
        name='RoboHash',
        description="Generate Unique images from any text. Robohash is a easy web service that makes it easy to provide unique, robot/alien/monster/whatever images for any text. Put in any text, such as IP address, email, filename, userid, or whatever else you like, and get back a pretty image for your site. With hundreds of millions of variations, Robohash is the among the leading robot-based hashing tools on the web.",
        base_url='https://robohash.org/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://robohash.org/',
        category='Test Data'
    )

    api.save()

    # ---------------
    # UI Names
    # ---------------

    endpoints = None

    api = Api(
        name='UI Names',
        description="Generate random fake names.",
        base_url='https://uinames.com/api/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://github.com/thm/uinames',
        category='Test Data'
    )

    api.save()

    # ---------------
    # UUID Generator
    # ---------------

    endpoints = None

    api = Api(
        name='UUID Generator',
        description="This API allows you to create UUIDs and GUIDs quickly on-the-fly for testing purposes. No authentication is required. We support generating all major UUID versions including version-1, version-3, version-4, version-5 and timestamp-first UUIDs. Read more about different UUID versions. No authentication is required. This is the same API that powers our UUID generator.Endpoints that accept a count argument allow you to create up to 100 UUIDs at once. All endpoints are limited to 60 requests per minute per IP address.",
        base_url='https://www.uuidtools.com/api/generate',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=False,
        docs='https://www.uuidtools.com/docs',
        category='Test Data'
    )

    api.save()

    # ---------------
    # Yes No
    # ---------------

    endpoints = None

    api = Api(
        name='Yes No',
        description="Generate yes or no randomly",
        base_url='https://yesno.wtf/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs=None,
        category='Test Data'
    )

    api.save()

    # ---------------
    # Randommer
    # ---------------

    endpoints = None

    api = Api(
        name='Randommer',
        description="We offer a RESTful API that you can access over HTTPS. We return all responses in JSON format, so you can use it with our app.",
        base_url='https://randommer.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://randommer.io/randommer-api',
        category='Test Data'
    )
    
    api.save()

    # ---------------
    # Short Id
    # ---------------

    endpoints = None

    api = Api(
        name='idgen',
        description="The idgen is an API to generate Ids with the following characteristics: Short: currently fixed at 6 characters, Alphanumeric: IDs contain both uppercase and lowercase letters, and digits, Unique: each Id is guaranteed to be unique, Random sequence",
        base_url='https://id.aslanta.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://github.com/aguedo/idgen',
        category='Test Data'
    )

    api.save()

    # ---------------
    # Softwium
    # ---------------

    endpoints = None

    api = Api(
        name='Softwium',
        description="Fake API. Free public API that enables developers to effortlessly obtain fake JSON data. Test API endpoints and retrieve dummy JSON data swiftly. No registration, tokens, or authentication is needed.",
        base_url='https://softwium.com/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://softwium.com/fake-api/',
        category='Test Data'
    )

    api.save()

    # Text Analysis

    # ---------------
    # Aylien Text Analysis
    # ---------------

    endpoints = None

    api = Api(
        name='Aylien Text Analysis',
        description="Welcome to Quantexa News API — the most powerful way to aggregate, filter, and integrate global news data into your apps and models.",
        base_url='https://api.aylien.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://docs.aylien.com/newsapi/v6/getting-started',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Cloudmersive Natural Language Processing
    # ---------------

    endpoints = None

    api = Api(
        name='Cloudmersive',
        description=" Powerful Natural Language Processing APIs. The most powerful and cost-effective NLP AI APIs, continuously updated.",
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
        docs='https://api.cloudmersive.com/docs/convert.asp',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Detect Language
    # ---------------

    endpoints = None

    api = Api(
        name='Detect Language API',
        description="The language detection web service analyzes the provided text and returns the identified language code along with a corresponding score. Detects 164 languages. High accuracy - handles long texts, short phrases and single words. Low latency worldwide. Supports batching. Ensures security and privacy. Free and premium plans.",
        base_url='https://ws.detectlanguage.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://detectlanguage.com/documentation',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Google Cloud Natural
    # ---------------

    endpoints = None

    api = Api(
        name='Cloud Natural Language',
        description="The Cloud Natural Language API provides natural language understanding technologies to developers, including sentiment analysis, entity analysis, entity sentiment analysis, content classification, and syntax analysis. This API is part of the larger Cloud Machine Learning API family.",
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
        docs='https://cloud.google.com/natural-language/docs/',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Semantira
    # ---------------

    endpoints = None

    api = Api(
        name='Semantria',
        description="In this documentation you will find comprehensive guides and documentation to help you start working with the Semantria API. The Semantria API is a paid Saas text analytics service from Lexalytics. Contact sales to discuss your use case. Semantria is a fully REST compliant API. You can interact with the API via our SDKs or by rolling your own using standard modules such as https://pypi.org/project/requests/2.7.0/ (for Python), or https://square.github.io/okhttp/ (for Java)",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://semantria-docs.lexalytics.com/docs/obtain-your-creds',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Spam Hunter
    # ---------------

    endpoints = None

    api = Api(
        name='Spam Hunter',
        description="Hey there! We're more than just a team – we're a dedicated group of professionals on a mission to combat spam and enhance online security. Our primary objective is to craft powerful yet user-friendly tools that empower individuals to shield themselves from unwanted emails, messages, and various other forms of spam. Leveraging our extensive expertise in data analysis and machine learning, we continuously refine our algorithms to accurately identify and filter out spam content. At our core, we prioritize transparency, openness, and a customer-centric ethos. We're committed to fostering trust and confidence by being forthright about our methods and dedicated to understanding and addressing the needs of our users. Driven by a passion for innovation, we're constantly pushing the boundaries to deliver cutting-edge solutions that set new standards in cybersecurity. Our tools are meticulously crafted with the latest technologies and adhere to industry best practices to ensure maximum effectiveness and reliability. But our journey doesn't end with the development of our products – it extends to providing exceptional support and guidance to our users. We're here every step of the way, ready to assist and empower individuals in navigating the complex landscape of online security. Ultimately, our vision is to cultivate a safer and more secure online environment for all.",
        base_url='https://backend.spam-hunter.ru/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://spam-hunter.ru/documentation',
        category='Text Analysis'
    )

    api.save()

    # ---------------
    # Yomi
    # ---------------

    endpoints = None

    api = Api(
        name='Yomi',
        description="Yomi API is a free-to-use Japanese tokenizer and morphological analysis web API. It can take a Japanese text as an input and return a JSON response containing the tokenized text.  ",
        base_url='https://yomi.onrender.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://github.com/ookii-tsuki/yomi',
        category='Text Analysis'
    )

    # Tracking

    # ---------------
    # Let's Count
    # ---------------

    endpoints = None

    api = Api(
        name='Lets Count API',
        description="This API uses the combination of a namespace and a key to identify a counter. The namespace is a string that identifies the application or service that is using it. This should be something like your domain or company name. The key is a string that identifies the counter within the namespace. This should be something memorable.",
        base_url='https://letscountapi.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://letscountapi.com/docs',
        category='Tracking'
    )

    api.save()

    # ---------------
    # Postmon
    # ---------------

    endpoints = None

    api = Api(
        name='Postmon',
        description="An API to query Brazilian ZIP codes and orders easily, quickly and free",
        base_url='https://api.postmon.com.br',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://postmon.com.br/',
        category='Tracking'
    )

    api.save()

    # ---------------
    # Sweden
    # ---------------

    endpoints = None

    api = Api(
        name='PostNord',
        description="PostNord creates solutions for e-commerce; fulfillment, supply chain, warehousing and a wide range of global delivery solutions. Our goal is to make you successful by providing a smooth cross-border delivery experience to your customers.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://developer.postnord.com/apis/active',
        category='Tracking'
    )

    api.save()

    # ---------------
    # UPS
    # ---------------

    endpoints = None

    api = Api(
        name='UPS',
        description="The Power of UPS on Your Digital Platform. Our APIs power the data connections needed to deliver value to customers through e-commerce platforms, supply chain visibility solutions and direct integrations.",
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
        docs='https://developer.ups.com/catalog?loc=en_US',
        category='Tracking'
    )

    api.save()

    # ---------------
    # WhatPulse
    # ---------------

    endpoints = None

    api = Api(
        name='WhatPulse',
        description="The Web API can be used to retrieve raw data from WhatPulse on users, teams and pulses. You can use this API to show statistics on your website, blog or use it for your own applications. In the following examples, we will assume that you want to display your statistics on a website. We will also assume that you have some working knowledge of web development.",
        base_url='https://api.whatpulse.org',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://whatpulse.org/help/api/web-api',
        category='Tracking'
    )

    api.save()

    # Transportation TODO

    # URL Shorteners

    # ---------------
    # Bitly
    # ---------------

    endpoints = None

    api = Api(
        name='bitly',
        description="Bitly is the most widely trusted link management platform in the world. By using the Bitly API, you will exercise the full power of your links through automated link customization, mobile deep linking, and click analytics. While shortening links is Bitly’s most basic functionality, our customers create and distribute links at scale via integrated apps and SMS by utilizing the Bitly API.",
        base_url='https://dev.bitly.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=None,
        docs='https://dev.bitly.com/api-reference',
        category='URL Shorteners'
    )

    api.save()

    # ---------------
    # CleanURI
    # ---------------

    endpoints = None

    api = Api(
        name='cleanuri.com',
        description="Given a long URL, returns a short link.",
        base_url='https://cleanuri.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://cleanuri.com/docs',
        category='URL Shorteners'
    )

    api.save()

    # ---------------
    # Rebrandly
    # ---------------

    endpoints = None

    api = Api(
        name='Rebrandly',
        description="Smart links, better results. Maximize every digital connection with Rebrandly's advanced tracking, branded short URLs, and AI-powered insights.",
        base_url='https://api.rebrandly.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://developers.rebrandly.com/docs/get-started',
        category='URL Shorteners'
    )

    api.save()

    # ---------------
    # T.LY
    # ---------------

    endpoints = None

    api = Api(
        name='T.LY',
        description="The World's Shortest Link Shortener service to track, brand, and share short links. Create short links to any website including Google, Spotify, TikTok, Instagram, Facebook, Amazon, YouTube, Twitter, WhatsApp, LinkedIn and more!  ",
        base_url='https://api.t.ly',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://t.ly/docs/',
        category='URL Shorteners'
    )

    api.save()

    # ---------------
    # Urlix
    # ---------------

    endpoints = None

    api = Api(
        name='URLIX',
        description="Your free and unlimited URL shortener service. Easily shorten long URLs into compact, shareable links and track redirection statistics — all in one place. Shorten long URLs to a simpler format. Customize the slug to create memorable links. Secure your links with password protection and set expiration dates. Generate QR codes for each URL for quick sharing. Monitor redirection statistics directly in your dashboard. Use advanced filters to manage and search your link. Access your API key to integrate our service into your apps (no usage limits)",
        base_url='https://urlix.me/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://app.urlix.me/api',
        category='URL Shorteners'
    )

    api.save()

    # Vehicle

    # ---------------
    # Brazilian Vehicles and Prices
    # ---------------

    endpoints = None

    api = Api(
        name='FIPE API',
        description="Vehicles information from Fundação Instituto de Pesquisas Econômicas - Fipe",
        base_url='https://parallelum.com.br/fipe/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://deividfortuna.github.io/fipe/',
        category='Vehicle'
    )

    api.save()

    # ---------------
    # CarsXE API
    # ---------------

    endpoints = None

    api = Api(
        name='CarsEX',
        description="Rev up your business with real-time, comprehensive vehicle data. The most comprehensive and accessible vehicle data API.",
        base_url='https://api.carsxe.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://api.carsxe.com/docs',
        category='Vehicle'
    )

    api.save()

    # ---------------
    # Kelley Blue Book
    # ---------------

    endpoints = None

    api = Api(
        name='Kelley Blue Book',
        description="Get all the vehicle data you need to build dynamic advertisements at lightning fast speeds. Data is fully managed for you. You don’t have to worry about applying data updates to stay in sync. Every week data is updated automatically without any changes required from you. Vehicle info, pricing, configuration, plus much more. Be empowered to build dynamic advertisements utilizing all the data we have to offer.",
        base_url=None,
        api_keywords=['KBB', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='http://developer.kbb.com/#!/data/99-Swagger',
        category='Vehicle'
    )

    api.save()

    # ---------------
    # Mercedes-Benz
    # ---------------

    endpoints = None

    api = Api(
        name='Mercedes-Benz',
        description="Telematics data, remotely access vehicle functions, car configurator, locate service dealers",
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
        docs='https://developer.mercedes-benz.com/products',
        category='Vehicle'
    )

    api.save()

    # ---------------
    # NHTSA
    # ---------------

    endpoints = None

    api = Api(
        name='NHTSA',
        description="The NHTSA Product Information Catalog Vehicle Listing (vPIC) Application Programming Interface (API) provides different ways to gather information on Vehicles and their specifications. The vPIC Dataset is populated using the information submitted by the Motor Vehicle manufacturers through the 565 submittals. All the information on how a VIN is assigned by the manufacturer is captured in this catalog and used to decode a VIN and extract vehicle information.",
        base_url='https://vpic.nhtsa.dot.gov/api/vehicles',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://vpic.nhtsa.dot.gov/api/',
        category='Vehicle'
    )

    api.save()

    # ---------------
    # Smartcar
    # ---------------

    endpoints = None

    api = Api(
        name='smartcar',
        description="Smartcar is the only car API built with the highest standard for privacy and security. We allow your application to communicate with millions of vehicles easily and securely while giving vehicle owners the choice of how they share their data.",
        base_url='https://api.smartcar.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='OAuth',
        https=True,
        cors=True,
        docs='https://smartcar.com/docs/api-reference/intro',
        category='Vehicle'
    )

    api.save()

    # Video TODO

    # Weather

    # ---------------
    # 7Timer!
    # ---------------

    endpoints = None

    api = Api(
        name='7Timer!',
        description="7Timer! is a series of web-based meteorological forecast products, mainly derived from the NOAA/NCEP-based numeric weather model, the Global Forecast System (GFS). 7Timer! was firstly established in July 2005 as an exploration product under supported of the National Astronomical Observatories of China and had been largely renovated in 2008 and 2011. Currently it is supported by the Shanghai Astronomical Observatory of Chinese Academy of Sciences.",
        base_url='http://www.7timer.info/bin/api.pl',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=None,
        docs='https://www.7timer.info/doc.php',
        category='Weather'
    )

    api.save()

    # ---------------
    # APIXU
    # ---------------

    endpoints = None

    api = Api(
        name='weatherstack',
        description="Real-Time & Historical World Weather Data API Retrieve instant, accurate weather information for any location in the world in lightweight JSON format",
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
        category='Weather'
    )

    api.save()

    # ---------------
    # DWD API
    # ---------------

    endpoints = None

    api = Api(
        name='Deutscher Wetterdienst',
        description="API des Deutschen Wetterdienstes (DWD) aus der DWD App. Neben unterschiedlichen Wetterwarnungen (s.u.) lassen sich unter /dwd.api.proxy.bund.dev/v30/stationOverviewExtended nach Angabe des Parameters stationIDs (z.B. 'G005') auch die Wetterdaten ausgewählter Wetterstationen anfordern (wobei die sog. 'Stationskennung' des DWD anzugeben ist).",
        base_url='https://app-prod-ws.warnwetter.de',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://dwd.api.bund.dev/',
        category='Weather'
    )

    api.save()

    # ---------------
    # Meteoblue
    # ---------------

    endpoints = None

    api = Api(
        name='meteoblue',
        description="Weather APIs. Instantly integrate weather data and make complex decisions easy",
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
        docs='https://content.meteoblue.com/en/business-solutions/weather-apis',
        category='Weather'
    )

    api.save()

    # ---------------
    # Meteorologisk Institutt
    # ---------------

    endpoints = None

    api = Api(
        name='MET Weather API',
        description="The MET Weather API is an interface to a selection of data produced by MET Norway. The data are freely available for use under a Creative Commons license, including commercial use.",
        base_url=None,
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://api.met.no/weatherapi',
        category='Weather'
    )

    api.save()

    # ---------------
    # NOAA Climate Data
    # ---------------

    endpoints = None

    api = Api(
        name='NOAA Climate Data',
        description="Climate Data Online (CDO) provides free access to NCDC's archive of global historical weather and climate data in addition to station history information. These data include quality controlled daily, monthly, seasonal, and yearly measurements of temperature, precipitation, wind, and degree days as well as radar data and 30-year Climate Normals. Customers can also order most of these data as certified hard copies for legal use.",
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
        docs='https://www.ncdc.noaa.gov/cdo-web/webservices',
        category='Weather'
    )

    api.save()

    # ---------------
    # ODWeather
    # ---------------

    endpoints = None

    api = Api(
        name='ODWeather',
        description="This is the API for the ODWeather service including real time and forecast information",
        base_url='https://api.oceandrivers.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=False,
        cors=True,
        docs='https://api.oceandrivers.com/static/docs.html',
        category='Weather'
    )

    api.save()

    # ---------------
    # Open-Meteo
    # ---------------

    endpoints = None

    api = Api(
        name='Open-Meteo',
        description="Free Weather API Open-Meteo is an open-source weather API and offers free access for non-commercial use. No API key required. Open-Meteo partners with national weather services to bring you open data with high resolution, ranging from 1 to 11 kilometers. Our powerful APIs intelligently select the most suitable weather models for your specific location, ensuring accurate and reliable forecasts.",
        base_url='https://api.open-meteo.com',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=True,
        docs='https://open-meteo.com/en/docs',
        category='Weather'
    )

    api.save()

    # ---------------
    # OpenUV
    # ---------------

    endpoints = None

    api = Api(
        name='OpenUV',
        description="Global Real-Time UV Index JSON API. 100% Free Real-Time UV Index JSON API for inspiring Devs, Innovators and Smart Home Enthusiasts",
        base_url='https://api.openuv.io/api',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.openuv.io/',
        category='Weather'
    )

    # ---------------
    # OpenWeatherMap
    # ---------------

    endpoints = None

    api = Api(
        name='OpenWeather',
        description="Make an API call to receive access to the various data: Current weather and forecasts: minute forecast for 1 hour, hourly forecast for 48 hoursm, daily forecast for 8 days, and government weather alerts. Weather data for any timestamp for 46+ years historical archive and 4 days ahead forecast. Daily aggregation of weather data for 46+ years archive and 1.5 years ahead forecast. Weather overview with a human-readable weather summary for today and tomorrow's forecast",
        base_url='https://api.openweathermap.org/data',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=False,
        cors=None,
        docs='https://openweathermap.org/api/one-call-3',
        category='Weather'
    )

    api.save()

    # ---------------
    # Storm Glass
    # ---------------

    endpoints = None

    api = Api(
        name='The Storm Glass API',
        description="Global Weather API. Weather forecasts & historical data from the world’s most trusted meteorological institutions in one single API. Coordinates In – Weather Data Out. The stormglass.io API provides high-resolution forecasts for up to 10 days ahead as well as historical data. Marine data including tide is available for all oceans and seas world wide.",
        base_url='https://api.stormglass.io/',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=True,
        docs='https://docs.stormglass.io/',
        category='Weather'
    )

    api.save()

    # ---------------
    # Weatherbit
    # ---------------

    endpoints = None

    api = Api(
        name='Weatherbit',
        description="With our API you can retrieve current weather observations from over 50,000 live weather stations, and historical weather data for the past 20+ years sourced from stations, doppler radar, satellite, and atmospheric re-analysis products. As well as highly localized weather forecasts for any point on the globe backed by the world's most trusted weather models, and machine learning.",
        base_url='https://api.weatherbit.io',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton='apiKey',
        https=True,
        cors=None,
        docs='https://www.weatherbit.io/api',
        category='Weather'
    )

    api.save()

    # ---------------
    # National Weather Service API
    # ---------------

    endpoints = None

    api = Api(
        name='National Weather Service API',
        description="The National Weather Service (NWS) API allows developers access to critical forecasts, alerts, and observations, along with other weather data. The API was designed with a cache-friendly approach that expires content based upon the information life cycle. The API is based upon of JSON-LD to promote machine data discovery.",
        base_url='https://api.weather.gov',
        api_keywords=['Test', 'testAPI'],
        popularity=randrange(0, 10),
        service_level=randrange(0, 10),
        latency=randrange(0, 1000),
        reliability=randrange(0, 10),
        endpoints=endpoints,
        authenticaton=None,
        https=True,
        cors=None,
        docs='https://www.weather.gov/documentation/services-web-api',
        category='Weather'
    )

    api.save()

    return


    # ---------------
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