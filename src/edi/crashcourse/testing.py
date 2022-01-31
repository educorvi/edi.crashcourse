# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.crashcourse


class EdiCrashcourseLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.crashcourse)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.crashcourse:default')


EDI_CRASHCOURSE_FIXTURE = EdiCrashcourseLayer()


EDI_CRASHCOURSE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_CRASHCOURSE_FIXTURE,),
    name='EdiCrashcourseLayer:IntegrationTesting',
)


EDI_CRASHCOURSE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_CRASHCOURSE_FIXTURE,),
    name='EdiCrashcourseLayer:FunctionalTesting',
)


EDI_CRASHCOURSE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_CRASHCOURSE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiCrashcourseLayer:AcceptanceTesting',
)
