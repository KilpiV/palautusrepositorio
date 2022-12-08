from matchers import *

class QueryBuilder:
    def __init__(self, query = All()): 
        self.query_obj = query

    def build(self):
        return self.query_obj

    def and_query(self, matchers):
        return QueryBuilder(And(self.query_obj, matchers))
    
    def oneOf(self, match1, match2):
        return QueryBuilder(Or(match1, match2))
 
    def not_query(self, matcher):
        return QueryBuilder(And(self.query_obj, Not(self.query_obj, matcher)))
 
    def playsIn(self, team):
        return QueryBuilder(And(self.query_obj, PlaysIn(team)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_obj, HasFewerThan(value, attr)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_obj, HasAtLeast(value, attr)))
    