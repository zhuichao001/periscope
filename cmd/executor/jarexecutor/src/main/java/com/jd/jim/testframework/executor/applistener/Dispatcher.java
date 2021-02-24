package com.jd.jim.testframework.executor.applistener;

import com.jd.jim.testframework.executor.autoconfig.CommandReceiverConfig;
import com.jd.jim.testframework.executor.autoconfig.ExecutorConfig;
import com.jd.jim.testframework.executor.autoconfig.ResultSenderConfig;
import com.jd.jim.testframework.executor.execute.CommandExecutor;
import com.jd.jim.testframework.executor.execute.CommandProcessor;
import com.jd.jim.testframework.executor.receive.CommandReceiver;
import com.jd.jim.testframework.executor.send.ResultSender;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationListener;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Slf4j
@Component
@Order(0)
public class Dispatcher implements ApplicationListener<ApplicationReadyEvent> {
    @Autowired
    CommandReceiverConfig commandReceiverConfig;
    @Autowired
    ResultSenderConfig resultSenderConfig;
    @Autowired
    ExecutorConfig executorConfig;

    CommandProcessor commandProcessor = new CommandProcessor();

    @Override
    public void onApplicationEvent(ApplicationReadyEvent applicationReadyEvent) {
        try {
            start();
        } catch (Exception e) {
            log.error("启动异常", e);
            System.exit(-1);
        }
    }

    private void start() throws Exception {
        init();
        startCommandReceiver();
        startCommandProcessor();
    }

    private void init() {
        ResultSender resultSender = resultSenderConfig.getResultSenderByConfig();
        commandProcessor.setResultSender(resultSender);

        CommandExecutor sourceExecutor = executorConfig.getExecutorByConfig("source");
        CommandExecutor destExecutor = executorConfig.getExecutorByConfig("dest");

        commandProcessor.setSourceExecutor(sourceExecutor);
        commandProcessor.setDestExecutor(destExecutor);
    }

    private void startCommandReceiver() throws Exception {
        CommandReceiver commandReceiver = commandReceiverConfig.getCommandReceiverByConfig();
        commandReceiver.start();
    }

    private void startCommandProcessor() {
        commandProcessor.start();
    }
}