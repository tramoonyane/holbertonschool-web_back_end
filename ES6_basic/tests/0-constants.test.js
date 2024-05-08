//Import the functions to be tested from 0-constants.js
import { taskFirst, getLast, taskNext } from '../0-constants';

// Test for taskFirst function
test('taskFirst function returns correct string', () => {
  const result = taskFirst();
  expect(result).toBe('I prefer const when I can.');
});

// Test for getLast function
test('getLast function returns correct string', () => {
  const result = getLast();
  expect(result).toBe(' is okay');
});

// Test for taskNext function
test('taskNext function returns correct combination', () => {
  const result = taskNext();
  expect(result).toBe('But sometimes let is okay');
});
