run_tests:
    echo "Before tests"
    pytest
    echo "After tests"
show_cases:
    pytest=–collect-only