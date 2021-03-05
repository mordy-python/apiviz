from rotten_tomatoes_client import RottenTomatoesClient, TvBrowsingCategory

def get_most_popular():
    results = RottenTomatoesClient.browse_tv_shows(
        category=TvBrowsingCategory.most_popular)
    return results['results']