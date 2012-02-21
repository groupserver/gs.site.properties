from gs.option.converter import GSOptionConverterFactory
import zope.schema
import zope.interface
import pytz
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

class IGSSiteOptions(zope.interface.Interface): 
    tz = zope.schema.Choice(title=u'Timezone',
      description=u'The timezone you wish to use as the default across the site.',
      required=False,
      vocabulary=SimpleVocabulary.fromValues(pytz.common_timezones))

    profileInterface = zope.schema.TextLine(title=u"Profile Interface",
                                  required=False)

    canonicalHost = zope.schema.TextLine(title=u"The hostname that should be used for this site",
                                  required=False)

    canonicalPort = zope.schema.Int(title=u"The port that should be used for this site",
                                  default=8080,
                                  constraint=lambda x: x >= 1 and x <= 65535,
                                  required=False)

class GSSiteOptionFactory(GSOptionConverterFactory):
    interface = IGSSiteOptions
    descriminators = ('site_id',)
    