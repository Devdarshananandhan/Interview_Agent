#!/usr/bin/env python
"""Simple test script for the audio transcription API"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health check endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")
    return response.status_code == 200

def test_api_info():
    """Test API info endpoint"""
    print("Testing API info endpoint...")
    response = requests.get(f"{BASE_URL}/api")
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Endpoints available: {list(data.get('endpoints', {}).keys())}\n")
    return response.status_code == 200

def test_transcribe_endpoint():
    """Test transcribe endpoint exists"""
    print("Testing API info for transcribe endpoint...")
    response = requests.get(f"{BASE_URL}/api")
    if response.status_code == 200:
        endpoints = response.json().get("endpoints", {})
        if "/api/transcribe" in endpoints:
            print(f"✓ Transcribe endpoint available: {endpoints['/api/transcribe']}")
            return True
        else:
            print("✗ Transcribe endpoint not found in API info")
            print(f"Available endpoints: {list(endpoints.keys())}")
            return False
    return False

if __name__ == "__main__":
    print("=" * 60)
    print("Communication Skills Scoring API - Test Suite")
    print("=" * 60 + "\n")
    
    try:
        test_health()
        test_api_info()
        test_transcribe_endpoint()
        print("\n" + "=" * 60)
        print("✓ Basic API tests passed!")
        print("=" * 60)
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        print("Make sure the backend is running on http://localhost:5000")
