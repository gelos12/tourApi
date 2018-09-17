from django.db import models
from django.contrib.auth import get_user_model

class TouristDestination(models.Model):
    tourist_id = models.IntegerField(unique=True,)
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='TD_like_user_set',
                                           through='TouristLike') # post.like_set 으로 접근 가능
    stars = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='TD_star_user_set',
                                           through='TouristStar') # post.like_set 으로 접근 가능
    @property                        
    def like_count(self):
        return self.like_user_set.count()


class TouristLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    td = models.ForeignKey(TouristDestination, on_delete=models.CASCADE , related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TouristStar(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    td = models.ForeignKey(TouristDestination, on_delete=models.CASCADE , related_name='star_set')
    score = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReView(models.Model):
    tourist = models.ForeignKey(TouristDestination, verbose_name= "관광지",on_delete=models.CASCADE,)
    content = models.TextField()
    photo = models.ImageField(
        verbose_name=('후기사진'),
        upload_to="review/%Y/%m/%d",
        blank=True,
        null=True,
    )
    like_user_set = models.ManyToManyField(get_user_model(),
                                           blank=True,
                                           related_name='RV_like_user_set',
                                           through='ReViewLike') # post.like_set 으로 접근 가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property                        
    def like_count(self):
        return self.like_user_set.count()

class ReViewLike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    td = models.ForeignKey(ReView, on_delete=models.CASCADE , related_name='like_set')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

