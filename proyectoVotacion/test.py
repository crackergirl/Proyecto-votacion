from unittest import TestCase
from back import Database

config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'db': 'voting_data',
}

class TestApp(TestCase):
    def testGetVotesCats(self):
        db = Database(config)
        result = db.getVotes('votation', 'cat')
        self.assertEqual(result, 2)

    def testGetVotesDogs(self):
        db = Database(config)
        result = db.getVotes('votation', 'dog')
        self.assertEqual(result, 3)

    def testCheckVotingExists(self):
        db = Database(config)
        self.assertTrue(db.checkVotingExists('votation'))

    def testCheckVotingExists(self):
        db = Database(config)
        self.assertFalse(db.checkVotingExists('series'))

    def testCheckCategoryCatExists(self):
        db = Database(config)
        self.assertTrue(db.checkCategoryExists('votation', 'cat'))

    def testCheckCategoryDogExists(self):
        db = Database(config)
        self.assertTrue(db.checkCategoryExists('votation', 'dog'))

    def testCheckCategoryExists(self):
        db = Database(config)
        self.assertFalse(db.checkCategoryExists('votation', 'wolf'))
    