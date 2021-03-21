from mongoengine import connect, Document, ListField, StringField, URLField, IntField
import json
connect(db="db_trendee", host="mongodb://localhost:27017/db_trendee", port=27017)


class Article(Document):
    kind = StringField()
    twitter = StringField()
    author_name = StringField()
    publisher_rank = IntField()
    avg_fb_share = IntField()
    domain_authority = IntField()
    published_date_diff = StringField()
    trending_score = IntField()
    title = StringField()
    url_image = URLField()
    fb_like = StringField()
    fb_share = StringField()
    youtube_like = StringField()
    youtube_views = StringField()
    twitter_like = StringField()
    twitter_share = StringField()
    total_share = StringField()
    total_react = StringField()


list_topic = ['news', 'sports', 'tech', 'business', 'science', 'polictics',
              'marketing', 'education', 'fashion', 'health', 'video', 'entertainment']
for kind in list_topic:
    print(kind)
    with open('data/trending/' + kind + '.json', 'r') as file:
        data = json.load(file)

    result = data['results']
    for item in result:
        article = Article(
            kind='news',
            twitter=item['author_details']['twitter']['username'] if len(
                item['author_details']['twitter']) != 0 else "None",
            author_name=item['author_details']['author_name'],
            publisher_rank=item['author_details']['publisher']['alexa_rank'],
            avg_fb_share=item['author_details']['publisher']['average_facebook_shares'],
            domain_authority=item['author_details']['publisher']['domain_authority'],
            published_date_diff=item['published_date_diff'],
            trending_score=item['trending_score'],
            title=item['title'],
            url_image=item['thumbnail'],
            fb_like=item['facebook_likes'] if isinstance(
                item['facebook_likes'], str) else str(item['facebook_likes']),
            fb_share=item['facebook_shares'] if isinstance(
                item['facebook_shares'], str) else str(item['facebook_shares']),
            youtube_like=item['youtube_likes'],
            youtube_views=item['youtube_views'],
            twitter_share=item['twitter_shares'] if isinstance(
                item['twitter_shares'], str) else str(item['twitter_shares']),
            total_share=item['total_shares'],
            total_react=item['total_reactions_percentage'] if isinstance(
                item['total_reactions_percentage'], str) else str(item['total_reactions_percentage'])
        )
        article.save()
