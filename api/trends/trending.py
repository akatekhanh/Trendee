import json
from cookies import cookies
from utils import Utils as _
import os


class Trending:
    '''
    Object to process scrape trendings from trending_url
        Parameters: 
            topic(str): One or multiple topics. Multiple topics must be separated by a comma
            hours(int): the mount of time you want to scrape.
            count(int): the number of articles you want to scrape.
            search_type(str): Either "trending_now" for articles sorted by trending score 
                or "most_shared" for articles sorted by total shares/engagement.
            domains(str): pass one or more domains(comma seperated) to see contents just from
                those sites.
            blocked_domains: pass one or more( comma separated) to hide contents from those sites
            session(object of requests module): to save the informations like cookies
    '''
    trending_url = 'https://app.buzzsumo.com/search/trends'

    def __init__(self, session, topic, hours, count, search_type,
                 domains, blocked_domains, cookie):
        self.topic = topic
        self.hours = hours
        self.count = count
        self.search_type = search_type
        self.domains = domains
        self.blocked_domains = blocked_domains
        self.cookie = cookie
        self.session = session

        if self.search_type not in ['trending_now', 'most_shared']:
            self.search_type = 'trending_now'

        self.params = {
            'sort': 'trending_now',
            # 'id': '67228',
            'language': 'en',
            'topic': topic,
            'hours': 24,
            'count': 24,
            'ignore': "false",
            'search_type': search_type,
            'domain': domains,
            'blocked_domains': blocked_domains,
        }

    '''
    Get trends from trending_url with params
        Params: None
        Return: a <request.Response> object 
    '''

    def get_trends(self):
        return self.session.get(self.trending_url, params=self.params, cookies=self.cookie)

    '''
    To parse data and save it to json files
    '''

    def write_to_json(self, data):
        path = os.path.join(
            os.getcwd(),
            "data",
            "trending"
        )
        _.make_path(path)
        path = os.path.join(path, "{}.json".format(self.topic))
        with open(path, 'w') as outfile:
            outfile.write(json.dumps(data.json(), indent=4))
