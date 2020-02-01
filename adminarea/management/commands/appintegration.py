from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Manage Object'

    def add_arguments(self, parser):
        parser.add_argument('--list', help="Display all Objects")

        subparsers = parser.add_subparsers(title="actions")

        parser_create = subparsers.add_parser("create", parents=[parser],
                                              add_help=False,
                                              description="The create parser",
                                              help="Create a Object")
        parser_create.add_argument("--name", help="Object Name Field")

        parser_update = subparsers.add_parser("update", parents=[parser],
                                              add_help=False,
                                              description="The update parser",
                                              help="Update a Object")

        parser_delete = subparsers.add_parser("delete", parents=[parser],
                                              add_help=False,
                                              description="The delete parser",
                                              help="Delete a Object")

        parser_delete.add_argument("--id", type=int, help="Object Name Field")




    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write('User "%s (%s)" deleted with success!' % (user.username, user_id))
            except User.DoesNotExist:
                self.stdout.write('User with id "%s" does not exist.' % user_id)
