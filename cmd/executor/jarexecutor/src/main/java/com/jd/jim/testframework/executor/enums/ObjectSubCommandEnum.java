package com.jd.jim.testframework.executor.enums;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-24 10:31
 * Email: wangjinshuai@jd.com
 */
public enum ObjectSubCommandEnum {

    REFCOUNT("REFCOUNT"),
    ENCODING("ENCODING"),
    IDLETIME("IDLETIME"),
    ;

    ObjectSubCommandEnum(String subCommand) {
        this.subCommand = subCommand;
    }

    private String subCommand;

    public String getSubCommand() {
        return subCommand;
    }
}
