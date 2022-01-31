# -*- coding: utf-8 -*-
from edi.crashcourse.content.crash_kurs import ICrashKurs  # NOQA E501
from edi.crashcourse.testing import EDI_CRASHCOURSE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CrashKursIntegrationTest(unittest.TestCase):

    layer = EDI_CRASHCOURSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_crash_kurs_schema(self):
        fti = queryUtility(IDexterityFTI, name='CrashKurs')
        schema = fti.lookupSchema()
        self.assertEqual(ICrashKurs, schema)

    def test_ct_crash_kurs_fti(self):
        fti = queryUtility(IDexterityFTI, name='CrashKurs')
        self.assertTrue(fti)

    def test_ct_crash_kurs_factory(self):
        fti = queryUtility(IDexterityFTI, name='CrashKurs')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICrashKurs.providedBy(obj),
            u'ICrashKurs not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_crash_kurs_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='CrashKurs',
            id='crash_kurs',
        )

        self.assertTrue(
            ICrashKurs.providedBy(obj),
            u'ICrashKurs not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('crash_kurs', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('crash_kurs', parent.objectIds())

    def test_ct_crash_kurs_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CrashKurs')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_crash_kurs_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='CrashKurs')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'crash_kurs_id',
            title='CrashKurs container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
