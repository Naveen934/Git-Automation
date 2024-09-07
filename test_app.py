import streamlit as st
import pytest
from streamlit.testing.v1 import AppTest
from app import home

def test_home():
    at = AppTest.from_function(home)
    at.run()
    
    # Check if the title is present
    assert at.title[0].value == "Hello World!"