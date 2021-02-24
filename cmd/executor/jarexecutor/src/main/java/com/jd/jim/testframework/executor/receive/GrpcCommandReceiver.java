package com.jd.jim.testframework.executor.receive;

import com.jd.jim.testframework.executor.grpc.ExecutorGrpcServer;

import java.io.IOException;

public class GrpcCommandReceiver implements CommandReceiver {

    ExecutorGrpcServer executorGrpcServer;

    public GrpcCommandReceiver(String receiverHost, int receiverPort) {
        executorGrpcServer = new ExecutorGrpcServer(receiverPort);
    }

    @Override
    public void start() throws IOException {
        executorGrpcServer.start();
    }

    @Override
    public void stop() {
        executorGrpcServer.shutdown();
    }

}
