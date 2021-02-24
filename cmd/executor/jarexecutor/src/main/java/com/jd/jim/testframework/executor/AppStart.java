package com.jd.jim.testframework.executor;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = {"com.jd.jim.testframework.executor"})
public class AppStart {

    public static void main(String[] args) {
        SpringApplication.run(AppStart.class, args);

        // 入口在 com.jd.jim.testframework.executor.applistener.Dispatcher
    }

}