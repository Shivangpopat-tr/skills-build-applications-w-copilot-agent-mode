from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password456"},
        ]

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]},
        ]

        # Test data for activities
        activities = [
            {"user": "john.doe@example.com", "type": "Running", "duration": 30, "date": "2025-04-15"},
            {"user": "jane.smith@example.com", "type": "Cycling", "duration": 45, "date": "2025-04-15"},
        ]

        # Test data for leaderboard
        leaderboard = [
            {"user": "john.doe@example.com", "score": 100},
            {"user": "jane.smith@example.com", "score": 150},
        ]

        # Test data for workouts
        workouts = [
            {"name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
            {"name": "HIIT", "description": "High-intensity interval training for advanced fitness levels."},
        ]

        # Insert test data into collections
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activity.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))