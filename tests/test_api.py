#!/usr/bin/env python3
"""
API Test Script for SmartEDU
Tests all main endpoints to ensure the application is working correctly
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_endpoints():
    print("=" * 60)
    print("SmartEDU API Test Suite")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Get Lessons
    print("\n[TEST 1] GET /api/lessons")
    try:
        response = requests.get(f"{BASE_URL}/api/lessons")
        if response.status_code == 200:
            data = response.json()
            count = data.get("count", 0)
            print(f"✅ PASSED - Found {count} lessons")
            tests_passed += 1
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - {str(e)}")
        tests_failed += 1
    
    # Test 2: Chatbot Recommendation
    print("\n[TEST 2] POST /api/chatbot (Book Recommendation)")
    try:
        response = requests.post(
            f"{BASE_URL}/api/chatbot",
            json={"age": 12, "interest": "Fantasy"}
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print(f"✅ PASSED - Recommendation received")
                print(f"   Response: {data.get('reply', '')[:100]}...")
                tests_passed += 1
            else:
                print(f"❌ FAILED - {data.get('error')}")
                tests_failed += 1
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - {str(e)}")
        tests_failed += 1
    
    # Test 3: Worksheet Generation
    print("\n[TEST 3] POST /api/generate-worksheet")
    try:
        response = requests.post(
            f"{BASE_URL}/api/generate-worksheet",
            json={
                "subject": "Science",
                "difficulty": "Beginner",
                "numQuestions": 5,
                "questionType": "Multiple Choice",
                "topic": "Photosynthesis"
            }
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print(f"✅ PASSED - Worksheet generated")
                print(f"   Subject: {data.get('subject')}")
                print(f"   Difficulty: {data.get('difficulty')}")
                tests_passed += 1
            else:
                print(f"❌ FAILED - {data.get('error')}")
                tests_failed += 1
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - {str(e)}")
        tests_failed += 1
    
    # Test 4: Content Analyzer
    print("\n[TEST 4] POST /api/analyze-content")
    try:
        response = requests.post(
            f"{BASE_URL}/api/analyze-content",
            json={
                "content": "Photosynthesis is a process by which plants convert light energy into chemical energy. The process involves the absorption of carbon dioxide and water, and the release of oxygen.",
                "analysisType": "summary",
                "detailLevel": "Detailed"
            }
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print(f"✅ PASSED - Content analyzed")
                print(f"   Analysis Type: {data.get('analysisType')}")
                print(f"   Analysis: {data.get('analysis', '')[:100]}...")
                tests_passed += 1
            else:
                print(f"❌ FAILED - {data.get('error')}")
                tests_failed += 1
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - {str(e)}")
        tests_failed += 1
    
    # Test 5: Get Specific Lesson
    print("\n[TEST 5] GET /api/lessons/1")
    try:
        response = requests.get(f"{BASE_URL}/api/lessons/1")
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                lesson = data.get("data", {})
                print(f"✅ PASSED - Lesson retrieved")
                print(f"   Title: {lesson.get('title')}")
                print(f"   Subject: {lesson.get('subject')}")
                tests_passed += 1
            else:
                print(f"❌ FAILED - {data.get('error')}")
                tests_failed += 1
        else:
            print(f"❌ FAILED - Status code: {response.status_code}")
            tests_failed += 1
    except Exception as e:
        print(f"❌ FAILED - {str(e)}")
        tests_failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {tests_passed}")
    print(f"❌ Failed: {tests_failed}")
    print(f"Total: {tests_passed + tests_failed}")
    
    if tests_failed == 0:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {tests_failed} test(s) failed")
    
    print("=" * 60)

if __name__ == "__main__":
    # Wait a bit for the server to fully start
    print("Waiting for server to be ready...")
    time.sleep(2)
    test_endpoints()
