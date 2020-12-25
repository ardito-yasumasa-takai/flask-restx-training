from flask_restx import fields


class ArticleModel:
    def __init__(self, api):
        self.api = api

    article_id = fields.Integer(
        title="articleId",
        description="記事ID",
        example=1,
    )
    title = fields.String(
        title="title",
        description="記事タイトル",
        example="flask-restxの使い方",
        required=True,
    )
    body = fields.String(
        title="body",
        description="記事本文",
        example="hogehoge",
    )
    created_at = fields.DateTime(
        title="createdAt",
        description="作成日",
    )
    created_by = fields.String(
        title="createdBy",
        description="作成者",
        example="山田 太郎",
    )
    updated_at = fields.DateTime(
        title="updatedAt",
        description="更新日",
    )
    updated_by = fields.String(
        title="updatedBy",
        description="更新者",
        example="山田 太郎",
    )

    def article_post_request_model(self):
        return self.api.model(
            "Article post request model",
            model={
                "title": self.title,
                "body": self.body,
            },
        )

    def article_put_request_model(self):
        return self.api.model(
            "Article put request model",
            model={
                "title": self.title,
                "body": self.body,
            },
        )

    def article_get_response_model(self):
        return self.api.model(
            "Article get response model",
            model={
                "ariticleId": self.article_id,
                "title": self.title,
                "body": self.body,
                "createdAt": self.created_at,
                "createdBy": self.created_by,
                "updatedAt": self.updated_at,
                "updatedBy": self.updated_by,
            },
        )
