import requests
import json
from cookies import cookies
from trends.trending import Trending
# from keywords.keywords import Keyword
# from questions.questions import Question
# from topics.topics import Topic
import os

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

LOGIN_URL = 'https://app.buzzsumo.com/login'

# Information to login buzzsumo
BUZZSUMO_EMAIL = 'akatekhanh0212@gmail.com'
BUZZSUMO_PASSWORD = 'Quockhanh0212_'

payload = {
    'email': BUZZSUMO_EMAIL,
    'password': BUZZSUMO_PASSWORD,
}


'''
Object to scrape the whole requirements
'''


class Run:
    # Init the session
    session = requests.Session()
    cookie = None

    def __init__(self):
        pass

    # Login to buzzsumo.com
    def login(self):

        burp0_url = "https://app.buzzsumo.com:443/"
        burp0_cookies = {"__cfduid": "d564364ad1e0f47bf3eb06d4652f9df9b1616226932", "first_referrer": "", "check": "true", "tracking-preferences": "{%22version%22:1%2C%22destinations%22:{%22ActiveCampaign%22:true%2C%22Facebook%20Pixel%22:true%2C%22FullStory%22:true%2C%22Google%20Analytics%22:true%2C%22Google%20Tag%20Manager%22:true%2C%22Intercom%22:true%2C%22Mixpanel%22:true%2C%22SatisMeter%22:true%2C%22Visual%20Tagger%22:true}%2C%22custom%22:{%22marketingAndAnalytics%22:true%2C%22advertising%22:true%2C%22functional%22:true}}", "ajs_anonymous_id": "%2244519a35-078a-4681-891c-8392a9495192%22", "_ga": "GA1.2.1586695038.1616226982", "_gid": "GA1.2.84586501.1616226982", "_ga": "GA1.3.1586695038.1616226982", "_gid": "GA1.3.84586501.1616226982", "fs_intercom": "5876939014283264:4817305218326528", "_fbp": "fb.1.1616227021355.1305110148", "laravel_session": "SEChkTxEPaAcvt2ZS8sRbH3FnJOPdnfGVaJlAYcx", "plan_id": "37", "mbox": "session#b21485b0c7d645c7a3bafe4e720cf23d#1616228797|PC#b21485b0c7d645c7a3bafe4e720cf23d.38_0#1679471847", "mboxEdgeCluster": "38", "__stripe_mid": "1896103a-fa21-4a54-816a-5ed1dd6a0f7c4bb0bc", "__stripe_sid": "8fbcc991-08f1-4fb6-88d5-80cff61a683107ee44", "ajs_user_id": "%22976740%22", "ajs_group_id": "%22977723%22", "mp_d35bcba68f65a6a6cf4e00a53e29ab56_mixpanel":
                         "%7B%22distinct_id%22%3A%20%22976740%22%2C%22%24device_id%22%3A%20%221784ea2946ad8-0fe843a945a777-230346d-1fa400-1784ea2946b6af%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22destinationTrackingPreferences%22%3A%20%7B%22ActiveCampaign%22%3A%20true%2C%22Facebook%20Pixel%22%3A%20true%2C%22FullStory%22%3A%20true%2C%22Google%20Analytics%22%3A%20true%2C%22Google%20Tag%20Manager%22%3A%20true%2C%22Intercom%22%3A%20true%2C%22Mixpanel%22%3A%20true%2C%22SatisMeter%22%3A%20true%2C%22Visual%20Tagger%22%3A%20true%7D%2C%22customTrackingPreferences%22%3A%20%7B%22marketingAndAnalytics%22%3A%20true%2C%22advertising%22%3A%20true%2C%22functional%22%3A%20true%7D%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22976740%22%2C%22mp_name_tag%22%3A%20%22akatekhanh0212%40gmail.com%22%2C%22company_name%22%3A%20null%2C%22account_id%22%3A%20977723%2C%22user_paying%22%3A%20false%2C%22plan_feature_level%22%3A%20%22pro%22%2C%22team_alerts_created%22%3A%200%2C%22role%22%3A%20null%2C%22goals%22%3A%20%5B%5D%2C%22plan_name%22%3A%20%22Pro%20-%20Monthly%22%2C%22plan_interval%22%3A%20%22month%22%2C%22plan_id%22%3A%2037%2C%22team_size%22%3A%201%2C%22user_on_free_trial%22%3A%20true%2C%22cancel_pending%22%3A%20false%2C%22last_api_update_from_web_app%22%3A%20%222021-03-20T07%3A57%3A24.000Z%22%2C%22email_verified%22%3A%20true%2C%22marketing_consent%22%3A%20false%2C%22api_auth%22%3A%20false%2C%22has_api_key%22%3A%20false%2C%22industry%22%3A%20null%2C%22max_company_size%22%3A%200%2C%22alexa_rank%22%3A%200%2C%22monthly_spend%22%3A%209900%2C%22previous_month_usage_score%22%3A%2065%2C%22usage_score%22%3A%2068%2C%22team_usage_score%22%3A%2068%2C%22free_trial_restart_count%22%3A%20null%2C%22webinar_type%22%3A%20null%2C%22used_analyze%22%3A%200%2C%22used_influencers%22%3A%200%2C%22used_articles%22%3A%200%2C%22used_sharers%22%3A%200%2C%22used_trending%22%3A%2022%2C%22used_shared_links%22%3A%200%2C%22used_links%22%3A%200%2C%22used_twitter_audience%22%3A%200%2C%22used_facebook_status%22%3A%200%2C%22used_projects%22%3A%200%2C%22used_exports%22%3A%200%2C%22used_alerts%22%3A%200%2C%22used_questions%22%3A%2053%2C%22opened_alert_email%22%3A%200%2C%22heard_about_from%22%3A%20null%2C%22landing_page_registration%22%3A%20false%2C%22cc_upfront%22%3A%20false%2C%22cc_upfront_trial_start_date%22%3A%20null%2C%22app_experiment_8%22%3A%20%22a%22%2C%22free_trial_started_at%22%3A%20%222021-03-02T01%3A23%3A15.000Z%22%2C%22last_login_at%22%3A%20%222021-03-20T07%3A57%3A21.000Z%22%2C%22team_usage_score_diff%22%3A%205%2C%22id%22%3A%20%22976740%22%2C%22%24created%22%3A%20%222021-03-02T01%3A23%3A15.000Z%22%2C%22%24email%22%3A%20%22akatekhanh0212%40gmail.com%22%2C%22%24first_name%22%3A%20%22Quoc%22%2C%22%24last_name%22%3A%20%22Khanh%22%2C%22%24name%22%3A%20%22Quoc%20Khanh%22%7D", "fs_uid": "rs.fullstory.com#1aXZ#5876939014283264:4817305218326528#127da9ea#/1647762981", "_dc_gtm_UA-44233940-1": "1", "XSRF-TOKEN": "eyJpdiI6IlExL00vY3JRYmh3aXd6d3hPR3AzNnc9PSIsInZhbHVlIjoic29jemVhT2dwTS9iemd4Zmo2YVgya0oxYkFzZ3FBZHU3V1dQdlhUemRwQmliWHBIdllzeFlZOU42R0lERGg5UWNhY1graHVIaUhDczBWWUdiRSs0OFZkWTJtT0E0VUxFWUZ1OXVTRFcrQzdWZ1B5VU8wZ1I1RFZ4dUVvcTkyMmYiLCJtYWMiOiI4NjYwYzY0NTQ5NmYwYmQyYzA4ZjAwOWVkYjRiNDY4Mjk4ZjM0ZjY0MTg2N2FjZGFiNTViM2ZhMzRkOTI1ZjgyIn0%3D", "_gat_UA-44233940-1": "1"}
        burp0_headers = {"Connection": "close", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                         "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
        self.session.get(burp0_url, headers=burp0_headers,
                         cookies=burp0_cookies)
        # self.session.post(LOGIN_URL, data=payload)
        # self.cookie = self.session.cookies.get_dict()
        # cookies.save_session(self.session)
        # cookies.load_sesion(self.session)

    '''
    To scrape trending
        Paramater:
            topic(str): One or multiple topics. Multiple topics must be separated by a comma
            hours(int): the mount of time you want to scrape.
            count(int): the number of articles you want to scrape.
            search_type(str): Either "trending_now" for articles sorted by trending score
                or "most_shared" for articles sorted by total shares/engagement.
            domains(str): pass one or more domains(comma seperated) to see contents just from
                those sites.
            blocked_domains: pass one or more( comma separated) to hide contents from those sites
            session(object of requests module): to save the informations like cookies
        Return: None
    '''

    def get_trends(self, topic, hours, count, search_type=None, domains=None, blocked_domains=None):
        trends = Trending(self.session, topic, hours, count,
                          search_type, domains, blocked_domains, self.cookie)

        # Return a Response object
        data = trends.get_trends()
        trends.write_to_json(data)
        return data


# To run program
def main():
    program = Run()
    program.login()

    list_topic = ['news', 'sports', 'tech', 'business', 'science', 'polictics',
                  'marketing', 'education', 'fashion', 'health', 'video', 'entertainment']

    # for item in list_topic:
    res = program.get_trends(topic='fashion',
                             hours=24,
                             count=50,
                             search_type='most_shared',
                             domains="facebook.com",
                             #  blocked_domains="bbc.com,katu.com"
                             )

    # return json.loads(res.text)
    return "Parse successfully!"


main()
