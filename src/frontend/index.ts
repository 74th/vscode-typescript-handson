import { TaskListView } from "./views/taskList";
import { NewTaskView } from "./views/newTask";

/**
 * フロントエンドのルート
 * Vue.jsのモジュールを初期化する
 */
window.addEventListener("load", () => {

    const taskListView = new TaskListView({
        el: "#taskListView",
    });
    const newTaskView = new NewTaskView({
        el: "#newTaskView",
    });

    newTaskView.$on("updateTaskList", () => {
        taskListView.loadTasks();
    });

    taskListView.loadTasks();
});
