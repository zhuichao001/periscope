package com.jd.jim.testframework.executor.utils;

import com.google.common.base.CharMatcher;
import com.google.common.base.Splitter;
import com.google.common.collect.Lists;
import com.jd.jim.testframework.executor.domain.CommandInfo;
import com.jd.jim.testframework.executor.enums.CommandEnum;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 19:07
 * Email: wangjinshuai@jd.com
 */
@Slf4j
public class CommandUtils {

    private static final Splitter commandSplitter = Splitter.onPattern("\\s+(?=([^\\\"]|\\\"[^\\\"]*\\\")*$)")
            .omitEmptyStrings()
            .trimResults(CharMatcher.anyOf("\"'"));

    private static CommandInfo parseCommand(String command) {
        if (StringUtils.isBlank(command)) {
            return null;
        }

        // 使用空白字符分割字符串，得到参数，双引号内的字符串不分割
        List<String> elements = commandSplitter.splitToList(command);

        // :: 开头的字符串命令为探针命令
        boolean isProbe = elements.get(0).startsWith("::");

        String commandStr = isProbe ? elements.get(0).substring(2) : elements.get(0);
        CommandEnum commandEnum = CommandEnum.getCommandEnumByType(commandStr);
        if (CommandEnum.UNKNOWN.equals(commandEnum)) {
            log.error("CommandUtils unSupport command:{}", commandStr);
            return null;
        }

        CommandInfo commandInfo = new CommandInfo();
        commandInfo.setCommand(command);
        commandInfo.setCommandEnum(commandEnum);
        commandInfo.setDetailList(elements.subList(1, elements.size()));
        commandInfo.setProbe(isProbe);

        return commandInfo;
    }

    public static List<CommandInfo> parseCommands(String commands) {
        if (StringUtils.isEmpty(commands)) {
            return Lists.newArrayList();
        }

        String[] commandArray = commands.split("\n");

        return Arrays.stream(commandArray)
                .map(CommandUtils::parseCommand)
                .filter(commandInfo -> commandInfo != null)
                .collect(Collectors.toList());
    }
}
