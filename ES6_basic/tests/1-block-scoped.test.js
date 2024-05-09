import taskBlock from '../1-block-scoped'; // Assuming the file containing the function is named 1-block-scoped.js

// Test case 1: When trueOrFalse is true, should return [true, false]
test('When trueOrFalse is true, should return [true, false]', () => {
  expect(taskBlock(true)).toEqual([true, false]);
});

// Test case 2: When trueOrFalse is false, should return [false, true]
test('When trueOrFalse is false, should return [false, true]', () => {
  expect(taskBlock(false)).toEqual([false, true]);
});
