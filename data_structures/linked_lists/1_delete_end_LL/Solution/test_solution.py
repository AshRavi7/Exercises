# import unittest
# import pytest
# from unittest.mock import patch
# from solution import Node,LinkedList


# class TestLinked(unittest.TestCase):

#     # @classmethod
#     # def setUpClass(cls):
#     #     print('setupClass')

#     # @classmethod
#     # def tearDownClass(cls):
#     #     print('teardownClass')
#     def setUp(self):
#         print('setUp')
#         self.l_1 =LinkedList()
#         # self.l_2 = Employee('Sue', 'Smith', 60000)

#     def tearDown(self):
#         print('tearDown\n')

#     def test_insert_at_start(self):
#         print('test_insert')
#         self.l_1.insert_at_start(100)
#         self.l_1.insert_at_start(200)
#         self.l_1.insert_at_start(300)
#         self.l_1.insert_at_start(400)
#         self.l_1.insert_at_start(500)
#         # self.l_1.insert_at_start(300)
#         # self.l_1.insert_at_start(700)
#         # self.assertEqual(self.l_1.__str__(), "100")
#         self.assertEqual(self.l_1.__str__(),'500')

#     def test_delete_at_end(self):
#         print('test_delete')
#         self.l_1.delete_at_end()
    
#     def test_traverse(monkeypatch):
#         print('test_traverse')
#         ret_val1= None
#         def g(num1,end=" "):
#             nonlocal ret_val1
#             ret_val1=num1
#         monkeypatch.setattr('builtins.print',g)

#         import solution
        
#         assert ret_val1==[i for i in  ['500','400','300','200']]

# if __name__=='__main__':
#      unittest.main()
