package com.jd.jim.testframework.executor.redis;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface InnerOrderRedisService {

    /**
     * dump
     * @param key
     * @return
     */
    String dump(String key);

    /**
     * restore
     * @param key
     * @param ttl
     * @param serializedValue
     * @return
     */
    String restore(String key, long ttl, byte[] serializedValue);
}
