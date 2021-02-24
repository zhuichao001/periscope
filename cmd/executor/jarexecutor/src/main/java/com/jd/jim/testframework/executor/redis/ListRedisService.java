package com.jd.jim.testframework.executor.redis;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface ListRedisService {

    /**
     * lPush
     * @param key
     * @param values
     * @return
     */
    String lPush(String key, String... values);

    /**
     * lPop
     * @param key
     * @return
     */
    String lPop(String key);

    /**
     * lPushX
     * @param key
     * @param value
     * @return
     */
    String lPushX(String key, String value);

    /**
     * rPush
     * @param key
     * @param values
     * @return
     */
    String rPush(String key, String... values);

    /**
     * rPushX
     * @param key
     * @param value
     * @return
     */
    String rPushX(String key, String value);

    /**
     * rPop
     * @param key
     * @return
     */
    String rPop(String key);

    /**
     * rPopLPush
     * @param source
     * @param destination
     * @return
     */
    String rPopLPush(String source, String destination);

    /**
     * lRem
     * @param key
     * @param count
     * @param value
     * @return
     */
    String lRem(String key, long count, String value);

    /**
     * lLen
     *
     * @param key
     * @return
     */
    String lLen(String key);

    /**
     * lIndex
     *
     * @param key
     * @param index
     * @return
     */
    String lIndex(String key, long index);

    /**
     * lInsert
     * @param key
     * @param position
     * @param pivot
     * @param value
     * @return
     */
    String lInsert(String key, String position, String pivot, String value);

    /**
     * lSet
     * @param key
     * @param index
     * @param value
     * @return
     */
    String lSet(String key, long index, String value);

    /**
     * lRange
     * @param key
     * @param begin
     * @param end
     * @return
     */
    String lRange(String key, long begin, long end);

    /**
     * lTrim
     * @param key
     * @param begin
     * @param end
     * @return
     */
    String lTrim(String key, long begin, long end);
}
