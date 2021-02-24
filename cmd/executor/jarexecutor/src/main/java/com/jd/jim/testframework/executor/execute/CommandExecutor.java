package com.jd.jim.testframework.executor.execute;

import com.jd.jim.testframework.executor.domain.CommandInfo;

public interface CommandExecutor {

    String executeCommand(CommandInfo commandInfo) throws Exception;

}
