package com.jd.jim.testframework.executor.constant;

import com.google.common.base.Joiner;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 10:06
 * Email: wangjinshuai@jd.com
 */
public class CommonConstant {

    /**
     * ok
     */
    public static final String OK ="ok";

    /**
     * true
     */
    public static final String TRUE = "true";

    /**
     * true
     */
    public static final String FALSE = "false";

    /**
     * 0
     */
    public static final String ZERO = "0";

    /**
     * string list joiner
     */
    public static final Joiner.MapJoiner MAP_JOINER = Joiner.on(",")
            .useForNull("null").withKeyValueSeparator(":");

    /**
     * 空
     */
    public static final String EMPTY = "";

    /**
     * 异常信息
     */
    public static final String INVALID_PARAM = "invalid param";

    /**
     * 不支持命令提示信息
     */
    public static final String UN_SUPPORT_PREFIX = "un support command:%s";

    /**
     * scan MATCH
     */
    public static final String MATCH = "MATCH";

    /**
     * scan COUNT
     */
    public static final String COUNT = "COUNT";
}
