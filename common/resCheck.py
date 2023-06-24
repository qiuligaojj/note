import unittest

class ResCheck(unittest.TestCase):
    def res_check(self,expected_body,response):
        self.assertEqual(len(expected_body),len(response))
        for k,v in expected_body.items():
            self.assertIn(k,response.keys())
            self.assertEqual(v,type(response[k]))
















