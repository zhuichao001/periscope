package com.jd.jim.testframework.executor.redis;

import java.util.concurrent.TimeUnit;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface ExpireRedisService {

    /**
     * expire
     * @param key
     * @param timeout
     * @param unit
     * @return
     */
    String expire(String key, long timeout, TimeUnit unit);

    /**
     * expireAt
     * @param key
     * @param unixTime
     * @return
     */
    String expireAt(String key, long unixTime);

    /**
     * ttl
     * @param key
     * @return
     */
    String ttl(String key);

    /**
     * persist
     * @param key
     * @return
     */
    String persist(String key);

    /**
     * expire
     * @param key
     * @param milliseconds
     * @return
     */
    String pexpire(String key, long milliseconds);

    /**
     * expireAt
     * @param key
     * @param millisecondUnixTime
     * @return
     */
    String pexpireAt(String key, long millisecondUnixTime);

    /**
     * pttl
     * @param key
     * @return
     */
    String pttl(String key);
}
