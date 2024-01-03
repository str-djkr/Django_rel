from django.test import TestCase
from django.utils.text import slugify
from .models import Category, Post, Comment, Tag
from django.contrib.auth.models import User
from django.utils import timezone


class CategoryModelTest(TestCase):
    def test_category_slug(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.slug, slugify(category.name))


class PostModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(title='Test Post', content='Content for the test post', category=self.category)

    def test_post_str(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_has_category(self):
        self.assertEqual(self.post.category, self.category)


class CommentModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(title='Test Post', content='Content for the test post', category=self.category)
        self.user = User.objects.create(username='testuser')

        self.comment_author = self.user
        self.comment_text = 'Test comment text'
        self.comment = Comment.objects.create(post=self.post, author=self.comment_author, text=self.comment_text)

