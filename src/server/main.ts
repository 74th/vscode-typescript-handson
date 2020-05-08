import * as api from "./api";
import * as process from "process"

var port = "8080";
if (process.env.PORT) {
    port = process.env.PORT
}

const conf: api.IConfig = {
    WebRoot: "./public/html",
    ListenHost: port,
};

const server = new api.API(conf);
server.Run();
