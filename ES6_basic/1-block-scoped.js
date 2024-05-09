export default function taskBlock(trueOrFalse) {
  var newtask = false;
  var newtask2 = true;

  if (trueOrFalse) {
    var task = true;
    var task2 = false;
  }

  return [task || newtask || false, task2 || newtask2 || true];
}
