import unittest
import statistics

class TestSkilz(unittest.TestCase):
    def test_agg(self):
        #
        # Find the minimum salary, store in
        # ``min_sal``
        #
        # ===========================================
        salaries = [81_840, 3_000_000, 1, 2_000_000, 700_000]

        min_sal = min(salaries)

        self.assertEqual(min_sal, 1)

        
        #
        # Create a variable, ``most_name``, that
        # has the person with the
        # biggest salary
        #
        # ===========================================
        people = [{'name': 'Bezos', 'salary': 3000000},
         {'name': 'Cook', 'salary': 2000000},
         {'name': 'Zuck', 'salary': 700000},
         {'name': 'Pichai', 'salary': 81840},
         {'name': 'Hastings', 'salary': 1}]

        most_name = max(people, key=lambda person: person['salary'])

        
        self.assertEqual(most_name, {'name': 'Bezos', 'salary': 3000000} )

        #
        # Calculate the mean value of the salary and
        # store in ``mean_sal``.
        #
        # ===========================================

        #mean_sal = statistics.mean(salaries)

        mean_sal = statistics.mean(person['salary'] for person in people)
        self.assertEqual(mean_sal, 1156368.2)

if __name__ == '__main__':
    unittest.main()
