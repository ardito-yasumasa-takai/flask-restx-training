def setup(api):

    from app.resources.article import api as article

    api.namespaces.clear()
    api.add_namespace(article)
