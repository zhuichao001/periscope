package com.jd.jim.testframework.executor.redis;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface BitRedisService {

    /**
     * setbit
     * @param key
     * @param offset
     * @param value
     * @return
     */
    String setbit(String key, long offset, boolean value);

    /**
     * getbit
     * @param key
     * @param offset
     * @return
     */
    String getbit(String key, long offset);

    /**
     * bitcount
     * @param key
     * @return
     */
    String bitcount(String key);

    /**
     * bitcount
     * @param key
     * @param start
     * @param end
     * @return
     */
    String bitcount(String key, long start, long end);

    /**
     * bitpos
     * @param key
     * @return
     */
    String bitpos(String key, boolean bit);

    /**
     * bitop
     * @param commandList
     * @return
     */
    String bitop(List<String> commandList);

    /**
     * bitop
     * @param commandList
     * @return
     */
    String bitfield(List<String> commandList);
}
