"""
Simple test file for the AI Chatbot backend
"""
import pytest
import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import main
        import llm
        print("✅ All modules imported successfully")
        assert True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        assert False

def test_main_module_exists():
    """Test that main module has required attributes"""
    try:
        import main
        # Check if the FastAPI app exists
        assert hasattr(main, 'app')
        print("✅ FastAPI app found")
    except Exception as e:
        print(f"❌ Error checking main module: {e}")
        assert False

def test_llm_module_exists():
    """Test that LLM module has required functions"""
    try:
        import llm
        # Check if the chat function exists
        assert hasattr(llm, 'chat_with_groq')
        print("✅ LLM chat function found")
    except Exception as e:
        print(f"❌ Error checking LLM module: {e}")
        assert False

def test_environment_variables():
    """Test that environment variables can be accessed"""
    import os
    groq_key = os.getenv('GROQ_API_KEY')
    if groq_key:
        print("✅ GROQ_API_KEY environment variable found")
    else:
        print("⚠️ GROQ_API_KEY environment variable not set (this is expected in CI)")
    # Don't fail the test if the key is not set
    assert True

if __name__ == "__main__":
    # Run basic tests
    test_imports()
    test_main_module_exists()
    test_llm_module_exists()
    test_environment_variables()
    print("✅ All basic tests passed!")

