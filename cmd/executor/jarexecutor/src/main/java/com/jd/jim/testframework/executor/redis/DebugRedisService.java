package com.jd.jim.testframework.executor.redis;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface DebugRedisService {

    /**
     * ping
     * @return
     */
    String ping();

    /**
     * ping
     * @param message
     * @return
     */
    String ping(String message);

    /**
     * echo
     * @param str
     * @return
     */
    String echo(String str);

    /**
     * object
     * @param subCommand
     * @param key
     * @return
     */
    String object(String subCommand, String key);
}
