package com.jd.jim.testframework.executor.redis;

import java.util.List;
import java.util.Map;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface SetRedisService {

    /**
     * sAdd
     * @param key
     * @param values
     * @return
     */
    String sAdd(String key, String... values);

    /**
     * sIsMember
     * @param key
     * @param value
     * @return
     */
    String sIsMember(String key, String value);

    /**
     * sPop
     * @param key
     * @return
     */
    String sPop(String key);

    /**
     * sRandMember
     * @param key
     * @param count
     * @return
     */
    String sRandMember(String key, Long count);

    /**
     * sRem
     * @param key
     * @param values
     * @return
     */
    String sRem(String key, String... values);

    /**
     * sMove
     * @param source
     * @param destination
     * @param value
     * @return
     */
    String sMove(String source, String destination, String value);

    /**
     * sCard
     * @param key
     * @return
     */
    String sCard(String key);

    /**
     * sMembers
     * @param key
     * @return
     */
    String sMembers(String key);

    /**
     * sscan
     * @param key
     * @param cursor
     * @param params
     * @return
     */
    String sscan(String key, String cursor, Map<String, String> params);

    /**
     * sInter
     * @param keys
     * @return
     */
    String sInter(String... keys);

    /**
     * sInterStore
     * @param destination
     * @param keys
     * @return
     */
    String sInterStore(String destination, String... keys);

    /**
     * sUnion
     * @param keys
     * @return
     */
    String sUnion(String... keys);

    /**
     * sUnionStore
     * @param destination
     * @param keys
     * @return
     */
    String sUnionStore(String destination, String... keys);

    /**
     * sDiff
     * @param keys
     * @return
     */
    String sDiff(String... keys);

    /**
     * sDiffStore
     * @param destination
     * @param keys
     * @return
     */
    String sDiffStore(String destination, String... keys);
}
