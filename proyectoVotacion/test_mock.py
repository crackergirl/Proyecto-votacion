from unittest import TestCase, mock


class TestApp(TestCase):
    """Clase para realizar los test unitarios."""

    @mock.patch('back.Database')
    def TestGetVotesCats(self, MockDatabase):
        """Comprobación de la obtención del número de votos."""
        db = MockDatabase()
        db.getVotes.return_value = 2
        self.assertEqual(2, db.getVotes('votation', 'cats'))

    @mock.patch('back.Database')
    def TestGetVotesDogs(self, MockDatabase):
        """Comprobación de la obtención del número de votos."""
        db = MockDatabase()
        db.getVotes.return_value = 3
        self.assertEqual(3, db.getVotes('votation', 'dogs'))

    @mock.patch('back.Database')
    def testCheckVotingExistsTrue(self, MockDatabase):
        """Comprobación de la existencia de una votación."""
        db = MockDatabase()
        db.checkVotingExists.return_value = True
        self.assertTrue(db.checkVotingExists('votation'))

    @mock.patch('back.Database')
    def testCheckVotingExistsFalse(self, MockDatabase):
        """Comprobación de la no existencia de una votación."""
        db = MockDatabase()
        db.checkVotingExists.return_value = False
        self.assertFalse(db.checkVotingExists('series'))

    @mock.patch('back.Database')
    def testCheckCategoryCatExists(self, MockDatabase):
        """Comprobación de la existencia de una categoría."""
        db = MockDatabase()
        db.checkCategoryExists.return_value = True
        self.assertTrue(db.checkCategoryExists('votation', 'cat'))

    @mock.patch('back.Database')
    def testCheckCategoryDogExists(self, MockDatabase):
        """Comprobación de la existencia de una categoría."""
        db = MockDatabase()
        db.checkCategoryExists.return_value = True
        self.assertTrue(db.checkCategoryExists('votation', 'dog'))

    @mock.patch('back.Database')
    def testCheckCategoryExists(self, MockDatabase):
        """Comprobación de la no existencia de una votación."""
        db = MockDatabase()
        db.checkCategoryExists.return_value = False
        self.assertFalse(db.checkCategoryExists('votation', 'wolf'))
