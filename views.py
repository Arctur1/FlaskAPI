from flask import request, jsonify
from flask.views import MethodView
from flask import Flask
from app import app
from models import Post


class PostView(MethodView):

    def get(self, post_id):
        post = Post.by_id(post_id)
        return jsonify(post.to_dict())

    def post(self):
        post = Post(**request.json)
        post.add()
        return jsonify(post.to_dict())

    def delete(self, post_id):
        post = Post.by_id(post_id)
        post.delete()
        return {'status': 'OK'}



@app.route('/health/', methods=['GET', ])
def health():
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

    return {'status': 'OK'}


app.add_url_rule('/posts/<int:post_id>', view_func=PostView.as_view('posts_get'), methods=['GET', 'DELETE', ])
app.add_url_rule('/posts/', view_func=PostView.as_view('posts_create'), methods=['POST', ])