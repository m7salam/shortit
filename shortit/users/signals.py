from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver





User = get_user_model()


@receiver(post_migrate)
def populate_models(sender, *args, **kwargs):
    # create super user for dev purposes
    try:
        User.objects.create_user(username="admin", email="mo@tier.app",
                                             password='Global1234', is_active=True, is_superuser=True, is_staff=True)
    except:
        pass