package com.jd.jim.testframework.executor.execute;

import com.jd.jim.testframework.executor.domain.CommandInfo;
import com.jd.jim.testframework.executor.domain.HandleResult;
import com.jd.jim.testframework.executor.receive.CommandContainer;
import com.jd.jim.testframework.executor.send.ResultSender;
import com.jd.jim.testframework.executor.utils.CommandUtils;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.lang3.StringUtils;

import java.util.List;

@Slf4j
@Data
public class CommandProcessor {
    private CommandExecutor sourceExecutor;
    private CommandExecutor destExecutor;
    private ResultSender resultSender;

    public void start() {
        while (true) {
            List<CommandInfo> commandInfoList = parseReceivedCommands();
            if (CollectionUtils.isNotEmpty(commandInfoList)) {
                processCommands(commandInfoList);
            }
        }
    }

    private List<CommandInfo> parseReceivedCommands() {
        String data = CommandContainer.getSingleton().getCommand();
        return CommandUtils.parseCommands(data);
    }

    private void processCommands(List<CommandInfo> commandInfoList) {
        // TODO 考虑用并行
        commandInfoList.forEach(commandInfo -> {
            HandleResult handleResult = new HandleResult();

            try {
                handleResult.setSource(getSourceExecutor().executeCommand(commandInfo));
            } catch (Exception e) {
                log.error("Executor source occur error, command:{}", commandInfo.getCommand(), e);
                handleResult.setSource(e.getMessage());
            }

            try {
                handleResult.setDest(getDestExecutor().executeCommand(commandInfo));
            } catch (Exception e) {
                log.error("Executor dest occur error, command:{}", commandInfo.getCommand(), e);
                handleResult.setDest(e.getMessage());
            }

            String result = buildResultString(commandInfo.getCommand(), handleResult);
            if (StringUtils.isNotBlank(result)) {
                log.info("Send Result: {}", result);
                resultSender.sendResult(result);
            }
        });
    }

    private String buildResultString(String command, HandleResult handleResult) {
        if (null == handleResult || StringUtils.isEmpty(command)) {
            return "";
        }

        StringBuilder temp = new StringBuilder();

        temp.append(command).append("|");
        temp.append(handleResult.getSource()).append("|");
        temp.append(handleResult.getDest());

        return temp.toString();
    }

}