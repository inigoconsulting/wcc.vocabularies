from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
import pycountry

RELIGIONS=[
    {
        'id': 'christian',
        'title': 'Christian',
        'follower': 'Christian'
    }, {
        'id': 'islam',
        'title': 'Islam',
        'follower': 'Muslim'
    }, {
        'id': 'buddhism',
        'title': 'Buddhism',
        'follower': 'Buddhist'
    }, {
        'id': 'hindu',
        'title': 'Hindu',
        'follower': 'Hindu'
    }, {
        'id': 'judaism',
        'title': 'Judaism',
        'follower': 'Jews'
    }, {
        'id': 'african-traditional',
        'title': 'African Traditional',
        'follower': 'African Traditional'
    }, {
        'id': 'other',
        'title': 'Other',
        'follower': 'Other'
    }
]

class VocabularyFactory(object):
    def __call__(self, context):
        terms = [SimpleTerm(value=i['id'],
                    title=i['title']) for i in RELIGIONS]
        return SimpleVocabulary(terms)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='wcc.vocabulary.religion')

class FollowerVocabularyFactory(object):
    def __call__(self, context):
        terms = [SimpleTerm(value=i['id'],
                    title=i['follower']) for i in RELIGIONS]
        return SimpleVocabulary(terms)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='wcc.vocabulary.religionfollower')
