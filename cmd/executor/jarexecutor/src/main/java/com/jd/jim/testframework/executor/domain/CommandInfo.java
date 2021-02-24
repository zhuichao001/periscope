package com.jd.jim.testframework.executor.domain;

import com.jd.jim.testframework.executor.enums.CommandEnum;
import lombok.Data;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 19:08
 * Email: wangjinshuai@jd.com
 */
@Data
public class CommandInfo {

    /**
     * 指令
     */
    private String command;

    /**
     * 指令枚举
     */
    private CommandEnum commandEnum;

    /**
     * 指令参数
     */
    private List<String> detailList;

    /**
     *
     */
    private Boolean probe;
}
