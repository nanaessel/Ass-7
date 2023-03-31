from daos.bookmark_dao import BookmarkDAO
from src.barkylib.domain.models import Bookmark
from typing import List


class BookmarkService:
    def __init__(self, bookmark_dao: BookmarkDAO):
        self.bookmark_dao = bookmark_dao

    def add_bookmark(self, url: str, title: str, notes: str) -> Bookmark:
      
        if not url or not title:
            raise ValueError("URL et titre sont requis")

      
        bookmark = Bookmark(url=url, title=title, notes=notes)

        return self.bookmark_dao.add_bookmark(bookmark)

    def update_bookmark(self, id: int, url: str, title: str, notes: str) -> Bookmark:
     
        if not url or not title:
            raise ValueError("URL et titre sont requis")

        
        bookmark = self.bookmark_dao.get_bookmark_by_id(id)
        if not bookmark:
            raise ValueError("Signet non trouvé")
        
        bookmark.url = url
        bookmark.title = title
        bookmark.notes = notes

        return self.bookmark_dao.update_bookmark(bookmark)

    def delete_bookmark(self, id: int) -> None:
        
        bookmark = self.bookmark_dao.get_bookmark_by_id(id)
        if not bookmark:
            raise ValueError("Signet non trouvé")

        return self.bookmark_dao.delete_bookmark(bookmark)

    def get_all_bookmarks(self) -> List[Bookmark]:
        
        return self.bookmark_dao.get_all_bookmarks()
