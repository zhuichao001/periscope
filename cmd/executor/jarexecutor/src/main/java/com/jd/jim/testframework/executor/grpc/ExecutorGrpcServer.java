package com.jd.jim.testframework.executor.grpc;

import com.jd.jim.testframework.executor.grpc.executor.Executor;
import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class ExecutorGrpcServer {

    private Server server;

    /**
     * @param port 服务端占用的端口
     */
    public ExecutorGrpcServer(int port) {
        server = ServerBuilder.forPort(port)
                // 将具体实现的服务添加到gRPC服务中
                .addService(new Executor())
                .build();
    }

    public void start() throws IOException {
        server.start();
    }

    public void shutdown() {
        server.shutdown();
    }
}
