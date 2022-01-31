# -*- coding: utf-8 -*-
from edi.crashcourse.content.mein_kurs import IMeinKurs  # NOQA E501
from edi.crashcourse.testing import EDI_CRASHCOURSE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MeinKursIntegrationTest(unittest.TestCase):

    layer = EDI_CRASHCOURSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mein_kurs_schema(self):
        fti = queryUtility(IDexterityFTI, name='MeinKurs')
        schema = fti.lookupSchema()
        self.assertEqual(IMeinKurs, schema)

    def test_ct_mein_kurs_fti(self):
        fti = queryUtility(IDexterityFTI, name='MeinKurs')
        self.assertTrue(fti)

    def test_ct_mein_kurs_factory(self):
        fti = queryUtility(IDexterityFTI, name='MeinKurs')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMeinKurs.providedBy(obj),
            u'IMeinKurs not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_mein_kurs_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='MeinKurs',
            id='mein_kurs',
        )

        self.assertTrue(
            IMeinKurs.providedBy(obj),
            u'IMeinKurs not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('mein_kurs', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mein_kurs', parent.objectIds())

    def test_ct_mein_kurs_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MeinKurs')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_mein_kurs_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MeinKurs')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'mein_kurs_id',
            title='MeinKurs container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
