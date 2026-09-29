# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
from collections import deque


class HtmlParser:
   def getUrls(self, url) -> list[str]:
       """
       :type url: str
       :rtype List[str]
       """
       return []

class Solution:
    # BFS
    # Time O(ml)
    # Space O(nl)
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        def get_hostname(url):
            # split url by slashes
            # for instance, "http://example.org/foo/bar" will be split into
            # "http:", "", "example.org", "foo", "bar"
            # the hostname is the 2-nd (0-indexed) element
            return url.split('/')[2]

        start_hostname = get_hostname(startUrl)

        # BFS while there are new things to add
        q = deque([startUrl])
        visited = {startUrl}
        while q:
            url = q.popleft()

            # Get all urls from this url and add any that aren't visited
            for next_url in htmlParser.getUrls(url):
                if get_hostname(next_url) == start_hostname and next_url not in visited:
                    q.append(next_url)
                    visited.add(next_url)

        return list(visited)
