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
import caesar

def escape_html(s):
    return cgi.escape(s, quote = True)




thecontent = """
<form method="post">
    <h1>Web Caesar</h1>
    <br>
    <label>Rotate by:
    <input type="number" name="rotvalue" value="%(rotvalue)s"/>
    </label>
    <br>
    <label>Type a message:
    <textarea name="thetext">%(thetext)s</textarea>
    </label>
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
        thenewtext = caesar.encrypt(user_text, user_rot)
        escaped_message = cgi.escape(thenewtext)
        self.write_content(escaped_message, user_rot)




app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
