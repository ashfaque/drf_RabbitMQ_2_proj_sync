from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import drf_RabbitMQ_2_proj_sync.base_functions as base_f
from django.utils import timezone


class UserDetail(AbstractUser):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    USER_TYPE_CHOICE = (
        ('admin', 'admin'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICE, max_length=20, default='student')
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=70,) # unique=True
    # user_code = models.CharField(default=return_timestamped_user_code, max_length=255, blank=True, null=True, unique=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    password_to_know = models.CharField(max_length=200, blank=True, null=True)
    profile_img = models.FileField(upload_to=base_f.get_directory_path, blank=True, null=True)
    class_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='u_class_teacher')
    session = models.CharField(max_length=20, blank=True, null=True)
    semester = models.CharField(max_length=20, blank=True, null=True)
    stream = models.CharField(max_length=20, blank=True, null=True)
    course = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    registered_on = models.DateTimeField(default=timezone.now)
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='u_registered_by')
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='u_updated_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='u_deleted_by')

    def __str__(self):    # ? Shows the details of specific fields if a user prints the 'instance' of this model.
        # return str(self.id)
        # return f"{self.first_name} - {self.last_name}"
        return str(self.first_name + ' ' + self.last_name)

    class Meta:
        db_table = 'user_detail'


class ConflictingUserSyncLog(models.Model):
    raw_message_body_json = models.TextField(null=True, editable=False)    # * Non-Editable in django forms or django admin.
    comment = models.TextField(blank=True, null=True, editable=False)
    exchange_name = models.TextField(null=True, editable=False)
    message_id = models.TextField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)

    def __str__(self):
        # return f"Log - ID: {self.id}"
        return str(self.id)

    class Meta:
        db_table = 'conflicting_user_sync_log'

