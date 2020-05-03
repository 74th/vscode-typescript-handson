import { Component, Vue } from "vue-property-decorator";
import { ITask } from "../../model/task/morimoto_task";
import { loadTasks, postTaskDone } from "../api/morimoto_task";

/**
 * タスクの一覧と、個々のタスク
 */
@Component
export class TaskListView extends Vue {

    private tasks: ITask[] = [];

    public async loadTasks(): Promise<void> {
        const tasks = await loadTasks();
        this.tasks = tasks;
    }

    public async clickDone(task: ITask): Promise<void> {
        // TODO: Doneをクリックした時に、

        await postTaskDone(task);
        //
        await this.loadTasks();
    }
}
