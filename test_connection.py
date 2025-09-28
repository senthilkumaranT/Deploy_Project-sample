#!/usr/bin/env python3
"""
Simple test script to verify backend connection
"""
import requests
import json

def test_backend():
    base_url = "http://localhost:8004"
    
    print("Testing backend connection...")
    
    # Test health check
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ Health check: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False
    
    # Test LLM endpoint
    try:
        test_data = {"question": "Hello, are you working?"}
        response = requests.post(
            f"{base_url}/llm",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data)
        )
        print(f"✅ LLM endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"   Response: {result.get('answer', 'No answer')[:100]}...")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ LLM endpoint failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = test_backend()
    if success:
        print("\n🎉 Backend is working correctly!")
    else:
        print("\n💥 Backend has issues. Please check the server.")
