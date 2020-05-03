import { TaskListView } from "./views/morimoto_taskList";
import { NewTaskView } from "./views/morimoto_newTask";

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
