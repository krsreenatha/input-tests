#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Firefox Input.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2010
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Vishal
#                 David Burns
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
'''
Created on Nov 24, 2010
'''
import input_base_page
import vars

import time
import re

page_load_timeout = vars.ConnectionParameters.page_load_timeout


class ThemesPage(input_base_page.InputBasePage):

    _page_title              =  'Themes'
    _messages_count          =  "css=div[id='big-count'] > p"

    def __init__(self, selenium):
        '''
            Creates a new instance of the class
        '''
        super(ThemesPage, self).__init__(selenium)

    def go_to_themes_page(self):
        self.sel.open('/en-US/themes/')
        count = 0
        while (re.search(self._page_title, self.sel.get_location(), re.IGNORECASE)) is None:
            time.sleep(1)
            count += 1
            if count == 20:
                raise Exception("Themes Page has not loaded")
