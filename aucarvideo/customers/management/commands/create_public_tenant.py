from django.core.management.base import BaseCommand, CommandError
from customers.models import Client
from django.conf import settings


class Command(BaseCommand):
    help = 'Creates the public tenant record for the project'

    def handle(self, **kwargs):
        public_tenant, created = Client.objects.get_or_create(
            # It should be your project domain, maybe you need to add it to
            # settings to handle your different project instances
            domain_url=settings.DOMAIN_NAME,
            schema_name='public',
            # Whatever you want
            name=settings.DOMAIN_NAME,
            # ...Your required fields for your Tenant model
        )
        if created:
            success_message = self.style.SUCCESS(
                f'Successfully created {public_tenant.domain_url} public tenant!'
            )
            self.stdout.write(success_message)
        else:
            raise CommandError('Public tenant is already created')