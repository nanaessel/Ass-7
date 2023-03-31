from unittest import TestCase, mock
from daos.bookmark_dao import BookmarkDAO
from src.barkylib.domain.models import Bookmark
from services.service import BookmarkService


class TestBookmarkService(TestCase):

    def setUp(self):
        self.mock_dao = mock.create_autospec(BookmarkDAO)
        self.bookmark_service = BookmarkService(self.mock_dao)

    def test_add_bookmark(self):
        bookmark = Bookmark(url='https://www.google.com', title='Google', notes='Search engine')
        self.mock_dao.add_bookmark.return_value = bookmark

        result = self.bookmark_service.add_bookmark('https://www.google.com', 'Google', 'Search engine')

        self.assertEqual(result, bookmark)
        self.mock_dao.add_bookmark.assert_called_once_with(bookmark)

    def test_add_bookmark_missing_url_and_title(self):
        with self.assertRaises(ValueError):
            self.bookmark_service.add_bookmark('', '', 'Search engine')

    def test_update_bookmark(self):
        bookmark = Bookmark(id=1, url='https://www.google.com', title='Google', notes='Search engine')
        self.mock_dao.get_bookmark_by_id.return_value = bookmark
        self.mock_dao.update_bookmark.return_value = bookmark

        result = self.bookmark_service.update_bookmark(1, 'https://www.google.com', 'Google', 'Search engine')

        self.assertEqual(result, bookmark)
        self.mock_dao.get_bookmark_by_id.assert_called_once_with(1)
        self.mock_dao.update_bookmark.assert_called_once_with(bookmark)

    def test_update_bookmark_missing_url_and_title(self):
        with self.assertRaises(ValueError):
            self.bookmark_service.update_bookmark(1, '', '', 'Search engine')

    def test_update_bookmark_not_found(self):
        self.mock_dao.get_bookmark_by_id.return_value = None

        with self.assertRaises(ValueError):
            self.bookmark_service.update_bookmark(1, 'https://www.google.com', 'Google', 'Search engine')

        self.mock_dao.get_bookmark_by_id.assert_called_once_with(1)

    def test_delete_bookmark(self):
        bookmark = Bookmark(id=1, url='https://www.google.com', title='Google', notes='Search engine')
        self.mock_dao.get_bookmark_by_id.return_value = bookmark

        self.bookmark_service.delete_bookmark(1)

        self.mock_dao.get_bookmark_by_id.assert_called_once_with(1)
        self.mock_dao.delete_bookmark.assert_called_once_with(bookmark)

    def test_delete_bookmark_not_found(self):
        self.mock_dao.get_bookmark_by_id.return_value = None

        with self.assertRaises(ValueError):
            self.bookmark_service.delete_bookmark(1)

        self.mock_dao.get_bookmark_by_id.assert_called_once_with(1)

    def test_get_all_bookmarks(self):
        bookmarks = [Bookmark(id=1, url='https://www.google.com', title='Google', notes='Search engine')]
        self.mock_dao.get_all_bookmarks.return_value = bookmarks

        result = self.bookmark_service.get_all_bookmarks()

        self.assertEqual(result, bookmarks)
        self.mock_dao.get_all_bookmarks.assert_called_once()
