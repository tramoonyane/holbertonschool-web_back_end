export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    task = true; // Modification of existing variable, not redeclaration
    task2 = false; // Modification of existing variable, not redeclaration
  }

  return [task, task2];
}
