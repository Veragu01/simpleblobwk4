from django.urls import path
from blog.views import home, categories, posts, category_detail, post_detail, category_create, category_update, \
    category_delete, post_create, PostList, PostList_GenericView, PostDetail_Generic, PostCreateView, PostUpdateView, \
    PostDeleteView

urlpatterns = [
    path("", home, name="home"),

    path("categories/", categories, name="categories"),

    path("posts/", posts, name="posts"),

    path("category/<int:category_id>/", category_detail, name="category_detail"),

    path("post/<int:post_id>/", post_detail, name="post_detail"),

    path("category/create/", category_create, name="category_create"),

    path("category/update/<int:category_id>/", category_update, name="category_update"),

    path("category/delete/", category_delete, name="category_delete"),

    path("post/create/", post_create, name="post_create"),

    path("posts_template_view/", PostList.as_view(), name="posts_template_view"),

    path("posts_list_view/", PostList_GenericView.as_view(), name="posts_list_view"),

    path("post_detail_view/<int:pk>/", PostDetail_Generic.as_view(), name="post_detail_view"),

    path("post_create/", PostCreateView.as_view(), name="post_create_view"),

    path("post_update_view/<int:pk>/", PostUpdateView.as_view(), name="post_update_view"),

    path("post_delete_view/<int:pk>/", PostDeleteView.as_view(), name="post_delete_view"),
]