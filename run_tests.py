#!/usr/bin/env python3
"""
Simple test runner for DeepTutor API tests
"""
import subprocess
import sys
import os

def run_tests():
    """Run all tests"""
    print("🧠 DeepTutor Test Runner")
    print("=" * 50)
    
    # Change to project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    # Install test dependencies
    print("📦 Installing test dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pytest", "fastapi-testclient"], check=True)
    
    # Run backend tests
    print("\n🔧 Running Backend Tests...")
    try:
        result = subprocess.run([sys.executable, "-m", "pytest", "tests/backend/", "-v"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            print("✅ Backend tests passed!")
        else:
            print("❌ Backend tests failed!")
            return result.returncode
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1
    
    print("\n🎉 All tests completed!")
    return 0

if __name__ == "__main__":
    sys.exit(run_tests())
