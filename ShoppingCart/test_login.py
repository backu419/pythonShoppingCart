import pytest
@pytest.mark.parametrize("username,password",[("Admin","HCL123"),("user","HCL123"),("hemanth",456)])
def test_users(username, password):
    assert username
    assert password



