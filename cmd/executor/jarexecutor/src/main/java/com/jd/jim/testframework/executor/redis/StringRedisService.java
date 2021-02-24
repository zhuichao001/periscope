package com.jd.jim.testframework.executor.redis;

import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface StringRedisService {

    /**
     * set
     * @param key
     * @param value
     */
    String set(String key, String value);

    /**
     * 获取值
     * @param key
     * @return
     */
    String get(String key);

    /**
     * getSet
     * @param key
     * @param value
     * @return
     */
    String getSet(String key, String value);

    /**
     * setNX
     * @param key
     * @param value
     * @return
     */
    String setNX(String key, String value);

    /**
     * setEx
     * @param key
     * @param value
     * @param timeout
     * @param unit
     * @return
     */
    String setEx(String key, String value, long timeout, TimeUnit unit);

    /**
     * strLen
     * @param key
     * @return
     */
    String strLen(String key);

    /**
     * setRange
     * @param key
     * @param value
     * @param offset
     * @return
     */
    String setRange(String key, String value, long offset);

    /**
     * psetex
     * @param key
     * @param milliseconds
     * @param value
     * @return
     */
    String psetex(String key, long milliseconds, String value);

    /**
     * mset
     * @param paramsList
     * @return
     */
    String mset(List<String> paramsList);

    /**
     * mget
     * @param keys
     * @return
     */
    String mget(String... keys);

    /**
     * exists
     * @param key
     * @param decrement
     * @return
     */
    String decrBy(String key, long decrement);

    /**
     * append
     * @param key
     * @param value
     * @return
     */
    String append(String key, String value);

    /**
     * getRange
     * @param key
     * @param start
     * @param end
     * @return
     */
    String getRange(String key, long start, long end);

    /**
     * incr
     * @param key
     * @return
     */
    String incr(String key);

    /**
     * incrBy
     * @param key
     * @param increment
     * @return
     */
    String incrBy(String key, long increment);

    /**
     * incrByFloat
     * @param key
     * @param increment
     * @return
     */
    String incrByFloat(String key, double increment);

    /**
     * decr
     * @param key
     * @return
     */
    String decr(String key);

    /**
     * msetnx
     * @param paramsList
     * @return
     */
    String msetnx(List<String> paramsList);
}
