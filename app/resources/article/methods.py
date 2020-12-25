from flask_restx import Namespace, Resource

from .models import ArticleModel

api = Namespace("articles", description="記事")
article_model = ArticleModel(api)


@api.route("")
class ArticleList(Resource):
    @api.marshal_list_with(article_model.article_get_response_model())
    def get(self):
        pass

    @api.expect(article_model.article_post_request_model())
    def post(self):
        pass


@api.route("/<int:id>")
class Article(Resource):
    @api.marshal_with(article_model.article_get_response_model())
    def get(self, id):
        pass

    @api.expect(article_model.article_put_request_model())
    def put(self, id):
        pass

    def delete(self, id):
        pass
