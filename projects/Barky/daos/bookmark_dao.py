from typing import List, Dict
from src.barkylib.domain.models import Bookmark

class BookmarkDAO:
    def __init__(self):
        self.bookmarks = []

    def create_bookmark(self, bookmark: Bookmark) -> int:
        bookmark.id = len(self.bookmarks) + 1
        self.bookmarks.append(bookmark)
        return bookmark.id

    def update_bookmark(self, bookmark_id: int, bookmark: Bookmark) -> None:
        for i in range(len(self.bookmarks)):
            if self.bookmarks[i].id == bookmark_id:
                self.bookmarks[i] = bookmark
                return

    def delete_bookmark(self, bookmark_id: int) -> None:
        for i in range(len(self.bookmarks)):
            if self.bookmarks[i].id == bookmark_id:
                del self.bookmarks[i]
                return

    def get_bookmark_by_id(self, bookmark_id: int) -> Bookmark:
        for bookmark in self.bookmarks:
            if bookmark.id == bookmark_id:
                return bookmark
        return None

    def get_all_bookmarks(self) -> List[Bookmark]:
        return self.bookmarks
