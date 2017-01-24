# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import cgi
from caesar import encrypt, rotate_character, alphabet_position

def escape_html(s):
    return cgi.escape(s, quote = True)




thecontent = """
<form method="post">
    What do you want rot13ed?
    <br>

    <label>
    <textarea name="thetext">%(thetext)s</textarea>
    </label>

    <label>
    <input type="text" name="rotvalue" value="%(rotvalue)s">
    </label>

    <br>
    <br>
    <input type="submit">
</form>"""



class MainPage(webapp2.RequestHandler):
    def write_content(self, thetext="", rotvalue=""):
        self.response.out.write(thecontent % {"thetext": thetext, "rotvalue": rotvalue})



    def get(self):
        self.write_content()

    def post(self):
        user_text = self.request.get('thetext')
        user_rot = self.request.get('rotvalue')
        thenewtext = encrypt(user_text, user_rot)
        self.write_content(thenewtext, user_rot)




app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
