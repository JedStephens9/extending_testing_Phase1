from lib.age_checker import is_old_enough

"""
test no data passed returns False
"""

def test_no_data_passed():
    response = is_old_enough()
    assert response == False
    """
    fails as arguments missing
    """

"""
test person born today returns False
"""
def test_born_today():
    response = is_old_enough(2023,1,5,13)
    assert response == False

"""
test person one day off being 13 returns False
"""
def test_one_day_under():
    response = is_old_enough(2010,1,6,13)
    assert response == False

"""
test person is 13 today returns True
"""
def test_thirteen_today():
    response = is_old_enough(2010,1,5,13)
    assert response == True

"""
test person is one day over 13 returns True
"""
def test_one_day_over():
    response = is_old_enough(2010,1,4,13)
    assert response == True

"""
test person born 100 years ago returns True
"""
def test_born_100_years_ago():
    response = is_old_enough(1913,1,5,13)
    assert response == True

"""
test person born on 29 feb 2008 returns True
"""
def test_29_Feb():
    response = is_old_enough(2008,2,29,13)
    assert response == True

"""
test wrong format date entered returns False
"""
def test_wrong_format():
    response = is_old_enough(2010,Jan,5,13)
    assert response == False
    """
    Fails as can only accept numerical data
    """
