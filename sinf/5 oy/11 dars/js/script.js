var tasks = [];


function addTask(task) {
  tasks.push(task);
  localStorage.setItem('tasks', JSON.stringify(tasks));
}
var task1 = { id: 1, title: 'Задача 1', description: 'Описание задачи 1' };
var task2 = { id: 2, title: 'Задача 2', description: 'Описание задачи 2' };

addTask(task1);
addTask(task2);


var storedTasks = JSON.parse(localStorage.getItem('tasks'));

console.log(storedTasks);
