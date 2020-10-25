import collections
import decimal
import csv
import json
import pickle
from decimal import Decimal

import pandas as pd
from django.db.models import Avg

from analytics.models import Rating
from recommender.models import Recs
from recs.base_recommender import base_recommender


class NonNegativeMFRecs(base_recommender):

    def __init__(self, save_path='./nnmf_recs.csv'):
        self.save_path = save_path
        self.model_loaded = False
        self.recs = dict()

    def load_model(self, save_path):

        with open(save_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                user, *reclist = row
                self.recs[user] = reclist
        print(f"model loaded with {len(self.recs.keys())} users")

    def predict_score(self, user_id, item_id):
        pass

    def recommend_items(self, user_id, num=6):

        if not self.model_loaded:
            print("loading model")
            self.load_model(self.save_path)
        print(user_id)
        active_user_items = Rating.objects.filter(user_id=user_id).order_by('-rating')[:100]
        rated_movies = [movie.movie_id for movie in active_user_items]
        print("active_user:", rated_movies)

        result = []
        for rec in self.recs.get(str(user_id), []):
            rec, rating = rec.split(':', 1)
            if rec not in rated_movies:
                result.append((rec, float(rating)))

        print("recs: ", result)
        return result[:num]

    def recommend_items_by_ratings(self, user_id, active_user_items, num=6):
        pass