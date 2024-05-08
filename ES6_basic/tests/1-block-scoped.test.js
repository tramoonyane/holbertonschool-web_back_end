// Import the function to be tested
import taskBlock from '../1-block-scoped';

// Test suite for taskBlock function
describe('taskBlock function', () => {
  // Test when trueOrFalse is true
  test('returns correct values when trueOrFalse is true', () => {
    const result = taskBlock(true);
    expect(result).toEqual([true, false]); // Task should be true, Task2 should be false
  });

  // Test when trueOrFalse is false
  test('returns correct values when trueOrFalse is false', () => {
    const result = taskBlock(false);
    expect(result).toEqual([false, true]); // Task should be false, Task2 should be true
  });
});
