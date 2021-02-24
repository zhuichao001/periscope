package com.jd.jim.testframework.executor.grpc.executor;

import io.grpc.stub.StreamObserver;

public class Executor extends com.jd.jim.testframework.executor.grpc.executor.ExecutorGrpc.ExecutorImplBase{

    public void sendToExecutor(com.jd.jim.testframework.executor.grpc.executor.ExecutorGrpcService.SendReq request,
                               StreamObserver<com.jd.jim.testframework.executor.grpc.executor.ExecutorGrpcService.Resp> responseObserver) {
        String commandStr = request.getAllCmds();
        com.jd.jim.testframework.executor.grpc.executor.ExecutorGrpcService.Resp resp = com.jd.jim.testframework.executor.grpc.executor.ExecutorGrpcService.Resp.newBuilder()
                .setMessage("success")
                .build();

        responseObserver.onNext(resp);
        responseObserver.onCompleted();
    }

}
