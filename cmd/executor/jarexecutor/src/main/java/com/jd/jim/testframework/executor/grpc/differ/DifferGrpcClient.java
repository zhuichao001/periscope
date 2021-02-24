package com.jd.jim.testframework.executor.grpc.differ;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

import java.util.concurrent.TimeUnit;

public class DifferGrpcClient {
    private final ManagedChannel channel;
    private final com.jd.jim.testframework.executor.grpc.differ.DifferGrpc.DifferBlockingStub blockingStub;

    /** Construct client connecting to HelloWorld server at {@code host:port}. */
    public DifferGrpcClient(String host, int port) {
        channel = ManagedChannelBuilder.forAddress(host, port)
                .usePlaintext(true)
                .build();
        blockingStub = com.jd.jim.testframework.executor.grpc.differ.DifferGrpc.newBlockingStub(channel);
    }

    public void sendToDiffer(String data) {
        com.jd.jim.testframework.executor.grpc.differ.DifferGrpcService.SendReq request = com.jd.jim.testframework.executor.grpc.differ.DifferGrpcService.SendReq.newBuilder()
                .setData(data)
                .build();

        com.jd.jim.testframework.executor.grpc.differ.DifferGrpcService.Resp response = blockingStub.sendToDiffer(request);
    }

    public void shutdown() throws InterruptedException {
        channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

}
