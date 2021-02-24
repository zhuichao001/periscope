package com.jd.jim.testframework.executor.receive;

import lombok.extern.slf4j.Slf4j;

import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

@Slf4j
public class CommandContainer {
    private static final CommandContainer instance = new CommandContainer();

    private Queue<String> commandQueue = new ConcurrentLinkedQueue();

    public static CommandContainer getSingleton() {
        return instance;
    }

    public void putCommand(String command) {
        log.info("Receive Command: {}", command);
        commandQueue.add(command);
    }

    public String getCommand() {
        Object obj = commandQueue.poll();
        return obj == null ? null : obj.toString();
    }
}
