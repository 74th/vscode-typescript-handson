import { ITask } from "src/model/task/morimoto_task";
import { describe, Suite, it } from "mocha";
import { Repository } from "src/model/task/morimoto_repository";
import * as assert from "assert";

describe("morimoto Task repository", () => {

    it("初期化されたときには、2レコード含まれていること", () => {
        // タスクリポジトリ
        const repo = new Repository();

        // リポジトリからタスクを取得
        const tasks = repo.ListTasks();

        // 初期化された時は2レコード含まれている
        assert.equal(tasks.length, 2);
    });

    it("1タスク追加できること", () => {
        // タスクリポジトリ
        const repo = new Repository();

        // 新しいタスク
        const newTasks: ITask = {
            id: 0,
            text: "new task",
        };
        // 新しいタスクを登録する
        repo.AddTask(newTasks);

        // タスクのリストを取得すると、
        // 追加したタスクが含まれていること
        const tasks = repo.ListTasks();
        assert.equal(tasks.length, 3);
        assert.notEqual(tasks.find((task: ITask): boolean => {
            return task.text === "new task";
        }), undefined);
    });

    it("タスクを完了にでき、完了にしたタスクはリストから見えなくなっていること", () => {
        // タスクリポジトリ
        const repo = new Repository();

        // 完了にするタスクを取得
        let tasks = repo.ListTasks();
        const firstTask = tasks[0];

        // TODO: タスクを完了にする

        // TODO: タスクが完了になって、見えなくなっていること

    });
});
