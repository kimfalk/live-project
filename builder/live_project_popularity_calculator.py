import os
from decimal import Decimal

import pandas as pd
import psycopg2
import sqlite3
import logging
from tqdm import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import coo_matrix
from datetime import datetime

from recommender.models import MovieDescriptions

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prs_project.settings")

import django

django.setup()

from analytics.models import Rating

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger('LiveProject Popularity Calculator')

class LiveProjectPopularityCalculator(object):

    def __init__(self, save_path='/.models/lp_charts/'):
        self.save_path = save_path


    def build(self, ratings):
        movie_descriptions = self.load_movies_with_genres()

    def load_movies_with_genres(self):
        """

        :return:
        """

        docs = list(MovieDescriptions.objects.all())
        data = ["{}, {}, {}".format(d.movie_id, d.title, d.genres) for d in docs]

        if len(data) == 0:
            print("No descriptions were found, run populate_sample_of_descriptions")
        return data, docs

def load_all_ratings(min_ratings=1):
    """
    Load all ratings from users who has a minimum of <min_ratings> ratings
    :return:
    """
    columns = ['user_id', 'movie_id', 'rating', 'type', 'rating_timestamp']

    ratings_data = Rating.objects.all().values(*columns)

    ratings = pd.DataFrame.from_records(ratings_data, columns=columns)

    user_count = ratings[['user_id', 'movie_id']].groupby('user_id').count()
    user_count = user_count.reset_index()
    user_ids = user_count[user_count['movie_id'] > min_ratings]['user_id']
    ratings = ratings[ratings['user_id'].isin(user_ids)]

    ratings['rating'] = ratings['rating'].astype(Decimal)
    return ratings

if __name__ == '__main__':

    logger.info("[BEGIN] Calculating charts")

    lppc = LiveProjectPopularityCalculator()
    loaded_ratings = load_all_ratings()
    logger.info("using {} ratings".format(loaded_ratings.shape[0]))

    lppc.build(loaded_ratings)
    logger.info("[DONE] Calculating charts")