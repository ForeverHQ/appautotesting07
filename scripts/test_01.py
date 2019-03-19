import allure


class Test01():
    # 设置测试步骤
    @allure.step("正在执行登录用例")
    def test001(self):
        # 设置测试描述
        allure.attach("输入用户名", "")
        allure.attach("输入密码", "")
        allure.attach("点击登录", "")
        print("test001被执行")

    # 设置测试步骤
    @allure.step("正在注册用例")
    def test002(self):
        # 设置测试描述
        allure.attach("输入用户名", "")
        allure.attach("输入密码", "")
        allure.attach("输入验证码", "")
        allure.attach("点击登录", "")
        print("test002被执行")


    @allure.step("失败截图")
    # 设置测试等级
    @allure.severity("critical")
    # 断言失败截图到报告
    def test003(self):
        with open("./img/fail.png", "rb") as f:
            allure.attach("失败原因:", f.read(), allure.attach_type.PNG)
            print("test003被执行")
            assert 0

    @allure.severity("blocker")
    @allure.step("级别被执行")
    def test004(self):
        print("test004被执行")
