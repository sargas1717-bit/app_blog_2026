from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostPageTests(TestCase):
	def setUp(self):
		self.post = Post.objects.create(
			title='Publicación de prueba',
			content='Contenido de prueba',
		)

	def test_read_page_links_to_post_detail(self):
		response = self.client.get(reverse('post_list'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, '_base.html')
		self.assertContains(
			response,
			reverse('post_detail', args=[self.post.pk]),
		)

	def test_detail_page_renders_post_with_base_template(self):
		response = self.client.get(
			reverse('post_detail', args=[self.post.pk])
		)

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, '_base.html')
		self.assertContains(response, self.post.title)
