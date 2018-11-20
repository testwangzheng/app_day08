import allure, pytest

class Test_001:
    @allure.step(title="这是一个练习例子")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001_1(self):
        # allure.attach("登录用户名","用户名是lili")
        # allure.attach("登录密码","密码是123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_001_6(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_001_2(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_001_3(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_001_4(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_001_5(self):
        assert True