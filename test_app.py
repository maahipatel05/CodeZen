from app import app

def test_index() : 
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_bug_fixing() : 
    response = app.test_client().get("/bug_fixing")
    assert response.status_code == 200

def test_code_optimization() : 
    response = app.test_client().get("/code_optimization")
    assert response.status_code == 200

def test_methodology() : 
    response = app.test_client().get("/methodology")
    assert response.status_code == 200

def test_contact() : 
    response = app.test_client().get("/contact")
    assert response.status_code == 200

def test_about() : 
    response = app.test_client().get("/about")
    assert response.status_code == 200