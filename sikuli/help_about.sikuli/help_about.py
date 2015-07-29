import sys
sys.path.insert(0, '/home/vagrant/Integration-Testing-Framework/sikuli/examples')

from flex_regions import *
from test_helper import TestHelper

# Setup
helper = TestHelper("help_about")
set_flex_helper(helper)

# Opening
#############
TOOLBARS.Click("Help.png", "Help button not found")
helper.Click("AboutLanguag.png", "About Language Explorer button not found")

# Goal
#############
helper.Exists("7AboutSILFle.png", "`About` screen didn't pop up")

# Closing
#############
helper.Click("OK.png", "`About` screen doesn't contain `OK`", restart=True)

helper.write_success()

