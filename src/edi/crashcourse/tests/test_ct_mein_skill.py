# -*- coding: utf-8 -*-
from edi.crashcourse.content.mein_skill import IMeinSkill  # NOQA E501
from edi.crashcourse.testing import EDI_CRASHCOURSE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MeinSkillIntegrationTest(unittest.TestCase):

    layer = EDI_CRASHCOURSE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'MeinKurs',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_mein_skill_schema(self):
        fti = queryUtility(IDexterityFTI, name='MeinSkill')
        schema = fti.lookupSchema()
        self.assertEqual(IMeinSkill, schema)

    def test_ct_mein_skill_fti(self):
        fti = queryUtility(IDexterityFTI, name='MeinSkill')
        self.assertTrue(fti)

    def test_ct_mein_skill_factory(self):
        fti = queryUtility(IDexterityFTI, name='MeinSkill')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMeinSkill.providedBy(obj),
            u'IMeinSkill not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_mein_skill_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='MeinSkill',
            id='mein_skill',
        )

        self.assertTrue(
            IMeinSkill.providedBy(obj),
            u'IMeinSkill not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('mein_skill', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mein_skill', parent.objectIds())

    def test_ct_mein_skill_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MeinSkill')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
