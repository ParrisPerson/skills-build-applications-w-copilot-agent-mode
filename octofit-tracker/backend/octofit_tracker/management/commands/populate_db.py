from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='dc')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='dc')

        # Create activities
        Activity.objects.create(user=ironman.name, type='run', duration=30)
        Activity.objects.create(user=captain.name, type='cycle', duration=45)
        Activity.objects.create(user=batman.name, type='swim', duration=25)
        Activity.objects.create(user=superman.name, type='yoga', duration=60)

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=85)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Sprints', description='Run 5 sprints')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
