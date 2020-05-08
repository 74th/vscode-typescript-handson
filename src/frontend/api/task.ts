import { ITask } from "../../model/task/task";

/**
 * フロントエンドにおいて、APIへのアクセスを担うモジュール
 */

export async function loadTasks(): Promise<ITask[]> {
    const url = "/api/tasks";
    const res = await fetch(url, { method: "GET" });
    return await res.json();
}

export async function postTask(task: ITask): Promise<ITask[]> {
    const url = "/api/tasks";
    const res = await fetch(url, {
        method: "POST",
        body: JSON.stringify(task),
        headers: {
            "Content-Type": "application/json",
        },
    });
    return await res.json();
}

/**
 * タスクの完了をリクエストする
 */
export async function postTaskDone(task: ITask): Promise<void> {
    // TODO: urlを作成する /api/tasks/<id>/done
    const url = "/api/TODO:";
    await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
    });
}
