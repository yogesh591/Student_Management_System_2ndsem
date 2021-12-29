import unittest
import yogeshSMS
from tkinter import *
rootval= Tk()
a=hi.SMS(rootval)
class Test_hi(unittest.TestCase):
    def test_search(self):
        array_test = [('1', 'Ram', 'Khadka', '32', 'Dillibazaar', 'Computing'),
                      ('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing')]
        ex_result = [('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing')]
        a.entrysearch.delete(0, 'end')
        a.searchbyCB.set('FirstName')
        a.entrysearch.insert(0, 'Riya')
        ac_result = a.search_item(array_test)
        print("search test")
        print(ac_result)
        self.assertEqual(ex_result, ac_result)

    def test_bubble_sort(self):
        array_test=[('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing'),('1', 'Ram', 'Khadka', '32', 'Dillibazaar', 'Computing')]
        ex_result=[('1', 'Ram', 'Khadka', '32', 'Dillibazaar', 'Computing'),('2', 'Shyam', 'Khadka', '32', 'Patan', 'Computing')]
        a.sortord.set("ASC")
        a.searchbyCB.set("ID")

        ac_result=a.bubble_sort(array_test)
        print('Sort test')
        print(ac_result)
        self.assertEqual(ex_result,ac_result)




if __name__=='__main__':
    unittest.main()