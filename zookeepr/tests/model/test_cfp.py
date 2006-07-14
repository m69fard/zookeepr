import md5

from zookeepr.tests.model import *

class TestCFP(ModelTest):
    model = 'CFP'

    samples = [dict(handle='testguy',
                    email_address='testguy@example.org',
                    password='passw04d',
                    firstname='Firstname',
                    lastname='Lastname',
                    title="title yo",
                    type=1,
                    abstract="abstract yo",
                    experience="some",
                    url="url",
                    assistance=True,
                    ),
               ]

    mangles = dict(password=lambda p: md5.new(p).hexdigest())

    def test_cfp_registration(self):
        # submit to the cfp
        # get out the url hash because i don't know how to trap smtplib
        # visit the url
        # check the rego worked

        pass