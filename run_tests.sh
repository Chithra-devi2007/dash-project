#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 Starting Continuous Integration Test Runner"
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "❌ Error: Virtual environment not found!"
    exit 1
fi
pytest
TEST_EXIT_CODE=$?
deactivate
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "✅ SUCCESS!"
    exit 0
else
    echo "❌ FAILURE!"
    exit 1
fi
