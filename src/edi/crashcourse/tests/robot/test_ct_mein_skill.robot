# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.crashcourse -t test_mein_skill.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.crashcourse.testing.EDI_CRASHCOURSE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/crashcourse/tests/robot/test_mein_skill.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a MeinSkill
  Given a logged-in site administrator
    and an add MeinKurs form
   When I type 'My MeinSkill' into the title field
    and I submit the form
   Then a MeinSkill with the title 'My MeinSkill' has been created

Scenario: As a site administrator I can view a MeinSkill
  Given a logged-in site administrator
    and a MeinSkill 'My MeinSkill'
   When I go to the MeinSkill view
   Then I can see the MeinSkill title 'My MeinSkill'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MeinKurs form
  Go To  ${PLONE_URL}/++add++MeinKurs

a MeinSkill 'My MeinSkill'
  Create content  type=MeinKurs  id=my-mein_skill  title=My MeinSkill

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MeinSkill view
  Go To  ${PLONE_URL}/my-mein_skill
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MeinSkill with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MeinSkill title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
