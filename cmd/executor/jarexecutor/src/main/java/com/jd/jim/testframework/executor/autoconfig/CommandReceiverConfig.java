package com.jd.jim.testframework.executor.autoconfig;

import com.jd.jim.testframework.executor.receive.CommandReceiver;
import com.jd.jim.testframework.executor.receive.GrpcCommandReceiver;
import com.jd.jim.testframework.executor.receive.UdpCommandReceiver;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

@Slf4j
@Configuration
public class CommandReceiverConfig {
    private static final String UDP = "udp";
    private static final String GRPC = "grpc";

    @Autowired
    Environment environment;

    public CommandReceiver getCommandReceiverByConfig() {
        String receiverType = environment.getProperty("receiver.type");
        String receiverHost = environment.getProperty("receiver.host");
        int receiverPort = Integer.valueOf(environment.getProperty("receiver.port"));

        CommandReceiver commandReceiver;

        if (UDP.equalsIgnoreCase(receiverType)) {
            commandReceiver = new UdpCommandReceiver(receiverHost, receiverPort);
        } else if (GRPC.equalsIgnoreCase(receiverType)) {
            commandReceiver = new GrpcCommandReceiver(receiverHost, receiverPort);
        } else {
            throw new IllegalArgumentException("recever.Type配置不正确");
        }

        return commandReceiver;
    }

}
