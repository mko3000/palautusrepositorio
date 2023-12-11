from matchers import *
from player_reader import PlayerReader
from statistics import Statistics

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._players = matcher

    def build(self):
        return self._players
    
    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team),self._players))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value,attr),self._players))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr),self._players))
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))