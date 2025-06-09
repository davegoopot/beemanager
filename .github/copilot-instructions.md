# Coding Approach

1. *Use test-driven development (TDD)*
  a. Write a failing test before writing the code to implement a feature. Only write one test at a time before checking that it fails
  b. Run the test
  c. Write the minimum code necessary to pass the test.
  d. Run the tests again to ensure all tests pass.
  e. Refactor the code if necessary, ensuring that all tests still pass.

2. Prefer using Python at the latest supported version.

3. Use Astral UV tools for managing dependencies and virtual environments. 
  a. For sinlge file scripts use the Astral UV script headers to manage dependencies and python version.

4. Try not to write comments. Instead prefer to write self-documenting code that is clear and easy to understand. If a function is called `test_get_nginx_version_uses_custom_certificate` do not write a comment that says `# Test that get_nginx_version uses custom certificate`. Instead, the function name itself should be clear enough to understand what it does.

  