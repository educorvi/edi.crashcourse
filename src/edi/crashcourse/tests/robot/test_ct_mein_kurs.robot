# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.crashcourse -t test_mein_kurs.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.crashcourse.testing.EDI_CRASHCOURSE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/crashcourse/tests/robot/test_mein_kurs.robot
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

Scenario: As a site administrator I can add a MeinKurs
  Given a logged-in site administrator
    and an add MeinKurs form
   When I type 'My MeinKurs' into the title field
    and I submit the form
   Then a MeinKurs with the title 'My MeinKurs' has been created

Scenario: As a site administrator I can view a MeinKurs
  Given a logged-in site administrator
    and a MeinKurs 'My MeinKurs'
   When I go to the MeinKurs view
   Then I can see the MeinKurs title 'My MeinKurs'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add MeinKurs form
  Go To  ${PLONE_URL}/++add++MeinKurs

a MeinKurs 'My MeinKurs'
  Create content  type=MeinKurs  id=my-mein_kurs  title=My MeinKurs

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the MeinKurs view
  Go To  ${PLONE_URL}/my-mein_kurs
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a MeinKurs with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the MeinKurs title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
