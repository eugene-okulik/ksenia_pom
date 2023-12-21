import allure


@allure.story('small')
def test_small1(demo):
    print(demo)
    assert 1 == 1
