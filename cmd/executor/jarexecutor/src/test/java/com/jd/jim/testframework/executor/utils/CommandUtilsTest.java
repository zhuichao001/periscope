package com.jd.jim.testframework.executor.utils;

import com.jd.jim.testframework.executor.domain.CommandInfo;
import com.jd.jim.testframework.executor.enums.CommandEnum;
import org.junit.Assert;
import org.junit.Test;

import java.util.List;

public class CommandUtilsTest {

    @Test
    public void testParse() {
        String msg = "eval       \"return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}\" 2     key1     key2   first second";
        List<CommandInfo> commandInfoList = CommandUtils.parseCommands(msg);

        CommandInfo commandInfo = commandInfoList.get(0);

        Assert.assertEquals(commandInfo.getCommandEnum(), CommandEnum.EVAL);
        List<String> elements = commandInfo.getDetailList();
        Assert.assertEquals(6, elements.size());
        Assert.assertEquals("2", elements.get(1));
    }
}
