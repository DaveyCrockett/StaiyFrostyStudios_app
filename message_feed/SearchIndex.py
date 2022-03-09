import datetime
from haystack import indexes
from .models import Message


class MessageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='creator')
    pub_date = indexes.DateTimeField(model_attr='created_on')

    def get_model(self):
        return Message

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())