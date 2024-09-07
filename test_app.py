from app import home
import streamlit as st

def test_home(monkeypatch):
    # This will store any streamlit commands called
    streamlit_calls = []
    
    # Mock the st.title function
    def mock_title(*args, **kwargs):
        streamlit_calls.append(('title', args, kwargs))
    
    # Replace st.title with our mock function
    monkeypatch.setattr(st, 'title', mock_title)
    
    # Call the home function
    home()
    
    # Check if st.title was called with "Hello World!"
    assert ('title', ('Hello World!',), {}) in streamlit_calls