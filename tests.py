import unittest
from main import app
from io import BytesIO
class IndexPageTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_page_renders_correctly(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Поиск самого частого слова в файле', response.data.decode('utf-8'))

    def test_file_upload_success(self):
        test_file = BytesIO(b'hello world')
        test_file.name = 'test.txt'
        response = self.app.post('/', data={'file': test_file})
        self.assertEqual(response.status_code, 200)

    def test_most_common_word_is_displayed(self):
        test_file = BytesIO(b'hello world hello')
        test_file.name = 'test.txt'
        response = self.app.post('/', data={'file': test_file})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'hello', response.data)

if __name__ == '__main__':
    unittest.main()