package com.jd.jim.testframework.executor.autoconfig;

import com.jd.jim.testframework.executor.send.GrpcResultSender;
import com.jd.jim.testframework.executor.send.ResultSender;
import com.jd.jim.testframework.executor.send.UdpResultSender;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

@Slf4j
@Configuration
public class ResultSenderConfig {
    private static final String UDP = "udp";
    private static final String GRPC = "grpc";

    @Autowired
    Environment environment;

    public ResultSender getResultSenderByConfig() {
        String senderType = environment.getProperty("sender.type");
        String senderHost = environment.getProperty("sender.host");
        int senderPort = Integer.valueOf(environment.getProperty("sender.port"));

        ResultSender resultSender;

        if (UDP.equalsIgnoreCase(senderType)) {
            resultSender = new UdpResultSender(senderHost, senderPort);
        } else if (GRPC.equalsIgnoreCase(senderType)) {
            resultSender = new GrpcResultSender(senderHost, senderPort);
        } else {
            throw new IllegalArgumentException("recever.Type配置不正确");
        }

        return resultSender;
    }

}
