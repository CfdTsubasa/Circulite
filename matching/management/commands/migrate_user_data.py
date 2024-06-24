from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from matching.models import CustomUser, UserInterest

class Command(BaseCommand):
    help = 'Migrate User data to CustomUser and update relations'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # カスタムユーザーモデルを取得
        for user in User.objects.all():
            try:
                custom_user = CustomUser.objects.get(id=user.id)
                UserInterest.objects.filter(user=user).update(user=custom_user)
                self.stdout.write(self.style.SUCCESS(f'Successfully updated UserInterest for user {user.username}'))
            except CustomUser.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'CustomUser not found for user {user.username}'))
