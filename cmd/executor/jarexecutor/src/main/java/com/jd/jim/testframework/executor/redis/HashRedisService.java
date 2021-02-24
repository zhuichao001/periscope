package com.jd.jim.testframework.executor.redis;

import java.util.List;
import java.util.Map;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface HashRedisService {

    /**
     * hset
     * @parma key
     * @param field
     * @param value
     * @return
     */
    String hset(String key, String field, String value);

    /**
     * hsetnx
     * @param key
     * @param field
     * @param value
     * @return
     */
    String hsetnx(String key, String field, String value);

    /**
     * hget
     * @param key
     * @param field
     * @return
     */
    String hget(String key, String field);

    /**
     * hexists
     * @param key
     * @param field
     * @return
     */
    String hexists(String key, String field);

    /**
     * hdel
     * @param key
     * @param field
     * @return
     */
    String hdel(String key, String... field);

    /**
     * hlen
     * @param key
     * @return
     */
    String hlen(String key);

    /**
     * TODO jimkvSDK 目前不支持此操作
     * hstrlen
     * @param key
     * @param field
     * @return
     */
    String hstrlen(String key, String field);

    /**
     * hincrby
     * @param key
     * @param field
     * @param increment
     * @return
     */
    String hincrBy(String key, String field, long increment);

    /**
     * hincrbyfloat
     * @param key
     * @param field
     * @param delta
     * @return
     */
    String hincrByFloat(String key, String field, double delta);

    /**
     * hmset
     * @param key
     * @param hash
     * @return
     */
    String hmset(String key, Map<String, String> hash);

    /**
     * hmget
     * @param key
     * @param fields
     * @return
     */
    String hmget(String key, String... fields);

    /**
     * hkeys
     * @param key
     * @return
     */
    String hkeys(String key);

    /**
     * hvals
     * @param key
     * @return
     */
    String hvals(String key);

    /**
     * hgetAll
     * @return
     */
    String hgetAll(String key);

    /**
     * TODO 支持 pattern 与 count
     * hscan
     * @param key
     * @param cursor
     * @param params
     * @return
     */
    String hscan(String key, String cursor, Map<String, String> params);

}
