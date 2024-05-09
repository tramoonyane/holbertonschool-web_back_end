export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Modification of existing variable, not redeclaration
    task = true; // This will cause an error with const, so you may not want to use const here
    task2 = false; // This will cause an error with const, so you may not want to use const here
  }

  return [task, task2];
}
