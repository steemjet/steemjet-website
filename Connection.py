from beem.discussions import Query, Discussions_by_trending, Discussions_by_blog
from beem.account import Account
from beem.comment import Comment
from beem.exceptions import ContentDoesNotExistsException

query = Query(limit=10, tag="steemjet")
query2 = Query(limit=10, tag="dimimp")


def post_info():
    info = []
    for post in Discussions_by_trending(query):
        if "image" in post.json_metadata:
            picture = post.json_metadata["image"]
            acc = Account(post["author"])
            rep = acc.rep
            info += [{
                "title": post["title"],
                "content": post.body[:200],
                "author": post["author"],
                "author_rep": rep,
                "image": picture[0],
                "permalink": post["permlink"]
            }]
        elif "image" in post.json_metadata:
            if "http" in post.json_metadata["image"]:
                picture = post.json_metadata["image"]
                acc = Account(post["author"])
                rep = acc.rep
                info += [{
                    "title": post["title"],
                    "content": post.body[:200],
                    "author": post["author"],
                    "author_rep": rep,
                    "image": picture[0],
                    "sec_image": picture[1],
                    "permalink": post["permlink"]
                }]
        else:
            acc = Account(post["author"])
            rep = acc.rep
            info += [{
                "title": post["title"],
                "content": post.body[:200],
                "author": post["author"],
                "author_rep": rep,
                "permalink": post["permlink"]
            }]
    return info


def info(permalink):
    post = Comment(permalink)
    p_export = post.json()
    p_info = [{
        "body": p_export["body"],
        "title": p_export["title"],
        "author": p_export["author"],
        "permalink": p_export["permlink"]
    }]
    return p_info


def post_activity():
    info = []
    for post in Discussions_by_blog(query2):
        if "image" in post.json_metadata:
            picture = post.json_metadata["image"]
            acc = Account(post["author"])
            rep = acc.rep
            info += [{
                "title": post["title"],
                "content": post.body[:200],
                "author": post["author"],
                "author_rep": rep,
                "image": picture[0],
                "permalink": post["permlink"]
            }]
        elif "image" in post.json_metadata:
            if "http" in post.json_metadata["image"]:
                picture = post.json_metadata["image"]
                acc = Account(post["author"])
                rep = acc.rep
                info += [{
                    "title": post["title"],
                    "content": post.body[:200],
                    "author": post["author"],
                    "author_rep": rep,
                    "image": picture[0],
                    "sec_image": picture[1],
                    "permalink": post["permlink"]
                }]
        else:
            acc = Account(post["author"])
            rep = acc.rep
            info += [{
                "title": post["title"],
                "content": post.body[:200],
                "author": post["author"],
                "author_rep": rep,
                "permalink": post["permlink"]
            }]
    return info