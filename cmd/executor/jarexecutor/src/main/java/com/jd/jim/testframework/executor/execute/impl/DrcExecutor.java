package com.jd.jim.testframework.executor.execute.impl;

import com.jd.jim.testframework.executor.domain.CommandInfo;
import com.jd.jim.testframework.executor.exception.DrcInconsistentException;
import com.jd.jim.testframework.executor.execute.CommandExecutor;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;

import java.util.concurrent.TimeUnit;

@Slf4j
@Data
public class DrcExecutor extends AbstractExecutor {
    private CommandExecutor writeExecutor;
    private CommandExecutor readExecutor;

    @Override
    public String executeCommand(CommandInfo commandInfo) throws Exception {
        String wResult = writeExecutor.executeCommand(commandInfo);

        if (commandInfo.getProbe()) {

            delay(500);

            String rResult = readExecutor.executeCommand(commandInfo);
            if (StringUtils.equals(wResult, rResult)) {
                return wResult;
            } else {
                throw new DrcInconsistentException(wResult, rResult);
            }
        }

        return wResult;
    }

    private void delay(long milliseconds) throws InterruptedException {
        TimeUnit.MILLISECONDS.sleep(milliseconds);
    }
}
