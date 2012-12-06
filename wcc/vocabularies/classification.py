from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
import pycountry

CLASSIFICATIONS=[
    {
        'id': 'developing-country',
        'title': 'Developing Country'
    },
]

class VocabularyFactory(object):
    def __call__(self, context):
        terms= [SimpleTerm(
                    value=i['id'], 
                    title=i['title']) for i in CLASSIFICATIONS]
        return SimpleVocabulary(terms)

grok.global_utility(VocabularyFactory, IVocabularyFactory,
        name='wcc.vocabulary.classification')
