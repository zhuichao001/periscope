package com.jd.jim.testframework.executor.send;

import com.jd.jim.testframework.executor.grpc.differ.DifferGrpcClient;

public class GrpcResultSender implements ResultSender {
    private DifferGrpcClient differGrpcClient;

    public GrpcResultSender(String grpcHost, int grpcPort) {
        differGrpcClient = new DifferGrpcClient(grpcHost, grpcPort);
    }

    @Override
    public void sendResult(String result) {
        differGrpcClient.sendToDiffer(result);
    }
}
