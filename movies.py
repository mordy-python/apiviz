from rotten_tomatoes_client import RottenTomatoesClient, TvBrowsingCategory, MovieBrowsingQuery, Service, Genre, SortBy, MovieBrowsingCategory


def get_most_popular():
    results = RottenTomatoesClient.browse_tv_shows(
        category=TvBrowsingCategory.most_popular)
    return results['results']

def get_action():
    query = MovieBrowsingQuery(
        services=[Service.netflix, Service.amazon_prime, Service.amazon, Service.vudu, Service.hbo_go], category=MovieBrowsingCategory.all_dvd_and_streaming, sort_by=SortBy.popularity, genres=[Genre.action])
    result = RottenTomatoesClient.browse_movies(query)
    result = result['results']
    return result
def get_comedy():
    query = MovieBrowsingQuery(
        services=[Service.netflix, Service.amazon_prime, Service.amazon, Service.vudu, Service.hbo_go], category=MovieBrowsingCategory.all_dvd_and_streaming, sort_by=SortBy.popularity, genres=[Genre.comedy])
    result = RottenTomatoesClient.browse_movies(query)
    result = result['results']
    return result
def get_kids_and_family():
    query = MovieBrowsingQuery(
        services=[Service.netflix, Service.amazon_prime, Service.amazon, Service.vudu, Service.hbo_go], category=MovieBrowsingCategory.all_dvd_and_streaming, sort_by=SortBy.popularity, genres=[Genre.kids_and_family])
    result = RottenTomatoesClient.browse_movies(query)
    result = result['results']
    return result