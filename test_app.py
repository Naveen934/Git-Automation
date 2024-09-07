import streamlit as st
import pytest
from streamlit.testing import TestClient
from app import home

def test_home():
    client = TestClient(home)
    response = client.get("/")
    
    assert response.status_code == 200
    assert b"Hello World!" in response.content