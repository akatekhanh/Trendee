from mongoengine import connect, Document, ListField, StringField, URLField
connect(db="db_trendee", host="mongodb://localhost:27017/db_trendee", port=27017)


class Test(Document):
    title = StringField(required=True, max_length=70)


test = Test(title="Ngo Quoc Khanh")
test.save()
print(Test.objects().first().title)
