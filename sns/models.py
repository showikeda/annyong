from django.db import models

# models.CharField – 文字数が制限されたテキストを定義するフィールド
# models.TextField – これは制限無しの長いテキスト用です。
# models.DateTimeField – 日付と時間のフィールド
# models.ForeignKey – これは他のモデルへのリンク
# author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# title = models.CharField(max_length=200)
# text = models.TextField()
# created_date = models.DateTimeField(default=timezone.now)
# published_date = models.DateTimeField(blank=True, null=True)

class Article(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, null = True)

# __str__()を呼ぶと、Articleのcontentのテキスト（string）が返ってきます。
    def __str__(self):
        return self.content
