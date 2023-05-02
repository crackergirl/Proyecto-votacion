from unittest import TestCase
from back import Database

configuracion = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'port': 3306,
    'db': 'voting_data'
}


class TestApp(TestCase):
    """Clase para realizar los test unitarios."""

    def testGetVotesCats(self):
        """Comprobación de la obtención del número de votos."""
        db = Database(configuracion)
        result = db.getVotes('votation', 'cat')
        self.assertEqual(result, 2)

    def testGetVotesDogs(self):
        """Comprobación de la obtención del número de votos."""
        db = Database(configuracion)
        result = db.getVotes('votation', 'dog')
        self.assertEqual(result, 3)

    def testCheckVotingExistsTrue(self):
        """Comprobación de la existencia de una votación."""
        db = Database(configuracion)
        self.assertTrue(db.checkVotingExists('votation'))

    def testCheckVotingExistsFalse(self):
        """Comprobación de la no existencia de una votación."""
        db = Database(configuracion)
        self.assertFalse(db.checkVotingExists('series'))

    def testCheckCategoryCatExists(self):
        """Comprobación de la existencia de una categoría."""
        db = Database(configuracion)
        self.assertTrue(db.checkCategoryExists('votation', 'cat'))

    def testCheckCategoryDogExists(self):
        """Comprobación de la existencia de una categoría."""
        db = Database(configuracion)
        self.assertTrue(db.checkCategoryExists('votation', 'dog'))

    def testCheckCategoryExists(self):
        """Comprobación de la no existencia de una votación."""
        db = Database(configuracion)
        self.assertFalse(db.checkCategoryExists('votation', 'wolf'))
